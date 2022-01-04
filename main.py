from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from DataPreprocessor import Datapreprocessor
from network import Hopfield



dataset_url = ""
model = ""
def openfile():
    global dataset_url
    dataset_url = filedialog.askopenfilename(title="Select file")


def prepare_data_list():
    dataset = Datapreprocessor.readfile(dataset_url)
    data_list,num_per_line = Datapreprocessor.generate_list(dataset)
    return data_list,num_per_line

def start_train():
    global model
    train_list,num_per_line = prepare_data_list()
    model = Hopfield(train_list)

def start_test():
    fig.clear()
    f_plot = fig.add_subplot(111)
    test_list,num_per_line = prepare_data_list()
    iterate = int(entry_epoch.get())
    test_element = np.array([test_list[int(test_index.get())]]).transpose()
    result = model.test(iterate, test_element)
    result=result.transpose()
    result=result.reshape(int(len(test_list[0])/num_per_line),num_per_line)
    f_plot.matshow(result)
    canvas.draw()


window = tk.Tk()
window.title('Hopfield')
window.geometry('500x500')
#plot
# the figure that will contain the plot
fig = Figure(figsize = (5, 5),
        dpi = 100)
# creating the Tkinter canvas
# containing the Matplotlib figure
canvas = FigureCanvasTkAgg(fig,
                            master = window)
# placing the canvas on the Tkinter window
canvas.get_tk_widget().pack()


#select train data and train
select_train_data_btn = tk.Button(window, text='select training dataset', command=openfile).pack()
start_train_btn = tk.Button(window, text='start training', command=start_train).pack()
select_test_data_btn = tk.Button(window, text='select test dataset', command=openfile).pack()
start_test_btn = tk.Button(window, text='start test', command=start_test).pack()

tk.Label(window, text='聯想次數: ').pack()
epoch = tk.IntVar()
entry_epoch = tk.Entry(window, textvariable=epoch)
entry_epoch.pack()

tk.Label(window, text='測試資料中第幾個: ').pack()
test_index = tk.IntVar()
entry_test_index = tk.Entry(window, textvariable=test_index)
entry_test_index.pack()

window.mainloop()