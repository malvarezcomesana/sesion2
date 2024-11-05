# Crear un programa que recoja por parámetro una ruta y una palabra clave y 
# termine con error ( sys.exit(n) ) en caso de que un archivo o más en el
# directorio contenga esa palabra clave
#
# Tip 1: Comando egrep de linux, método walk de la librería os, etc.
# Tip 2: Códigos de salida con error para github
# https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions
import sys
import os
import subprocess
from unittest import removeResult
def main():
    ruta = sys.argv[1]
    clave = sys.argv[2]
    result = subprocess.run(['egrep', '-R', clave,ruta], capture_output=True, text=True)
    print(result)
    if (result.returncode == 0):
        sys.exit(1)
if __name__ == "__main__":
    if len(sys.argv)!=3:
        print("Uso: python secret_finder_v2.py <ruta> <clave>")
        sys.exit(1)
    main()