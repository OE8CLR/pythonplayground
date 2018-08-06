from flask import Flask
from flask_restful import Api, Resource
import Employee 

app = Flask(__name__)
api = Api(app)

# Default Route
@app.route("/", methods=["GET"])
def home():
    return "<h1>API DEMO</h1><p>This site is a prototype API for playing around with recast.ai.</p>"

# Extended Routes
api.add_resource(Employee.Employee, '/employee')

if __name__ == '__main__':
     app.run(port='8080', debug=True)