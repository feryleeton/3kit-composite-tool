import re
import requests

import config

def get_assets(tag=None):
    """
    Pulls assets that belong to the organization
    https://developer.threekit.com/reference/exportproducts
    :return: response.json() - response from Three-Kit API
    """
    url = f"https://preview.threekit.com/api/products/export/json?orgId={config.THREEKIT_ORG_ID}"

    if tag:
        # if tag argument provided filtering assets by tag value
        url += f"&tags={tag}"

    headers = {
        "accept": "application/json",
        f"authorization": f"Bearer {config.THREEKIT_BEARER_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def get_assets_by_tag(tag):
    tag = re.sub(r'#', '', tag)
    print('Pulling assets by tag: ', tag)

    nested_assets = get_assets(tag)

    items = list(map(lambda item: item['product'].get('id'), nested_assets))
    print('ITEMS: ', items)
    return items
