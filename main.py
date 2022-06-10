from github import Github
import pickle

with open('credentials.dat', 'rb') as file:
    data = pickle.load(file)
    username, password = data ['username'], data['password']

    git = Github(username,password)
    user = git.get_user()

    repos = user.get_repos()

    for i in repos:
        print(i)