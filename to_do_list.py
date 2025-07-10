import tkinter as tk
from PIL import Image,ImageTk

def exit_app():
    root.destroy()
root =tk.Tk()
width=250
height=250
root.overrideredirect(True)
root.wm_attributes("-topmost",1)
canvas = tk.Canvas(root, width=width, height=height, highlightthickness=0)
canvas.pack()
screen_width= root.winfo_screenwidth()
screen_height= root.winfo_screenheight()
x=screen_width - (width+20)
y=20
root.geometry(f"{width}x{height}+{x}+{y}")
menu=tk.Menu(root, tearoff=0)
menu.add_command(label="Exit",command=exit_app)
def show_context_menu(event):
    menu.tk_popup(event.x_root, event.y_root)
root.bind("<Button-3>",show_context_menu)   
#background image
bg_image =Image.open("background.png").resize((250,250),Image.Resampling.LANCZOS)
bg_photo =ImageTk.PhotoImage(bg_image)
canvas.create_image(0,0,image=bg_photo, anchor="nw")
#task entries
task_entries=[]
for i in range(10):
    entry=tk.Entry(root,font=("Red Hat Display",11,"bold"), fg="#9b431b", bg="#8fa9a9", relief="flat", justify="left")
    entry.place(x=42, y=30+i*20, width=140)
    task_entries.append(entry)
root.mainloop()
