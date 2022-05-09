from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if 'word' in dic:
            full_url = "" # pass in a url
            response = requests.get(full_url + dic["word"]) # comes in as JSON > we want this as an object
            data = response.json() # parses this JSON into a python Object

            defs = []
            for word_data in data:

        else:
