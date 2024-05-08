import pandas as pd

from core.location.GetLocations import GetLocations


class LocationsLoader:
    def get_locations(self) -> pd.DataFrame:
        locations = self.load_locations()

        # Sample location dataset
        locations = pd.DataFrame(locations)
        locations.to_csv('locations.csv', index=False)

        return locations

    def load_locations(self):
        return GetLocations().run()
