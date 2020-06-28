from pingpong.model.pingpong_dao import PingPongDao

class PingPongService:

    def ping(self):
        pingpong_dao = PingPongDao()
        result = pingpong_dao.ping()

        return result
