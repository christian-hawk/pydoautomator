from requests import Session


class ApiAdapter:
    """Prepare requests connection as request.session.Session instance
    """
    token = ''
    headers = {}
    __session = Session()

    def __init__(self, token: str):
        """Construtor: Prepare requests connection as
        request.session.Session instance

        :param token: Digital Ocean Token
        :type token: str
        """
        self.token = token
        self.headers = {'Authorization': 'Bearer ' + self.token}
        self.__session.headers.update(self.headers)
        self.requests = self.__session
