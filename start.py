# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from api import hello_api


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

    prefix = "/{}/{}/{}".format("test", "api", "v1")
    app.register_blueprint(hello_api, url_prefix=prefix)
    app.run(host="127.0.0.1", port="47000", threaded=True)


if __name__ == "__main__":
    main()
