from __future__ import absolute_import
from opsgenie.response import BaseResponse

class GetTeamResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        initial_data = self.pop('data', {})
        for key in initial_data:
            setattr(self, key, initial_data[key])

        self.decode()
