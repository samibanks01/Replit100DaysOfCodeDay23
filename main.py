print("Replit Login System")

print()

def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password?: ")
    if username == "Sam" and password == "homieisback":
      print("Welcome to Replit!")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      continue

login()

