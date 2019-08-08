
import flask


blueprint = flask.Blueprint('auth', __name__)

@blueprint.route('/sign-in', methods=[ 'GET', 'POST' ])
def sign_in():
    context = {
        'title': 'Python | Sysadmin',
    }
    return flask.render_template('sign-in.html', context=context)