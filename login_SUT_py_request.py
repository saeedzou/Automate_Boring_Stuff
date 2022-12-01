# import requests library
import requests

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
    # return the session
    return session

# define main function
def main():
    # define username and password
    username = "Enter your username"
    password = "Enter your password here"
    # call login function
    session = login(username, password)
    # print whether the login was successful or not
    print("Login was successful" if session else "Login was not successful")

    
# call main function
main()



