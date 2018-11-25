class AppOptions:
    def __init__(self, port: int, interval: int):
        self.__port = port
        self.__interval = interval

    def port(self) -> int:
        return self.__port

    def interval(self) -> int:
        return self.__interval
