
from tkinter import *
from ventana import *
import pymongo



def main():
    root = Tk()
    root.wm_title("Crud Python MySQL")
    app = Ventana(root)
    app.mainloop()




if __name__ == "__main__":
    main()