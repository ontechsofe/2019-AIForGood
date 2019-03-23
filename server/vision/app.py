from flask import Flask, request
import io
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json

app = Flask(__name__)


@app.route('/')
def root():
    return 'Welcome to root directory.'


@app.route('/vision', methods=['POST'])
def vision():
    data = dict()
    data['can_id'] = request.form['can_id']
    data['trash_item'] = prediction(request.form['image'])
    json_data = json.dumps(data)
    send_server(json_data)
    return json_data


def prediction(b64):
    headers = {
        # Request headers
        'Content-Type': 'multipart/form-data',
        'Prediction-key': '4128a622079d4a5381c7a9267528a750',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'iterationId': '5c3926ab-6c78-4b87-b150-6487bfeab75a',
    })

    try:
        conn = http.client.HTTPSConnection(
            'southcentralus.api.cognitive.microsoft.com')
        b64 = b64.split(',')
        with open('temp.hide.jpg', "wb") as fh:
            fh.write(base64.b64decode(b64[1]))

        f = open('temp.hide.jpg', 'rb', buffering=0)

        conn.request('POST', '/customvision/v1.0/Prediction/14375ed8-f31f-4115-ace3-6c70d2eabcf3/image?%s' %
                     params, f.readall(), headers)
        response = conn.getresponse()
        data = json.loads(response.read().decode('utf-8'))
        conn.close()
        return data['Predictions'][0]['Tag']
    except Exception as e:
        print(e)

def send_server(json_data):
    conn = http.client.HTTPConnection(
        '127.0.0.1', port=5001)
    conn.request('POST', '/api/Waste', json_data)
    conn.close()

if __name__ == '__main__':
    app.run(port=5000)
