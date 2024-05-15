"""
Terminal simple
Auteur: Antoine Chassaigne
2024


Pour trouver le bon port COM sous windows:
>Gestionnaire de peripheriques>Ports (COM et LPT)>STMicroelectronics STLink Virtual COM Port (COMXX)
                                                                                              -----
"""


import serial


mon_port = serial.Serial(port="COM33", baudrate=115200)
mon_port.close()
mon_port.open()

while(1):
    try:
        print(mon_port.readline().decode("UTF-8"))
    except:
        print("Erreur de décodage.")
