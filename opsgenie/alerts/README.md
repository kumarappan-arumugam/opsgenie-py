# Alert API

## Getting Started

Example shown below demonstrates how to initialize our client and make a create alert request.
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
</pre></code>
