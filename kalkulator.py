
def addNumbers(parm1, parm2):
  return int(parm1) + int(parm2)
 
def subNumbers(parm1, parm2):
  return int(parm1) - int(parm2)
 
 
def divNumbers(parm1, parm2):
  return int(parm1) / int(parm2)
 
 
def mulNumbers(parm1, parm2):
  return int(parm1) * int(parm2)
 
 
 
 
# This function will call all the functions
def main():
  opr = input("Choose what operation you want to do ( +, -, /, *) : ")
 
  num1 = input("Write your first number: ")
  num2 = input("Write your second number: ")
 
 
  
  if(opr == '+'):
    print("Your addition result is: ");
    print(addNumbers(num1, num2));
 
  elif(opr == '-'):
    print("Your Subscraction result is: ");
    print(subNumbers(num1, num2));
 
  elif(opr == '/'):
    print("Your Divition result is: ");
    print(divNumbers(num1, num2));
 
 
  elif(opr == '*'):
    print("Your Multiplication result is: ",  mulNumbers(num1, num2));
  
 
 
 
# calling main function 
main()
