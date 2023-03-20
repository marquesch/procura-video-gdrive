import json
import datetime
import os
from services.util.logutil import append_log, read_last_json

logdir = 'logs'
jsonlogdir = 'json'
main_path = os.path.dirname(__file__)
json_logspath = os.path.join(main_path, '..', '..', logdir, jsonlogdir)


def check_json_folder():
    if not os.path.exists(json_logspath):
        os.makedirs(json_logspath)


def obj_to_json(obj):
    json_obj = json.dumps(obj, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)
    return json_obj


def json_to_dict(json_obj):
    return json.loads(json_obj)


def load_json_file_as_dict(filename=read_last_json()):
    json_path = os.path.join(json_logspath, filename)

    if not os.path.exists(json_path) or filename == 'empty':
        return None

    with open(json_path, 'r') as openfile:
        json_dict = json.load(openfile)

    return json_dict


def write_json_file(folder):
    json_obj = obj_to_json(folder)
    logdatetime = datetime.datetime.now().strftime('%d-%m-%Y-%H%M')

    filename = 'jsonlog' + logdatetime + '.json'
    path_name = os.path.join(json_logspath, filename)
    check_json_folder()
    with open(path_name, "w") as outfile:
        outfile.write(json_obj)

    append_log(filename)
