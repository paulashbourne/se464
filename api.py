from app import Blueprint
from flask import request
from models import Employer
import ujson

api = Blueprint('api', __name__)

@api.get('/employer/<employer_id>')
def get_employer(employer_id):
    employer = Employer.find_by({ 'id' : employer_id })
    if employer is None:
        # TODO: throw error here
        pass
    return ujson.dumps(employer)

@api.post('/employer')
def create_employer():
    if 'employer' not in request.args:
        # throw error
        pass

    employer = Employer.create(request.args.get('employer'))
    employer.save() 

