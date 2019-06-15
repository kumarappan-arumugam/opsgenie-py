from __future__ import absolute_import
from opsgenie.request import (
    BaseRequest,
    max_value,
    required,
)

class CreateAlertRequest(BaseRequest):
    def __init__(self, message, alias=None, description=None, responders=None, visibleTo=None, actions=None,
                 tags=None, details=None, entity=None, source=None, priority='P3', user=None, note=None):
        """
        Used to hold required parameters of Create Alert Request call.
        https://docs.opsgenie.com/docs/alert-api#section-create-alert

        Parameters
        ----------
        message : str, required (limited to 130 characters)
            Message of the alert
        alias : str, optional (limited to 512 characters)
            A user defined identifier of the alert, that is also the key element of Alert De-Duplication (https://docs.opsgenie.com/docs/alert-deduplication).
        description : str, optional (limited to 15000 characters)
            Description field of the alert that is generally used to provide a detailed information about the alert.
        responders : list of dicts, optional (limited to 50 teams, users, escalations or schedules)
            Teams, users, escalations and schedules that the alert will be routed to send notifications.
            `type` field is mandatory for each item, where possible values are team, user, escalation and schedule.
            If the API Key belongs to a team integration, this field will be overwritten with the owner team.
            Either id or name of each responder should be provided.
        visibleTo : list of dicts, optional (50 teams or users in total)
            Teams and users that the alert will become visible to without sending any notification.
            `type` field is mandatory for each item, where possible values are team and user.
            In addition to the type field, either id or name should be given for teams and either id or username should be given for users.
            Please note: that alert will be visible to the teams that are specified withinteams field by default, so there is no need to re-specify them within visibleTo field.
        actions : list of str, optional
            Custom actions which can be executed for the alert.
        tags : list of str, optional
            A comma separated list of labels attached to the alert.
        details : dict, optional
            Map of key-value pairs to use as custom properties of the alert.
        entity : str, optional
            Entity field of the alert that is generally used to specify which domain alert is related to.
        source : str, optional
            Field to specify source of alert. Default is IP address of incoming request
        priority : str, optional
            Priority level of the alert. Possible values are P1, P2, P3, P4 and P5. Default value is P3.
        user : str, optional (limited to 100 characters)
            Sets default owner of the execution. Default is owner of account.
        note : str, optional (limited to 25000 characters)
            Additional note that will be added while creating the alert.
        """
        BaseRequest.__init__(self)
        self.message = message
        self.alias = alias
        self.description = description
        self.responders = responders
        self.visibleTo = visibleTo
        self.actions = actions
        self.tags = tags
        self.details = details
        self.entity = entity
        self.source = source
        self.priority = priority
        self.user = user
        self.note = note

    @required("message")
    @max_value("message", 130)
    @max_value("alias", 512)
    @max_value("description", 15000)
    @max_value("entity", 512)
    @max_value("source", 100)
    @max_value("user", 100)
    @max_value("note", 25000)
    def validate(self):
        pass

    def decode(self):
        return {
            'message': self.message,
            'alias': self.alias,
            'description': self.description,
            'responders': self.responders,
            'visibleTo': self.visibleTo,
            'actions': self.actions,
            'tags': self.tags,
            'details': self.details,
            'entity': self.entity,
            'source': self.source,
            'priority': self.priority,
            'user': self.user,
            'note': self.note
        }
