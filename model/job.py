from app import app
import json
from flask import request

from model.database import mongo

class Job:
    def __init__(self):
        self.job_dao = mongo.db.jobs
    

    def create(self, job_dict):
        self.job_dao.insert_one(job_dict)


    def update(self, job_dict, updated_job):
        condition = {"job_id": job_dict.get("job_id")}
        self.job_dao.update_one(condition, {"$set": updated_job})


    def get(self, job_dict):
        condition = {"job_id": job_dict.get('job_id')}
        job = self.job_dao.find_one(condition)
        return job


    def get_all(self):
        jobs = self.job_dao.find()
        return jobs


    def delete(self, job_dict):
        self.job_dao.delete_one(job_dict)


    def delete_many(self, job_dict):
        self.job_dao.delete_many(job_dict)

@app.route('/demo-job')
def demo_job():
    job = Job()
    print("get job oong")
    print(job.get({"job_id": "2941233156"}))
    return "ok"
