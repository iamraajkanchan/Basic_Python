from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from waitress import serve

app = Flask(__name__)

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# JWT config
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # change this in production!

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)

# Import and register blueprints
try:
    from login import login_bp
    from routes import todo_bp
    app.register_blueprint(login_bp)
    app.register_blueprint(todo_bp)
except Exception as e:
    print(f"Blueprint import failed: {e}")

# Health routes
@app.route("/")
def index():
    return "<h2>ToDo API is running. Try /login or /todos</h2>"

@app.route("/ping")
def ping():
    return "pong"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    serve(app, host="0.0.0.0", port=8080)
