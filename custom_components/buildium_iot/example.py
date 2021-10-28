# import sys
# import struct
# import re
# import os.path
# import argparse
import requests
from time import time, sleep, localtime, strftime


@service
def hello_world(
    action=None,
    id=None,
    unit=None,
    property=None,
    Title=None,
    description=None,
    priority=None,
    buildium_client_id=None,
    buildium_client_secret=None,
):
    """hello_world example using pyscript."""
    log.info(
        f"hello world: got action {action} id {id} unit {unit} property {property} Title {Title} description {description} priority {priority} cid {buildium_client_id} cs {buildium_client_secret}"
    )
    sleep_period = 10

    payload = {
        "Title": Title,
        "Description": description,
        "CategoryId": 1684,
        "SubCategoryId": 8,
        "PropertyId": property,
        "UnitId": unit,
        "AssignedToUserId": 1171705,
        "TaskStatus": "New",
        "Priority": priority,
        "DueDate": "2019-08-24",
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br",
        "X-BUILDIUM-CLIENT-ID": buildium_client_id,
        "X-BUILDIUM-CLIENT-SECRET": buildium_client_secret,
    }
    events = task.executor(
        requests.post,
        "https://publicapi.buildiumstaging.com/v1/tasks/todorequests",
        json=payload,
        headers=headers,
    )
    log.info(f"sent {payload} {headers}")
    log.info(f"stuff {str(events)}")
