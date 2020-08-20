import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello prueba!')

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/blog', MainPage)],
                              debug=True)
