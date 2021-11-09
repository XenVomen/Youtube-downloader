from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from pytube import YouTube, streams



Folder_Name =""
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
                          downloadLabel.config(text=Folder_Name, fg="green")
                          DownloadVideo() 
    else:
                          downloadLabel.config(text="Choose Folder to save", fg="red")

def DownloadVideo():

 try:

    choose =   ytbChoice.get()
    url = urlEntry.get()

    if(len(url) > 1):
        urlError.config(text="")
        yt = YouTube(url)

        if (choose == chooses[0]):
            select = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
        elif(choose == chooses[1]):
            select  = yt.streams.filter(progressive=True, fiel_extension="mp4").get_lowest_resolution()                                                                    
        elif(choose == chooses[2]):
            select = yt.streams.filter(only_audio=True).first()
    else:
        urlError.config(text="Paste URL again!", fg="red")
    select.download(Folder_Name)
    downloadLabel.config(text="Download Completed!", fg="green")
 except EXCEPTION as err:
            print(err)                                                                                               
                                                                                            
                                                                                            
                                                                               
#UI
root= Tk()
root.title('Youtube video Downloader')
root.columnconfigure(0, weight=1) 

#the title 
title = Label(root, text="Youtube video Downloader",fg="red" , font=('jost',20),)

        
                     
title.grid(row=0, padx=100, pady=20)

urlLabel = Label(root, text="Paste Video URL", font=('jost', 15))
urlLabel.grid(row=1)

 #url textbox

urlEntry = Entry(root,width=40, fg="blue" , font=("jost", 15))
urlEntry.grid(row=2, pady=5)

#error label
urlError = Label(root, text="", fg="red", font=("jost", 13))
urlError.grid(row=3)



choicelabel= Label(root, text="Chose type and quality", font=('jost',15))
choicelabel.grid(row=4)




#combobox
chooses =["High quality video", "Low quality Video", "Audio file"]
ytbChoice = ttk.Combobox(root, values=chooses, font=('jost', 15))

ytbChoice.grid(row=5, pady=10)


#Button
downloadBtn = Button(root, command= openLocation, text="Download", width=20, bg="red", fg="White",font=('jost', 15))
downloadBtn.grid(row=6, pady=10)


downloadLabel = Label(root, text="", fg="red", font=("jost", 13))
downloadLabel.grid(row=7, pady=10)


root.mainloop()