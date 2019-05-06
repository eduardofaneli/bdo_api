from flask import jsonify
from datetime import date
import json, os
from pathlib import Path

class BossRoutes(object):
    def __init__(self):        
        self.boss_json = self.load_json().get("days")
        self.full_json = self.load_json()

    def load_json(self):
        try:                                
            file = open('./routes/table_boss.json', encoding='UTF-8').read()                    
            return json.loads(file)            
        except Exception as ex:                    
            return jsonify({'success': False, 'message': ex.args}), 401    

    def get_table(self):
        try:            
            return jsonify(self.full_json), 200
        except Exception as ex:
            return jsonify({'success': False, 'message': ex.args}), 401   

    def get_today(self):
        try:
            return jsonify(self.boss_json[date.today().weekday()]), 200
        except Exception as ex:
            return jsonify({'success': False, 'message': ex.args}), 401    

    def get_by_day(self, day):
        try:            
                            
            return jsonify(self.boss_json[int(day) - 1]), 200
        except Exception as ex:
            return jsonify({'success': False, 'message': ex.args}), 401    

