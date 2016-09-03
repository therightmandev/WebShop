from .. import db
from ..models import User


#~~~USER~~~#
def is_username_available(username):
    found = User.query.filter_by(username=username).first()
    if found is None:
        return True
    else:
        return False

def is_email_available(email):
    found = User.query.filter_by(email=email).first()
    if found is None:
        return True
    else:
        return False
