1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
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