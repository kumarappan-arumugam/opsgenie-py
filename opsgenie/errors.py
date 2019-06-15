from __future__ import absolute_import
import json

class OpsGenieError(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)

class InvalidRequestError(OpsGenieError):
    pass

class ApiKeyMissingError(OpsGenieError):
    def __init__(self):
        super(ApiKeyMissingError, self).__init__('Api Key is not configured!')

class EndpointMissingError(OpsGenieError):
    def __init__(self):
        super(EndpointMissingError, self).__init__('OpsGenie end-point is not configured!')

class InvalidConfigurationError(OpsGenieError):
    def __init__(self, message):
        super(InvalidConfigurationError, self).__init__(message)

class ServerError(OpsGenieError):
    def __init__(self, json_str):
        try:
            self.json_obj = json.loads(json_str)
            self.message = self.json_obj.get('message', None)
            self.requestId = self.json_obj.get('requestId', None)
        except ValueError:
            self.message = json_str
        super(ServerError, self).__init__(self.message)
        self.code = -1
