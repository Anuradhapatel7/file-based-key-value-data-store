import threading 
from threading import*
import time

container={} #Dictionary in which we  will be storing data

#for create operation look down 

def create(key,value,timeout=0):
    if key in container:
        print("Opps, this key already exists error:/") #will give an error if key alreadt exist
    else:
        if(key.isalpha()):
            if len(container)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size < 1GB & Jasonobject value < 16KB 
                if timeout==0:
                    d=[value,timeout]
                else:
                    d=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars in file
                    container[key]=d
            else:
                print("Oops Memory limit exceeded!! error:/ ")#will give an error if memory limit exceeds!
        else:
            print("Please enter a valind key_name that must have key name  contain only alphabets strictly!")#will give error for invalid key name

#for read operation look down
            
def read(key):
    if key not in container:
        print("Oops given key does not exist please enter a valid key") #will give error for key not existing in database
    else:
        c=container[key]
        if c[1]!=0:
            if time.time()<c[1]: #comparing the present time with to-live time given
                stry=str(key)+":"+str(c[0]) #JasonObject is created i.e.,"key_name:value" is created
                return stry
            else:
                print("error! time-to-live of",key,"has expired.") #will give an error if time to live has expired!
        else:
            stry=str(key)+":"+str(c[0])
            return stry

#for delete operation look down

def delete(key):
    if key not in container:
        print("Oops given key does not exist please enter a valid key") #error message
    else:
        c=container[key]
        if c[1]!=0:
            if time.time()<c[1]: #comparing the current time with to-live time given
                del container[key]
                print("key is successfully deleted!")
            else:
                print("error: time-to-live of",key,"has expired.") #will give an error if time to live has expired!
        else:
            del container[key]
            print("key is successfully deleted!")

#This issource code for Data Storing using Key-Value pair
#It will supports basic CRD operation that is create,delete,read!
