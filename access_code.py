#Complie module of MAIN FILE and then  import main file as a library in this file

import source_code as s #importing the main file("source_code" is the name of the file I have used) as a library in sourcecode


s.create("London",99) #to create a key with key_name,value given and with no time-to-live property


s.create("Chicago",34,6700) #to create a key with key_name,value given and with time-to-live property value given(number of seconds)


s.read("London") #it will returns the value of the respective key in Jason object format 'key_name:value'

s.read("Chicago") #it  will returns the value of the respective key in Jason object format 'key_name:value'

s.read("London") #it will returns the value of the respective key in Jason object format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR

s.create("London",32) #it will returns an ERROR since the key_name already exists in the database 

s.delete("London") #it will deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like following
th1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
th1.start()
th1.sleep()
th2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
th2.start()
th2.sleep()
#this can be accesed upto thn
