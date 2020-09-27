class User:
    user_info = {}

    def __init__(self, main_info):
        self.user_info.update({'name': main_info['login']})
        self.user_info.update({'unique_external_id': main_info['id']})
        self.user_info.update({'description': main_info['html_url']})

    def get_user(self):
        return self.user_info
