from handlers.userhandler import AddUserHandler
from handlers.userhandler import DeleteUserHandler
# from handlers.index import EditUserHandler
from handlers.userhandler import MainHandler
from handlers.userhandler import UserLogin
from handlers.uploadhandler import UploadHandler
from handlers.getposthandler import GetFriendPostHandler
# from handlers.index import UpdateUserInfoHandler

urls = [          
    ( r'/', MainHandler ),     
    ( r'/upload', UploadHandler),               
    ( r'/AddUser', AddUserHandler ),
    ( r'/Login', UserLogin),
    # ( r'/EditUser', EditUserHandler ),
    ( r'/DeleteUser', DeleteUserHandler ),
    ( r'/GetFriendPostId', GetFriendPostHandler),
    # ( r'/UpdateUserInfo', UpdateUserInfoHandler ),
]