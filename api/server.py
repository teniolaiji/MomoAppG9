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

    def do_GET(self):
        if not self.authorize_user():
            return

        path = urllib.parse.urlparse(self.path).path

        print("Received GET request for path:", path)

        if path == '/transactions':
            self._send_response(200, transactions)
            return

        if path.startswith('/transactions/'):
            try:
                transaction_id = int(path.split('/')[-1])
            except:
                self._send_response(400, {"message": "Invalid ID"})
                return

            for txn in transactions:
                if txn['id'] == transaction_id:
                    self._send_response(200, txn)
                    return

            self._send_response(404, {"message": "Not found"})
            return

        self._send_response(404, {"message": "Not Found"})

    def do_POST(self):
        if not self.authorize_user():
            return

        path = urllib.parse.urlparse(self.path).path
        if path != '/transactions':
            self._send_response(404, {"message": "Not Found"})
            return

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            transaction = json.loads(post_data)
        except:
            self._send_response(400, {"message": "Invalid JSON"})
            return

        if 'transaction_type' not in transaction or 'timestamp' not in transaction or 'amount' not in transaction:
            self._send_response(400, {"message": "Missing fields"})
            return

        try:
            new_id = transactions[-1]['id'] + 1
        except:
            new_id = 1

        new_transaction = {
            'id': new_id,
            'transaction_type': transaction['transaction_type'],
            'timestamp': transaction['timestamp'],
            'amount': transaction['amount']
        }

        if 'sender' in transaction:
            new_transaction['sender'] = transaction['sender']
        if 'receiver' in transaction:
            new_transaction['receiver'] = transaction['receiver']

        transactions.append(new_transaction)
        dump_transactions()
        self._send_response(201, new_transaction)


    def do_PUT(self):
        if not self.authorize_user():
            return

        path = urllib.parse.urlparse(self.path).path
        if not path.startswith('/transactions/'):
            self._send_response(404, {"message": "Not Found"})
            return

        try:
            transaction_id = int(path.split('/')[-1])
        except:
            self._send_response(400, {"message": "Invalid ID"})
            return

        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)

        try:
            transaction = json.loads(put_data)
        except:
            self._send_response(400, {"message": "Invalid JSON"})
            return

        for txn in transactions:
            if txn['id'] == transaction_id:
                if 'timestamp' in transaction:
                    txn['timestamp'] = transaction['timestamp']
                if 'amount' in transaction:
                    txn['amount'] = transaction['amount']
                if 'sender' in transaction:
                    txn['sender'] = transaction['sender']
                if 'receiver' in transaction:
                    txn['receiver'] = transaction['receiver']
                dump_transactions()
                self._send_response(200, {"message": "Updated"})
                return

        self._send_response(404, {"message": "Not found"})

    def do_DELETE(self):
        if not self.authorize_user():
            return

        path = urllib.parse.urlparse(self.path).path
        if not path.startswith('/transactions/'):
            self._send_response(404, {"message": "Not Found"})
            return

        try:
            transaction_id = int(path.split('/')[-1])
        except:
            self._send_response(400, {"message": "Invalid ID"})
            return

        for txn in transactions:
            if txn['id'] == transaction_id:
                transactions.remove(txn)
                dump_transactions()
                self._send_response(200, {"message": "Deleted"})
                return

        self._send_response(404, {"message": "Not found"})    


if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), APIHandler)
    print("Server started at http://localhost:8080")
    server.serve_forever()
