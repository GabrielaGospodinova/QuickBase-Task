import argparse
import ApiCommunicator


def command_line_reader():
    parser = argparse.ArgumentParser(description='Enter Github user and Freshdesk subdomain')
    parser.add_argument('GitHub user', type=str, help='GitHub username')
    parser.add_argument('Freshdesk subdomain', type=str, help='Freshdesk subdomain')
    args = parser.parse_args()
    return vars(args)


def main():
    # read info from command line
    info = command_line_reader()

    # get info for the Github user you typed in command line
    user = ApiCommunicator.GithubApi.user_auth(info['GitHub user'])
    
    # save the subdomain from command line in variable
    subdomain = info['Freshdesk subdomain']

    # create contact in Freshdesk API, with the info from github
    ApiCommunicator.FreshdeskApi.create_contact(user, subdomain)

    # modify already existing contact in Freshdesk API
    ApiCommunicator.FreshdeskApi.modify_contact(user, subdomain)


if __name__ == "__main__":
    main()