from flask import jsonify
from datetime import date
import json, os

class BossTable(object):
    def __init__(self):
        pass

    def load_json(self):
        try:
            file = open('./table_new.json', encoding='UTF-8').read()
            return json.loads(file)            
        except Exception as ex:
            return jsonify({'success': False, 'message': ex.args}), 401    

    def get_table(self):
        try:
            return jsonify(self.load_json()), 200
        except Exception as ex:
            return jsonify({'success': False, 'message': ex.args}), 401   

    def get_today(self):
        try:
            return jsonify(self.load_json()[date.today().weekday()]), 200
        except Exception as ex:
            return jsonify({'success': False, 'message': ex.args}), 401    

    def get_by_day(self, day):
        try:
            return jsonify(self.load_json()[int(day)]), 200
        except Exception as ex:
            return jsonify({'success': False, 'message': ex.args}), 401    

