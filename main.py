from tkinter import *
from tkinter import ttk
import random
from quicksort import quick_sort
from mergesort import merge_sort
from timsort import timSort_algorithm

import pdb


# Main window and its attributes
root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='#2F4F4F')



# variables
current_algorithm = StringVar()
data = []


def popupmsg(msg):
    popup = Tk()
    popup.geometry('300x100')
    popup.config(bg='#2F4F4F')
    popup.wm_title("Information")
    label = Label(popup, text=msg, font=("Comic Sans MS", 10),bg='#2F4F4F',fg='white')
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="OK", command=popup.destroy, bg='grey', width=10)
    B1.pack()
    popup.mainloop()

def drawData(data,colorlist):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 20
    spacing = 10
    normalized_data = [ i / max(data) for i in data]
    for i, height in enumerate(normalized_data):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorlist[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]),fill="orange")
    root.update_idletasks()
def Generate():
    global data
    print('Selected Algorithm: ' + current_algorithm.get())
    minVal = int(min_value.get())
    maxVal = int(max_value.get())
    size = int(size_value.get())
    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))
    drawData(data, ['#B22222' for x in range(len(data))])

def StartAlgorithm():
    global data
    if not data:
        return
    if algorithm_menu.get() == "Quick Sort":
        elapsed_time_fl=quick_sort(data,0, len(data)-1,drawData,speed_rate.get())
        drawData(data,['green' for x in range(len(data))])
        popupmsg(f'Selected Algorithm: {current_algorithm.get()}\n\nExecution Time: {elapsed_time_fl}')
    elif algorithm_menu.get() == "Merge Sort":
        elapsed_time_fl=merge_sort(data,drawData,speed_rate.get())
        popupmsg(f'Selected Algorithm: {current_algorithm.get()}\n\nExecution Time: {elapsed_time_fl}')
    elif algorithm_menu.get() == "Tim Sort":
        elapsed_time_fl = timSort_algorithm(data, drawData, speed_rate.get())
        popupmsg(f'Selected Algorithm: {current_algorithm.get()}\n\nExecution Time: {elapsed_time_fl}')


# frame / base layout
UI_frame = Frame(root, width= 600, height=200,bg="#2F4F4F")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='black',highlightbackground="white")
canvas.grid(row=1, column=0, padx=10, pady=5)


Label(UI_frame, text="Algorithm: ", bg='#8FBC8F').grid(row=0, column=0, padx=5, pady=5, sticky=W,)
algorithm_menu = ttk.Combobox(UI_frame,state="readonly", textvariable=current_algorithm, values=['Quick Sort', 'Merge Sort', 'Tim Sort'])
algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
algorithm_menu.current(0)
Label(UI_frame, text="Speed ", bg='#8FBC8F').grid(row=0, column=2, padx=5, pady=5, sticky=W)
speed_rate = Scale(UI_frame, from_=0.1, to=5.0, resolution=0.2, length=100, digits=2 ,orient=HORIZONTAL, font=("Comic Sans MS", 14, "italic bold"),
                   relief=GROOVE, bd=2, width=10)
speed_rate.grid(row=0, column=3, padx=5, pady=5, sticky=W)
Button(UI_frame, text="Generate", command=Generate, bg='#B22222',activebackground="#DC143C",activeforeground="white").grid(row=0, column=4, padx=5, pady=5)
Button(UI_frame, text="Start Sorting", command=StartAlgorithm ,bg='lime',activebackground="#05945B",activeforeground="#F8F8FF").grid(row=0, column=5, padx=5, pady=5)
# Row[1]
Label(UI_frame, text="Size ", bg='#8FBC8F').grid(row=1, column=0, padx=5, pady=5, sticky=W)
size_value = Scale(UI_frame, from_=1, to=99, resolution=1, orient=HORIZONTAL, font=("Comic Sans MS", 14, "italic bold"),
                   relief=GROOVE, bd=2, width=10)
size_value.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Min Value ", bg='#8FBC8F').grid(row=1, column=2, padx=5, pady=5, sticky=W)
min_value = Scale(UI_frame, from_=1, to=10, resolution=1, orient=HORIZONTAL, font=("Comic Sans MS", 14, "italic bold"),
                   relief=GROOVE, bd=2, width=10)
min_value.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Max Value ", bg='#8FBC8F').grid(row=1, column=4, padx=5, pady=5, sticky=W)
max_value = Scale(UI_frame, from_=1, to=100, resolution=1, orient=HORIZONTAL, font=("Comic Sans MS", 14, "italic bold"),
                   relief=GROOVE, bd=2, width=10)
max_value.grid(row=1, column=5, padx=5, pady=5, sticky=W)

root.mainloop()
