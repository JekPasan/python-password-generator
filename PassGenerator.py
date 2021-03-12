from random import randint
class PassGenerator(object):
  def add(self, x: str, y: str) -> None:
    # x = pasword
    # y = what you want to pick to add to x
    random = y[randint(0, len(y)-1)]
    x += random
    return x
  
  def generate(self) -> None:
    use = input("what do you intend on using it for? ")
    raw_parameters = input("words you want within your password: ")
    parameters = raw_parameters.split(",")
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRTUVWXYZ"
    signs = "!@#$%^&*-_=+"
    digits = "0123456789"
    password = ""
    
    while len(parameters) != 0:
      # decides whether to add a chosen paramter, a random letter, digit or a sign to the currently generated password
      a = randint(1, 5+1)
      # a = 1 --> add a parameter
      # a = 2 --> add a lower case letter
      # a = 3 --> add a upper case letter
      # a = 4 --> add a sign
      # a = 5 --> add a digit

      if len(password) >= 10 and len(parameters) <= len(parameters)/2:
        # add the remainign parameters if the password is too long
        for parameter in parameters:
          password += str(parameter)
        else:
          # the else gets executed after the for loop finished
          break
      
      if a == 1:
        random_parametrer = parameters[randint(0, len(parameters)-1)]
        password += random_parametrer
        parameters.remove(random_parametrer)
      elif a == 2:
        password = self.add(password, lower_alphabet)
      elif a == 3:
        password = self.add(password, upper_alphabet)
      elif a == 4:
        password = self.add(password, signs)
      elif a == 5:
        password = self.add(password, digits)
    f = open("passwords.txt", "a")
    f.write("\n" + use + ": " + password + "\n")
    f.close()
    print("generated password is: " + password)