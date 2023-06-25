import requests
import json
from flask import Flask, request, Response
app = Flask(__name__)
@app.route('/trains', methods=['GET'])
def get_trains():
    access_token = request.headers.get('Authorization')
    response = requests.get(
        'http://104.211.219.98/train/trains',
        headers={'Authorization': access_token}
    )
    if response.status_code == 200:
        trains = response.json()
        trains = [train for train in trains if train['departureTime'] >= 3600]
        trains = sorted(trains, key=lambda train: (train['price'], -train['seatsAvailable'], -train['departureTime']))
        return Response(json.dumps(trains), mimetype='application/json')
    else:
        return Response('Error getting trains', status=400)
if __name__ == '__main__':
    app.run(debug=True)
