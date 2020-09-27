# QuickBase-Task

Link to the task:
  https://github.com/QuickBase/interview-demos/tree/master/python
  
Main Idea:
  Create a command line Python program, which retrieves the information of a GitHub User and creates a new Contact or updates an existing contact in Freshdesk, using their respective APIs.
  
My approach:

        -Created 3 classes, which implement the logic  -> User, GithubApi, FreshdeskApi
        
        User - object to wrap the user info, provided by github
        GithubApi - provides function to authenticate the user in github by his username and fetches the info to User object
        FreshdeskApi - provides functions to create new contact in Freshdesk and update existing one
        
Starting the programm:
    
    - to compile the programm you need to run main.py file and 
      enter in command line proper gihub username and Freshdesk subdomain
    - you also need to add values to two environmental variables : GITHUB_TOKEN, FRESHDESK_TOKEN
