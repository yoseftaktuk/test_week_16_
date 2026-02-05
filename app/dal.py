from connection import Mongo_connection
import json
import pymongo
my_connection = Mongo_connection()


collection = my_connection.collection

def seve_data(file_name):# seve the data from the json file
    with open(file_name) as f:
        data = json.load(f)
        collection.insert_many(data)
seve_data('employee_data_advanced.json')

class Mongo_qury:

    def serialize_doc(self, doc):
        if doc and "_id" in doc:
            doc["_id"] = str(doc["_id"])
        return doc

    def serialize_docs(self, docs):# func to replise the objectid to str
        return [self.serialize_doc(doc) for doc in docs]    

    def get_engineering_high_salary_employees(self):
        qury = {'$and':[{'job_role.department': 'Engineering'},
                        {'salary': {'$gt': 65000}}]}
        select = {'_id':0, 'employee_id': 1, 'name': 1 ,'salary': 1}
        result = collection.find(qury, select).to_list()
        return result   
    
    def get_employees_by_age_and_role(self):
        qury = {'$and':[{'age':{'$gte': 30}}, {'age': {'$lte': 45}},
                        {'$or':[{'job_role.title': 'Engineer'}, {'job_role.title': 'Specialist'}]}]}
        select = {}
        result = collection.find(qury, select).to_list()
        result = self.serialize_docs(result)
        return result
    
    def get_top_seniority_employees_excluding_hr(self):
        qury = {'job_role.department': {'$ne': 'HR'}}
        select = {}
        result = collection.find(qury, select).sort('years_at_company',pymongo.DESCENDING).limit(7)
        result = self.serialize_docs(result)
        return result
    
    def get_employees_by_age_or_seniority(self):
        qury = {'$or':[{'age':{'$gt': 50}},{'years_at_company': {'$lt': 3}}]}
        select = {'_id':0, 'employee_id': 1, 'name': 1, 'age': 1, 'years_at_company': 1}
        result = collection.find(qury, select).to_list()
        return result
    
    def get_managers_excluding_departments(self):
        qury = {'$and': [{'job_role.title': 'Manager'},
                         {'job_role.department': {'$ne': 'Sales'}},
                         {'job_role.department': {'$ne': 'Marketing'}}]}
        select = {}
        result = collection.find(qury, select).to_list()
        result = self.serialize_docs(result)
        return result
    
    def get_employees_by_lastname_and_age(self):
        qury = {'$and': [{'$or':[{'name':{'$regex': 'Nelson$'}} ,
                                 {'name':{'$regex': 'Wright$'}}]},
                                   {'age': {'$lt': 35}}]}
        select = {'_id': 0, 'name': 1, 'age': 1, 'job_role.department': 1}
        result = collection.find(qury, select).to_list()
        return result