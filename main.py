'''
Antonio Leon
11/15/2023
Files Organizer UI Version
'''
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import shutil
import os
import sys
import subprocess

class FilesOrganizerUI:
    def __init__(self, window):
        self.window = window
        self.window.geometry("600x500")
        self.window.configure(bg="lightgray")
        self.window.title("Files Organizer")
        
        self.create_ui(Event)
    
    def create_ui(self, event):
        #Canvas 1 and 2.
        self.canvas_1 = tk.Canvas(window, width=1920, height=35, bg="#221270", highlightbackground="#221270")    
        self.canvas_1.pack(padx=5, pady=5)
        
        self.canvas_2 = tk.Canvas(window, width=1920, height=1080, bg="white")
        self.canvas_2.pack(padx=5, pady=5)

        #Buttons reset, about, and move. 
        self.reset_button = tk.Button(window, text="Reset", relief=FLAT, bg="#221270", fg="white", width=5, height=1, command=self.reset)
        self.canvas_1.create_window(30, 20, window=self.reset_button)
        
        self.about_button = tk.Button(window, text="About", relief=FLAT, bg="#221270", fg="white", width=5, height=1, command="")
        self.canvas_1.create_window(557, 20, window=self.about_button)
        
        self.move_button = tk.Button(window, text="Move", relief=FLAT, bg="#221270", fg="white", width=12, height=1, command=self.move_files)
        self.canvas_2.create_window(300, 400, window=self.move_button)
        
        #Labels.
        self.source_label = tk.Label(window, text="Enter SOURCE path", font=("helvetica", 15), bg="white")
        self.canvas_2.create_window(300, 70, window=self.source_label)
        
        self.destination_label = tk.Label(window, text="Enter DESTINATION path", font=("helvetica", 15), bg="white")
        self.canvas_2.create_window(300, 180, window=self.destination_label)
        
        self.user_selection_label = tk.Label(window, text="Select an option from the menu", font=("helvetica", 10), bg="white")
        self.canvas_2.create_window(300, 290, window=self.user_selection_label)
    
        #Entry Boxes source and destination.
        self.source_entrybox = tk.Entry(window, width=45, font=("helvetica", 12), bd=1, relief=tk.SOLID)
        self.canvas_2.create_window(300, 100, window=self.source_entrybox)
        
        self.destination_entrybox = tk.Entry(window, width=45, font=("helvetica", 12), bd=1, relief=tk.SOLID)
        self.canvas_2.create_window(300, 210, window=self.destination_entrybox)
        
        #Combobox to select options jpg, mp4, etc...
        self.combobox = ttk.Combobox(window, values=("jpg-jpeg-JPG", "mp4-MP4", "png-PNG"), )
        self.combobox.config(state="readonly")
        self.combobox.config(width=30)
        #self.combobox.bind("<<ComboboxSelected>>", self.move_files)
        self.canvas_2.create_window(300, 310, window=self.combobox)
      
    def reset(self):
        self.window.destroy()
        subprocess.Popen([sys.executable] + sys.argv)
                
    def move_jpg(self):  
        
        try: 
            for filename in os.listdir(self.src):
                if filename.endswith('.jpg') or filename.endswith('jpeg') or filename.endswith('JPG'):
                    src_file = os.path.join(self.src, filename)
                    dst_file = os.path.join(self.dst, filename)
                        
                    #Move file src to folder destination to dst.
                    shutil.move(src_file, dst_file)
                        
        except FileNotFoundError:
            messagebox.showwarning("Warning", "File jpg not found :(")

    def move_mp4(self):
    
        try:
            for filename in os.listdir(self.src):
                if filename.endswith('.mp4') or filename.endswith('.MP4'):
                    src_file = os.path.join(self.src, filename)
                    dst_file = os.path.join(self.dst, filename)
                    
                    #Move file src to folder destination to dst.
                    shutil.move(src_file, dst_file)
                    
        except FileNotFoundError:
            messagebox.showwarning("Warning", "File mp4 not found :(")
                    
    def move_png(self):
        
        try:
            for filename in os.listdir(self.src):
                if filename.endswith('.png') or filename.endswith('.PNG'):
                    src_file = os.path.join(self.src, filename)
                    dst_file = os.path.join(self.dst, filename)
                    
                    #Move file src to folder destination to dst.
                    shutil.move(src_file, dst_file)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "File png not found :(")            

    def move_files(self):
        #Getting user input from the entry boxes source and destination.
        self.user_source = self.source_entrybox.get()
        self.user_source = self.user_source.replace('"', '').replace("'", '')
        self.src = self.user_source
        
        self.user_destination = self.destination_entrybox.get()
        self.user_destination = self.user_destination.replace('"', '').replace("'", '')
        self.dst = self.user_destination
        
        self.selected_option = self.combobox.get()
        
        if self.selected_option == "jpg-jpeg-JPG":
            self.move_jpg()
        elif self.selected_option == "mp4-MP4":
            self.move_mp4()
        elif self.selected_option == "png-PNG":
            self.move_png()
        else:
            messagebox.showwarning("Warning", "Select an option from the menu!")
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    window = Tk()
    file_organizer_UI = FilesOrganizerUI(window)
    file_organizer_UI.run()