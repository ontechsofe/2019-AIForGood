from flask import Flask, request
from resources.bin import Bin
import json

bins = []
categories = dict()
categories['Can'] = 0
categories['Paper'] = 1
categories['Plastic'] = 2
categories['Garbage'] = 3

app = Flask(__name__)
b = None
@app.route('/')
def root():
    bins.append(Bin('Whitby', 0))
    return 'Welcome to root directory.'

@app.route('/api/waste', methods=['GET', 'POST'])
def throw_out():
    bins[0].new_garbage(json.loads(request.data.decode('utf-8'))['trash_item'])
    

if __name__ == "__main__":
    app.run(port=5001, debug=True)