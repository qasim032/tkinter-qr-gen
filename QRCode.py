from customtkinter import *
import qrcode
from PIL import Image, ImageTk

def generate():
    #Saving the image in disk
    qr = qrcode.make(entry.get())
    qr.save("qr.png") 
    
    # Image load 
    img = ImageTk.PhotoImage(Image.open("qr.png").resize((200, 200)))
    
    #Defines the postion and display the qrcode image
    qr_label = CTkLabel(master=app, text="") 
    qr_label.place(relx=0.5, rely=0.75, anchor="center")
    qr_label.configure(image=img)
    qr_label.image = img  


set_appearance_mode("Dark")
set_default_color_theme("blue")

# Window setup
app = CTk()
app.geometry("600x600")
app.title("QR Code Generator by Qasim")

# Entry
entry = CTkEntry(master=app, placeholder_text="Paste link here", width=300, text_color="#FFFFFF")
entry.place(relx=0.5, rely=0.4, anchor="center")

# Button
btn = CTkButton(master=app, text="Generate QRCode", command=generate, corner_radius=32, fg_color="#8B1740", hover_color="#059FFF")
btn.place(relx=0.5, rely=0.55, anchor="center")


# Run
app.mainloop()
