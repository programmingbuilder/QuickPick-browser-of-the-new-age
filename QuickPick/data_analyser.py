import socket

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

def analyse_browser_history(browser):
    browser_edit=browser.lower()
    try:
        if browser_edit == 'firefox':
            pass
        else:
            print ( 'successfully loaded' )
        if browser_edit == 'opera':
            pass
        else:
            print('successfully loaded')
        webbrowser.get ( using=browser )
    except:
        len(max('google','opera','microsoft edge'))
        hostname = socket.gethostname ()
        IPAddr = socket.gethostbyname ( hostname )
        append_new_line(file_name='userdata.TXT',text_to_append=f'hostname={hostname},IDAddress:{IPAddr}')
