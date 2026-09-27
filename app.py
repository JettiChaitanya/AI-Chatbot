try:
    from importlib import import_module

    Flask = import_module("flask").Flask
except ModuleNotFoundError:
    from wsgiref.simple_server import make_server

    class Flask:
        def __init__(self, name):
            self._routes = {}

        def route(self, path):
            def decorator(function):
                self._routes[path] = function
                return function

            return decorator

        def run(self, debug=False):
            def application(environ, start_response):
                response = self._routes.get(environ.get("PATH_INFO"), lambda: "Not found")()
                status = "200 OK" if response != "Not found" else "404 NOT FOUND"
                start_response(status, [("Content-Type", "text/html; charset=utf-8")])
                return [response.encode("utf-8")]

            make_server("127.0.0.1", 5000, application).serve_forever()

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>AI Document Chatbot</h1><p>Flask is working successfully!</p>"

if __name__ == "__main__":
    app.run(debug=True)