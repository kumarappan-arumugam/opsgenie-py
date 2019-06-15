# User API

## Getting Started

Example shown below demonstrates how to initialize our client and retrieve user info.
<pre><code>
from opsgenie import OpsGenie
from opsgenie import Configuration
from opsgenie import GetUserRequest

config = Configuration(apikey="YOUR_API_KEY", endpoint="OPTIONAL") # default endpoint is api.opsgenie.com
client = OpsGenie(config)
user = client.users.get_user(GetUserRequest(identifier='example@user.com'))
</code></pre>
