import requests

from .config import settings

def get_redshift():

    SITE_ID = 'thinkbox.compliance.flexnetoperations.com'

    # use fastapiv pydantic settings
    SERVER_ID = settings.fno_server

    SERVER_BASE_URL = f'https://{SITE_ID}/api/1.0/instances/{SERVER_ID}'
    SERVER_LOGIN_URL = SERVER_BASE_URL + '/authorize'
    SERVER_FEATURE_SUMMARY_URL = SERVER_BASE_URL + '/features/summaries'


    login_dict = {
        'user': 'admin',
        'password': settings.fno_password
    }

    session = requests.Session()

    try:
        login_request = session.post(SERVER_LOGIN_URL, json = login_dict).json()
    except Exception as e:
        print(f"Error when trying to log in: {e}")

    auth_token = login_request['token']

    auth_header = {
        'Authorization': f'Bearer {auth_token}'
    }

    try:
        data = session.get(url=SERVER_FEATURE_SUMMARY_URL, headers=auth_header).json()
    except Exception as e:
        print("Error while collecting capabilities: {e}")

    for feature_name, value in data.items():
        # We only have one version of any license
        value = value['0.00']

        print("Feature:       {:} ".format(feature_name))
        print("    Entitled:  {:,}".format(int(value['totalCount'])))
        print("    Used:      {:,}".format(int(value['totalUsed'])))
        print("    Overage:   {:,}".format(int(value['totalOverdraftCount'])))
        print("    Available: {:,}".format(int(value['totalAvailable'])))

        if feature_name.lower() == 'deadline-redshift':
            # return f'{value["totalAvailable"]:,}'
            # just return int
            return value["totalAvailable"]

def get_redshift2():

    SITE_ID = 'thinkbox.compliance.flexnetoperations.com'

    # use fastapiv pydantic settings
    SERVER_ID = settings.fno_server

    SERVER_BASE_URL = f'https://{SITE_ID}/api/1.0/instances/{SERVER_ID}'
    SERVER_LOGIN_URL = SERVER_BASE_URL + '/authorize'
    SERVER_FEATURE_SUMMARY_URL = SERVER_BASE_URL + '/features/summaries'


    login_dict = {
        'user': 'admin',
        'password': settings.fno_password
    }

    session = requests.Session()

    try:
        login_request = session.post(SERVER_LOGIN_URL, json = login_dict).json()
    except Exception as e:
        print(f"Error when trying to log in: {e}")

    auth_token = login_request['token']

    auth_header = {
        'Authorization': f'Bearer {auth_token}'
    }

    try:
        data = session.get(url=SERVER_FEATURE_SUMMARY_URL, headers=auth_header).json()
    except Exception as e:
        print("Error while collecting capabilities: {e}")

    for feature_name, value in data.items():
        # We only have one version of any license
        value = value['0.00']

        print("Feature:       {:} ".format(feature_name))
        print("    Entitled:  {:,}".format(int(value['totalCount'])))
        print("    Used:      {:,}".format(int(value['totalUsed'])))
        print("    Overage:   {:,}".format(int(value['totalOverdraftCount'])))
        print("    Available: {:,}".format(int(value['totalAvailable'])))

        if feature_name.lower() == 'deadline-redshift':
            dict = {
                'redshift_entitled': value['totalCount'],
                'redshift_used' : value['totalUsed'],
                'redshift_available': value['totalAvailable']
                }
            
            return dict