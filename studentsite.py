import tornado.ioloop
import tornado.web
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):

        self.render('/Users/jamespetullo/Downloads/studenthost-master/studentscout/home.html')

class StudentRegster(tornado.web.RequestHandler):
    def get(self):
        self.render("/Users/jamespetullo/Downloads/studenthost-master/studentscout/student_register.html")

    def post(self):
        first_name = self.get_argument("first_name")
        last_name = self.get_argument("last_name")
        email = self.get_argument("email")

        username = self.get_argument("username")
        password = self.get_argument("password")
        headers = ("first_name", "last_name", "email", "username", "password")
        data = (first_name, last_name, email, username, password)
        data_dict = dict(zip(headers, data))




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

