import traceback
from log import log
from flask_restplus import Api

api = Api(version="1.0", title="BDO API", description="API em desenvolvimento com informações referente ao Black Desert")

@api.errorhandler
def default_error_handler(e):
    message= "A unhandled exception ocurred."
    log.exception(message)
    return {"message": message}, 500