# -*- coding: utf-8 -*-
from .request import Request


class Activity:
    def __init__(self, player_id, get_access_token):
        self.player_id = player_id
        self.request = Request(get_access_token)

    def list(self, start=0, limit=20):
        return self.request.json(
            '/api/profiles/{}/activities/?start={}&limit={}'.format(self.player_id, start, limit))

    def get_activity(self, activity_id):
        return self.request.json(
            '/api/profiles/{}/activities/{}'.format(
                self.player_id, activity_id))
