__author__ = 'mredman'

import requests
import json

base_url = "https://saucelabs.com/rest/v1/"


class SauceHelper:
    #sauce_username = ""
    #sauce_access_key = ""

    def __init__(self, sauce_username, sauce_access_key):
        self.sauce_username = sauce_username
        self.sauce_access_key = sauce_access_key

    def get(self, final_url):
        print "Working on: " + final_url
        fully_qualified_resource = final_url
        r = requests.get(fully_qualified_resource, auth=(self.sauce_username, self.sauce_access_key))
        return r.json()

    def get_user(self):
        uri = "users/" + self.sauce_username
        final_url = base_url + uri
        r = self.get(final_url)
        return json.dumps(r, sort_keys=True, indent=4, separators=(',', ': '))

    def get_user_concurrency(self):
        uri = "/concurrency"
        final_url = base_url + "users/" + self.sauce_username + uri
        r = self.get(final_url)
        return json.dumps(r, sort_keys=True, indent=4, separators=(',', ': '))

    def get_jobs(self):
        uri = "/jobs"
        final_url = base_url + self.sauce_username + uri
        r = self.get(final_url)
        return json.dumps(r, sort_keys=True, indent=4, separators=(',', ': '))


# Account based stuff
sh = SauceHelper("michaelbredman", "81097e3b-d1b7-4c8f-8114-05f049da93ce")
# print sh.get_user()
# print sh.get_user_concurrency()

# User job stuff
print sh.get_jobs()

