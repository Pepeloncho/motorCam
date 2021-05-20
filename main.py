import motorlib as ml
import tkinter as tk
import cv2
from tkinter import filedialog

directory: str = '/directorioFotos'
if __name__ == '__main__':


    window = tk.Tk()
    window.title("motorCam GUI")
    selected = tk.IntVar()
    singleradius = tk.Radiobutton(window, text='Paso singular', value=1, variable=selected)
    doubleradius = tk.Radiobutton(window, text='Paso doble', value=2, variable=selected)
    halfradius = tk.Radiobutton(window, text='Medio paso', value=3, variable=selected)


    def detspeed(speed):
        if speed == 1:
            return 0.02
        if speed == 2:
            return 0.018
        if speed == 3:
            return 0.016
        if speed == 4:
            return 0.014
        if speed == 5:
            return 0.012
        if speed == 6:
            return 0.010
        if speed == 7:
            return 0.009
        if speed == 8:
            return 0.008
        if speed == 9:
            return 0.007
        if speed == 10:
            return 0.006


    def detmethod(method):
        if method == 1:
            return 'singleStep'
        if method == 2:
            return 'doubleStep'
        if method == 3:
            return 'halfStep'
        else:
            return 'singleStep'


    def exec():
        pspeed = int(speed.get())
        pmethod = selected
        global directory
        directory = directory + '/'
        print('Solicitando ejecución con parámetros: '+str(pspeed)+' '+str(pmethod)+' '+directory)
        ml.photoloop(ml.board, detspeed(pspeed), directory, detmethod(pmethod))



    def getPath():
        global directory
        directory = tk.filedialog.askdirectory()


    execlb = tk.Label(window, text="Escoger Rutina")
    execbtn = tk.Button(window, text="Ejecutar", command=exec)
    speedlb = tk.Label(window, text="Escoger Velocidad")
    dirlb = tk.Label(window, text="")
    speed = tk.Spinbox(window, from_=1, to=10)
    filelb = tk.Label(window, text="Escoger directorio raiz")
    filebtn = tk.Button(window, text="Elegir Directorio", command=getPath)
    filelb.grid(column=0, row=0)
    filebtn.grid(column=1, row=0)
    speedlb.grid(column=0, row=1)
    speed.grid(column=1, row=1)
    execlb.grid(column=0, row=2)
    singleradius.grid(column=0, row=3)
    doubleradius.grid(column=1, row=3)
    halfradius.grid(column=2, row=3)
    execbtn.grid(column=1, row=4)

    tk.mainloop()
    cv2.destroyAllWindows()
