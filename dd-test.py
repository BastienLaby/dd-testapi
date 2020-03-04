from datadog import initialize, api
import time

options = {
    "api_key": "<api_key>",
    "app_key": "<app_key>",
    "api_host": "https://api.datadoghq.eu",
}

initialize(**options)

bounds = {
    5: 1,
    6: 1,
    7: 2,
    8: 3,
    9: 9,
    10: 9,
    11: 4,
    12: 3,
    13: 10,
    14: 9,
    15: 9,
}

for y, deathCount in bounds.items():
    for count in range(deathCount):
        api.Metric.send(metric="platformer.death", points=y)
