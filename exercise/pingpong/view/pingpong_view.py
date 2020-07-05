from flask import (
    request,
    jsonify,
    Blueprint,
)

from pingpong.service.pingpong_service import PingPongService

class PingPongView:

    """ 핑퐁 뷰
    
    Authors:
        shlee@gracefulrain.co
        jjuggumih@gmail.com
    
    History:
        2020-06-28 (jjuggumih@gmail.com): 초기 생성
        2020-06-28 (shlee@gracefulrain.co): flask 레이어 분리

    """

    pingpong_app = Blueprint('pingpong_app', __name__, url_prefix = '/ping')

    @pingpong_app.route('', methods = ['GET'])
    def ping():
        pingpong_service = PingPongService()
        result = pingpong_service.ping()

        return result
