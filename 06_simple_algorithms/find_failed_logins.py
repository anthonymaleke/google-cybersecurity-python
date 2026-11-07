# Algorithm to search for specific events
def find_failed(log_list):
    return [log for log in log_list if 'failed' in log.lower()]
