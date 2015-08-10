import tornado.web
import os
import uuid

__UPLOADS__ = "static/uploads/"

class UploadHandler(tornado.web.RequestHandler):
	def post(self):
		# fileinfo = self.request.files['filearg'][0]
		# print ("fileinfo is", fileinfo)
		# fname = fileinfo['filename']
		# extn = os.path.splitext(fname)[1]
		# cname = str(uuid.uuid4()) + extn
		# fh = open(__UPLOADS__ + cname, 'w')
		# fh.write(str(fileinfo['body']))
		# self.finish(cname + " is uploaded!! Check %s folder" %__UPLOADS__)

		file1 = self.request.files['image'][0]
		fname = file1['filename']
		output_file = open(__UPLOADS__ + fname, 'wb')
		output_file.write(file1['body'])
		self.finish("file" + fname + " is uploaded ok")
