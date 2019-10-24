from artifactory_api_client import ArtifactoyApiClient
from artifactory_metrics import ArtifactoryMetrics
import datetime


class ArtifactoryMetricsUpdater:
    def __init__(self, api_client: ArtifactoyApiClient):
        self.__api_client = api_client
        self.__search_minutes_intervals = [1, 5, 60]

    def update(self, metrics: ArtifactoryMetrics):
        for realm, count in self.__api_client.users().items():
            metrics.users(count, realm)

        metrics.groups(self.__api_client.groups())

        licences = self.__api_client.license()
        metrics.license(licences[0], licences[1])

        version = self.__api_client.version()
        metrics.version(version[0], version[1])

        repositories = self.__api_client.repositories()
        for repository, data in repositories.items():
            metrics.repositories(data[0], repository, data[1])

            for minutes_ago in self.__search_minutes_intervals:
                date_ago = datetime.datetime.now() - datetime.timedelta(
                    minutes=minutes_ago)

                created = self.__api_client.search_created_since(
                    date_ago, repository)

                metrics.created(created, str(minutes_ago), repository)

                downloaded = self.__api_client.search_downloaded_since(
                    date_ago, repository)

                metrics.downloaded(downloaded, str(minutes_ago), repository)
