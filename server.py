#!/usr/bin/env python

# This is a Web Server for UserManager

import tornado.httpserver                         # 引入tornado的一些模块文件
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from application import application

define( 'port', default = 9999, help = 'run on the given port', type = int )




def MainProcess():                                        # 主过程，程序的入口
        tornado.options.parse_command_line()
        http_server = tornado.httpserver.HTTPServer( application )
        http_server.listen( options.port )                # 在上面的的define中指定了端口为9999
        tornado.ioloop.IOLoop.instance().start()          # 启动服务器
        session_manager = session.SessionManager(settings["session_secret"], settings["store_options"], settings["session_timeout"])

if __name__ == '__main__':                                # 文件的入口
        MainProcess()
