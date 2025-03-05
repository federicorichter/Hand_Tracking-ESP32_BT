import serial
import time

# Puerto serie asociado con el dispositivo Bluetooth
puerto_serie = serial.Serial('/dev/rfcomm0', 9600)  # Reemplaza 'COMX' con el puerto de tu dispositivo Bluetooth

while True:
    # Datos que deseas enviar
    datos_a_enviar = "Hola, ESP32!"

    # Envía los datos
    puerto_serie.write(datos_a_enviar.encode('utf-8'))

    time.sleep(1)  # Puedes ajustar este valor según sea necesario

