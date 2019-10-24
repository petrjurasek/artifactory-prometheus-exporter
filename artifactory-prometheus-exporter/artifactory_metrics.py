from prometheus_client import Gauge


class ArtifactoryMetrics:
    def __init__(self):
        self.__users = Gauge("artifactory_security_users",
                             "Number of artifactory users", ['realm'])
        self.__groups = Gauge("artifactory_security_groups",
                              "Number of artifactory groups")
        self.__license = Gauge("artifactory_system_licence",
                               "Licence information", ['expires'])
        self.__version = Gauge("artifactory_system_revision",
                               "Version information", ['version'])
        self.__created = Gauge("artifactory_artifacts_created",
                               "Created artifacts", ['minutes_ago', 'key'])
        self.__downloaded = Gauge("artifactory_artifacts_downloaded",
                                  "Downloaded artifacts",
                                  ['minutes_ago', 'key'])
        self.__repositories = Gauge("artifactory_repository_files_count",
                                    "Artifactory repository file count",
                                    ['key', 'type'])

    def users(self, count: int, realm: str):
        self.__users.labels(realm=realm).set(count)

    def groups(self, count: int):
        self.__groups.set(count)

    def license(self, valid_days_left: int, expires: str):
        self.__license.labels(expires=expires).set(valid_days_left)

    def version(self, revision: int, version: str):
        self.__version.labels(version=version).set(revision)

    def created(self, count: int, minutes_ago: str, key: str):
        self.__created.labels(minutes_ago=minutes_ago, key=key).set(count)

    def downloaded(self, count: int, minutes_ago: str, key: str):
        self.__downloaded.labels(minutes_ago=minutes_ago, key=key).set(count)

    def repositories(self, count: int, key: str, type: str):
        self.__repositories.labels(key=key, type=type).set(count)
