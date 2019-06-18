def accept_login(users, username, password):
    if username in users.keys():
        if password == users[username]:
            return True
        else: return False
    else: return False
users = { "user1" : "password1", "user2" : "password2", "user3" : "password3" }
username = input('Enter a username: ')
password = input('Enter a password: ')
print(accept_login(users, username, password))
