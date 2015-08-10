from urls import urls

import tornado.web
import os

settings = dict(
	template_path = os.path.join(os.path.dirname(__file__), 'templates'),
	static_path = os.path.join(os.path.dirname(__file__), "static"),
)

session_settings = dict(
            driver = "redis",
            driver_settings = dict(
                host = 'localhost',
                port = 6379,
                db = 0,
                max_connections = 1024,
            )
        )
settings.update(session = session_settings)
application = tornado.web.Application(handlers = urls, **settings)