from restplus import api
from flask_restplus import Resource, fields
from business.boss_bo import BossRoutes

ns_boss = api.namespace('boss', description='Operações referente a tabela de boss')

@ns_boss.route('/')
class BossTable(Resource):
    def get(self):
        return BossRoutes().get_table()

@ns_boss.route('/<int:day>')
@api.response(404, 'Day not found.')
class BossDay(Resource):    
    def get(self, day):        
        return BossRoutes().get_by_day(day)

@ns_boss.route('/today')
class BossToday(Resource):
    def get(self):
        return BossRoutes().get_today()