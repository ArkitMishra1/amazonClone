import os
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        # Set the path to the index.html file
        index_path = os.path.join(os.path.dirname(__file__), 'index.html')
        
        # Serve the index.html file if it exists
        if os.path.exists(index_path):
            self.response.headers['Content-Type'] = 'text/html'
            with open(index_path, 'r') as file:
                self.response.write(file.read())
        else:
            self.response.set_status(404)
            self.response.write("<h1>404 Not Found</h1><p>The requested page could not be found.</p>")

# Define the webapp2 application
app = webapp2.WSGIApplication([
    ('/', MainPage),  # Map the root URL to the MainPage handler
], debug=True)
