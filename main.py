from pydub import AudioSegment
import os
import pandas as pd
import ffmpeg_handler as fh
from tkinter import *
from tkinter import filedialog,messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageFont, ImageDraw, ImageTk
import textwrap
import threading
import time


fh.check()

cols = [1,2,3]
# col = [2]
counter = 1

window = Tk()

window.title('Audio Splitter v1.0.0')

window.geometry("1000x1000")

window.resizable(0,0)

window_icon = ImageTk.PhotoImage(file="audio_logo.jpg")
window.iconphoto(False,window_icon)

audio_loc = StringVar()
excel_loc = StringVar()
dict_loc = StringVar()
image_loc = StringVar()
image_op = StringVar()
var = IntVar()

def browse_audio():
    global audio_loc
    audio_input = filedialog.askopenfilename(initialdir="/",
                                          title="Select a Audio File",
                                          filetypes=(("Audio Files",
                                                      f"*.flac*"),
                                                     ("all files",
                                                      "*.*")))
    audio_loc.set(f"{audio_input}")
def browse_excel():
    global excel_loc
    excel_input = filedialog.askopenfilename(initialdir="/",
                                          title="Select an Excel File",
                                          filetypes=(("Excel Files",
                                                      f"*.xlsx*"),
                                                     ("all files",
                                                      "*.*")))
    excel_loc.set(f"{excel_input}")
def browse_img():
    global image_loc
    image_input = filedialog.askopenfilename(initialdir="/",
                                          title="Select an Image File",
                                          filetypes=(("Image Files",
                                                      f"*.jpg*"),
                                                     ("all files",
                                                      "*.*")))
    image_loc.set(f"{image_input}")

def browse_dict():
    global dict_loc
    dict_input = filedialog.askdirectory()
    dict_loc.set(f"{dict_input}")
def browse_dict_img():
    global image_op
    image_dict_input = filedialog.askdirectory()
    image_op.set(f"{image_dict_input}")


def audio():   
        global counter,audio_loc,excel_loc,dict_loc,var
        choice  = var.get()
        if choice == 1:
            audio_type = "flac"
        elif choice == 2:
            audio_type =  "mp3"
        elif choice == 3:
            audio_type =  "wav"
        user_input = audio_loc.get()
        excel_input = excel_loc.get()
        file_dest = dict_loc.get()
        image_path = image_loc.get()
        image_dest = image_op.get()
        if len(user_input) == 0 or len(excel_input) == 0 or len(file_dest) == 0:
            messagebox.showerror(title="Empty Inputs",message="The Input Fields are Empty!")
            return
        else:
            try:
                df = pd.read_excel (f'{excel_input}', usecols = cols) 
                df = df.replace('\?','',regex=True) 
                temp = df.columns.values.tolist()
                count_row = df.shape[0]
            except FileNotFoundError:
                messagebox.showerror(title="File Not Found!",message="Splitting Stopped! File Not Found")
                return
            else:
                pb = Progressbar(window,orient = HORIZONTAL,length = 100,mode = 'determinate')
                pb.place(x=500, y=750)
                progress_text = Label(window,text= "Splitting in Process: ",font=("Courier", 10))
                progress_text.place(x=300,y=750)
                txt = Label(window,text = '0%',bg = '#345',fg = '#fff')
                txt.place(x=620 ,y=750)
                for i in range(count_row):                
                        window.update_idletasks()
                        pb['value'] += 100/count_row
                        time.sleep(1)
                        txt['text']=pb['value'],'%'
                        time1 = df.at[i,temp[1]]
                        time2 = df.at[i,temp[2]]
                        file_name = df.at[i,temp[0]]
                        t1 = get_seconds(str(time1))
                        t2 = get_seconds(str(time2))  
                        try:             
                            if audio_type=="mp3":
                                newAudio = AudioSegment.from_mp3(user_input)
                            elif audio_type=="wav":
                                newAudio = AudioSegment.from_wav(user_input)
                            else:
                                newAudio = AudioSegment.from_file(user_input)
                        except FileNotFoundError:
                            messagebox.showerror(title="File Not Found!",message="Splitting Stopped! File Not Found")
                            progress_text.destroy()
                            txt.destroy()
                            pb.destroy()
                            return
                        else:
                            newAudio = newAudio[t1:t2]
                        try:
                            newAudio.export(f'{file_dest}\\Q{counter}_{file_name}.'+audio_type, format=audio_type)
                        except FileNotFoundError:
                            messagebox.showerror(title="File Not Found!",message="Splitting Stopped! File Not Found")
                            progress_text.destroy()
                            txt.destroy()
                            pb.destroy()
                            return
                        else:
                            counter += 1
                        try:
                            image(image_path,image_dest,file_name,i)
                        except FileNotFoundError:
                            messagebox.showerror(title="File Not Found!",message="Splitting Stopped! File Not Found")
                            progress_text.destroy()
                            txt.destroy()
                            pb.destroy()
                            return
                choice = messagebox.askquestion(title="Splitting Sucessful!",message="Do you want to Split another Audio?")
                if choice == "yes":
                    audio_entry.delete(0,END)
                    excel_entry.delete(0,END)
                    output_entry.delete(0,END)
                    image_entry.delete(0,END)
                    image_output.delete(0,END)
                    progress_text.destroy()
                    txt.destroy()
                    pb.destroy()
                if choice == "no":
                        window.destroy()

