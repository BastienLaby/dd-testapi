import time
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dd.test.bitcoin')

from datadog import initialize, api


options = {
    "api_key": "<>",
    "app_key": "<>",
    "api_host": "https://api.datadoghq.com",
}

initialize(**options)


while True:

    r = requests.get("http://api.coindesk.com/v1/bpi/currentprice.json")

    if r.status_code:

        data = r.json()

        logger.info(f'{data["time"]["updated"]} ')

        for devise, deviseData in data["bpi"].items():

            logger.info(f'{devise} {deviseData["rate_float"]}')

            api.Metric.send(
                metric="money.bitcoin.value",
                points=float(deviseData["rate_float"]),
                host="api.coindesk.com",
                tags=[
                    deviseData["code"],
                    deviseData["description"]
                ],
            )
    else:
        logger.error(f'Fail to GET api.coindesk.com : {r.status_code}')

    time.sleep(10)
