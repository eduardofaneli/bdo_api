from flask import Blueprint
from routes.boss import BossRoutes

boss_table  = Blueprint('boss_table', __name__, url_prefix="/boss")

@boss_table.route('/', methods=["GET"])
def index():
    return BossRoutes().get_table()

@boss_table.route('/<day>', methods=['GET'])
def boss_by_day(day):
    return BossRoutes().get_by_day(day)

@boss_table.route('/today', methods=['GET'])
def boss_today():
    return BossRoutes().get_today()        