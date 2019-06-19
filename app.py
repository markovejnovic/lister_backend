from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources import Root, Listings, Users, Auth, Listing, Register, \
	Categories, Category

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret';

api = Api(app)
jwt = JWTManager(app)

api.add_resource(Root, '/')
api.add_resource(Auth, '/auth')
api.add_resource(Listings, '/listings')
api.add_resource(Listing, '/listings/<int:listing_id>')
api.add_resource(Users, '/users')
api.add_resource(Register, '/register')
api.add_resource(Categories, '/categories')
api.add_resource(Category, '/categories/<int:category_id>')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# TODO: Remove, used for bootstrap purposes
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
