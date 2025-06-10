# -*- coding:utf-8 -*-
import requests
from .. import logger

class DiscordWebhookHandler:
    def __init__(self, name, webhook_url, client_name):
        # Logger
        self._logger = logger.Logger.register(__name__)

        # Settings
        self._task_name = name
        self._webhook = webhook_url
        self._client_name = client_name

        # Log creation
        self._logger.debug('Webhook handler for task %s created with url %s', self._task_name, self._webhook)

    # Send a webhook when torrent deletion is successful
    def send_success(self, torrent):
        self._logger.info("Sending success webhook for torrent: %s", torrent)
        fields = [
            {
                "name": "Torrent",
                "value": torrent
            }
        ]
        self.send_webhook("Torrent Deleted Successfully", 5091684, fields)

    # Send a webhook when torrent deletion fails
    def send_failure(self, torrent, reason):
        self._logger.info("Sending failure webhook for torrent %s with reason: %s", torrent, reason)
        fields = [
            {
                "name": "Torrent",
                "value": torrent
            },
            {
                "name": "Reason",
                "value": reason
            }
        ]
        self.send_webhook("Torrent Deletion Failed", 11619684, fields)

    # Send a webhook with discord embed format
    def send_webhook(self, title, color, fields):
        payload = {
            "username": "autoremove-torrents",
            "embeds": [
                {
                    "author": {
                        "name": self._client_name,
                    },
                    "title": title,
                    "color": color,
                    "fields": 
                        fields
                }
            ]
        }
        result = requests.post(self._webhook, json=payload, headers={"Content-Type": "application/json"}, timeout=10)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            self._logger.error("Failed to deliver webhook: %s", err)
        else:
            self._logger.info("Webhook delivered successfully with status code %s.", result.status_code)
