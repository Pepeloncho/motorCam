import cv2
import os
import pyfirmata
import time
import datetime

cam = cv2.VideoCapture(0)  # initializes video capture

#  DEFINIR PUERTO COM DE LA PLACA ARDUINO AQUI.
#  SI SE TIENE DUDAS RECURRIR AL TROUBLESHOOTING DE ARDUINO O REVISAR EL PUERTO COM EN EL IDE DE ARDUINO.
#  EN WINDOWS LOS PUERTOS TENDRAN NOMBRES COMO 'COM4', 'COM5'
#  EN LINUX TENDRAN NOMBRES COMO '/dev/ttyACM0' O '/dev/ttyUSB0'
puerto = 'COM4'
board = pyfirmata.Arduino(puerto)


# DEFINIR PINES DIGITALES EN LOS QUE SE CONECTA EL MOTOR DE PASO
coilpin1 = 10
coilpin2 = 11
coilpin3 = 12
coilpin4 = 13


# DEFINIR EL DIRECTORIO EN EL QUE SE CREARAN LAS FOTOS
# DENTRO DE ESTE DIRECTORIO RAIZ SE CREARAN LOS DIRECTORIOS HIJO DE CADA ITERACION.
directory = '/directorioFotos/'
try:
    os.mkdir(directory)
except FileExistsError:
    pass

# DEFINIR EL DELAY POR DEFECTO QUE TARDARAN LOS PULSOS
# ESTO DETERMINA LA VELOCIDAD DE GIRO
delay = 0.01

# Establecer conexión firmata con arduino.
# Asegurarse de subir el sketch 'StandardFirmata' a la placa arduino.
# El sketch está de ejemplo en ArduinoIDE.
# Para abrirlo en el menú superior desplegable del IDE acceder a:
# File->Examples->Firmata->StandardFirmata
# Luego subir el Sketch a la placa arduino.


def getDateName():
    dateTimeObj = datetime.datetime.now()
    timestampStr = dateTimeObj.strftime("%d_%b_%Y_%H-%M-%S/")
    return timestampStr

def makedirectory(directory):
    path = getDateName()
    os.mkdir(directory+path)
    return directory+path


def screenshot(path,name):
    global cam
    cv2.imshow("screenshot", cam.read()[1])   # shows the screenshot directly
    cv2.imwrite(path+name+'.png',cam.read()[1]) # or saves it to disk

def motorStep(board, pdelay):
    coils = [1,2,3,4]
    for i in range(64):
        for coil in coils:
            if coil == 1:
                board.digital[coilpin1].write(1)
                board.digital[coilpin2].write(0)
                board.digital[coilpin3].write(0)
                board.digital[coilpin4].write(0)
                time.sleep(pdelay)
            if coil == 2:
                board.digital[coilpin1].write(0)
                board.digital[coilpin2].write(1)
                board.digital[coilpin3].write(0)
                board.digital[coilpin4].write(0)
                time.sleep(pdelay)
            if coil == 3:
                board.digital[coilpin1].write(0)
                board.digital[coilpin2].write(0)
                board.digital[coilpin3].write(1)
                board.digital[coilpin4].write(0)
                time.sleep(pdelay)
            if coil == 4:
                board.digital[coilpin1].write(0)
                board.digital[coilpin2].write(0)
                board.digital[coilpin3].write(0)
                board.digital[coilpin4].write(1)
                time.sleep(pdelay)
    board.digital[coilpin1].write(0)
    board.digital[coilpin2].write(0)
    board.digital[coilpin3].write(0)
    board.digital[coilpin4].write(0)


