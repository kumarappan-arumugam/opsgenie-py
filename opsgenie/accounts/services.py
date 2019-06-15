from __future__ import absolute_import
from opsgenie.service import (
    BaseService,
    execute,
)
from .requests import *
from .responses import *


class AccountService(BaseService):

    @execute("GET", url_suffix="/account", response_cls=GetAccountResponse)
    def get_account(self, request=GetAccountRequest()):
        """
        OpsGenie Get Team API call
        https://docs.opsgenie.com/docs/account-api#section-get-account-info

        Parameters
        ----------
        request : GetAccountRequest

        Returns
        --------
        GetTeamResponse
        """
        pass
