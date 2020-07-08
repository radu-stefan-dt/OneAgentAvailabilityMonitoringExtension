# OneAgent Availability Monitoring Extension
An ActiveGate Extension for Dynatrace which is intended to provide alerting for those availability situations that Dynatrace doesn't see as Problem-opening. For example when the OneAgent service has stopped, or the host has gone into an Unmonitored state, this won't open an Availability Problem as there wasn't any crash or connecitivity loss involved. Nevertheless, the host is Unmonitored until the agent is started again which may not happen for a while without an alert. This Extension will open an availability Problem for that host.

## Repository structure
* /main_plugin/
   * This is the main plugin that only alerts on Unmonitored state
   * [Check it out](https://github.com/radu-stefan-dt/OneAgentAvailabilityMonitoringExtension/blob/master/main_plugin/README.md)
* /all-states_variant
   * This is a version of the main plugin that alerts on all states (anything except for Monitored)
   * [Check it out](https://github.com/radu-stefan-dt/OneAgentAvailabilityMonitoringExtension/blob/master/all-states_variant/README.md)
* /reporting_variant
   * This is a version of the main plugin which uses metrics to track state changes over time
   * This version does not send out alert events
   * [Check it out](https://github.com/radu-stefan-dt/OneAgentAvailabilityMonitoringExtension/blob/master/reporting_variant/README.md)
   
## How to deploy it
Each repo folder has a pre-packaged archive that is ready for deploying to Dynatrace (built on Linux 64-bit).
However, it is recommended to get the individual python and json file for the variant you want to deploy, and first build the plugin yourself using the [Dynatrace Plugin SDK](https://www.dynatrace.com/support/help/extend-dynatrace/extensions/development/install-extension-sdk/) on the O/S and bitness you intend to deploy it to.

Not sure how to deploy a plugin? Check out the [Dynatrace Help](https://www.dynatrace.com/support/help/extend-dynatrace/extensions/development/extension-how-tos/deploy-an-activegate-plugin/) pages.
   
