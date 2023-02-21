"""singleton persisten with json"""
import json

# this is not necesary but my mind needs it ;)
DATA = 0

try:
    with open('config.json', 'r', encoding="utf-8") as f:
        DATA = json.load(f)
except FileNotFoundError:
    DATA = {}
except Exception as err:
    raise err


def save():
    """
    Save the file of the json
    that is being used as global config
    """

    json_object = json.dumps(DATA, indent=4)

    try:
        with open(
                "config.json", "w", encoding="utf-8"
                ) as outfile:
            outfile.write(json_object)
    except Exception as error:
        raise error
