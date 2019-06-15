from __future__ import absolute_import
from opsgenie.service import (
    BaseService,
    execute,
)
from .responses import *


class TeamService(BaseService):

    @execute("GET", url_suffix="/teams/:identifier", response_cls=GetTeamResponse)
    def get_team(self, request):
        """
        OpsGenie Get Team API call
        https://docs.opsgenie.com/docs/team-api#section-get-team

        Parameters
        ----------
        request : GetTeamRequest

        Returns
        --------
        GetTeamResponse
        """
        pass
