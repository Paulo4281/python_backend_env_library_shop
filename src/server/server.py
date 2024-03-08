from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from src.database.database_config import *
from os import getenv
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from src.server.imports import *

load_dotenv()

# ------------------------------------------------------------------------------------------------------------------
# App Server & Cors ------------------------------------------------------------------------------------------------------------------

app = Flask(__name__, template_folder="../templates", static_folder="../templates/assets")
CORS(app, origins="*", send_wildcard=True)

# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------
# Routes Blueprint ------------------------------------------------------------------------------------------------------------------

    # View Routes
app.register_blueprint(view_routes)

    # User Routes
app.register_blueprint(user_routes)

    # Book Routes
app.register_blueprint(book_routes)
app.register_blueprint(category_routes)
app.register_blueprint(review_routes)

# End Routes Blueprint ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------
# App Config Credentials ------------------------------------------------------------------------------------------------------------------

app.config["CORS_HEADERS"] = getenv("APP_CORS_HEADERS")
app.config["SECRET_KEY"] = getenv("APP_SECRET_KEY")
app.config["RESTX_MASK_SWAGGER"] = False
app.config["JWT_SECRET_KEY"] = getenv("TOKEN_SECRET")

# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

# JWT Manager

JWTManager(app)

# ------------------------------------------------------------------------------------------------------------------
# API Config ------------------------------------------------------------------------------------------------------------------

api = Api(
    title="Flask RESTFul API",
    version="1.0",
    description="Description",
    doc="/docs"
)

# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# API Namespaces ------------------------------------------------------------------------------------------------------------------

    # User Namespaces
api.add_namespace(user_namespace, path="/user")

    # Book Namespaces
api.add_namespace(book_namespace, path="/book")
api.add_namespace(category_namespace, path="/book/category")
api.add_namespace(author_namespace, path="/book/author")
api.add_namespace(review_namespace, path="/book/review")

# ------------------------------------------------------------------------------------------------------------------
# API Init ------------------------------------------------------------------------------------------------------------------

api.init_app(app)

# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------