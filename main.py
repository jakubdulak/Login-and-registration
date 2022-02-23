users = {"username": "admin", "password": "admin1"}

password = users.get("password")
username = users.get("username")

def panel():
  login = input("Podaj login: ")
  haslo = input("Podaj hasło: ")
  choose == '1'
  logowanie()
  return

def logowanie(): 
  if  login == users["username"] and haslo == users["password"]:
    print("Zalogowano pomyślnie\n")
    print("Oto tajne informacje...\n")
  else:
    if password != haslo:
      print("Hasło nierawidłowe !")
      panel()
    if username != login:
      print("Login nieprawidłowy !")
      panel()
      return

def rejestrowanie():
  users['username'] = login
  users['password'] = haslo
  print("Rejestracja przebiegła pomyślnie\n")
  print("Teraz możesz się zalogować\n")
  panel()
  return

print("Aby uzyskać dostęp zaloguj się lub zarejestruj: \n")
login = input("Podaj login: ")
haslo = input("Podaj hasło: ")

print("Wybierz czynność wprowadzając '1' lub '2' \n")
choose = input("1. Zaloguj się\n"
    "2. Zarejestruj się")

if choose == '1':
  print("Logowanie..\n")
  logowanie()
elif choose == '2':
  print("Rejestrowanie..\n")
  rejestrowanie()
