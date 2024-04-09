from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import (
    MetaData,
    select,
    func,
    create_engine,
)
from flask_login import LoginManager, login_user, logout_user
from .config import PEPPER, DB_URI
import bcrypt

app = Flask(__name__)
# db config
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
# image upload config
app.config["UPLOAD_FOLDER"] = "./images"

# cross origin
CORS(
    app,
    origins="http://localhost:5173/*",
    supports_credentials=True,
)

# needed for session https://flask.palletsprojects.com/en/3.0.x/quickstart/#sessions
app.secret_key = b"12c94f7cc774abab813afe4cce94c348ba02b07d46b5a5e2752e68a4e1d857a0"

metadata_obj = MetaData()


@app.route("/")
def hello_world():
    return "Hello world"


# import sys

# import sys
# from pathlib import Path # if you haven't already done so
# file = Path(__file__).resolve()
# parent, root = file.parent, file.parents[1]
# sys.path.append(str(root))

# print(root)

# # Additionally remove the current file's directory from sys.path
# try:
#     print(parent)
#     sys.path.remove(str(parent))
# except ValueError: # Already removed
#     pass
