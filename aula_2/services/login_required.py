import functools

import flask

def login_required(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		if not flask.session.get('is-logged'):
			return flask.redirect('/sign-in')
		return function(*args, **kwargs)
	return wrapper