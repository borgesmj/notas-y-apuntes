import os

while True:
  username = input('username > ')
  password = input('password > ')

  if os.environ['adminUser'] == username and os.environ['adminPassword'] == password:
    print('Welcome Admin')
    break
  elif os.environ['username'] == username and os.environ['userPassword'] == password:
    print('welcome user')
    break
  else:
    print('try again')