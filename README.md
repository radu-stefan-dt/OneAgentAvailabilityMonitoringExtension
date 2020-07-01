# OneAgent Availability Monitoring Extension
An ActiveGate Extension for Dynatrace which does not require any custom metrics and is intended to provide alerting for those availability situations that Dynatrace doesn't see as Problem-opening. For example when the OneAgent service has stopped, or the host has gone into an Unmonitored state, this won't open an Availability Problem as there wasn't any crash or connecitivity loss involved. Nevertheless, the host is Unmonitored until the agent is started again which may not happen for a while. This Extension will open an availability Problem for that host.

**Limitations:**
* Works with SaaS only
* Requires an API Token with relevant permissions
* Requires the "OneAgent on a Host" Environment API endpoints on the SaaS tenant
* Will close the Problem automatically after 1 hour and 5 minutes since the host went into Unmonitored state, even if host is still in that state

## How does it work?
1. API calls are made to /api/v1/oneagents until whole tenant is parsed, saving Host IDs for hosts in Unmonitored state
1. For hosts found Unmonitored, a Problem-opening Availability Event is sent via API
  * the event expires in 5 minutes, but will be resent every minute
