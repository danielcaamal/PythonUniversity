from flask import Flask, Response, abort, redirect, render_template, request, session, url_for
from logging.config import dictConfig


# Logging
dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
        'logger_base' : {
            'format': '[%(asctime)s %(levelname)s %(filename)s:%(lineno)s] %(message)s'
        }
    },
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'logger_base'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

app.secret_key = 'SECRET'

@app.route("/")
def home():
    # Logging
    app.logger.debug('Printing hello world (DEBUG)')
    app.logger.info('Printing hello world (INFO)')
    app.logger.warning('Printing hello world (WARNING)')
    app.logger.error('Printing hello world (ERROR)')

    # Sessions
    if 'username' in session:
        return f'User logged {session["username"]}'
    else:
        return 'User not logged'

    # Hello World
    app.logger.info(f'Request Path: {request.path}')
    return "<p>Hello World from Flask!</p>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username')
    return redirect(url_for('home'))

@app.route("/greetings/<name>")
def greetings(name):
    return f'Hi {name}'

@app.route('/age/<int:age>')
def show_age(age):
    return f"You're {age} years old"

@app.route("/show/<name>", methods=['GET', 'POST'])
def show_name(name):
    if request.method == 'POST':
        app.logger.info('Type POST')
    elif request.method == 'GET':
        app.logger.info('Type GET')
    params = {
        'key_name': name
    }
    return render_template('show.html', **params)

@app.route('/redirecting')
def redirecting():
    return redirect(url_for('show_name', name='Juan'))

@app.route('/exit')
def exit():
    return abort(404)

@app.errorhandler(404)
def error404(error):
    return render_template('error404.html', error=error), 404

# REST Representational State Transfer
@app.route('/api/show/<name>')
def show_json(name):
    values = {
        'name': name,
        'method': request.method
    }
    return values

