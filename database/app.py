from flask import Flask, request
from bin import Bin

categories = dict()
categories['Can'] = 0
categories['Paper'] = 1
categories['Plastic'] = 2
categories['Garbage'] = 3

app = Flask(__name__)
b = None
@app.route('/')
def root():
    b = Bin('Whitby', 0)
    return 'Welcome to root directory.'

@app.route('/api/waste', methods['GET', 'POST'])
def throw_out():
    b.new_garbage(request.data['trash_item'])
    

if __name__ == "__main__":
    app.run(port=5001, debug=True)