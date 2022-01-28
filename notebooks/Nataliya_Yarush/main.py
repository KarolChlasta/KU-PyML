class Nata:

 def __init__(Nata,country, city):
       Nata.country = country
       Nata.city = city
       
 def myfunc(Nata):
     print("Welcome to "+ Nata.city)
     
x = Nata("Poland","Warsaw :)")
  
x.myfunc()