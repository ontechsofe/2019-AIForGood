from flask import jsonify, request
from flask_restful import Resource
from Model import db, GarbageCan, Waste, GarbageCanSchema

garbage_cans_schema = GarbageCanSchema(many=True)
garbage_can_schema = GarbageCanSchema()

class GarbageCanResource(Resource):
    def get(self):
        garbage_cans = GarbageCan.query.all()
        garbage_cans = garbage_cans_schema.dump(garbage_cans).data
        return {"status":"success", "data":garbage_cans}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = garbage_cans_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        garbage_can = GarbageCan.query.filter_by(name=data['name']).first()
        if not garbage_can_id:
            return {'status': 'error', 'message': 'Noot found'}, 400
        garbagecan = GarbageCan(
            name=json_data['name']
            )
        db.session.add(garbage_can)
        db.session.commit()

        result = garbage_can_schema.dump(garbage_can).data

        return {'status': "success", 'data': result}, 201

    # You can add the other methods here...