def motorDoubleStep(board, pdelay):
    coils = [1,2,3,4]
    for i in range(64):
        for coil in coils:
            if coil == 1:
                board.digital[coilpin1].write(1)
                board.digital[coilpin2].write(1)
                board.digital[coilpin3].write(0)
                board.digital[coilpin4].write(0)
                time.sleep(pdelay)
            if coil == 2:
                board.digital[coilpin1].write(0)
                board.digital[coilpin2].write(1)
                board.digital[coilpin3].write(1)
                board.digital[coilpin4].write(0)
                time.sleep(pdelay)
            if coil == 3:
                board.digital[coilpin1].write(0)
                board.digital[coilpin2].write(0)
                board.digital[coilpin3].write(1)
                board.digital[coilpin4].write(1)
                time.sleep(pdelay)
            if coil == 4:
                board.digital[coilpin1].write(1)
                board.digital[coilpin2].write(0)
                board.digital[coilpin3].write(0)
                board.digital[coilpin4].write(1)
                time.sleep(pdelay)
    board.digital[coilpin1].write(0)
    board.digital[coilpin2].write(0)
    board.digital[coilpin3].write(0)
    board.digital[coilpin4].write(0)


def motorHalfStep(board, pdelay):
    coils = [1,2,3,4,5,6,7,8]
    for i in range(64):
        for coil in coils:
            if coil == 1:
                board.digital[coilpin1].write(1)
                board.digital[coilpin2].write(0)
                board.digital[coilpin3].write(0)
                board.digital[coilpin4].write(0)
                time.sleep(pdelay)
            if coil == 2:
                board.digital[coilpin1].write(1)
                board.digital[coilpin2].write(1)
                board.digital[coilpin3].write(0)
                board.digital[coilpin4].write(0)
                time.sleep(pdelay)
            if coil == 3:
                board.digital[coilpin1].write(0)
                board.digital[coilpin2].write(1)
                board.digital[coilpin3].write(0)
                board.digital[coilpin4].write(0)
                time.sleep(pdelay)
            if coil == 4:
                board.digital[coilpin1].write(0)
                board.digital[coilpin2].write(1)
                board.digital[coilpin3].write(1)
                board.digital[coilpin4].write(0)
                time.sleep(pdelay)
            if coil == 5:
                board.digital[coilpin1].write(0)
                board.digital[coilpin2].write(0)
                board.digital[coilpin3].write(1)
                board.digital[coilpin4].write(0)
                time.sleep(pdelay)
            if coil == 6:
                board.digital[coilpin1].write(0)
                board.digital[coilpin2].write(0)
                board.digital[coilpin3].write(1)
                board.digital[coilpin4].write(1)
                time.sleep(pdelay)
            if coil == 7:
                board.digital[coilpin1].write(0)
                board.digital[coilpin2].write(0)
                board.digital[coilpin3].write(0)
                board.digital[coilpin4].write(1)
                time.sleep(pdelay)
            if coil == 8:
                board.digital[coilpin1].write(1)
                board.digital[coilpin2].write(0)
                board.digital[coilpin3].write(0)
                board.digital[coilpin4].write(1)
                time.sleep(pdelay)
    board.digital[coilpin1].write(0)
    board.digital[coilpin2].write(0)
    board.digital[coilpin3].write(0)
    board.digital[coilpin4].write(0)


## LLAMAR ESTA FUNCION PARA DAR 8 PASOS Y TOMAR FOTOS.
## PRIMER PARAMETRO CORRESPONDE A LA PLACA
## SEGUNDO PARAMETRO AL RETARDO (VELOCIDAD MOTOR)
## TERCER PARAMETRO EL DIRECTORIO RAIZ A GUARDAR
## CUARTO PARAMETRO EL METODO DE PASOS
## LOS PARAMETROS MENOS LA PLACA VIENEN CON UN VALOR POR DEFECTO DEFINIDO AL PRINCIPIO DE ESTE DOCUMENTO
def photoloop(board, delayt = delay, pdir = directory, method = 'singleStep'):
    path = makedirectory(pdir)
    for i in range(8):
        a = str(i)
        if method == 'singleStep':
            motorStep(board, delayt)
        if method == 'doubleStep':
            motorDoubleStep(board,delayt)
        if method == 'halfStep':
            motorHalfStep(board, delayt)
        time.sleep(0.5)
        screenshot(path,a)
        time.sleep(0.5)
    return path