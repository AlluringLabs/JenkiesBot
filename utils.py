import sys
import json
import contextlib


def update_json_file(file_path: str, update_func: callable):
    """ Utility function for updating a json file's contents by
    passing it to a callable function `update_func`.

    Params:
        file_path   - Path to the json file to update.
        update_func - Callable function that accepts a single parameter,
                      the json file's contents. This function should return
                      the new json file's contents.
    """
    with open(file_path, 'r+') as json_file:
        json_val = json.loads(json_file.read())
        updated_json = update_func(json_val)
        json_file.seek(0)
        json_file.write(json.dumps(updated_json))
        json_file.truncate()

