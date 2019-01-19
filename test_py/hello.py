import tornado.web
import tornado.ioloop

class IndexHander(tornado.web.RequestHandler):
	def get(self):
		self.write("hello world")


if __name__ == "__main__":
	app = tornado.web.Application([(r"/index",IndexHander),])
	app.listen(8000)
	tornado.ioloop.IOLoop.current().start()