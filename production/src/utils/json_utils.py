import json


def read_json(file_name):
    """
    This function opens the file file_name and loads the json content inside the file
    """
    # read file
    with open(file_name, 'r') as myfile:
        data = myfile.read()

    # parse file
    obj = json.loads(data)
    return obj


def write_json(file_name, content):
    """
    This function opens the file file_name and writes down the json content
    """
    with open(file_name, 'w') as outfile:
        json.dump(content, outfile, indent=True)
    return


def print_json(content):
    """
    Print the json content
    """
    for key in content.keys():
        print(key, " : ", content[key])
