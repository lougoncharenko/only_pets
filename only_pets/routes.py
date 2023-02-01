from only_pets.extensions import app, db
from only_pets.routes import main

app.register_blueprint(main)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
