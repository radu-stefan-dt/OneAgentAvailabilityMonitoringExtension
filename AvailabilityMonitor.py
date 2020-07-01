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

    def query(self, **kwargs):
        env_api = f"https://{self.tenant}.live.dynatrace.com/api/v1"
        auth = dict(Authorization=f"Api-Token {self.token}")

        # Make API call, retrieve unmonitored hosts.
        nextPageKey = 1
        hosts = []

        logger.info("Parsing tenant")
        # Loop until whole tenant was parsed in case there's more than 1 page of results
        while nextPageKey:
            query = f"?relativeTime=hour&availabilityState=UNMONITORED"
            if nextPageKey != 1:
                query += f"?{nextPageKey}"

            response = requests.get(
                url=env_api+"/oneagents"+query, headers=auth).json()

            if len(response.get('hosts')) > 0:
                for host in response.get('hosts'):
                    hosts.append(host.get('hostInfo').get('entityId'))

            nextPageKey = response.get('nextPageKey')

        # Push events to the offending hosts (if any)
        if len(hosts) > 0:
            logger.info("Sending an event.")
            for host in hosts:
                event = dict(eventType="AVAILABILITY_EVENT",
                             start=round(time())/1000,
                             timeoutMinutes=5,
                             attachRules=dict(entityIds=[host]),
                             description="Host detected as Unmonitored",
                             title="Host state changed to Unmonitored",
                             source="OneAgent Availability Monitor"
                             )
                requests.post(url=env_api+"/events", json=event, headers=auth)
        else:
            logger.info("No events to push.")
