from __future__ import absolute_import
from opsgenie.request import (
    BaseRequest,
    max_value,
    required,
)

class GetUserRequest(BaseRequest):
    def __init__(self, identifier, expand=''):
        """
        Used to hold required parameters of Get User Request call.
        https://docs.opsgenie.com/docs/user-api#section-get-user

        In-Line Parameters
        ----------
        identifier : str, required
            Username or id of the user

        Query Parameters
        ----------
        expand : str
            Comma separated list of strings to create a more detailed response. The only expandable field for user api is contact
        """
        BaseRequest.__init__(self)
        self.identifier = identifier
        self.expand = expand

    @required("identifier")
    def validate(self):
        pass

    def decode(self):
        return {
            'expand': self.expand
        }
