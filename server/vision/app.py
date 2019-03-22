from flask import Flask
from predict import prediction

app = Flask(__name__)

@app.route('/')
def root():
    return 'Welcome to root directory.'

@app.route('/vision/<image_64>')
def predict():
    return prediction(image_64)

if __name__ == '__main__':
    app.run(port=8080)