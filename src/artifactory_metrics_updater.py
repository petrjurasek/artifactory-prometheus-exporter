from artifactory_api_client import ArtifactoyApiClient
from artifactory_metrics import ArtifactoryMetrics
import datetime


class ArtifactoryMetricsUpdater:
    def __init__(self, api_client: ArtifactoyApiClient):
        self.__api_client = api_client

    def update(self, metrics: ArtifactoryMetrics):
        for realm, count in self.__api_client.users().items():
            metrics.users(count, realm)

        metrics.groups(self.__api_client.groups())

        licences = self.__api_client.license()
        metrics.license(licences[0], licences[1])

        version = self.__api_client.version()
        metrics.version(version[0], version[1])

        for minutes_ago in [1, 5, 60]:
            date_ago = datetime.datetime.now() - datetime.timedelta(
                minutes=minutes_ago)

            metrics.downloads(
                self.__api_client.search_downloaded_since(date_ago),
                str(minutes_ago))
