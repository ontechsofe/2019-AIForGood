from flask import Blueprint
from flask_restful import Api
from resources.hello import hello
from resources.Category import CategoryResource
from resources.Comment import CommentResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(hello, '/hello')
api.add_resource(CategoryResource, '/Category')
api.add_resource(CommentResource, '/Comment')