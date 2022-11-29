from django.http import HttpResponse
import json
import logging
from .policy import service_config, location, avatar, reg

def service_configuration(request):
    logging.info(request)
    response = HttpResponse(json.dumps(service_config(request)), content_type="application/json")

    return response

def participant_location(request):
    logging.info(request)
    response = HttpResponse(json.dumps(location(request)), content_type="application/json")

    return response

def participant_avatar(request):
    logging.info(request)
    response = HttpResponse(json.dumps(avatar(request)), content_type="application/json")

    return response

def registrations(request):
    logging.info(request)
    response = HttpResponse(json.dumps(reg(request)), content_type="application/json")

    return response
