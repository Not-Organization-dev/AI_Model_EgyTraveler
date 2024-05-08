import requests as req
from requests.exceptions import RequestException

class GetLocations:
    def run(self):
        url = 'https://egytravel.codepeak.live/api/v1/place/all-places'

        try:
            response = req.get(url, verify=False)
            response.raise_for_status()
            locations = response.json()['data']['places']
            return locations
        
        except RequestException as e:
            print(f"An error occurred: {e}")
            return []