def startaudio():
    threading.Thread(target=audio).start()

canvas = Canvas(height = 300, width=300)
img = Image.open("audio_logo.jpg")
resized_image= img.resize((200,200), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(resized_image)
canvas.create_image(150,150,image=img2)
canvas.place(x=350,y=5)


temp = Canvas(window)

type_label = Label(text="Format of Audio:")
type_label.config(font=("Courier", 10))
type_label.place(x=50,y=310)
audio_label = Label(text="Location of the Audio File:")
audio_label.config(font=("Courier", 10))
audio_label.place(x=50,y=380)
excel_label = Label(text="Location of Excel File:")
excel_label.config(font=("Courier", 10))
excel_label.place(x=50,y=450)
output_label = Label(text="Location for Audio Export:")
output_label.config(font=("Courier", 10))
output_label.place(x=50,y=520)
image_label = Label(text="Location of Image:")
image_label.config(font=("Courier", 10))
image_label.place(x=50,y=590)
image_output_label = Label(text="Location of Image Export:")
image_output_label.config(font=("Courier", 10))
image_output_label.place(x=50,y=660)

var.set(1)
Radiobutton(window, text="FLAC", variable=var, value=1,font=("Courier", 10)).place(x=350,y=305)
Radiobutton(window, text="MP3", variable=var, value=2,font=("Courier", 10)).place(x=440,y=305)
Radiobutton(window, text="WAV", variable=var, value=3,font=("Courier", 10)).place(x=530,y=305)

audio_entry = Entry(width=70,textvariable=audio_loc,borderwidth=0)
audio_entry.place(x=350,y=380,height=20)
excel_entry = Entry(width=70,textvariable=excel_loc,borderwidth=0)

excel_entry.place(x=350,y=450,height=20)
output_entry = Entry(width=70,textvariable=dict_loc,borderwidth=0)
output_entry.place(x=350,y=520,height=20)

image_entry = Entry(width=70,textvariable=image_loc,borderwidth=0)
image_entry.place(x=350,y=590,height=20)
image_output = Entry(width=70,textvariable=image_op,borderwidth=0)
image_output.place(x=350,y=660,height=20)



audio_button = Button(text="Add Location",width=20,bg="#4D90FE",fg="white",font=("Courier",10),borderwidth=0,command=browse_audio)
audio_button.place(x=800,y=380)

excel_button = Button(text="Add Location",width=20,bg="#4D90FE",fg="white",font=("Courier",10),borderwidth=0,command=browse_excel)
excel_button.place(x=800,y=450)

output_button = Button(text="Add Location",width=20,bg="#4D90FE",fg="white",font=("Courier",10),borderwidth=0,command=browse_dict)
output_button.place(x=800,y=520)
image_button = Button(text="Add Location",width=20,bg="#4D90FE",fg="white",font=("Courier",10),borderwidth=0,command=browse_img)
image_button.place(x=800,y=590)
image_output_button = Button(text="Add Location",width=20,bg="#4D90FE",fg="white",font=("Courier",10),borderwidth=0,command=browse_dict_img)
image_output_button.place(x=800,y=660)


export_button = Button(text="SPLIT AUDIO",width=60,bg="#4D90FE",fg="white",font=("Courier",10, "bold"), borderwidth=0, command=startaudio)
export_button.place(x=300,y=710)

def get_seconds(time):
    hh, mm, ss = time.split(':')
    seconds = int(hh) * 3600 + int(mm) * 60 + int(ss) 
    return seconds * 1000



def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=40)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text += line_height



def image(img_path,image_dest,file_name,i):
    my_image = Image.open(img_path)
    text_start_height = 1750
    myFont = ImageFont.truetype('C:/Windows/Fonts/LCALLIG.ttf', 65)
    draw_multiple_line_text(my_image, f"{file_name}?", myFont, (0,0,0), text_start_height)
    my_image.save(f"{image_dest}\\Q_{i+1}{file_name}.jpg")



window.mainloop()
