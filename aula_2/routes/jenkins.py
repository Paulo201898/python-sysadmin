
import flask


blueprint = flask.Blueprint('jenkins', __name__)

@blueprint.route('/jenkins', methods=[ 'GET', 'POST' ])
def jenkins():
    context = {
        'title': 'Python | Sysadmin'
    }
    return flask.render_template('jenkins.html', context=context)

@blueprint.route('/jenkins/<jobname>', methods=[ 'GET', 'POST' ])
def jenkins_update(jobname):
    context = {
        'title': 'Python | Sysadmin'        
    }
    return flask.render_template('jenkins_update.html', context=context)