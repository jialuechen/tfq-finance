import json
import requests

def send_to_blockchain(data, blockchain_url):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(blockchain_url, data=json.dumps(data), headers=headers)
    return response.json()

if __name__ == "__main__":
    data = {
        'transaction_id': '1234567890',
        'amount': 1000,
        'currency': 'USD'
    }
    blockchain_url = 'http://example-blockchain.com/api/transaction'

    response = send_to_blockchain(data, blockchain_url)
    print("Blockchain Response:")
    print(response)