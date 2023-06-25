from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')
    numbers = set()
    
    for url in urls:
        try:
            response = requests.get(url, timeout=0.5)
            if response.status_code == 200:
                data = response.json()
                numbers.update(data['numbers'])
        except requests.exceptions.Timeout:
            continue
        except requests.exceptions.RequestException:
            continue
    
    response_data = {"numbers": sorted(list(numbers))}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(port=3000)
