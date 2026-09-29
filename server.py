import http.server, functools

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

http.server.test(HandlerClass=functools.partial(NoCacheHandler, directory='.'), port=8899)
