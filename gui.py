import os
import tkinter
from tkinter import *
import customtkinter

from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

from detection import Detection

class GUI:
    def __init__(self):
        customtkinter.set_appearance_mode("light")
        self.app = customtkinter.CTk()
        self.app.geometry("%dx%d+0+0" % (self.app.winfo_screenwidth(), self.app.winfo_screenheight()))
        self.app.title("MaskSure")
        self.preload()
        self.app.mainloop()
        # self.m = tkinter.Tk()

    def preload(self):
        self.app.configure(fg_color='white')

        self.preload_label = customtkinter.CTkLabel(self.app, text="MaskSure", font=("Plus Jakarta Sans", 70, "bold"), bg_color="black", fg_color="white")
        self.preload_label.place(relx=0.5, rely=0.5, anchor="center")

        self.app.after(2000, lambda: (self.preload_label.destroy(), self.home()))
        
        
    def home(self):
        self.app.configure(fg_color='white')

        self.stack = customtkinter.CTkFrame(self.app, corner_radius=0, fg_color="white")
        self.stack.pack(fill="y")

        self.label_home = customtkinter.CTkLabel(self.stack, text="Masukkan gambar untuk melakukan pendeteksian!", font=("Plus Jakarta Sans", 40, "bold"), bg_color="black", fg_color="white")
        self.label_home.pack(pady=25)

        self.button = customtkinter.CTkButton(self.stack, text="Upload image", font=("Plus Jakarta Sans", 15, "bold"), corner_radius=5, command=self.browse_file, border_spacing=10)
        self.button.pack(pady=0)


        self.file_path = StringVar()
        self.image_container = customtkinter.CTkFrame(self.stack, corner_radius=0, fg_color="white")
        self.image_container.pack(fill="x")

        
        self.show_image(self.file_path.get())
        self.image_label = None

        self.width = 0
        self.height = 0
    
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

                width, height = img.size 
                self.width = width
                self.height = height

                if width > 1000:
                    img = img.resize((width // 3, height // 3))  
                elif width < 500:
                    img = img.resize((width * 2, height * 2))
                else:
                    img = img.resize((width // 2, height // 2))  
                    
                img = ImageTk.PhotoImage(img)

                for widget in self.image_container.winfo_children():
                    widget.destroy()

                original_label = customtkinter.CTkLabel(
                    self.image_container,
                    image=img,
                    text="Gambar asli",
                    compound="top",
                    font=("Plus Jakarta Sans", 15, "bold")
                )
                original_label.image = img  
                original_label.grid(row=0, column=2, padx=10, pady=10)

                self.process_image()

            except Exception as e:
                print(f"Error loading image: {e}")
                messagebox.showerror("Error", f"Failed to load image: {e}")

    
    def process_image(self):
        image_path = self.file_path.get()
        if not os.path.isfile(image_path):
            messagebox.showerror("Error", "Please upload a valid image first.")
            return

        processed_image = Detection.detect(image_path)
        if processed_image is not None:
            try:
                if self.width > 1000:
                    # img = img.resize((width // 3, height // 3))  
                    processed_image = processed_image.resize((processed_image.width // 3, processed_image.height // 3))
                elif self.width < 500:
                    processed_image = processed_image.resize((processed_image.width * 2, processed_image.height * 2))
                else:
                    # img = img.resize((width // 2, height // 2))  
                    processed_image = processed_image.resize((processed_image.width // 2, processed_image.height // 2))
                    
                img = ImageTk.PhotoImage(processed_image)

                processed_label = customtkinter.CTkLabel(self.image_container, image=img, text="Hasil deteksi", compound="top", font=("Plus Jakarta Sans", 15, "bold"))
                processed_label.image = img 
                processed_label.grid(row=0, column=3, padx=10, pady=10)

            except Exception as e:
                print(f"Error displaying processed image: {e}")
                messagebox.showerror("Error", f"Failed to display processed image: {e}")
