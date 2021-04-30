from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from project_secrets import FLASK_SECRET_KEY
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_homepage():
    """Show pet adoption homepage"""

    pets = Pet.query.all()
    return render_template("home_page.html", pets=pets)


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


@app.route('/<int:pet_id_number>', methods=["GET", "POST"])
def show_pet(pet_id_number):
    """Shows a pet and it's edit form"""

    pet = Pet.query.get_or_404(pet_id_number)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f'/{pet_id_number}')
    else:
        return render_template("pet_display.html", pet=pet, form=form)
