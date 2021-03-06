import webapp2
import os

from functools import partial
from markii.frameworks.webapp2 import handle_error
from paste import httpserver


class Handler(webapp2.RequestHandler):
    def get(self, n):
        self.response.write(str(int(n)))


root = os.path.abspath(os.path.dirname(__file__))
app = webapp2.WSGIApplication([
    webapp2.Route(r"/<n:.*>", handler=Handler)
], debug=True)
app.error_handlers[400] = partial(handle_error, code=400, app_root=root)
app.error_handlers[404] = partial(handle_error, code=404, app_root=root)
app.error_handlers[500] = partial(handle_error, code=500, app_root=root)

if __name__ == "__main__":
    httpserver.serve(app, host="127.0.0.1", port="8080")
