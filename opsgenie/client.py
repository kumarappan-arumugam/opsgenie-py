from .alerts import AlertService
from .users import UserService
from .teams import TeamService
from .accounts import AccountService
from .config import Configuration
from .errors import InvalidConfigurationError


class OpsGenie:
    def __init__(self, configuration):
        """
        Init OpsGenie client to interact with OpsGenie Api
        Parameters
        ----------
        configuration : Configuration
        """
        if not isinstance(configuration, Configuration):
            InvalidConfigurationError()
        configuration.validate()
        self.configuration = configuration
        self._alertService = AlertService(configuration)
        self._userService = UserService(configuration)
        self._teamService = TeamService(configuration)
        self._accountService = AccountService(configuration)

    @property
    def accounts(self):
        """
        Returns
        -------
        UserService
        """
        return self._accountService

    @property
    def alerts(self):
        """
        Returns
        -------
        AlertService
        """
        return self._alertService

    @property
    def users(self):
        """
        Returns
        -------
        UserService
        """
        return self._userService

    @property
    def teams(self):
        """
        Returns
        -------
        UserService
        """
        return self._teamService
