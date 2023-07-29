import requests

def internet_connectivity_check(url='http://www.google.com/', timeout=2):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False