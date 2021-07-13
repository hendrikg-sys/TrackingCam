import tkinter as tk
from tkinter.constants import ANCHOR
import cv2
import PIL
from tkinter import filedialog

class MainWindow(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.master.title("GUI")
        #self.master.geometry("1000x600")

        self.Listbox1 = tk.Listbox(self.frame)
        self.Listbox1.grid(row=0, column=0, columnspan=6, sticky="ew")

        self.Button1 = tk.Button(self.frame,text="Add", command=MainWindow.load_video)
        self.Button1.grid(row=1, column=0, sticky="w")

        self.Button2 = tk.Button(self.frame,text="Remove")
        self.Button2.grid(row=1, column=1 ,columnspan=2, sticky="w")

        self.Button3 = tk.Button(self.frame,text="Clear")
        self.Button3.grid(row=1, column=2, sticky="w")

        self.Listbox2 = tk.Listbox(self.frame)
        self.Listbox2.grid(row=2, column=0, columnspan=6, sticky="ew")

        self.Button4 = tk.Button(self.frame,text="New")
        self.Button4.grid(row=3, column=0, sticky="w")

        self.Button5 = tk.Button(self.frame,text="Rename")
        self.Button5.grid(row=3, column=1, sticky="w")

        self.Button6 = tk.Button(self.frame,text="Remove")
        self.Button6.grid(row=3, column=2, sticky="w")

        self.Button7 = tk.Button(self.frame,text="Clear")
        self.Button7.grid(row=3, column=3, sticky="w")

        self.Button8 = tk.Button(self.frame,text="Save")
        self.Button8.grid(row=3, column=4, sticky="w")

        self.Button9 = tk.Button(self.frame,text="Load")
        self.Button9.grid(row=3, column=5, sticky="w")

        self.Button9 = tk.Button(self.frame,text="Add to movement")
        self.Button9.grid(row=4, column=0, columnspan=3, sticky="ew")

        self.Listbox2 = tk.Listbox(self.frame, width=25)
        self.Listbox2.grid(row=5, column=0, columnspan=3, sticky="ew")

        self.Listbox3 = tk.Listbox(self.frame, width=25)
        self.Listbox3.grid(row=5, column=3, columnspan=3, sticky="ew")

        self.Button10 = tk.Button(self.frame,text="New")
        self.Button10.grid(row=6, column=0, sticky="w")

        self.Button11 = tk.Button(self.frame,text="Rename")
        self.Button11.grid(row=6, column=1, sticky="w")

        self.Button12 = tk.Button(self.frame,text="Remove")
        self.Button12.grid(row=6, column=2, sticky="w")

        self.Button13 = tk.Button(self.frame,text="Clear")
        self.Button13.grid(row=6, column=3, sticky="w")

        self.Button14 = tk.Button(self.frame,text="Save")
        self.Button14.grid(row=6, column=4, sticky="w")

        self.Button15 = tk.Button(self.frame,text="Load")
        self.Button15.grid(row=6, column=5, sticky="w")

        self.canvas = tk.Canvas(self.frame, width=800, height=600, bg="white")
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.grid(row= 0,rowspan=6,column=7, sticky="n")
        
    def draw(self,event):
        x1, y1 = (event.x - 10),(event.y - 10 )
        x2, y2 = (event.x + 10),(event.y + 10)
        self.canvas.create_oval(x1,y1,x2,y2, fill="black")

    def load_video():
        video_source = filedialog.askopenfile(filetypes=[("Videofiles", '*.mpeg')])

        #TODO use filepath to load video and put frame on canvas

    # def update(self):
    #      # Get a frame from the video source
    #      ret, frame = self.vid.get_frame()
 
    #      if ret:
    #          self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    #          self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
 
    #      self.window.after(self.delay, self.update)
           
class Video:
    def __init__(self, filepath) -> None:
        self.Filepath = filepath

        self.video_file = cv2.VideoCapture(filepath)
        self.width = self.video_file.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.video_file.get(cv2.CAP_PROP_FRAME_HEIGHT)



def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
    


if __name__ == '__main__':
    main()