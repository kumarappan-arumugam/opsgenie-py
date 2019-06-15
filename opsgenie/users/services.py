from __future__ import absolute_import
from opsgenie.service import (
    BaseService,
    execute,
)
from .responses import *


class UserService(BaseService):

    @execute("GET", url_suffix="/users/:identifier", response_cls=GetUserResponse)
    def get_user(self, request):
        """
        OpsGenie Get User API call
        https://docs.opsgenie.com/docs/user-api#section-get-user

        Parameters
        ----------
        request : GetUserRequest

        Returns
        --------
        GetUserResponse
        """
        pass
