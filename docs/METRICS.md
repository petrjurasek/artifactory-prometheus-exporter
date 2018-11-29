# Example metrics

```
# HELP artifactory_artifacts_downloaded Downloaded artifacts
# TYPE artifactory_artifacts_downloaded gauge
artifactory_artifacts_downloaded{key="example-repo-local",minutes_ago="1"} 0.0
artifactory_artifacts_downloaded{key="example-repo-local",minutes_ago="60"} 0.0
artifactory_artifacts_downloaded{key="example-repo-local",minutes_ago="5"} 0.0
# HELP artifactory_artifacts_created Created artifacts
# TYPE artifactory_artifacts_created gauge
artifactory_artifacts_created{key="example-repo-local",minutes_ago="1"} 0.0
artifactory_artifacts_created{key="example-repo-local",minutes_ago="60"} 0.0
artifactory_artifacts_created{key="example-repo-local",minutes_ago="5"} 0.0
# HELP artifactory_repository_files_count Artifactory repository file count
# TYPE artifactory_repository_files_count gauge
artifactory_repository_files_count{key="example-repo-local",type="LOCAL"} 0.0
# HELP artifactory_security_users Number of artifactory users
# TYPE artifactory_security_users gauge
artifactory_security_users{realm="internal"} 4.0
# HELP artifactory_security_groups Number of artifactory groups
# TYPE artifactory_security_groups gauge
artifactory_security_groups 1.0
# HELP artifactory_system_licence Licence information
# TYPE artifactory_system_licence gauge
artifactory_system_licence{expires="Dec 21, 2018"} 21.0
# HELP artifactory_system_revision Version information
# TYPE artifactory_system_revision gauge
artifactory_system_revision{version="6.5.8"} 60508900.0
```
