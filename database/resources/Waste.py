from flask import request
from flask_restful import Resource
from Model import db, Waste, WasteSchema, GarbageCan

wastes_schema = WasteSchema(many=True)
waste_schema = WasteSchema()

class WasteResource(Resource):
    def get(self):
        wastes = Waste.query.all()
        wastes = waste_schema.dump(wastes).data
        return {'status': 'success', 'data': wastes}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = waste_schema.load(json_data)
        if errors:
            return errors, 422
        garbage_can = GarbageCan.query.filter_by(id=data['garbage_can_id']).first()
        if waste:
            return {'message': 'Waste already exists'}, 400
        waste = Waste(
            name=json_data['name']
            )

        db.session.add(waste)
        db.session.commit()

        result = waste_schema.dump(waste).data

        return { "status": 'success', 'data': result }, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = waste_schema.load(json_data)
        if errors:
            return errors, 422
        category = Waste.query.filter_by(id=data['id']).first()
        if not waste:
            return {'message': 'Waste does not exist'}, 400
        waste.name = data['name']
        db.session.commit()

        result = waste_schema.dump(waste).data

        return { "status": 'success', 'data': result }, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = waste_schema.load(json_data)
        if errors:
            return errors, 422
        waste = waste.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = waste_schema.dump(waste).data

        return { "status": 'success', 'data': result}, 204