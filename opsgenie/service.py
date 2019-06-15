from __future__ import absolute_import
import platform

import pkg_resources
from requests import session as Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry

from .errors import (
    InvalidRequestError,
    ServerError,
)
from .request import BaseRequest


def generate_timeout_and_retry(http_config):
    """
    Generate timeout and retry mechanism for requests to use
    Parameters
    ----------
    http_config : HttpConfiguration
    Returns
    -------
    tuple (tuple, Retry)
    """
    timeout = (http_config.connect_timeout, http_config.read_timeout)

    retry = Retry(total=http_config.max_retry, status_forcelist=[500, 501, 502, 503])

    return timeout, retry


def generate_user_agent():
    version = pkg_resources.get_distribution("opsgenie").version
    return "opsgenie-python-sdk/{0}; {1}/{2}; {3}".format(
                                                            version,
                                                            platform.system(),
                                                            platform.release(),
                                                            platform.python_version()
                                                        )


def parse_url_for_inline_params(request, url_suffix):
    url_suffix = url_suffix.split('/:')
    parts = []
    for part in url_suffix:
        if '/' in part:
            parts.append(part)
        else:
            parts.append(getattr(request, part))
    return '/'.join(parts)

def execute_http_call(method, url, params, retry, timeout, apiKey, apiKeyPrefix):
    """
    Executes http call using requests library
    Parameters
    ----------
    method : str
    url : str
    params : dict
    retry : Retry
    timeout : tuple
    Returns
    -------
    Response
    """
    # set session
    session = Session()
    session.mount('https://', HTTPAdapter(max_retries=retry))  # Documented in HTTPAdapter
    session.headers = {
        'Authorization': '{} {}'.format(apiKeyPrefix, apiKey),
        'Content-Type': 'application/json',
        'User-Agent': generate_user_agent(),
    }

    if method is "GET":
        response = session.get(url, params=params, timeout=timeout)
    elif method is "POST":
        response = session.post(url, json=params, timeout=timeout)
    else:
        raise NotImplementedError()

    return response


def execute(method, url_suffix, response_cls):
    """
    Executes http call with given parameters
    Parameters
    ----------
    method : {'POST'|'GET'}
    url_suffix : str
    response_cls : class
        Class of response type
    """

    def request_wrapper(__):
        def request_call(self, request):
            """
            Parameters
            ----------
            self : BaseService
            request : instance of BaseRequest subclass
            Returns
            -------
            Instance of response_cls
            """
            if not isinstance(request, BaseRequest):
                raise InvalidRequestError("Request is not an instance of BaseRequest")

            request.validate()
            parsed_url_suffix = parse_url_for_inline_params(request, url_suffix)
            url = self.configuration.endpoint + parsed_url_suffix
            params = request.decode()
            timeout, retry = generate_timeout_and_retry(self.configuration.http_config)

            response = execute_http_call(
                        method,
                        url,
                        params,
                        retry,
                        timeout,
                        self.configuration.api_key,
                        self.configuration.api_key_prefix
                    )

            handle_error(response)
            return response_cls(response.content)

        return request_call

    return request_wrapper


def handle_error(response):
    if response.status_code not in (200, 201, 202, 204):
        raise ServerError(response.content)


class BaseService:
    def __init__(self, configuration):
        """
        Parameters
        ----------
        configuration : Configuration
        """
        self.configuration = configuration
