from flask import jsonify, Blueprint, abort

from flask.ext.restful import (Resource, Api, reqparse,
                               inputs, fields, marshal,
                               marshal_with, url_for)

import models

cat_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'color': fields.String
}




def course_or_404(course_id):
    try:
        course = models.Cats.get(models.Cats.id==cat_id)
    except models.Cats.DoesNotExist:
        abort(404)
    else:
        return cat


class CatList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            help='No cat name provided',
            location=['form', 'json']

        )
        self.reqparse.add_argument(
            'color',
            required=True,
            help='No color provided',
            location=['form', 'json']


        )
        super(Resource, self).__init__()

    def get(self):
        cat = [marshal(cat, cat_fields)
                   for cat in models.Cats.select()]
        return {'cat': cat}

    @marshal_with(cat_fields)
    def post(self):
        args = self.reqparse.parse_args()
        cat = models.Cats.create(**args)
        return cat


class Cat(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=False,
            help='No cat name provided',
            location=['form', 'json']

        )
        self.reqparse.add_argument(
            'color',
            required=False,
            help='No cat color provided',
            location=['form', 'json']


        )
        super(Resource, self).__init__()

    @marshal_with(cat_fields)
    def get(self, id):
        return (cat_or_404(id))

    @marshal_with(cat_fields)
    def put(self, id):
        args = self.reqparse.parse_args()
        query = models.Cats.update(**args).where(models.Cats.id==id)
        query.execute()
        return models.Cats.get(models.Cats.id == id)

    def delete(self, id):
        query = models.Cats.delete().where(models.Cats.id==id)
        query.execute()


cats_api = Blueprint('resources.cats', __name__)
api = Api(cats_api)
api.add_resource(
    CatList,
    '/api/v1/cats',
    endpoint='cats'
)
api.add_resource(
    Cat,
    '/api/v1/cats/<int:id>',
    endpoint='cat'
)
