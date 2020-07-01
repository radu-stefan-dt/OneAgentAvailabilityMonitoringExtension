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
  * the event expires in 5 minutes, but will be resent every minute (fixed extention execution frequency) thus extending it
  * event uses entity IDs to attach to the correct hosts
  ![Plugin Events](https://github.com/radustefandynatrace/OneAgentAvailabilityMonitoringExtension/blob/master/imgs/plugin_events.PNG)
  
## How to deploy?
It works tenant-wide and the built-in query is for 1 hour, meaning if your host has been Unmonitored for more than 1 hour it will no longer show up in the query results and the Availability event will not be extended. Maximum Problem duration is then 1 hour and 5 minutes.
![Plugin Problem](https://github.com/radustefandynatrace/OneAgentAvailabilityMonitoringExtension/blob/master/imgs/plugin_problem.PNG)

Setup requires:
* Tenant ID - ID of the SaaS (public) Tenant to monitor
* API Token - token with event and oneagents permissions for the Tenant
* ActiveGate - Environment ActiveGate enabled for running plugins
![Plugin Setup](https://github.com/radustefandynatrace/OneAgentAvailabilityMonitoringExtension/blob/master/imgs/plugin.PNG)
