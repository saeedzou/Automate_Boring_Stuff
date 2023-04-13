import requests
import argparse

# write a function to login to "https://net2.sharif.edu/login" using post method
def login(username, password):
    # create a session
    session = requests.Session()
    # create a payload
    payload = {
        "username": username,
        "password": password
    }
    # send a post request to "https://net2.sharif.edu/login" with payload
    response = session.post("https://net2.sharif.edu/login", data=payload)
    # check the status code of the response
    if response.status_code != 200:
        return None
    # return the session
    return session

# define main function
def main():
    # create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Login to Sharif University Net2")
    # add arguments for username and password
    parser.add_argument("--username", help="username for login", required=True)
    parser.add_argument("--password", help="password for login", required=True)
    # parse the command-line arguments
    args = parser.parse_args()
    # call login function
    session = login(args.username, args.password)
    # check the returned session
    if session:
        print("Login was successful")
    else:
        print("Login was not successful")

    
# call main function
if __name__ == "__main__":
    main()