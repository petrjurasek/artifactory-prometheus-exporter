import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
from artifactory_options import ArtifactoryOptions


class ArtifactoyApiClient:
    def __init__(self, options: ArtifactoryOptions):
        self.__options = options

    def users(self):
        users = self.__request('/security/users')[0]

        realms = {}

        for user in users:
            realm = user['realm']
            if realm not in realms:
                realms[realm] = 0
            realms[realm] += 1

        return realms

    def groups(self) -> int:
        return len(self.__request('/security/groups')[0])

    def license(self):
        licenses = self.__request('/system/licenses')[0]

        now = datetime.now()
        expiry = datetime.strptime(licenses['validThrough'], '%b %d, %Y')

        return (expiry - now).days, licenses['validThrough']

    def version(self):
        version = self.__request('/system/version')[0]

        return version['revision'], version['version']

    def search_created_since(self, since: datetime) -> int:
        response = self.__request(
            '/search/dates?dateFields=created&from={}000'.format(
                since.strftime("%s")))
        if response[1] == 200:
            return len(response[0]['results'])

        return 0

    def search_downloaded_since(self, since: datetime) -> int:
        response = self.__request(
            '/search/dates?dateFields=lastDownloaded&from={}000'.format(
                since.strftime("%s")))
        if response[1] == 200:
            return len(response[0]['results'])

        return 0

    def __request(self, url: str):
        auth = HTTPBasicAuth(self.__options.user(), self.__options.password())
        response = requests.get(self.__options.api_url(url), auth=auth)

        return json.loads(response.text), response.status_code
