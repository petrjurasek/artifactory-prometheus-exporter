# Prometheus exporter for Artifactory

Exposes metrics for [Artifactory](https://jfrog.com/artifactory/) from its 
[REST API](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API) to 
[Prometheus endpoint](https://prometheus.io/docs/prometheus/latest/getting_started/#configuring-prometheus-to-monitor-itself).

This project is heavily inspired by <https://github.com/m4h/prometheus>.

## Configuration 

This exporter needs following environment variables to run correctly:

### Required

* ```ARTIFACTORY_URL``` - URL of Artifactory instance e.g. ```https://acme.jfrog.io/acme```.
* ```ARTIFACTORY_USER``` - Artifactory user.
* ```ARTIFACTORY_PASSWORD```  - Artifactory password.

### Optional

* ```APP_PORT``` - the port on which exporter listens, defaults ot 9600. 
* ```APP_INTERVAL``` - interval in seconds for getting metrics from Artifactory REST API.
* ```APP_LOG_LEVEL``` - log level.

## Docker

Run from Docker Hub:

```docker run -p 9600:9600 -e ARTIFACTORY_URL=http://artifactory -e ARTIFACTORY_USER=admin -e ARTIFACTORY_PASSWORD=admin petrjurasek/artifactory-prometheus-exporter```

Build and run docker image:

```docker build -t <image-name> .```
```docker run -p 9600:9600 -e ARTIFACTORY_URL=http://artifactory -e ARTIFACTORY_USER=admin -e ARTIFACTORY_PASSWORD=admin <image-name>```

## Metrics

Metrics are then available on listening port and examples can be found in [METRICS](docs/METRICS.md) page.

## Development

### Requirements

* python 3.5 is required.
* pipenv to be installed (```pip install pipenv```).
* run ```pipenv shell``` to switch to virtual env, then run ```pipenv install```. 


### Formatting code

Install dev dependcies ```pipenv install --dev``` and run ```yapf``` formatter - ```yapf -r . --in-place```.
