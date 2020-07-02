# OneAgent Availability Monitoring Extension
An ActiveGate Extension for Dynatrace which is intended to provide alerting for those availability situations that Dynatrace doesn't see as Problem-opening. For example when the OneAgent service has stopped, or the host has gone into an Unmonitored state, this won't open an Availability Problem as there wasn't any crash or connecitivity loss involved. Nevertheless, the host is Unmonitored until the agent is started again which may not happen for a while without an alert. This Extension will open an availability Problem for that host.

# Repository structure
* /main_plugin/
   * This is the main plugin that only alerts on Unmonitored state
* /all-states_variant
   * This is a version of the main plugin that alerts on all states (anything except for Monitored)
* /reporting_variant
   * This is a version of the main plugin which uses metrics to track state changes over time
   * This version does not send out alert events
   
