import sys
import os
sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src'))

import configargparse
import asyncio
from prometheus_client import start_http_server
from app_options import AppOptions
from artifactory_metrics import ArtifactoryMetrics
from artifactory_options import ArtifactoryOptions
from artifactory_api_client import ArtifactoyApiClient
from artifactory_metrics_updater import ArtifactoryMetricsUpdater

parameters = configargparse.ArgParser()
parameters.add('--app-port', env_var='APP_PORT', default=9600, type=int)
parameters.add('--app-interval', env_var='APP_INTERVAL', default=60, type=int)
parameters.add(
    '--artifactory-url', env_var='ARTIFACTORY_URL', type=str, required=True)
parameters.add(
    '--artifactory-user', env_var='ARTIFACTORY_USER', type=str, required=True)
parameters.add(
    '--artifactory-password',
    env_var='ARTIFACTORY_PASSWORD',
    type=str,
    required=True)
options = parameters.parse_args()

app_options = AppOptions(options.app_port, options.app_interval)
artifactory_metrics = ArtifactoryMetrics()
artifactory_options = ArtifactoryOptions(options.artifactory_url,
                                         options.artifactory_user,
                                         options.artifactory_password)
artifactory_api_client = ArtifactoyApiClient(artifactory_options)
artifactory_metrics_updater = ArtifactoryMetricsUpdater(artifactory_api_client)


async def update_metrics():
    while True:
        artifactory_metrics_updater.update(artifactory_metrics)

        await asyncio.sleep(app_options.interval())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start_http_server(app_options.port())

    loop.create_task(update_metrics())
    try:
        loop.run_forever()

    except KeyboardInterrupt:
        loop.close()
    finally:
        loop.close()
