from app import Blueprint
import ujson

api = Blueprint('api', __name__)

@api.get('/employer/<employer_id>')
def get_employer(employer_id):
    employer = Employer.find_by({ 'id' : employer_id })
    if employer is None:
        # TODO: throw error here
        pass
    return ujson.dumps(employer)
