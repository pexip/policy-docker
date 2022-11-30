import requests
import json
import re
import logging


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
        "action": "continue",
        "type": "media_location",
    }

    logging.info(policy_response)

    return policy_response


def avatar(request):
    call_info = request.GET.dict()
    logging.info(call_info)

    policy_response = {"status": "success", "action": "continue", "type": "avatar"}

    logging.info(policy_response)

    return policy_response


def reg(request):
    call_info = request.GET.dict()
    logging.info(call_info)

    policy_response = {
        "status": "success",
        "action": "continue",
        "type": "registrations",
    }

    logging.info(policy_response)

    return policy_response
