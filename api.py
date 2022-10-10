from tkinter import *
from pytube import YouTube

# API window
root = Tk()
root.geometry('500x200') # Size
root.resizable(0, 0) # makes the window adjustable with its features
root.title('Lauz YT downloader')

# Link Entry
Label(root, text="Lauz Youtube Downloader", font="san-serif 14 bold").pack()
link = StringVar() # Specifying the variable type
Label(root, text="Paste your link here", font="san-serif 15 bold").place(x=150,y=55)
link_enter = Entry(root, width=70, textvariable=link).place(x=30,y=85)

# Download Function
def Download():
    url = YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
    fetch_link = url.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    Label(root, text="Finished Download", font="arial 15 bold", fg="green").place(x=150, y=110) # Once the video is downloaded, this label `downloaded` is displayed to show dowload completion.
    
Button(root, text='Download', font='san-serif 16 bold', bg='orange', padx=2, command=Download).place(x=180,y=140)
    
root.mainloop()