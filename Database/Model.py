from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Waste(db.Model):
    __tablename__ = 'waste'
    id = db.Column(db.Integer, primary_key=True)
    item_type = db.Column(db.String(250), nullable=True)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    garbage_can_id = db.Column(db.Integer, db.ForeignKey('Garbage_Can.id', ondelete='CASCADE'), nullable=False)


    def __init__(self, waste, garbage_can_id):
        self.waste = waste
        self.garbage_can_id = garbage_can_id


class GarbageCan(db.Model):
    __tablename__ = 'Garbage_Can'
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    one_full = db.Column(db.Float, nullable=False)
    two_full = db.Column(db.Float, nullable=False)
    three_full = db.Column(db.Float, nullable=False)
    four_full = db.Column(db.Float, nullable=False)
    
    def __init__(self, name):
        self.name = name


class GarbageCanSchema(ma.Schema):
    id = fields.Integer(dump_only = True)
    latitude = fields.Float()
    longitude = fields.Float()
    one_full = fields.Float()    
    two_full = fields.Float()
    three_full = fields.Float()
    four_full = fields.Float()

class WasteSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    item_type = fields.Integer(required=True)
    creation_date = fields.DateTime()
    garbage_can_id = fields.Integer(required = True)