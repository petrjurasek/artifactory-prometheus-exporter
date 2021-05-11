import sys
import os
sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vendor'))
sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src'))


import configargparse
import logging
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
    '--app-log-level', env_var='APP_LOG_LEVEL', default=logging.INFO, type=str)
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

logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S',
    level=options.app_log_level,
    stream=sys.stdout)
logger = logging.getLogger()

app_options = AppOptions(options.app_port, options.app_interval)
artifactory_metrics = ArtifactoryMetrics()
artifactory_options = ArtifactoryOptions(options.artifactory_url,
                                         options.artifactory_user,
                                         options.artifactory_password)
artifactory_api_client = ArtifactoyApiClient(artifactory_options)
artifactory_metrics_updater = ArtifactoryMetricsUpdater(artifactory_api_client)


def exception_handler(loop, context):
    loop.default_exception_handler(context)

    exception = context.get('exception')
    if isinstance(exception, Exception):
        logger.error(exception)
        loop.stop()


async def update_metrics():
    while True:
        logger.info('Updating metrics')
        artifactory_metrics_updater.update(artifactory_metrics)

        await asyncio.sleep(app_options.interval())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start_http_server(app_options.port())

    loop.set_exception_handler(exception_handler)
    loop.create_task(update_metrics())
    try:
        loop.run_forever()

    except KeyboardInterrupt:
        logger.info('Caught keyboard interrupt')
        loop.close()
    finally:
        logger.info('Closing loop')
        loop.close()
