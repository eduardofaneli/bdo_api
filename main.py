# -*- coding: utf-8 -*-
from flask import Flask#, jsonify
from flask_cors import CORS

from boss_table.views import boss_table

app = Flask(__name__)
cors = CORS(app, resources = {r"/*": {"origins": "*"}})
app.register_blueprint(boss_table)

if __name__ == "__main__":
    app.run(debug=True)