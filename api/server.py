import base64
import urllib.parse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from dsa.parser import parse_transactions


# hardcoded credentials (user:1234)
correct_creds = b"user:1234"
encoded_correct_creds = base64.b64encode(correct_creds).decode()

# load transactions
transactions = parse_transactions("modified_sms_v2.xml")


def dump_transactions():
    with open("transactions.json", "w") as f:
        f.write(json.dumps(transactions, indent=4))


class APIHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_AUTH(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Test"')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data = {"message": "Unauthorized"}
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def authorize_user(self):
        auth_header = self.headers.get("Authorization")
        if auth_header is None:
            self.do_AUTH()
            return False

        if auth_header[6:] != encoded_correct_creds:
            self._send_response(401, {"message": "Invalid credentials"})
            return False
        return True
