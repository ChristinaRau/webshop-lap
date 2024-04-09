from sqlalchemy import select
from sqlalchemy.orm import Session
from .app import app
from flask import request, session as flask_session, make_response, jsonify
from flask_login import LoginManager, login_user, logout_user, current_user
from .models.user import User
from .config import PEPPER, DB_URI
import bcrypt
from .db import engine

# login

login_manager = LoginManager()
# registers after_request call and attaches LoginManager to it (app.login_manager)
login_manager.init_app(app)


@app.route("/login", methods=["POST"])
def login():
    # user = User.query.filter_by(username=request.form.get("username")).first()

    statement = select(User).where(User.username == request.form.get("username"))
    session = Session(engine)
    user = session.scalars(statement).first()

    if user is not None and bcrypt.checkpw(
        (request.form.get("password", "") + PEPPER).encode(), user.password.encode()
    ):
        # user.is_authenticated = True
        # db.session.add(user)
        # db.session.commit()

        login_user(user, remember=True, force=True)

        print("actual user id", user.id)
        flask_session["user_id"] = user.id
        print("session user id", flask_session.get("user_id", -1))

        #  current_user = user
        print("logged in user:", user)
        print("logged in current user:", current_user)
        return jsonify({"username": user.username, "id": user.id})
    return make_response("Wrong password", 401)


@app.get("/check_login")
def check_login():
    print(current_user)
    print(current_user.is_authenticated)

    if current_user.is_authenticated:
        return jsonify({"is_authenticated": True})
    return jsonify({"is_authenticated": False})


@app.route("/logout")
def logout():
    logout_user()
    flask_session.pop("user_id", default=None)
    return "Logged out"


@app.route("/register", methods=["POST"])
def register():
    hashed_password = bcrypt.hashpw(
        (request.form.get("password", "") + PEPPER).encode(), bcrypt.gensalt(14)
    )
    # user = User(username=request.form.get("username"), password=hashed_password)
    print(request.form)
    # object in transient state
    user = User(username=request.form.get("username"), password=hashed_password)
    with Session(engine, expire_on_commit=False) as session:
        # object in pending state (look at session.new)
        session.add(user)
        # object in persistent state
        session.commit()

    return jsonify({"username": user.username, "id": user.id})
