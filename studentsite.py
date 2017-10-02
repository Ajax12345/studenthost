import tornado.ioloop
import tornado.web
import os
import config

class MainHandler(tornado.web.RequestHandler):
    def get(self):

        self.render('/Users/davidpetullo/Documents/studentscout/home.html')

def make_app():
    settings = {"static_path": os.path.join(os.path.dirname(__file__), "student_style")}
    return tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


#http://localhost:8888
#Works so far style wise
