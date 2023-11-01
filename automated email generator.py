import random
import string

def op1():

  def email():
   a=random.randint(6,30)
   b=random.randint(8,100)

   if a>=6 and a<=30:

    def gen_email(a):
     gen= string.ascii_letters+string.digits
     email_id=''.join(random.choice(gen)for i in range(a))
     return (f"{email_id}@gmail.com")

    print("email id:",gen_email(a))

    if b>=8 and b<=100:

     def gen_pass(b):
      gen= string.ascii_letters+string.digits+string.punctuation
      password=''.join(random.choice(gen)for i in range(b))
      return (f"{password}")

     print("password:",gen_pass(b))

    else:
     print("invalid password entry")

   else:
     print("invalid Email entry") 

  email()   

  def reply():   
   rep=input("please type 'yes' to generate another pair of email id and password [OR] please type 'no' to exit ")
   return(rep)

  rep=reply()

  while rep=='yes' or rep=='Yes':
   option()
   rep=reply()
   
   while rep=='no' or rep=='No':
    quit()

  else:
   quit() 

def op2():

  def email():
   a=int(input("enter the length of the gmail id(6-30)"))
   b=int(input("enter the length of the password(8-100)"))

   if a>=6 and a<=30:

    def gen_email(a):
     gen= string.ascii_letters+string.digits
     email_id=''.join(random.choice(gen)for i in range(a))
     return (f"{email_id}@gmail.com")

    print("email id:",gen_email(a))

    if b>=8 and b<=100:

     def gen_pass(b):
      gen= string.ascii_letters+string.digits+string.punctuation
      password=''.join(random.choice(gen)for i in range(b))
      return (f"{password}")

     print("password:",gen_pass(b))

    else:
     print("invalid password entry")

   else:
    print("invalid Email entry") 

  email()  

  def reply():   
   rep=input("please type 'yes' to generate another pair of email id and password [OR] please type 'no' to exit ")
   return(rep)

  rep=reply()

  while rep=='yes' or rep=='Yes':
   option()
   rep=reply()

  while rep=='no' or rep=='No':
    quit()
  else:
   quit()   

def option():
  option=int(input("enter your option 1-->random \n                  2-->specific\n       "))
  if option==1:
   op1()

  elif option==2:
   op2()

  else:
   print("invalid entry")  
    
option() 
