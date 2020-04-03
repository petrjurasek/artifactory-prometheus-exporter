from artifactory_api_client import ArtifactoyApiClient
from artifactory_metrics import ArtifactoryMetrics
import datetime
from num_transform import bytesstr2float,  percentstr2float, remove_comma


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
        storage_info = self.__api_client.metadata()
        binaries = storage_info['binariesSummary']
        filesinfo = storage_info['fileStoreSummary']
        metrics.binaries_count(remove_comma(binaries['binariesCount']))
        metrics.binaries_size(bytesstr2float(binaries['binariesSize']))
        metrics.artifacts_size(bytesstr2float(binaries['artifactsSize']))
        metrics.optimization(percentstr2float(binaries['optimization']))
        metrics.items_count(remove_comma(binaries['itemsCount']))
        metrics.artifacts_count(remove_comma(binaries['artifactsCount']))
        metrics.storage_total(
            bytesstr2float(filesinfo['totalSpace']), filesinfo['storageType'], filesinfo['storageDirectory'])
        metrics.storage_used(
            bytesstr2float(filesinfo['usedSpace']), filesinfo['storageType'], filesinfo['storageDirectory'])
        metrics.storage_free(
            bytesstr2float(filesinfo['freeSpace']), filesinfo['storageType'], filesinfo['storageDirectory'])

        repositories = self.__api_client.repositories()
        for repository, data in repositories.items():
            metrics.repositories(data[0], repository, data[1])
            metrics.repo_size(data[2], repository, data[1])
            for minutes_ago in self.__search_minutes_intervals:
                date_ago = datetime.datetime.now() - datetime.timedelta(
                    minutes=minutes_ago)

                created = self.__api_client.search_created_since(
                    date_ago, repository)

                metrics.created(created, str(minutes_ago), repository)

                downloaded = self.__api_client.search_downloaded_since(
                    date_ago, repository)

                metrics.downloaded(downloaded, str(minutes_ago), repository)
