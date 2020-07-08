# OneAgent Availability Monitoring Extension - All States Variant
This is a variant of the main plugin which uses metrics to track tenant-wide state changes.
It will keep count of all hosts in states other than "Monitored" but will not send out alerting events.

## How does it work?
The plugin creates a Custom Device Group called "OneAgent Availability Monitors" which will contain all the Custom Devices created (one per endpoint, each representing a SaaS tenant). It reports one key metric which is the total number of hosts in a state other than Monitored.

  ![Device Group](https://github.com/radu-stefan-dt/OneAgentAvailabilityMonitoringExtension/blob/master/imgs/device_group.PNG)

**Note:** while you can still set the timeframe when setting up your endpoint, it really doesn't matter as only the current state of the host is returned.

Under the individual device (tenant), it reports two key charts for the total number of hosts in a non-monitored state and an stacked breakdown of individual states.

  ![Device](https://github.com/radu-stefan-dt/OneAgentAvailabilityMonitoringExtension/blob/master/imgs/device.PNG)

You can go into furhter details to get individual charts per state:

  ![Further details](https://github.com/radu-stefan-dt/OneAgentAvailabilityMonitoringExtension/blob/master/imgs/further_details.PNG)

## Custom metrics requirements
This variant of the plugin will consume 8 custom metrics per endpoint (tenant).

  ![Custom metrics](https://github.com/radu-stefan-dt/OneAgentAvailabilityMonitoringExtension/blob/master/imgs/metrics.PNG)
