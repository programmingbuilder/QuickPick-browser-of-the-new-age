import time
import webbrowser
from tkinter import BOTTOM , LEFT , TOP , RIGHT , ttk , FLAT , END , Y , messagebox
from tkinter.ttk import Menubutton
import tkinterweb
import customtkinter
import tkinter
import data_analyser
import security
import extensions_manager
security.ID_Scan(ID='1908',name='rishabh')
data_analyser.analyse_browser_history(browser='chrome')
security.login_record()
extensions_manager.extensions()
def extensions():
    def add_extensions():
        f = open ( 'extensions/main.py', 'r' )
        temp = f.read ()
        f.close ()

        code = compile ( temp , 'main.py' , 'exec' )
        exec ( code )
    add_extensions()
    def extension1():
        f = open ( 'extensions/main2.py' , 'r' )
        temp = f.read ()
        f.close ()

        code = compile ( temp , 'main2.py' , 'exec' )
        exec ( code )
    extension1()
def contribute():
    webbrowser.open ( f'https://github.com/programmingbuilder/QuickPick-browser-of-the-new-age' , autoraise=True , new=1 )
def Browser():
    data_analyser.append_new_line('history.TXT',f'{entry.get()}')
def BrowserHistory():
    def open_site():
        listbox=Lb.get ( Lb.curselection ()[0] )
        webbrowser.open(listbox)
    pop=customtkinter.CTkToplevel(window)
    Lb = tkinter.Listbox (pop, bg="#292929" , fg='silver' , width=65 , height=30 )
    Lb.pack ()
    f = open ( "history.TXT" , "r" )
    for x in f:
        Lb.insert ( END , x )
    f.close ()
    Lb.bind ( ("<<ListboxSelect>>" , open_site()))

    pop.title("History")
    pop.geometry('500x500')
    pop.mainloop()
def Search():
    frame10.load_website(f'https://www.google.com/search?q={entry.get()}')
    Browser ()
def home():
    frame10.load_website('www.google.com')
def bookmarks():
    def add_bookmark():
        data_analyser.append_new_line('Bookmark.TXT',f'<{entry1.get()}> added on:{time.asctime()}')
    pop=customtkinter.CTkToplevel(window)
    frame2=customtkinter.CTkFrame(pop)
    frame2.pack()
    entry1=customtkinter.CTkEntry(frame2,placeholder_text='Enter the url...',width=300,height=50,border_color='red')
    entry1.pack(pady=20,padx=20)
    button2=customtkinter.CTkButton(frame2,text='+add bookmark',hover=True,corner_radius=50,bg_color='red',hover_color='red',width=300,height=50,command=add_bookmark)
    button2.pack(pady=10,padx=20)
    Lb = tkinter.Listbox ( frame2 , bg="#292929" , fg='silver' , width=65 , height=30 )
    Lb.pack ()
    f = open ( "Bookmark.TXT" , "r" )
    for x in f:
        Lb.insert ( END , x )
    f.close ()

    pop.title('bookmarks')
    pop.geometry('500x500')
    pop.mainloop()
def antivirus():
    def VPN():
        messagebox.showinfo('vpn','vpn on')
    pop=customtkinter.CTkToplevel(window)
    frame2=customtkinter.CTkFrame(pop)
    frame2.pack()
    label=customtkinter.CTkLabel(frame2,text='Login record',text_font='arial')
    label.pack()
    Lb = tkinter.Listbox ( frame2 , bg="#292929" , fg='silver' , width=65 , height=30 )
    Lb.pack ()
    f = open ( "login record.TXT" , "r" )
    for x in f:
        Lb.insert ( END , x )
    f.close ()
    frame3=customtkinter.CTkFrame(pop)
    frame3.pack()

    switch_1 = customtkinter.CTkSwitch ( frame3 , text="VPN" ,command=VPN,
                                         onvalue="on" , offvalue="off" )
    switch_1.pack ( padx=20 , pady=10 )
    pop.geometry('500x500')
    pop.title('HyperAV')
    pop.mainloop()
def newsapp():
    pop=customtkinter.CTkToplevel()
    newsframe = tkinterweb.HtmlFrame ( pop )  # create the HTML browser
    newsframe.load_website ( "https://en.wikinews.org/wiki/Main_Page" )  # load a website
    newsframe.pack ( fill="both" , expand=True )
    pop.geometry('500x500')
    pop.title('news')
    pop.mainloop()

