from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm
from project_secrets import FLASK_SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = FLASK_SECRET_KEY
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_homepage():
    return render_template("home_page.html")


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding pets."""

    form = AddPetForm()

    if form.validate_on_submit():
        pet_name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(pet_name=pet_name,
                  species=species,
                  photo_url=photo_url,
                  age=age,
                  notes=notes)

        db.session.add(pet)
        db.session.commit()
        return redirect("/add")
    else:
        return render_template("pet_add_form.html", form=form)
