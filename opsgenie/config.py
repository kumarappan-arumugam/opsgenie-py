from __future__ import absolute_import
from .errors import (
    ApiKeyMissingError,
    EndpointMissingError,
)


class Configuration:
    DEFAULT_ENDPOINT = 'https://api.opsgenie.com/v2'

    def __init__(self, apikey=None, endpoint=DEFAULT_ENDPOINT, http_config=None):
        """
        Configuration for OpsGenie client
        Parameters
        ----------
        apikey : str
            OpsGenie API KEY
        endpoint : str, optional
            OpsGenie WebApi url to use with OpsGenie client. (Default: http://api.opsgenie.com/v2)
        http_config : HttpConfiguration or dict
        """
        self.api_key = apikey
        self.endpoint = endpoint
        self.api_key_prefix = 'GenieKey'

        if http_config:
            if isinstance(http_config, HttpConfiguration):
                self.http_config = http_config
            else:
                self.http_config = HttpConfiguration(**http_config)
        else:
            self.http_config = HttpConfiguration()

    def validate(self):
        if not self.api_key:
            raise ApiKeyMissingError()

        if not self.endpoint:
            raise EndpointMissingError()

        self.http_config.validate()


class HttpConfiguration:
    DEFAULT_TIMEOUT = 30
    DEFAULT_MAX_RETRY = 5

    def __init__(self, connect_timeout=DEFAULT_TIMEOUT, read_timeout=DEFAULT_TIMEOUT, max_retry=DEFAULT_MAX_RETRY):
        """
        Http Configuration to use with OpsGenie client
        Parameters
        ----------
        connect_timeout : int, optional
            Connection timeout (Default: 30)
        read_timeout : int, optional
            Read timeout (Default: 30)
        max_retry : int, optional
            Retry count of the failed requests (excluding first request). (Default:5)
        """
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout
        self.max_retry = max_retry

    def validate(self):
        pass
