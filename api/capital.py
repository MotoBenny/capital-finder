from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    # https://restcountries.com/v3.1/name/peru

    def get_GET(self):
        url_components = parse.urlsplit(self.path)
        query_list = parse.parse_qsl(url_components.query)
        dict = dict(query_list)

        if 'country' in dict:
            url = "https://restcountries.com/v3.1/name/"
            complete_url = url + dict['country']
            response = requests.get(complete_url)
            data = response.json(response)

            capital = data['capital']
            message = str(capital)

        else:
            message = "Type a country in the query to get its capital city."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return
