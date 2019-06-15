from __future__ import absolute_import
from opsgenie.request import (
    BaseRequest,
    max_value,
    required,
)

class GetAccountRequest(BaseRequest):
    def __init__(self):
        """
        Used to hold required parameters of Get Account Request call.
        https://docs.opsgenie.com/docs/account-api#section-get-account-info
        """
        BaseRequest.__init__(self)

    def decode(self):
        return {}
