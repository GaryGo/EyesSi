
import tornado.web

from tornado.escape import json_encode, json_decode
import json
import redis

DEFAULT_SHOW_POST_NUM = 10
db = redis.StrictRedis(host="localhost", port=6379, db=1)

len_post = db.llen("post:1")
post = db.lrange("post:1", 0, min(len_post, DEFAULT_SHOW_POST_NUM))

# print(post)

post_id = {}
# for i in range(len_post):
#     post_id[i] = post[i].decode("utf-8")

# print(post_id)

class GetFriendPostHandler(tornado.web.RequestHandler):
    def post(self):
    	obj = self.request.body
    	obj = obj.decode('utf-8')
    	print(obj)
    	obj = json.loads(obj)
    	user_id = obj['uid']
    	print(user_id)
    	len_post = db.llen("post:{}".format(user_id))
    	print(len_post)
    	post = db.lrange("post:{}".format(user_id), 0, min(len_post, DEFAULT_SHOW_POST_NUM))
    	post_id = {}
    	for i in range(len_post):
    		post_id[str(i)] = post[i].decode("utf-8")
    	print(post_id)
    	self.write(json_encode(post_id))




        