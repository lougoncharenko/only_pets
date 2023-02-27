from only_pets.extensions import app, db
from only_pets.main.routes import main
from only_pets.auth.routes import auth

app.register_blueprint(main)
app.register_blueprint(auth)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=3000)
