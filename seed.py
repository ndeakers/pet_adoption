from models import Pet, db

db.drop_all()
db.create_all()

Pet.query.delete()

fluffy_pic = "https://images.theconversation.com/files/350865/original/file-20200803-24-50u91u.jpg?ixlib[…]t=37%2C29%2C4955%2C3293&q=45&auto=format&w=926&fit=clip"

fluffy = Pet(pet_name='Fluffy',
             species='cat',
             photo_url=fluffy_pic,
             age='baby',
             notes="likes to sit on your mouse when you're working")

db.session.add(fluffy)
db.session.commit()
