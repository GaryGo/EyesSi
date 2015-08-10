#!/usr/bin/env python

from sqlalchemy import *
from sqlalchemy.orm import *
from model.dbsetting import database_setting



# 下面这个类就是实体类，对应数据库中的user表
class User( object ):
        def __init__( self, uid, uname,
                        upw, uemail, profile_img_path, friend_num, post_num ):
                self.uid = uid
                self.uname = uname
                self.upw = upw
                self.uemail = uemail
                self.profile_img_path = profile_img_path
                self.friend_num = friend_num
                self.post_num = post_num

# 这个类就是直接操作数据库的类
class UserManagerORM():
        def __init__( self ):
                '''
                    # 这个方法就是类的构造函数，对象创建的时候自动运行
                '''
                self.engine = create_engine(       # 生成连接字符串，有特定的格式
                                database_setting[ 'database_type' ] +
                                '+' +
                                database_setting[ 'connector' ] +
                                '://' +
                                database_setting[ 'user_name' ] +
                                ':' +
                                database_setting[ 'password' ] +
                                '@' +
                                database_setting[ 'host_name' ] +
                                '/' +
                                database_setting[ 'database_name' ]
                                )
                self.metadata = MetaData( self.engine )
                self.user_table = Table( 'user', self.metadata, 
                                autoload = True )
                
                mapper( User, self.user_table )

                # 生成一个会话类，并与上面建立的数据库引擎绑定
                self.Session = sessionmaker()
                self.Session.configure( bind = self.engine )
                
                # 创建一个会话
                self.session = self.Session()

        def createNewUser( self, user_info ):
                '''
                    # 这个方法根据传递过来的用户信息列表新建一个用户
                    # user_info是一个列表，包含了从表单提交上来的信息
                '''
                new_user = User( 
                                user_info['uid'],
                                user_info[ 'uname' ],
                                user_info[ 'upw' ],
                                user_info[ 'uemail' ],
                                user_info[ 'profile_img_path' ],
                                user_info[ 'friend_num' ],
                                user_info[ 'post_num' ]
                                )
                self.session.add( new_user )                       # 增加新用户
                self.session.commit()                              # 保存修改

        def getUserByEmail( self, uemail ):                   # 根据用户名返回信息
            if not self.session.query( User ).filter_by(uemail = uemail ).all():
                return None
            else:
                return self.session.query( User ).filter_by( 
                                uemail = uemail ).all()[ 0 ]

        def getAllUser( self ):                                    # 返回所有用户的列表
                return self.session.query( User )

        # def UpdateUserInfoByName( self, user_info ):               
        #         uname = user_info[ 'uname' ]
        #         user_info_without_name = { 'user_age':user_info[ 'user_age' ],
        #                         'user_sex':user_info[ 'user_sex' ],
        #                         'user_score':user_info[ 'user_score' ],
        #                         'user_subject':user_info[ 'user_subject' ]
        #                         }
        #         self.session.query( User ).filter_by( user_name = user_name ).update( 
        #                         user_info_without_name )
        #         self.session.commit()

        def deleteUserById( self, uid ):                  # 删除指定用户名的用户
                user_need_to_delete = self.session.query( User ).filter_by( 
                                uid = uid ).all()[ 0 ]
                self.session.delete( user_need_to_delete )
                self.session.commit()