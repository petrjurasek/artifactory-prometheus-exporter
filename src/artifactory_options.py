class ArtifactoryOptions:
    def __init__(self, url: str, user: str, password: str):
        self.__url = url
        self.__user = user
        self.__password = password

    def api_url(self, path):
        return '{}/api{}'.format(self.__url, path)

    def user(self) -> str:
        return self.__user

    def password(self) -> str:
        return self.__password