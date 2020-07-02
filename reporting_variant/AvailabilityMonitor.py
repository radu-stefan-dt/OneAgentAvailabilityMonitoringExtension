import requests
from ruxit.api.base_plugin import RemoteBasePlugin
from time import time
import logging

logger = logging.getLogger(__name__)


class PluginMain(RemoteBasePlugin):
    def initialize(self, **kwargs):
        logger.info(f"Using config: {self.config}")
        self.token = self.config.get('api_token')
        self.tenant = self.config.get('tenant_id')
        self.timeframe = self.config.get('timeframe')

    def query(self, **kwargs):
        env_api = f"https://{self.tenant}.live.dynatrace.com/api/v1"
        auth = dict(Authorization=f"Api-Token {self.token}")

        # Make API call, retrieve unmonitored hosts.
        nextPageKey = 1
        hosts = []

        logger.info("Parsing tenant")
        # Loop until whole tenant was parsed in case there's more than 1 page of results
        while nextPageKey:
            query = f"?relativeTime={self.timeframe}"
            if nextPageKey != 1:
                query += f"?{nextPageKey}"

            response = requests.get(
                url=env_api+"/oneagents"+query, headers=auth).json()

            if len(response.get('hosts')) > 0:
                for host in response.get('hosts'):
                    host_id = host.get('hostInfo').get('entityId')
                    host_state = host.get('availabilityState')

                    if host_state != "MONITORED":
                        hosts.append(dict(id=host_id,state=host_state))

            nextPageKey = response.get('nextPageKey')
        
        unmonitored = len([_ for _ in hosts if _.state == "UNMONITORED" ])
        crashed = len([_ for _ in hosts if _.state == "CRASHED" ])
        shutdown = len([_ for _ in hosts if _.state == "SHUTDOWN" ])
        unexpected = len([_ for _ in hosts if _.state == "UNEXPECTED_SHUTDOWN" ])
        unknown = len([_ for _ in hosts if _.state == "UNKNOWN" ])
        lost = len([_ for _ in hosts if _.state == "LOST" ])
        pre = len([_ for _ in hosts if _.state == "PRE_MONITORED" ])
        non_monitored = len(hosts)

        device_group = self.topology_builder.create_group("OneAgent Availability Monitors", "OneAgent Availability Monitors")
        device = device_group.create_device(f"Tenant {self.tenant}", f"Tenant {self.tenant}")
 
        device.absolute(key="unmonitored", value=unmonitored)
        device.absolute(key="unexpected_shutdown", value=unexpected)
        device.absolute(key="crashed", value=crashed)
        device.absolute(key="unknown", value=unknown)
        device.absolute(key="lost", value=lost)
        device.absolute(key="pre_monitored", value=pre)
        device.absolute(key="non_monitored", value=non_monitored)
        device.absolute(key="shutdown", value=shutdown)