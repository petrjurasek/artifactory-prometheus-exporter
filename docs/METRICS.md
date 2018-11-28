# Example metrics

```
# HELP artifactory_artifacts_created Created artifacts
# TYPE artifactory_artifacts_created gauge
artifactory_artifacts_created{minutes_ago="1"} 1.0
artifactory_artifacts_created{minutes_ago="60"} 18.0
artifactory_artifacts_created{minutes_ago="5"} 1.0
# HELP artifactory_security_groups Number of artifactory groups
# TYPE artifactory_security_groups gauge
artifactory_security_groups 12.0
# HELP artifactory_repository_files_count Artifactory repository file count
# TYPE artifactory_repository_files_count gauge
artifactory_repository_files_count{key="example-repo-local",type="LOCAL"} 8.0
# HELP artifactory_security_users Number of artifactory users
# TYPE artifactory_security_users gauge
artifactory_security_users{realm="ldap"} 32.0
artifactory_security_users{realm="internal"} 17.0
# HELP artifactory_system_licence Licence information
# TYPE artifactory_system_licence gauge
artifactory_system_licence{expires="Mar 8, 2019"} 99.0
# HELP artifactory_system_revision Version information
# TYPE artifactory_system_revision gauge
artifactory_system_revision{version="6.0.0"} 60000900.0
# HELP artifactory_artifacts_downloaded Downloaded artifacts
# TYPE artifactory_artifacts_downloaded gauge
artifactory_artifacts_downloaded{minutes_ago="1"} 2138.0
artifactory_artifacts_downloaded{minutes_ago="60"} 2495.0
artifactory_artifacts_downloaded{minutes_ago="5"} 2161.0
```
