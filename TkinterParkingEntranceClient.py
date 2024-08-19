# Modules importation
from tkinter import *
from time import sleep
from time import strftime
from PIL import Image, ImageTk
from multiprocessing.connection import Client
import time

# Functions
def generate_barcode():
    from barcode import EAN13
    from barcode.writer import ImageWriter
    import random
    # Specify the code number as a string
    ticket_number = '7' + ''.join([str(random.randint(0, 9)) for _ in range(11)])
    # Create an EAN13 barcode object
    barcode = EAN13(ticket_number, writer=ImageWriter())   
    # Save the barcode as a PNG file
    barcode.save(ticket_number)
    return ticket_number 

def resize_image(file_name):
    img = Image.open(file_name)
    w = img.width
    h = img.height
    scale = 3
    img = img.resize((int(w/scale), int(h/scale)), Image.ADAPTIVE)
    # img.show()
    return img

def print_ticket():
    print('INFO:The printing has launched')
    ticket_number = generate_barcode()
    # Open and resize image to fit canvas 
    img = ImageTk.PhotoImage(resize_image(ticket_number + ".png"))  
    # Keep reference of your image (displaying image won't work otherwise)
    screen.image = img  
    # Add image to the Canvas items
    screen.create_rectangle(4, 4, 200, 150, fill="white", outline="white")
    screen.create_image(15,60, anchor=NW, image=img) 
    # Ajouter le code qui envoie l'information a turtle(server)
    send_message()

def send_message():
    # Client
    conn = Client(('localhost', 8080), authkey=b'PY C-2024')
    sleep(1)
    conn.send('ready to open')
    sleep(2)
    conn.send('close connection')
    conn.close()
  
def call_help():
    print('The help is coming, Please wait')

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

def reset_screen():
    screen.delete('all')

# Tkinter window as root
root = Tk()  # create parent window
root.title('Ticket Kiosk')
root.geometry("300x500")
root.config(bg="yellow")

# Creating the Clock
# Styling the label widget so that clock will look more attractive
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='limegreen',
            foreground='white') 
# Placing clock at the centre of the tkinter window
lbl.pack(anchor='center')
time()

# Creating the canvas
screen = Canvas(root, width=201, height=151)
screen.pack()
screen.create_rectangle(4, 4, 200, 150, fill="white", outline="white")
screen.create_text(25,25, anchor=CENTER, text=strftime('%H:%M:%S %p'))
time()
   
start = Button(root, text="Press for ticket", command=print_ticket,
               font=('calibri', 20, 'bold'))
start.pack()
start.config(activebackground="gray", bg="green")

call = Button(root, text="Call for help", command=call_help,
              font=('calibri', 20, 'bold'))
call.pack()
call.config(activebackground="gray", bg="blue")

# Keep tkinter window open
root.mainloop()
