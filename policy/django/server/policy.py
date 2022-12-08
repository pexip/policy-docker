import requests
import json
import re
import logging
import base64


def service_config(request):
    call_info = request.GET.dict()
    logging.info(call_info)

    policy_response = {
        "status": "success",
        "action": "continue",
        "type": "service_config",
    }

    logging.info(policy_response)

    return policy_response


def location(request):
    call_info = request.GET.dict()
    logging.info(call_info)

    policy_response = {
        "status": "success",
        "result": {
            "location": "non_existent_location_to_force_fallback",
        },
        "type": "media_location",
    }

    logging.info(policy_response)

    return policy_response


def avatar(request, alias):
    call_info = request.GET.dict()
    logging.info(call_info)

    with open("/app/server/blank.jpg", "rb") as f:
        policy_response = base64.b64encode(f.read()).decode()

    logging.info(policy_response)

    return policy_response


def directory(request):
    call_info = request.GET.dict()
    logging.info(call_info)

    policy_response = {
        "status": "success",
        "result": [],
        "type": "directory",
    }

    logging.info(policy_response)

    return policy_response


def registration(request, alias):
    call_info = request.GET.dict()
    logging.info(call_info)

    policy_response = {
        "status": "success",
        "action": "continue",
        "result": {},
        "type": "registration",
    }

    logging.info(policy_response)

    return policy_response
