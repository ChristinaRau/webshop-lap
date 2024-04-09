from .app import app

from .authentication import *

# from stats import *
# from .controllers.computer_controller import *
from flask_cors import CORS
from .controllers.base_controllers import *
from .controllers.order_controller import *
from .upload import *

from werkzeug.middleware.proxy_fix import ProxyFix

application = app

# DON'T FORGET TO INCLUDE CREDENTIALS ON FETCH!!!
# fetch("http://localhost:5000/projects", {method: "GET", mode: "cors", credentials: "include"})

if __name__ == "__main__":
    CORS(
        application,
        origins="http://localhost:5173/*",
        supports_credentials=True,
    )

    # this user_loader callback is used to reload user object from user ID (stored in session)
    @login_manager.user_loader
    def user_loader(user_id):
        print("LOAD USER")
        # returns None if user_id is not valid
        try:
            statement = select(User).where(User.id == user_id)
            session = Session(engine)
            user = session.scalars(statement).first()

            return user
        except:
            return None

    application.run()
