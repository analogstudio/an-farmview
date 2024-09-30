import requests

from .config import settings

def get_ubl_data():

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
        print(f"Error while collecting capabilities: {e}")

    ubl_data = {}

    for feature_name, value in data.items():

        # We only have one version of any license
        value = value.get('0.00')

        # feature named 'enable-usage' has been added? It does not have the value[0.00]
        if not value:
            print(f"The feature named \'{feature_name}\' does not have expected data, skipping...")
            continue

        print("Feature:       {:} ".format(feature_name))
        print("    Entitled:  {:,}".format(int(value['totalCount'])))
        print("    Used:      {:,}".format(int(value['totalUsed'])))
        print("    Overage:   {:,}".format(int(value['totalOverdraftCount'])))
        print("    Available: {:,}".format(int(value['totalAvailable'])))

        if feature_name.lower() == 'deadline-redshift':
            redshift_data = {
                'redshift_entitled': value['totalCount'],
                'redshift_used' : value['totalUsed'],
                'redshift_available': value['totalAvailable']
            }
            
            ubl_data.update(redshift_data)

        if feature_name.lower() == 'deadline-nuke':
            nuke_data = {
                'nuke_entitled': value['totalCount'],
                'nuke_used' : value['totalUsed'],
                'nuke_available': value['totalAvailable']
            }
            
            ubl_data.update(nuke_data)

        if feature_name.lower() == 'deadline-vray-usabled':
            vray_data = {
                'vray_entitled': value['totalCount'],
                'vray_used' : value['totalUsed'],
                'vray_available': value['totalAvailable']
            }
            
            ubl_data.update(vray_data)


    return ubl_data