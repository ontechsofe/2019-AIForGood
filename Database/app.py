from flask import Blueprint
from flask_restful import Api
from resources.Waste import WasteResource
from resources.GarbageCan import GarbageCanResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(WasteResource, '/Waste')
api.add_resource(GarbageCanResource, '/Garbage')
