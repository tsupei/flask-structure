# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from config import init_db
from api import hello_api, term_api, law_api, opinion_api

def main():
    app = Flask(__name__)
    # Cross-Origin Resource Sharing
    CORS(app)

    # Settings
    app.config["ip"] = "127.0.0.1"
    app.config["port"] = "47000"
    # app.config["db"] =
    # app.config["env"] =
    # ...

    prefix = "/{}/{}/{}".format("autocomplete", "api", "v1")

    # current app
    with app.app_context():
        init_db()

        # register api
        app.register_blueprint(hello_api, url_prefix=prefix)
        app.register_blueprint(term_api, url_prefix=prefix)
        app.register_blueprint(law_api, url_prefix=prefix)
        app.register_blueprint(opinion_api, url_prefix=prefix)


    app.run(host="127.0.0.1", port="47000", threaded=True)


if __name__ == "__main__":
    main()
