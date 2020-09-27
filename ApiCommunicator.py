import os
import requests
import json
import copy
import User


class GithubApi:
    api_key = os.environ['GITHUB_TOKEN']

    @classmethod
    def user_auth(cls, username):
        headers = {'Authorization': 'token' + cls.api_key}
        response = requests.get('https://api.github.com/users/' + username, headers=headers)

        if response.status_code == 200:
            github_main_info = response.json()
            user = User.User(github_main_info)
            return user.get_user()
        else:
            print('Not valid github username or unsuccessful connection to github')
            return False

    @classmethod
    def print_user_info(cls, username):
        if not cls.user_auth(username):
            print(cls.user_auth(username))


class FreshdeskApi:
    freshdesk_api_key = os.environ['FRESHDESK_TOKEN']

    # function, which is checking whether user is existing in freshdesk
    @classmethod
    def check_existing(cls, user={}, subdomain={}):
        headers = {
            'Content-Type': 'application/json',
        }
        # default value of contact_id, which is invalid one for a real user
        contact_id = -1
        username = user.get('name')

        response_id = requests.get(subdomain + '/api/v2/contacts',
                                   auth=(cls.freshdesk_api_key, 'test'), headers=headers)

        if response_id.status_code == 200:
            contact_id = cls.find_contact_id(response_id.json(), username)

        return contact_id != -1

    @classmethod
    def create_contact(cls, contact_info={}, subdomain={}):
        if not cls.check_existing(contact_info, subdomain):
            headers = {"Content-Type": "application/json"}

            # copying contact info, because we will modify the values to create contact
            contact_info_copy = copy.deepcopy(contact_info)
            contact_info_copy.pop('description')

            response = requests.post(subdomain + "/api/v2/contacts",
                                     auth=(cls.freshdesk_api_key, 'test'), data=json.dumps(contact_info_copy), headers=headers)

            if response.status_code == 201:
                print('Contact created successfully')
            else:
                print('Contact wasn\'t created successfully')
        else:
            print('Contact already exists')

    @classmethod
    def find_contact_id(cls, dict_info, username):
        for user in dict_info:
            if user['name'] == username:
                return user['id']
        return -1

    @classmethod
    def modify_contact(cls, contact_info={}, subdomain={}):
        if cls.check_existing(contact_info, subdomain):
            headers = {"Content-Type": "application/json"}

            username = contact_info.get('name')
            contact_id = -1

            contact_info_copy = copy.deepcopy(contact_info)
            contact_info_copy.pop('name')
            contact_info_copy.pop('unique_external_id')

            response_contacts = requests.get(subdomain + '/api/v2/contacts',
                                             auth=(cls.freshdesk_api_key, 'test'), headers=headers)

            if response_contacts.status_code == 200:
                contact_id = cls.find_contact_id(response_contacts.json(), username)

            response = requests.put(subdomain + "/api/v2/contacts/" + f'{contact_id}',
                                    auth=(cls.freshdesk_api_key, 'test'), data=json.dumps(contact_info_copy),
                                    headers=headers)

            if response.status_code == 200:
                print('Contact updated successfully')
            else:
                print('Contact wasn\'t updated successfully')

        else:
            print('Contact doesn\'t exist')
