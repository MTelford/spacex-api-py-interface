import json
import requests


class SpaceXAPIInterface():

    """ Provides methods for aquiring API data 
        from SpaceX base URL with specified route. """

    def __init__(self):

        self.base_url = ('https://api.spacexdata.com/v4/')
        
        self.company_info = 'company'
    
    def setup_api_route_py_data(self, api_route):

        """ returns space x api data in py format.
            from api base url https://api.spacexdata.com/v4/
            Accessible via var py_spacex_info """        
        
        # gives us the SpaceX company info as JSON str
        spacex_info = requests.get(self.base_url + api_route)
        json_spacex_info = spacex_info.text

        # converts JSON to Python dict
        py_spacex_info = json.loads(json_spacex_info)
        return py_spacex_info

    def get_capsules_info(self):
        ''' returns api info as dict for pythonic access'''
        return self.setup_api_route_py_data('capsules')
    
    def get_company_info(self):
        ''' returns api info as dict for pythonic access'''
        return self.setup_api_route_py_data('company')
    
    def get_cores_info(self):
        ''' returns api info as dict for pythonic access'''
        return self.setup_api_route_py_data('cores')

    def get_crew_info(self):
        ''' returns api info as dict for pythonic access'''
        return self.setup_api_route_py_data('crew')

    def get_dragons_info(self):
        ''' returns api info as dict for pythonic access'''
        return self.setup_api_route_py_data('dragons')

    def get_landpads_info(self):
        ''' returns api info as dict for pythonic access'''
        return self.setup_api_route_py_data('landpads')

    def get_launches_info(self):
        ''' returns api info as dict for pythonic access''' 
        return self.setup_api_route_py_data('launches')

    def get_launchpads_info(self):
        ''' returns api info as dict for pythonic access'''
        return self.setup_api_route_py_data('launchpads')

    def get_payloads_info(self):
        ''' returns api info as dict for pythonic access'''
        return self.setup_api_route_py_data('payloads')

    def get_roadster_info(self):
        ''' returns api info as dict for pythonic access'''
        return self.setup_api_route_py_data('roadster')

    def get_rockets_info(self):
        ''' returns api info as dict for pythonic access'''
        return self.setup_api_route_py_data('rockets')

    def get_ships_info(self):
        ''' returns api info as dict for pythonic access'''
        return self.setup_api_route_py_data('ships')

    def get_starlink_info(self):
        ''' returns api info as dict for pythonic access'''
        return self.setup_api_route_py_data('starlink')

    def get_history_info(self):
        ''' returns api info as dict for pythonic access'''
        return self.setup_api_route_py_data('history')

    


spacexapi = SpaceXAPIInterface()

company_info = spacexapi.get_company_info()

print(company_info)