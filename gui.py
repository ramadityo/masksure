import os
import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class GUI:
    def __init__(self):
        self.m = tkinter.Tk()
        self.m.title("masksure")
        self.m.geometry("%dx%d+0+0" % (self.m.winfo_screenwidth(), self.m.winfo_screenheight()))
        self.m.configure(bg='white')

        self.label = Label(self.m, text='Silakan masukkan gambar untuk melakukan pendeteksian!', font=("Arial", 30))
        self.label.pack()

        self.file_path = StringVar()
        self.entry = Entry(self.m, textvariable=self.file_path, width=50)
        self.entry.pack()

        self.button = Button(self.m, text="Browse", command=self.browse_file)
        self.button.pack()

        self.show_image(self.file_path.get())
        self.image_label = None
        self.m.mainloop()
    
    def browse_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        if path: 
            self.file_path.set(path)
            self.show_image(path)

    def show_image(self, image_path):
        if os.path.isfile(image_path):

            try:
                img = Image.open(image_path)
                img = img.resize((img.width // 2, img.height // 2))
                img = ImageTk.PhotoImage(img)
                
                if self.image_label:
                    self.image_label.destroy()
                
                # Tambahkan label baru untuk menampilkan gambar
                self.image_label = Label(self.m, image=img)
                self.image_label.image = img
                self.image_label.pack()
            except Exception as e:
                print(f"Error loading image: {e}")
                messagebox.showerror("Error", f"Failed to load image: {e}")