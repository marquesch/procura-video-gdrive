import os

logname = 'jsonlog.txt'
logdir = 'logs'

main_location = os.path.dirname(__file__)
log_dir_path = os.path.join(main_location, '..', '..', logdir)
log_path = os.path.join(log_dir_path, logname)


def check_log_folder():
    if not os.path.exists(log_dir_path):
        os.makedirs(log_dir_path)


def append_log(json_file_name):
    check_log_folder()
    with open(log_path, "a") as logfile:
        logfile.write("\n" + json_file_name)


def read_last_json():
    check_log_folder()
    if not os.path.exists(log_path):
        return 'empty'

    with open(log_path) as logfile:
        for line in logfile:
            pass
        last_json_log = line
    return last_json_log
