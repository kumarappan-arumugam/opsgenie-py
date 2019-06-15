# Team API

## Getting Started

Example shown below demonstrates how to initialize our client and retrieve team info.
```
from opsgenie import OpsGenie
from opsgenie import Configuration
from opsgenie import GetTeamRequest

config = Configuration(apikey="YOUR_API_KEY", endpoint="OPTIONAL") # default endpoint is api.opsgenie.com
client = OpsGenie(config)
team = client.teams.get_team(GetTeamRequest(identifier='exampleTeam', identifierType='name'))
```
