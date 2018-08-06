from flask import request
from flask_restful import Resource, reqparse

employees = [
    {
        "id": "1",
        "name": "Max Mustermann",
        "occupation": "CEO"
    }
]  
        
class Employee(Resource):
    
    def get(self):
        eId = request.args.get('id')
        
        if eId is None:
            return employees, 200
            
        for employee in employees:
            if(employee["id"] == eId):
                return employee, 200
        
        return {"error": "Entity not found"}, 404
        
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("name")
        parser.add_argument("occupation")
        args = parser.parse_args()
        
        for employee in employees:
            if(args["id"] == employee["id"]):
                return {"error": "Employee with id {} already exists".format(args["id"])}, 400
        
        employee = {
            "id": args["id"],
            "name": args["name"],
            "occupation": args["occupation"]
        }
        employees.append(employee)
        
        return employee, 201
      
    def put(self):
        eId = request.args.get('id')
        
        if eId is None:
            return {"error": "EmployeeId not found!"}, 400
            
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("occupation")
        args = parser.parse_args()
        
        for employee in employees:
            if(employee["id"] == eId):
                employee["name"] = args["name"]
                employee["occupation"] = args["occupation"]
                return employee, 200
        
        return {"error": "Entity not found"}, 404
        
    def delete(self):
        eId = request.args.get('id')
        
        if eId is None:
            return {"error": "EmployeeId not found!"}, 400
            
        global employees
        employees = [employee for employee in employees if employee["id"] != eId]
        return "Employee {} deleted".format(eId), 200
        
        
        