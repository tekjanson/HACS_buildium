import sys

# import struct
# import re
# import os.path
# import argparse
# import os
import json
import yaml
import requests
from time import time, sleep, localtime, strftime


@service
def property_unit_pull(
    buildium_client_id=None,
    buildium_client_secret=None,
):
    """hello_world example using pyscript."""
    payload = {}
    headers = {
        "Content-Type": "application/json",
        "X-BUILDIUM-CLIENT-ID": buildium_client_id,
        "X-BUILDIUM-CLIENT-SECRET": buildium_client_secret,
    }
    events = task.executor(
        requests.get,
        "https://publicapi.buildiumstaging.com/v1/rentals/units",
        headers=headers,
        data=payload,
    )
    response = events.json()
    # log.info(f"sent {payload} {headers}")
    # log.info(f"stuff {str(events.content)}")
    fruits_list_x = {}
    for x in response:
        # log.info(f"zzz {x.keys()}")
        Id = x["Id"]
        PropertyId = x["PropertyId"]
        BuildingName = x["BuildingName"]
        unit = "unit_" + BuildingName
        property = "property_" + BuildingName
        dict_file = {
            # "input_text": {
            unit.replace(" ", "_")
            .replace("'", "_")
            .lower(): {
                "name": unit.replace(" ", "_").replace("'", "_").lower(),
                "initial": Id,
                "min": -10000,
                "max": 100000000,
                "mode": "box",
                "step": 1,
            },
            property.replace(" ", "_")
            .replace("'", "_")
            .lower(): {
                "name": property.replace(" ", "_").replace("'", "_").lower(),
                "initial": PropertyId,
                "min": -10000,
                "max": 100000000,
                "mode": "box",
                "step": 1,
            },
            # }
        }
        fruits_list_x.update(dict_file)
    input_text = {"input_number": fruits_list_x}
    log.info(f"unit id : {input_text}")

    config_yaml = "/config/configuration.yaml"

    # log.info(
    #     f"unit id : {Id}, PropertyId : {PropertyId}, BuildingName : {BuildingName}"
    # )
    with open(config_yaml, "r") as sources:
        lines = sources.readlines()
    with open(config_yaml, "w") as sources:
        for line in lines:
            if "!include" in line:
                _LOGGER.info("skipping!")
            else:
                sources.write(line)

    with open(config_yaml, "r+") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        fruits_list = yaml.load(file, Loader=yaml.FullLoader)
        input_text["input_text"] = {}
        input_text["input_text"]["client_id"] = {
            "name": "client_id",
            "initial": fruits_list["input_text"]["client_id"]["initial"],
        }
        input_text["input_text"]["client_secret"] = {
            "name": "client_secret",
            "initial": fruits_list["input_text"]["client_secret"]["initial"],
            "mode": "password",
        }
        fruits_list.update(input_text)

        # "client_id": {
        #     "name": "client_id",
        #     "initial": config_entry.data.get(CONF_BUILDIUM_SECRET, False),
        #     "mode": "password",
        # },
        # "client_secret": {
        #     "name": "client_secret",
        #     "initial": config_entry.data.get(CONF_BUILDIUM_CLIENT_ID, False),
        #         },
        # file.write(yaml.safe_dump(fruits_list))

    with open(config_yaml, "w") as myfile:
        myfile.write(yaml.safe_dump(fruits_list))
        # yaml.safe_dump(fruits_list, file)

    with open(config_yaml, "a") as myfile:
        myfile.write("group: !include groups.yaml\n")
        myfile.write("automation: !include automations.yaml\n")
        myfile.write("script: !include scripts.yaml\n")
        myfile.write("scene: !include scenes.yaml\n")