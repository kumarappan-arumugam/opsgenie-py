from __future__ import absolute_import
from opsgenie.response import BaseResponse

class CreateAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.message = self.pop('result', self.pop('message', ''))
        self.requestId = self.pop('requestId')

        self.decode()
