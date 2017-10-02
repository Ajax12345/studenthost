import tornado.ioloop
import tornado.web
import os
import config

class MainHandler(tornado.web.RequestHandler):
    def get(self):

        self.render('/Users/davidpetullo/Documents/studentscout/home.html')

class StudentRegster(tornado.web.RequestHandler):
    def get(self):
        self.render("/Users/davidpetullo/Documents/studentscout/student_register.html")

    def post(self):
        username = self.get_body_argument("username", default=None, strip=False)
        password = self.get_body_argument("password", default=None, strip=False)
        print (username, password)

def make_app():
    settings = {"static_path": os.path.join(os.path.dirname(__file__), "student_style")}
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/student_register', StudentRegster)
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


#http://localhost:8888
#Works so far style wise
