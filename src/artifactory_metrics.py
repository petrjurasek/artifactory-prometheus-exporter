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
        self.__binaries_count = Gauge("artifactory_binaries_count",
                                      "binariesCount")
        self.__binaries_size = Gauge("artifactory_binaries_size",
                                     "binariesSize")
        self.__artifacts_size = Gauge("artifactory_artifacts_size",
                                      "artifactsSize")
        self.__optimization = Gauge("artifactory_optimization",
                                    "optimization")
        self.__items_count = Gauge("artifactory_items_count",
                                   "itemsCount")
        self.__artifacts_count = Gauge("artifactory_artifacts_count",
                                       "artifactsCount")
        self.__storage_total_space = Gauge("artifactory_storage_total_space_bytes",
                                           "totalSpace", ['type', 'dir'])
        self.__storage_used_space = Gauge("artifactory_storage_used_space_bytes",
                                          "usedSpace", ['type', 'dir'])
        self.__storage_free_space = Gauge("artifactory_storage_free_space_bytes",
                                          "freeSpace", ['type', 'dir'])

        self.__created = Gauge("artifactory_artifacts_created",
                               "binariesCount", ['minutes_ago', 'key'])
        self.__downloaded = Gauge("artifactory_artifacts_downloaded",
                                  "Downloaded artifacts",
                                  ['minutes_ago', 'key'])
        self.__repositories = Gauge("artifactory_repository_files_count",
                                    "Artifactory repository file count",
                                    ['key', 'type'])
        self.__repo_size = Gauge("artifactory_repository_used_space_bytes",
                                 "Artifactory repository used_space_bytes",
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

    def repo_size(self, size: float, key: str, type: str):
        self.__repo_size.labels(key=key, type=type).set(size)

    def binaries_count(self, count: int):
        self.__binaries_count.set(count)

    def binaries_size(self, size: float):
        self.__binaries_size.set(size)

    def artifacts_size(self, size: float):
        self.__artifacts_size.set(size)

    def optimization(self, percent: float):
        self.__optimization.set(percent)

    def items_count(self, count: int):
        self.__items_count.set(count)

    def artifacts_count(self, count: int):
        self.__artifacts_count.set(count)

    def storage_total(self, size: float, type: str, directory: str):
        self.__storage_total_space.labels(type=type, dir=directory).set(size)

    def storage_used(self, size: float, type: str, directory: str):
        self.__storage_used_space.labels(type=type, dir=directory).set(size)

    def storage_free(self, size: float, type: str, directory: str):
        self.__storage_free_space.labels(type=type, dir=directory).set(size)
