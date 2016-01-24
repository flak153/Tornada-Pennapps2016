import tornado.ioloop
import tornado.web
import tornado.websocket


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/ws", EchoWebSocket),
        (r"/", MainHandler),
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()