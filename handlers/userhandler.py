from model import User
import tornado.web
from torndsession.sessionhandler import SessionBaseHandler
from tornado.escape import json_encode, json_decode
import json
import redis

user_orm = User.UserManagerORM() 

class MainHandler( tornado.web.RequestHandler ):           # 主Handler，用来响应首页的URL
        '''
            MainHandler shows all data and a form to add new user
        '''
        def get( self ):                                   # 处理主页面(UserManager.html)的GET请求
                # show all data and a form
            title = 'User Manager V0.1'                
            self.render( 'UserManager.html', title = title)      # 并显示该模板页面
                
        def post( self ):
                pass                                       # 这里不处理POST请求

class AddUserHandler( tornado.web.RequestHandler ):        # 响应/AddUser的URL
        '''
            AddUserHandler collects info to create new user
        '''
        def get( self ):
                pass
        
        def post( self ):                                  # 这个URL只响应POST请求，用来收集用户信息并新建帐号
                # Collect info and create a user record in the database
                user_info = {
                                'uid':0,
                                'uname':self.get_argument( 'uname' ),
                                'uemail':self.get_argument( 'uemail' ),
                                'upw':self.get_argument( 'upw' ),
                                'profile_img_path': '',
                                'friend_num':0,
                                'post_num':0
                                }
                user_orm.createNewUser( user_info )        # 调用ORM的方法将新建的用户信息写入数据库

                self.redirect( 'http://localhost:9999' )   # 页面转到首页



# class UpdateUserInfoHandler( tornado.web.RequestHandler ):          # 用户信息编辑完毕后，将会提交到UpdateUserInfo，由此Handler处理
#         '''
#             Update user info by given list
#         '''
#         def get( self ):
#                 pass

#         def post( self ):                                  # 调用ORM层的UpdateUserInfoByName方法来更新指定用户的信息
#                 user_orm.UpdateUserInfoByName({
#                         'user_name':self.get_argument( 'user_name' ),
#                         'user_age':self.get_argument( 'user_age' ),
#                         'user_sex':self.get_argument( 'user_sex' ),
#                         'user_score':self.get_argument( 'user_score' ),
#                         'user_subject':self.get_argument( 'user_subject' ),
#                         })
#                 self.redirect( 'http://localhost:9999' )   

class DeleteUserHandler( tornado.web.RequestHandler ):     
        '''
            Delete user by given name
        '''
        def get( self ):
                
                user_orm.deleteUserById( self.get_argument( 'uid' ) )
                
                self.redirect( 'http://localhost:9999' )   # 数据库更新后，转到首页

        def post( self ):
                pass

class UserLogin(SessionBaseHandler):
    def get(self):
        user = user_orm.getUserByEmail("sysugjf@gmail.com")
        obj = {
            'status' : "login",
            'uid' : str(user.uid),
            'uname' : user.uname,
            'uemail' : user.uemail,
            'profile_img_path' : user.profile_img_path,
            'friend_num' : str(user.friend_num),
            'post_num' : str(user.post_num),
            'sid' : self.session.id
        }
        self.write(json_encode(obj))

    def post(self):
        self.set_cookie("msid", self.session.id) 
        is_auto_login = self.get_argument("auto")

        if is_auto_login == "false":
            uemail = self.get_argument('uemail')
            upw = self.get_argument('upw')
            user = user_orm.getUserByEmail(uemail)
        
            if not user:
                obj = {
                    'status' : "not",
                }
                self.write(json_encode(obj))

            elif user.upw == upw:
                self.session['uemail'] = uemail
                obj = {
                    'status' : "login",
                    'uid' : str(user.uid),
                    'uname' : user.uname,
                    'uemail' : user.uemail,
                    'profile_img_path' : user.profile_img_path,
                    'friend_num' : str(user.friend_num),
                    'post_num' : str(user.post_num),
                }
                self.write(json_encode(obj))
            else:
                obj = {
                    'status' : "fail",
                }
                self.write(json_encode(obj))
        else:
            if (self.request.headers['Cookie'][5:] == self.session.id):
                obj = {
                    'status' : "auto",
                }
            else:
                obj = {
                    'status' : "expired",
                }
            self.write(json_encode(obj))
            
