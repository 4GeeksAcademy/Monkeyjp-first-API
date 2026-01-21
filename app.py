from flask import Flask
from routes import character_bp

app = Flask(__name__)
#le indica a flask que el conte4xto actual existe. documentacion de flask

#CRUD
# create read update delete

#esto va despues
app.register_blueprint(character_bp)

#esto si va al inicio
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
