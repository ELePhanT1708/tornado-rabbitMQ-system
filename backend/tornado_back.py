import tornado
import tornado.web
import os
import uuid
from tornado.options import define, options
from send import send_message_to_rabbit

define("port", default=81, help="run on the given port", type=int)


def parse_arguments(args):
    surname: str = args[0]
    name: str = args[1]
    parent: str = args[2]
    phone: str = args[3]
    body: str = args[4]
    return dict({
        'surname': surname,
        'name': name,
        'parent': parent,
        'phone': phone,
        'request_body': body
    })


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/form", FormHandler),
        ]
        settings = dict(
            title=u" Обращение ",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            cookie_secret=uuid.uuid4().int,
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        self.render("index.html")


class FormHandler(tornado.web.RequestHandler):
    async def post(self):
        surname = self.get_argument("surname", strip=False)
        name = self.get_argument("name", strip=False, )
        parent = self.get_argument("otchestvo", strip=False)
        phone = self.get_argument("phone", strip=False)
        request_body = self.get_argument("question", strip=False)
        req = parse_arguments([surname, name, parent, phone, request_body])
        status = send_message_to_rabbit(body=req)
        if status == 'Success':
            self.render("success.html", request=req)
        else:
            self.render("success.html", request=req)


if __name__ == "__main__":
    app = Application()
    app.listen(options.port)
    print(f"Listening on port: {options.port}")
    tornado.ioloop.IOLoop.current().start()
