from __future__ import absolute_import
from opsgenie.service import (
    BaseService,
    execute,
)
from .responses import *


class AlertService(BaseService):

    @execute("POST", url_suffix="/alerts", response_cls=CreateAlertResponse)
    def create_alert(self, request):
        """
        OpsGenie Create Alert API call
        https://docs.opsgenie.com/docs/alert-api#createAlertRequest

        Parameters
        ----------
        request : CreateAlertRequest

        Returns
        --------
        CreateAlertResponse
        """
        pass
