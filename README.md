# OpsGenie Python SDK

Inspired by [opsgenie](https://github.com/opsgenie/opsgenie-python-sdk)

## Aim and Scope

OpsGenie Python SDK aims to access OpsGenie Web API through HTTP calls from a client application in Python language.

OpsGenie Python SDK covers:

- [Alert API](https://github.com/kumarappan-arumugam/opsgenie-py/tree/master/opsgenie/alerts) (Under development)
- [Account API](https://github.com/kumarappan-arumugam/opsgenie-py/tree/master/opsgenie/accounts) (Under development)
- [User API](https://github.com/kumarappan-arumugam/opsgenie-py/tree/master/opsgenie/users) (Under development)
- [Team API](https://github.com/kumarappan-arumugam/opsgenie-py/tree/master/opsgenie/teams) (Under development)

## Pre-requisites

-   The API is specifically built for Python 2.7 but can also be used with other Python versions.
-   Before you begin, you need to sign up  [OpsGenie](http://www.opsgenie.com/)  if you don't have a valid account yet. Create an API Integration and get your API key.

## Installation

To download all packages in the repo with their dependencies, simply execute

`pip install https://github.com/kumarappan-arumugam/opsgenie-py/archive/<version>.zip`

## Getting Started

One can start using OpsGenie Python SDK by initializing client and making a request. Example shown below demonstrates how to initialize our client and make a create alert request.
<pre><code>
from opsgenie import OpsGenie
from opsgenie import Configuration
from opsgenie import CreateAlertRequest

config = Configuration(apikey="YOUR_API_KEY", endpoint="OPTIONAL") # default endpoint is api.opsgenie.com
client = OpsGenie(config)
alert_request = CreateAlertRequest(
			        message = "An example alert message",
			        alias = "",
			        description = "Every alert needs a description",
			        responders = [
				        {"name":"Example", "type":"team"},
				        {"username":"example@example.com", "type":"user"},
				        {"name":"Example Escalation", "type":"escalation"},
				        {"name":"Example Schedule", "type":"schedule"}
				    ],
			        visibleTo = [
				        {"name":"Example","type":"team"},
				        {"username":"example@example.com","type":"user"}
				    ],
			        actions = ["Restart", "AnExampleAction"],
			        tags = ["Example","Environment"],
			        details = {"key1":"value1","key2":"value2"},
			        entity = "An example entity",
			        priority = "P1"
                )
client.alert.create_alert(alert_request)
</code></pre>

## Importance of Alias

[Alert De-Duplication](https://docs.opsgenie.com/docs/alert-deduplication)

## The Web API

Please follow the links below for more information and details about the Web API.

- [Alert API](https://docs.opsgenie.com/docs/alert-api)
- [Account API](https://docs.opsgenie.com/docs/account-api)
- [User API](https://docs.opsgenie.com/docs/user-api)
- [Team API](https://docs.opsgenie.com/docs/team-api)

## Bug Reporting and Feature Requests

If you like to report a bug, or a feature request; please create a github issue.
