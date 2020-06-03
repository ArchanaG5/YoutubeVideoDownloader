from pytube import *
from tkinter import *  #for gui making
from tkinter.filedialog import *  #fordynamic ask directory
from tkinter.messagebox import *  #for message dialogue box
from threading import *  #to create thread

#total size container
file_size=0

#progressbar check function
def progress(stream, chunk, file_handle, remaining=None):
    #get the percentage of file
    file_downloaded=(file_size - file_handle)
    per=(file_downloaded / file_size) * 100
    dBtn.config(text="{:00.0f} % downloaded".format(per))

#function to download the youtube file
def startdownload():
    global file_size
    try:
        url=urlField.get()
        #print(url)
        if url == "":
            showinfo("Warning", "Please Enter Url")
            return
        # changing button text
        dBtn.config(text="Please Wait...")
        dBtn.config(state=DISABLED)
        path_to_save_vedio = askdirectory()
        #print(path_to_save_vedio)

        if path_to_save_vedio is None:
            return
        # create youtube object with url
        ob = YouTube(url, on_progress_callback=progress)  #automatically call progresschk function by own

        # get first streams
        strm= ob.streams.first()
        file_size=strm.filesize
        vediotitle.config(text=strm.title)
        #print(file_size)
        # for downloading the vedio
        strm.download(path_to_save_vedio)
        #print("done")
        dBtn.config(text="Start Download")
        dBtn.config(state=NORMAL)
        showinfo("Download Finished","Downloaded Successfully")
        urlField.delete(0,END)
    except Exception as e:
        print(e)
        print("error")

#creating a thread function
def startdownloadthread():
    #create thread
    thread=Thread(target=startdownload)
    thread.start()

####creating GUI building

#dialogue windw
mainwindow=Tk()  #main window of Tk class
mainwindow.title("My Youtube Downloader")  #setting dialog title
mainwindow.iconbitmap("img.ico")  #set the icon
mainwindow.geometry("400x500")  #setting the height and width
file=PhotoImage(file="img.png")
headerIcon=Label(mainwindow,image=file,width=120, height=100)
headerIcon.pack(side=TOP,ipadx=100,ipady=100)

#url text field
urlField=Entry(mainwindow,font=("verdana",14),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)

#download button
dBtn=Button(mainwindow, text="Start Download", font=("verdana", 15), relief='ridge', command=startdownloadthread)
dBtn.pack(side=TOP, pady=20)

#title name
vediotitle=Label(mainwindow,text="vedio title",font=("verdana",10))
vediotitle.pack(side=TOP,pady=5)

#dialogue window visible
mainwindow.mainloop()