def Passwordmanager():
    def add_password():
        site=entry2.get()
        password=entry1.get()
        list=f"website{site},password{password}"
        data_analyser.append_new_line(f'Passwords.TXT',list)
    pop=customtkinter.CTkToplevel(window)
    frame2=customtkinter.CTkFrame(pop)
    frame2.pack()
    entry2 = customtkinter.CTkEntry ( frame2 , placeholder_text='type for which site' , border_color='red',width=300,height=60 )
    entry2.pack ()
    entry1=customtkinter.CTkEntry(frame2,placeholder_text='type your password',border_color='red',width=300,height=60)
    entry1.pack()
    button2=customtkinter.CTkButton(frame2,text='add',width=100,height=50,corner_radius=50,hover_color='green',command=add_password)
    button2.pack()
    frame3=customtkinter.CTkFrame(pop)
    frame3.pack()
    Lb = tkinter.Listbox ( frame3 , bg="#292929" , fg='silver' , width=45 , height=30 )
    Lb.pack ()
    f = open ( "passwords.txt" , "r" )
    for x in f:
        Lb.insert ( END , x )
    f.close ()
    pop.title('password manager')
    pop.geometry('300x650')
    pop.mainloop()
window=customtkinter.CTk()
customtkinter.set_appearance_mode('dark')
customtkinter.set_appearance_mode('blue')


search_bar1=customtkinter.CTkFrame(window)
search_bar1.pack(side=TOP)
entry=customtkinter.CTkEntry(search_bar1,placeholder_text='Search',width=600,height=40,border_color='red')
entry.pack()
search_tools=customtkinter.CTkFrame(search_bar1)
search_tools.pack()


class Google_Search:
    def __init__(self):
        webbrowser.open(f'https://www.google.com/search?q={entry.get()}',autoraise=True,new=1)
        Browser ()


button1=customtkinter.CTkButton(search_tools,text='search on google',command=Google_Search)
button1.pack(side=LEFT)


class URL_search:
    def __init__(self):
        frame10.load_website(entry.get())
        Browser()


button2=customtkinter.CTkButton(search_tools,text='search url',command=URL_search)
button2.pack(side=LEFT)





button3=customtkinter.CTkButton(search_tools,text='search',command=Search)
button3.pack(side=LEFT)
search_bar=customtkinter.CTkFrame(window,corner_radius=50,border_color='red')
search_bar.pack(side=TOP)
frame10 = tkinterweb.HtmlFrame (search_bar) #create the HTML browser
frame10.load_website("https://www.google.com") #load a website
frame10.pack(fill="both", expand=True)

frame1=customtkinter.CTkFrame(window,corner_radius=50,border_color='red')
frame1.pack(side=RIGHT)
home=customtkinter.CTkButton(frame1,text='home',command=home)
home.pack()
menubutton = Menubutton ( frame1 , text="☰"  )


menubutton.menu = tkinter.Menu ( menubutton )

menubutton["menu"] = menubutton.menu

menubutton.menu.add_checkbutton ( label="Hindi" )

menubutton.menu.add_checkbutton ( label="English" )

menubutton.pack (side=TOP)


frame=customtkinter.CTkFrame(window,corner_radius=50,border_color='red')
frame.pack(side=BOTTOM)
btnContribute=customtkinter.CTkButton(frame,text='contribute',corner_radius=20,hover_color='green',width=50,height=50,command=contribute)
btnContribute.pack(side=LEFT)
btnPassWordManager=customtkinter.CTkButton(frame,text='Password Manager',corner_radius=20,hover_color='green',width=50,height=50,command=Passwordmanager)
btnPassWordManager.pack(side=LEFT)
btnNews=customtkinter.CTkButton(frame,text='news',corner_radius=20,hover_color='green',width=50,height=50,command=newsapp)
btnNews.pack(side=LEFT)
btnAntivirus=customtkinter.CTkButton(frame,text='antivirus',corner_radius=20,hover_color='green',width=50,height=50,command=antivirus)
btnAntivirus.pack(side=LEFT)
btnBookmark=customtkinter.CTkButton(frame,text='bookmarks',corner_radius=20,hover_color='green',width=50,height=50,command=bookmarks)
btnBookmark.pack(side=LEFT)
btnBrowserHistory=customtkinter.CTkButton(frame,text='History',corner_radius=20,hover_color='green',width=50,height=50,command=BrowserHistory)
btnBrowserHistory.pack(side=LEFT)
window.geometry("1000x700")
window.title("Quick Pick")
window.mainloop()
