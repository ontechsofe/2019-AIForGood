from flask import Flask, request
import  io, http.client, urllib.request, urllib.parse, urllib.error, base64, json

app = Flask(__name__)

@app.route('/')
def root():
    return 'Welcome to root directory.'

@app.route('/not/<hi>')
def not_root(hi):
    return f'Welcome to root directory. {hi}'

@app.route('/vision', methods=['POST'])
def vision():
    # print(request.form)
    # print(request.form['image'])
    return prediction(request.form['image'])

def prediction(b64):
    headers = {
        # Request headers 
        'Content-Type': 'multipart / form-data', 
        'Prediction-key': '4128a622079d4a5381c7a9267528a750', 
    }

    params = urllib.parse.urlencode({ 
        # Request parameters 
        'iterationId': '5c3926ab-6c78-4b87-b150-6487bfeab75a', 
    })

    try : 
        conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com') 
        # print(b64)
        # f = open('data/JPEG_20190322_175157.jpg', 'rb', buffering=0)
        # b64 = base64.b64encode(f.read()).split(',')
        # print(b64[])
        b64 = b64.split(',')
        with open('temp.jpg', "wb") as fh:
            fh.write(base64.b64decode(b64[1]))
        
        f = open('temp.jpg', 'rb', buffering=0)

        conn.request("POST" , "/customvision/v1.0/Prediction/14375ed8-f31f-4115-ace3-6c70d2eabcf3/image?%s" % params, f.readall(), headers) 
        response = conn.getresponse()
        data = response.read()
        # data = json.load(data)
        conn.close()
        return data
    except Exception as e: 
        # print ("[Errno {0}] {1}". format (e. errno, e. strerror)) 
        print(e)


if __name__ == '__main__':
    app.run(port=8080)