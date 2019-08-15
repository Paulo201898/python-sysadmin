
import flask
import requests


blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET', 'POST' ])
def gitlab():

	res = requests.get('http://localhost:8000/api/v4/users', headers={
		'Private-Token': 'TggkxFBN81FzvwpBeQcJ'
	})

	projects = requests.get('http://localhost:8000/api/v4/projects', headers={
		'Private-Token': 'TggkxFBN81FzvwpBeQcJ'
	})

	context = {
		'title': 'Python | Sysadmin',
		'users': res.json() if res.status_code == 200 else [],
		'projects': projects.json() if projects.status_code == 200 else []
	}
	return flask.render_template('gitlab.html', context=context)

@blueprint.route('/gitlab/<projectid>', methods=[ 'GET', 'POST' ])
def get_commits(projectid):

	url = 'http://localhost:8000/api/v4/projects/{}/repository/commits'.format(projectid)

	commits = requests.get(url, headers={
		'Private-Token': 'TggkxFBN81FzvwpBeQcJ'
		})

	context = {
		'title': ' Python | Sysadmin ',
		'commits': commits.json() if commits.status_code == 200 else []
	}

	return flask.render_template('gitlab_commits.html', context=context)