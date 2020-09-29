import json
import os

from requests import Session, Request

EACW_API_URL = os.getenv('EACW_API_URL')
API_VERSION = os.getenv('EACW_API_VERSION')


def request_to_eacw_api(config):
    """Request to eacw api method"""
    try:
        session = Session()
        request = Request(
            method=config.get('method'),
            url=EACW_API_URL + config.get('uri') if not API_VERSION else EACW_API_URL + '/' + API_VERSION + config.get(
                'uri'),
            headers={
                'content-type': 'application/json',
            },
            data=json.dumps(config.get('body'))
        )
        prepped = session.prepare_request(request)

        response = session.send(prepped)

    except Exception as error:
        raise error

    return response.json()
