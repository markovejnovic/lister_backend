from flask_restful import Resource
from controllers import categories

class Categories(Resource):

    def get(self):
    	return categories.get_all()

class Category(Resource):
    def get(self, category_id):
        return categories.get_single(category_id)