# Example metrics

```
# HELP artifactory_artifacts_created Created artifacts
# TYPE artifactory_artifacts_created gauge
artifactory_artifacts_created{minutes_ago="5"} 28.0
artifactory_artifacts_created{minutes_ago="1"} 0.0
artifactory_artifacts_created{minutes_ago="60"} 30.0
# HELP artifactory_system_revision Version information
# TYPE artifactory_system_revision gauge
artifactory_system_revision{version="6.2.0"} 60200900.0
# HELP artifactory_system_licence Licence information
# TYPE artifactory_system_licence gauge
artifactory_system_licence{expires="Dec 21, 2018"} 24.0
# HELP artifactory_artifacts_downloaded Downloaded artifacts
# TYPE artifactory_artifacts_downloaded gauge
artifactory_artifacts_downloaded{minutes_ago="5"} 6.0
artifactory_artifacts_downloaded{minutes_ago="1"} 0.0
artifactory_artifacts_downloaded{minutes_ago="60"} 7.0
# HELP artifactory_security_users Number of artifactory users
# TYPE artifactory_security_users gauge
artifactory_security_users{realm="internal"} 14.0
# HELP artifactory_security_groups Number of artifactory groups
# TYPE artifactory_security_groups gauge
artifactory_security_groups 11.0
```
