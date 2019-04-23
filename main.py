# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_cors import CORS
from boss_table import BossTable

app = Flask(__name__)

cors = CORS(app, resources = {r"/*": {"origins": "*"}})

@app.route('/', methods=["GET"])
def boss_table():          
    return BossTable().get_table()

@app.route('/<day>', methods=['GET'])
def boss_by_day(day):
    return BossTable().get_by_day(day)

@app.route('/today', methods=['GET'])
def boss_today():
    return BossTable().get_today()    

if __name__ == "__main__":
    app.run()