
import os
import requests

BASE_URL = "http://pokeapi.co/api/v2/pokemon"



def validate(resource_id=None):
    
    if resource_id is not None and not isinstance(resource_id, int) and not isinstance(resource_id, str):

        raise ValueError("Bad id '{}'".format(resource_id))

    return None


def api_url_build_pokemon(resource_id=None, subresource=None):
    validate(resource_id)

    if resource_id is not None:
        if subresource is not None:
            return "/".join([BASE_URL, str(resource_id), subresource, ""])

        return "/".join([BASE_URL, str(resource_id), ""])

    return "/".join([BASE_URL, ""])









###----------------------------------------------------------------------------------------------------------------------

def _call_api_pokemon(resource_id=None, subresource=None, short=False):
    url = api_url_build_pokemon(resource_id, subresource)

    # Get a list of resources at the endpoint, if no resource_id is given.
    get_endpoint_list = resource_id is None

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if short is False and get_endpoint_list and data["count"] != len(data["results"]):
        # We got a section of all results; we want ALL of them.
        num_items = dict(limit=data["count"])

        response = requests.get(url, params=num_items)
        response.raise_for_status()

        data = response.json()
    
   
    return data['name']

#url = api_url_build_pokemon("pikachu")
#print(url)
#x= _call_api_pokemon(14)
#print(x)
#response = requests.get(url)
#print(response.status_code)
#response = response.json()
#print(response['name'])