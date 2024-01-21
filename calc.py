def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def power(a, b):
  return a ** b

def modulus(a, b):
  return a % b

def factorial(a):
  if a == 0:
    return 1
  else:
    return a * factorial(a - 1)

def log(a):
  return math.log(a)

def exp(a):
  return math.exp(a)

def sin(a):
  return math.sin(a)

def cos(a):
  return math.cos(a)

def tan(a):
  return math.tan(a)

def cot(a):
  return 1 / math.tan(a)

def sec(a):
  return 1 / math.cos(a)

def csc(a):
  return 1 / math.sin(a)

def main():
  while True:
    print("Select an operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    print("6.Modulus")
    print("7.Factorial")
    print("8.Log")
    print("9.Exp")
    print("10.Sin")
    print("11.Cos")
    print("12.Tan")
    print("13.Cot")
    print("14.Sec")
    print("15.Csc")
    print("16.Exit")

    choice = input("Enter your choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'):
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))

      if choice == '1':
        result = add(num1, num2)
      elif choice == '2':
        result = subtract(num1, num2)
      elif choice == '3':
        result = multiply(num1, num2)
      elif choice == '4':
        result = divide(num1, num2)
      elif choice == '5':
        result = power(num1, num2)
      elif choice == '6':
        result = modulus(num1, num2)
      elif choice == '7':
        result = factorial(num1)
      elif choice == '8':
        result = log(num1)
      elif choice == '9':
        result = exp(num1)
      elif choice == '10':
        result = sin(num1)
      elif choice == '11':
        result = cos(num1)
      elif choice == '12':
        result = tan(num1)
      elif choice == '13':
        result = cot(num1)
      elif choice == '14':
        result = sec(num1)
      elif choice == '15':
        result = csc(num1)

      print(result)

    elif choice == '16':
      break
    else:
      print("Invalid input")

if __name__ == "__main__":
  main()5