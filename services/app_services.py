def map_item_render_layers(from_data, to_data):
    mapped_layers = []
    for from_val in from_data.values():
        for to_val in to_data.values():
            if to_val['name'] == from_val['name']:
                mapped_layers.append({
                    from_val['name']:
                        {
                            'renderId': from_val['id'],
                            'itemId': to_val['id'],
                            'attributes': from_val['plugs']['Properties'][0]['attributes']
                        }})
    return mapped_layers

def get_configuration_permutations(idx, attribute_map, configuration):
    print(attribute_map)

