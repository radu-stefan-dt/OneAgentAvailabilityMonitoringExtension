# OneAgent Availability Monitoring Extension - All States Variant
This is a variant of the main plugin which alerts on any state changes.

It works the exact same way as the main plugin in that
* you link to a tenant (using ID and API Token)
* you select your timeframe
* and events will fire off to each host with an expiration period of 5 minutes
However, the difference is that Availabilty Events will be created for any host state other than Monitored.
