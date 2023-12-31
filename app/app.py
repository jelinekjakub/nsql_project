from flask import Flask
from extensions.env import Config

# App init
app = Flask(__name__)
app.secret_key = Config().get("APP_KEY")

# Database
from extensions.db import db

# Seeders
import seeders.user_seeder
import seeders.recipes_seeder

# Routes
from app.routes import bp
app.register_blueprint(bp)
print(Config().get("APP_DEBUG"))
if __name__ == '__main__':
    app.run(debug=False, host=Config().get("APP_HOST", "0.0.0.0"), port=Config().get("APP_PORT", 5000))



