""" Layer service """

from geetiles.errors import LayerNotFound

from geetiles.utils.request import request_to_eacw_api


class LayerService(object):
    @staticmethod
    def execute(config):
        response = request_to_eacw_api(config)
        if not response or response.get('errors'):
            raise LayerNotFound(message='Layer not found')

        return response

    @staticmethod
    def get(layer):
        config = {
            'uri': '/layers/' + layer + "/",
            'method': 'GET'
        }
        return LayerService.execute(config)
