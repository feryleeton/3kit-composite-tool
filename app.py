import json
import config
from services import api_services, app_services

if __name__ == '__main__':

    # getting all organization assets and filtering them by product id
    items = list(filter(lambda item: (item['product'].get('id') == config.FROM_COMPOSITE), api_services.get_assets()))
    print(items)
    # collecting attributes of given items
    items_attributes = list(map(lambda item: item['product'].get('attributes', None), items))

    references = []
    str_values = []

    for item_attributes in items_attributes:
        for attribute in item_attributes:
            if attribute['type'] == 'Asset':
                for value in attribute['values']:
                    if isinstance(value, str):
                        # assuming values are tags
                        references.extend(api_services.get_assets_by_tag(value))
                    elif isinstance(value, dict):
                        # assuming values are list of assets
                        print('dict value')

            elif attribute['type'] == 'String':
                print('string')
                str_values.extend(attribute['values'])

    print(references)
    print(str_values)


    # === 3 ===
    with open('json/from.json') as from_json, open('json/to.json') as to_json:
        from_data = json.load(from_json)
        to_data = json.load(to_json)
        new_objects = app_services.map_item_render_layers(from_data, to_data)
    # === 3 ===

    # === 4 ===
    for obj in new_objects:
        for layer_name, layer in obj.items():
            if layer_name != 'Global Layer' and layer_name != 'BG':
                app_services.get_configuration_permutations(0, layer['attributes'], {})
                pass

    # === 4 ===

    


