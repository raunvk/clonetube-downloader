import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

foldername = 'Current Folder'
filesize = 0
maxfilesize = 0

def opendir():
    global foldername
    foldername = filedialog.askdirectory()
    if(len(foldername)>1):
        saveerror.config(text=foldername)
    else:
        saveerror.config(text='....Invalid Folder....')


def download():
    global maxfilesize, filesize, select
    ch = choice.get()
    url = entry.get()

    if(len(url)>1):
        entryerror.config(text='')
        print(url, 'saved in : ', foldername)
        yt = YouTube(url, on_progress_callback=progress)
        print('File name is : ', yt.title)
            
        if(ch==choicevar[0]):
            print('....mp4 HD is downloading....')
            completelabel.config(text='....mp4 HD is downloading....')
            select = yt.streams.filter(progressive=True).first()
        elif(ch==choicevar[1]):
            print('....mp4 SD is downloading....')
            completelabel.config(text='....mp4 SD is downloading....')
            select = yt.streams.filter(progressive=True).order_by('480p')
        elif(ch==choicevar[2]):
            print('....mp4 LD is downloading....')
            completelabel.config(text='....mp4 LD is downloading....')
            select = yt.streams.filter(progressive=True).last()
        elif(ch==choicevar[3]):
            print('....mp3 Audio is downloading....')
            completelabel.config(text='....mp3 Audio is downloading....')
            select = yt.streams.filter(only_audio=True).first()

        filesize = select.filesize
        maxfilesize = filesize/1024000
        print('File Size = {:00.00f} MB'.format(maxfilesize))

        select.download(foldername)
        print('Download Location : {}'.format(foldername))
        complete()

    else:
        entryerror.config(text='....Invalid Link....')


def progress(stream, chunk, file_handle, remaining=0):
    percent = ((filesize-remaining)/filesize)*100
    print('{:00.00f}% downloaded'.format(percent))


def complete():
    completelabel.config(text='Download Complete. File Size = {:00.00f} MB.'.format(maxfilesize))


#CreateWindow
root = Tk()
root.title("CloneTube Downloader")
if os.name=='nt':
    root.iconbitmap(bitmap='icon.ico')
root.geometry('800x900')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#Image
file = PhotoImage(file='icon.png')
image = Label(root, image=file)
image.grid(pady=(20, 0), padx=(15,0))


#LinkEntry
linklabel = Label(root, text='Paste Youtube Link Here', fg='#1a237e', font=('Verdana', 20))
linklabel.grid(pady=(5, 0))
entryvar = StringVar()
entry = Entry(root, width=60, textvariable=entryvar)
entry.grid(pady=(5, 0))
entryerror = Label(root, fg='#c62828', text='', font=('Verdana', 15))
entryerror.grid(pady=(5, 0))

#FilePathEntry
savelabel = Label(root, text='Select Save Location', fg='#1a237e', font=('Verdana', 20))
savelabel.grid(pady=(40, 0))
save = Button(root, width=20, bg='#388e3c', fg='#fafafa', text='Choose Folder', font=('Verdana', 15), command=opendir)
save.grid(pady=(5, 0))
saveerror = Label(root, fg='#c62828', text='', font=('Verdana', 15))
saveerror.grid(pady=(5, 0))

#Resolution/FileExtension
choicelabel = Label(root, text='Select File Type', fg='#1a237e', font=('Verdana', 20))
choicelabel.grid(pady=(40, 0))
choicevar = ['mp4 HD', 'mp4 SD', 'mp4 LD', 'mp3 Audio']
choice = ttk.Combobox(root, values=choicevar)
choice.grid(pady=(5, 0))

#DownloadButton
download = Button(root, width=20, bg='#388e3c', fg='#fafafa', text='Download', font=('Verdana', 15), command=download)
download.grid (pady=(80, 0))
completelabel = Label(root, text='', fg='#c62828', font=('Verdana', 15))
completelabel.grid(pady=(5, 0))

#Credit
creditlabel =  Label(root, text='Developed by ©Raunak Das', font=('Verdana', 10))
creditlabel.grid(pady=(30, 20))

root.mainloop()
