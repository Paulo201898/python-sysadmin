
import flask
import ldap3
import logging

blueprint = flask.Blueprint('auth', __name__)

@blueprint.route('/sign-in', methods=[ 'GET', 'POST' ])
def sign_in():

	context = {
		'title': 'Python | Sysadmin',
	}
	
	if flask.request.method == 'POST':

		form = flask.request.form
		print(form)

		email = form.get('email')
		password = form.get('password')

		conn = ldap3.Connection(
			ldap3.Server('ldap://127.0.0.1'),
			'cn=admin,dc=dexter,dc=com,dc=br',
			'4linux'
		)

		conn.bind()

		conn.search(
			'uid={},dc=dexter,dc=com,dc=br'.format(email), '(objectClass=person)',
			attributes=[ 'sn', 'userPassword']
		)

		user = None
		try:
			user = conn.entries[0]
		except IndexError:
			logging.warning('Falha ao se logar')
			return flask.redirect('/sign-in')

		saved_password = user.userPassword[0].decode()

		if saved_password == password:
			flask.session['is-logged'] = True
			return flask.redirect('/docker')
		
	return flask.render_template('sign-in.html', context=context)