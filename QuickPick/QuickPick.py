from tkinter import BOTTOM , LEFT , TOP , RIGHT , ttk , FLAT
from tkinter.ttk import Menubutton

import tkinterweb
import customtkinter
import tkinter


import data_analyser
import security
security.ID_Scan(ID='1908',name='rishabh')
data_analyser.analyse_browser_history()
window=customtkinter.CTk()
customtkinter.set_appearance_mode('dark')
customtkinter.set_appearance_mode('blue')

search_bar=customtkinter.CTkFrame(window,corner_radius=50,border_color='red')
search_bar.pack(side=TOP)
frame = tkinterweb.HtmlFrame (search_bar) #create the HTML browser
frame.load_website("https://www.bing.com") #load a website
frame.pack(fill="both", expand=True)

frame1=customtkinter.CTkFrame(window,corner_radius=50,border_color='red')
frame1.pack(side=RIGHT)
menubutton = Menubutton ( frame1 , text="☰"  )


menubutton.menu = tkinter.Menu ( menubutton )

menubutton["menu"] = menubutton.menu

menubutton.menu.add_checkbutton ( label="Hindi" )

menubutton.menu.add_checkbutton ( label="English" )

menubutton.pack (side=TOP)

frame=customtkinter.CTkFrame(window,corner_radius=50,border_color='red')
frame.pack(side=BOTTOM)
btnContribute=customtkinter.CTkButton(frame,text='contibute',corner_radius=20,hover_color='green',width=50,height=50)
btnContribute.pack(side=LEFT)
btnPassWordManager=customtkinter.CTkButton(frame,text='Password Manager',corner_radius=20,hover_color='green',width=50,height=50)
btnPassWordManager.pack(side=LEFT)
window.geometry("1000x700")
window.title("Quick Pick")
window.mainloop()