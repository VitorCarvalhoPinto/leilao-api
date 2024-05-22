from flask import Flask
from flask_cors import CORS
# from src import create_app

main = Flask(__name__)
CORS(main)
@main.route('/', methods=['GET'])
def hello():
    return 'hello world'

if __name__ == '__main__':
    main.run(host='0.0.0.0', port=5000)