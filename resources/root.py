from flask_restful import Resource
from controllers import config

class Root(Resource):
    def get(self):
        """Returns the list of supported endpoints of the REST api"""
        return {
                "listings": "https://" + config.get_root() + "/listings?{all},{q=%s}",
                "users": "https://" + config.get_root() + "/users",
                "auth": "https://" + config.get_root() + "/auth",
                "register": "https://" + config.get_root() + "/register"
        }

