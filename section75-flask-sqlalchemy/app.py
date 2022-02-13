from flask import Flask, redirect, render_template, request, url_for
from models import Person
from forms import PersonForm
from database import db
from flask_migrate import Migrate

app = Flask(__name__)

# Bd Configuration
USER_DB = 'daniel'
PASS_DB = 'daniel'
URL_DB = '192.168.100.32'
NAME_DB = 'sap_flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Flask migrate
migrate = Migrate()
migrate.init_app(app, db)

app.config['SECRET_KEY'] = 'SECRET'

'''
MAKE MIGRATIONS
    1. $flask db init
    2. $flask db migrate
    3. $flask db upgrade

VERIFY MIGRATIONS
    1. $flask db stamp head
'''

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def home():
    people = Person.query.order_by('id')
    total = Person.query.count()
    app.logger.debug(f'People: {people}')
    app.logger.debug(f'Total: {total}')
    return render_template('index.html', people=people, total=total)


@app.route('/show/<int:id>')
def show_detail(id):
    # person = Person.query.get(id)
    # SELECT
    person = Person.query.get_or_404(id)
    # app.logger.debug(f'Person: {person}')
    return render_template('detail.html', person=person)

@app.route('/add', methods=['POST', 'GET'])
def add():
    person = Person()
    person_form = PersonForm(obj=person)
    if request.method == 'POST':
        if person_form.validate_on_submit():
            person_form.populate_obj(person)
            app.logger.debug(f'Person to insert: {person.first_name}')
            # INSERT
            db.session.add(person)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('add.html', form=person_form)


@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    person = Person.query.get_or_404(id)
    person_form = PersonForm(obj=person)
    if request.method == 'POST':
        if person_form.validate_on_submit():
            person_form.populate_obj(person)
            app.logger.debug(f'Person to update: {person.first_name}')
            # UPDATE
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('edit.html', form=person_form)


@app.route('/delete/<int:id>')
def delete(id):
    person = Person.query.get_or_404(id)
    app.logger.debug(f'Person to delete: {person.first_name}')
    # UPDATE
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for('home'))

