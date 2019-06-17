from .util import is_empty_str

def username(username):
	if is_empty_str(username):
		return False
	else:
		return True

def password(password):
	if is_empty_str(password):
		return False
	else:
		return True