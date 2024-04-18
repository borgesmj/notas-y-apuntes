import random, os, time, datetime
from replit import db



def clearScreen(seconds):
  time.sleep(seconds)
  os.system('clear')

def loadData():
  posts = []
  try:
    loadedPosts = db['posts']
    for post in loadedPosts:
      posts.append({
        'post': post['post'],
        'timestamp': post['timestamp']
      })
    return posts
  except:
    return []

def seeAllEntries(posts):
  if len(posts) == 0:
    clearScreen(1)
    print('Aun no hay entradas en tu diario privado, intenta agregar la primera desde el menu inicial\n')
    input('presione ENTER para continuar ')
  else:
    index = 0
    postsSorted = sorted(posts, key=lambda x: x['timestamp'], reverse=True)
    while index <= (len(postsSorted) - 1):
      clearScreen(1)
      print(f"""
    [{postsSorted[index]['timestamp']}]: {postsSorted[index]['post']}
    """)
      userInput = input('¿Ver siguiente?\ns/n > ')
      if userInput == 's':
        index += 1
      else: 
        break
    else:
      clearScreen(1)
      print('Ya no hay mas post para ver')
      input('Presione ENTER para regresar al menu inicial')

def addNewEntry(posts):
  clearScreen(1)
  post = input('Escribe lo que piensas hoy\n> ')
  timestamp = round(datetime.datetime.now().timestamp())
  newPost = {
    'post': post,
    'timestamp': timestamp
  }
  posts.append(newPost)
  db['posts'] = posts
  


def menuInicial():
  while True:
    posts = loadData()
    clearScreen(1)
    print('Bienvenido\n\nMenu Inicial\n1. Agregar entrada nueva\n2. Ver todas las entradas\n3. Salir')
    userInput = input('> ')
    if userInput == '3':
      login()
    elif userInput == '2':
      seeAllEntries(posts)
    elif userInput == '1':
      addNewEntry(posts)
    elif userInput == '9':
      for key in db.keys():
        del db[key]


def login():
  while True:
    keys = db.keys()
    if len(list(keys)) == 0:
      print('Crea tu usuario y contraseña')
      username = input('Username > ')
      password = input('Contraseña > ')
      salt = random.randint(1000, 9999)
      newPassword = hash(f"{password}{salt}")
      db[username]= {
        'salt': salt,
        'password': newPassword
      }
    else:
      clearScreen(1)
      print('Login')
      username = input('Username > ')
      password = input('Passqword > ')
      try:
        salt = db[username]['salt']
        if hash(f"{password}{salt}") == db[username]['password']:
          menuInicial()
          break
        else:
          print('No estas autorizado a entrar aqui')
      except:
        print('Usuario no registrado')

login()

