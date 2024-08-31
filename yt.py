# from pytube import YouTube
 
 
# def download_vid(url, path= '.'):
    
#     try:
#         yt= YouTube(url)
        
#         stream= yt.streams.get_highest_resolution()
        
#         print(f"Dowmloading '{yt.title}'...")
#         stream.download(output_path=path)
        
#         print("DOWNLOAD COMPLETED!")
        
#     except Exception as e:
#         print(f"An error occurd: {e}")
        
# def convert_mp4(url, path='.'):
#     try:
#         yt= YouTube(url)
        
#         stream= yt.streams.filter(only_audio=True).first()
        
#         print(f"Downloading mp4 of {yt.title}")
        
#         stream.download(output_path=path)
        
#         print(f"{yt.title} is DOWNLOADED")
        
#     except Exception as e:
#         print(f"An error occured: {e}")
        
# def convertmp4(url, path= '.'):
#     try: 
#         yt=YouTube(url)
#         stream= yt.streams.filter(file_extension='mp4').get_highest_resolution()
        
#         print(f"Downloading mp4 of {yt.title}")
        
#         stream.download(output_path=path)
        
#         print(f"{yt.title} is DOWNLOADED")
        
#     except Exception as e:
#         print(f"An error occured: {e}")
# if __name__=="__main__":
    
#     vid_url= input("Youtube video url: ")
    
#     pth= input("Download Path(or leave blank): ")
    
#     pth= pth if pth else '.'
    
#     convert_mp4(vid_url, pth)


import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import customtkinter as ctk
from moviepy.editor import VideoFileClip
from datetime import datetime
import json
import os

root = ctk.CTk()
root.title("YouTube Video Downloader")
root.attributes("-fullscreen", True)
root.configure(fg_color='white')



