from flask_restful import Resource, reqparse
from flask import request
from controllers import listings
from flask_jwt_extended import jwt_required

class Listings(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str)
        self.parser.add_argument('userId', type=int)
        self.parser.add_argument('descriptionBrief', type=str)
        self.parser.add_argument('descriptionLong', type=str)
        self.parser.add_argument('isActive', type=bool)
        self.parser.add_argument('price', type=int)
        self.parser.add_argument('categoryId', type=int)
        super().__init__()

    def get(self):
        if 'all' in request.args and request.args['all'] != 0 and \
                request.args['all'].lower() != 'false':
            return listings.get_all()
        if 'q' in request.args:
            return listings.get_available_q(request.args['q'])
        else:
            return listings.get_available()

    @jwt_required
    def post(self):
        args = self.parser.parse_args()
        listings.insert(
                str(args['title']),
                int(args['userId']),
                str(args['descriptionBrief']),
                str(args['descriptionLong']),
                int(args['isActive']),
                int(args['price']),
                int(args['categoryId'])
        )
        return 200

class Listing(Resource):
    def get(self, listing_id):
        return listings.get_single(listing_id)
