import os
import time
import socket

def ID_Scan(ID,name):
    list=['rishabh','john','navneet']
    list1=['1908','1890','2908']
    if ID in list1:
        print('user Verified')
    else:
        print('not verified')
        exit()
    if name in list:
        print ( 'user Verified' )
    else:
        print ( 'not verified' )
        exit ()
def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)
def login_record():
    hostname = socket.gethostname ()
    IPAddr = socket.gethostbyname ( hostname )
    record=f'on:{time.asctime()},by:{hostname},Ip address:{IPAddr}'
    append_new_line(file_name='login record.TXT',text_to_append=record)