class Main:
    def __init__(self):
        self.label_size = 40
        self.history_file= 'download_history.json'   

    def toggle_fullscreen(self, event=None):
        root.attributes("-fullscreen", not root.attributes("-fullscreen"))

    def main(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme('green')
        
        notebook = ttk.Notebook(root)
        notebook.place(x=255, y=80, width=800, height=1000)

        self.download_tab = tk.Frame(notebook, bg='snow2')
        notebook.add(self.download_tab, text='Download Video from YouTube')
        self.create_download_tab()

       
        self.history_tab = tk.Frame(notebook, bg='snow2')
        notebook.add(self.history_tab, text='Download History')
        self.history()
        
        self.mp4_tab= tk.Frame(notebook,bg= 'snow1' )
        notebook.add(self.mp4_tab, text= "Youtube Video to MP4")
        self.create_dlmp4_tab()

        upper = tk.Frame(root, bg='green2', highlightbackground='green3', highlightthickness=2, width=1366, height=150)
        upper.place(x=0, y=0)

        upper2 = tk.Frame(root, bg='chartreuse2', width=1366, height=50, highlightthickness=2, highlightbackground='green3')
        upper2.place(x=0, y=150)

        self.lx = 400
        self.ly = 70

        lbl = ctk.CTkLabel(upper, text="Download Video from YouTube", text_color='White', font=('Roboto Black', self.label_size))
        lbl.place(x=self.lx, y=self.ly)
        lbl.bind("<Button-1>", lambda event: notebook.select(self.download_tab))

        ytvid = ctk.CTkLabel(upper2, text="YouTube Video Download", font=('Roboto Black', 18))
        ytvid.place(x=350, y=10)
        ytvid.bind("<Button-1>", lambda event: notebook.select(self.download_tab))

        ytmusic = ctk.CTkLabel(upper2, text="YouTube Video to MP4", font=('Roboto Black', 18))
        ytmusic.place(x=800, y=10)
        ytmusic.bind("<Button-1>", lambda event: notebook.select(self.mp4_tab))

        menu = ctk.CTkLabel(upper2, text="Download History", font=('Roboto Black', 18))
        menu.place(x=100, y=10)
        menu.bind("<Button-1>", lambda event: notebook.select(self.history_tab))

        root.bind("<Escape>", self.toggle_fullscreen)
        root.mainloop()

    def create_download_tab(self):
        disclaimer = ctk.CTkLabel(self.download_tab, text="(DISCLAIMER: Ensure that downloading this video complies with YouTube's Terms of Service and copyright laws.)", font=('Roboto Black', 9))
        disclaimer.place(x=190, y=390)

        lbl2 = ctk.CTkLabel(self.download_tab, text="Do you have permission to download this video?: ", font=('Roboto', 15))
        lbl2.place(x=190, y=300)

        # search = ctk.CTkLabel(self.download_tab, text="Search: ", font=('Roboto', 18))
        # search.place(x=190, y=190)

        # searchtb = ctk.CTkTextbox(self.download_tab, width=400, height=40, border_width=3, border_color='DarkOliveGreen4', border_spacing=3)
        # searchtb.place(x=260, y=190)

        # lbl4 = ctk.CTkLabel(self.download_tab, text="OR", font=('Roboto', 14))
        # lbl4.place(x=430, y=250)

        yn = ['yes', 'no']
        option_var = tk.StringVar(root)
        option_var.set(yn[0])
        opt = tk.OptionMenu(self.download_tab, option_var, *yn)
        opt.config(width=20, background='green2')
        opt.place(x=270, y=360)

        lbl3 = ctk.CTkLabel(self.download_tab, text="Enter URL: ", font=('Roboto', 17))
        lbl3.place(x=190, y=200)

        self.entry = ctk.CTkTextbox(self.download_tab, width=400, height=40, border_width=3, border_color='DarkOliveGreen4', border_spacing=3)
        self.entry.place(x=270, y=200)

        self.entry.bind("<Return>", self.start_url)
        
        self.progress = ctk.CTkProgressBar(self.download_tab, width=450, height=70)
        self.progress.place(x=190, y=450)
        self.progress.set(0)

    
        
    def create_dlmp4_tab(self,):
        disclaimer = ctk.CTkLabel(self.mp4_tab, text="(DISCLAIMER: Ensure that downloading this video complies with YouTube's Terms of Service and copyright laws.)", font=('Roboto Black', 9))
        disclaimer.place(x=190, y=470)

        lbl2 = ctk.CTkLabel(self.mp4_tab, text="Do you have permission to download this video?: ", font=('Roboto', 15))
        lbl2.place(x=190, y=390)

        search = ctk.CTkLabel(self.mp4_tab, text="Search: ", font=('Roboto', 18))
        search.place(x=190, y=150)

        searchtb = ctk.CTkTextbox(self.mp4_tab, width=400, height=40, border_width=3, border_color='DarkOliveGreen4', border_spacing=3)
        searchtb.place(x=260, y=150)

        lbl4 = ctk.CTkLabel(self.mp4_tab, text="OR", font=('Roboto', 14))
        lbl4.place(x=430, y=200)

        yn = ['yes', 'no']
        option_var = tk.StringVar(root)
        option_var.set(yn[0])
        opt = tk.OptionMenu(self.mp4_tab, option_var, *yn)
        opt.config(width=20, background='green2')
        opt.place(x=270, y=430)

        lbl3 = ctk.CTkLabel(self.mp4_tab, text="Enter URL: ", font=('Roboto', 17))
        lbl3.place(x=190, y=250)

        self.entry2= ctk.CTkTextbox(self.mp4_tab, width=400, height=40, border_width=3, border_color='DarkOliveGreen4', border_spacing=3)
        self.entry2.place(x=270, y=250)

        self.entry2.bind("<Return>", self.mp4_url)
        
        self.enter= ctk.CTkButton(self.mp4_tab, text="ENTER", bg_color='green2', width= 200, height=60, border_width=0, command= self.mp4_url)
        self.enter.place(x=350, y=310)
        
        
        self.progress = ctk.CTkProgressBar(self.mp4_tab, width=400, height=50)
        self.progress.place(x=190, y=530)
        self.progress.set(0)
        
        
    def mp4_url(self, event=None):
        get_mp4= self.entry2.get(1.0, tk.END).strip()
        
        try:
            yt=YouTube(get_mp4, on_progress_callback= self.on_progress)
            stream= yt.streams.filter(only_audio=True).first()
            path = r"C:\Users\asus\Documents\Downloaded Videos"
            
            self.show_message(f"{yt.title} is DOWNLOADING")
            
            stream.download(output_path=path)
            
            self.show_message(f"{yt.title} is DOWNLOADED in {path}")
            
            ht=self.create_history_tab(yt.title, path)
        except Exception as e:
            self.show_message(f"An error occurred: {e}", error=True)
        
    def start_url(self, event=None):
        self.url()

    def url(self):
        get_url = self.entry.get(1.0, tk.END).strip()
        if not get_url:
            self.show_message("No URL entered.", error=True)
            return

        try:
            yt = YouTube(get_url, on_progress_callback=self.on_progress)
            stream = yt.streams.get_highest_resolution()
            path = r"C:\Users\asus\Documents\Downloaded Videos"

            self.show_message(f"{yt.title} is DOWNLOADING....")
            stream.download(output_path=path)
            self.show_message(f"{yt.title} is DOWNLOADED in {path}")

        except Exception as e:
            self.show_message(f"An error occurred: {e}", error=True)
            
    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        percent = percentage_of_completion / 100
        self.progress.set(percent)

    def show_message(self, message, error=False):
        color = 'red' if error else 'green'
        label = ctk.CTkLabel(self.download_tab, text=message, text_color=color, font=('Roboto Black', 12))
        label.place(x=160, y=560)
       
    def create_history_tab(self, title, path):
        lbl = ctk.CTkLabel(self.history_tab, text="Download History", font=('Roboto', 18))
        lbl.place(x=350, y=10)     
        
        downloads= {'title': title, 'path': path, 'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r')as file:
                history= json.load(file)
                
        else:
            history=[]
        history.append(downloads)
        
        with open(self.history_file, 'w') as file:
            json.dump(history, file, indent=3)
            
    def history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as file:
                history= json.load(file)
                for entry in history:
                    lbl= tk.LabelFrame(self.history_tab, width=600, height=130)
                    lbl.place(x=100, y=100)
                    
                    lbll= ctk.CTkLabel(lbl, text= f"TITLE: {entry['title']}- PATH: {entry['path']}- DATE: {entry['time']}")
                    lbll.place(x=100, y=70)
                    
                  
        else:
            n= ctk.CTkLabel(self.history_tab, text= "NO DOWNLOADED VIDEOS")
            n.place(x=100, y=300)
          
                
        

m = Main()
m.main()
