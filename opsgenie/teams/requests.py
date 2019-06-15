from __future__ import absolute_import
from opsgenie.request import (
    BaseRequest,
    max_value,
    required,
)

class GetTeamRequest(BaseRequest):
    def __init__(self, identifier, identifierType='id'):
        """
        Used to hold required parameters of Get Team Request call.
        https://docs.opsgenie.com/docs/team-api#section-get-team

        In-Line Parameters
        ----------
        identifier : str, required
            Identifier of the team

        Query Parameters
        ----------
        identifierType : str
            Type of the identifier that is provided as an in-line parameter. Possible values are id and name. Default value is id
        """
        BaseRequest.__init__(self)
        self.identifier = identifier
        self.identifierType = identifierType

    @required("identifier")
    def validate(self):
        pass

    def decode(self):
        return {
            'identifierType': self.identifierType,
        }
