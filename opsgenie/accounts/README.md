# Account API

## Getting Started

Example shown below demonstrates how to initialize our client and retrieve account info.
<pre><code>
from opsgenie import OpsGenie
from opsgenie import Configuration
from opsgenie import CreateAlertRequest

config = Configuration(apikey="YOUR_API_KEY", endpoint="OPTIONAL") # default endpoint is api.opsgenie.com
client = OpsGenie(config)
account = client.accounts.get_account()
</code></pre>
