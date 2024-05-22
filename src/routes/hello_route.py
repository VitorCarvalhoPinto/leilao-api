from flask import Blueprint 

hello = Blueprint('hello', __name__)

@hello.route('/hello', methods=['GET'])
def get_hello(): return 'hello world'