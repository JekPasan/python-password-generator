from random import randint
class PassGenerator(object):
  def __init__(self) -> None:
      pass
  def generate(self) -> None:
    raw_parameters = input("words you want within your password: ")
    parameters = raw_parameters.split(",")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    password = ""
    
    while len(parameters) != 0:
      # decides whether to add a chosen paramter, a random letter or a digit to the currently generated password
      a = randint(1, 4+1)
      # a <= 2 --> add a parameter
      # a = 3 --> add a letter
      # a = 4 --> add a digit

      if len(password) >= 10:
        # add the remainign parameters if the password is too long
        for parameter in parameters:
          password += str(parameter)
        else:
          # the else gets executed after the for loop finished
          break
      
      if a <= 2:
        random_parametrer = parameters[randint(0, len(parameters)-1)]
        password += random_parametrer
        parameters.remove(random_parametrer)
      elif a == 3:
        random_letter = alphabet[randint(0, len(alphabet))]
        password += random_letter
      elif a == 4:
        random_digit = digits[randint(0, len(digits))]
        password += random_digit
    print("generated password is: " + password)