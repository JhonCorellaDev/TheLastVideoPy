
#Librerias en uso
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

#Aqui se define la URL del canal
channel_url = 'https://www.youtube.com/@TuTioJhon/'

#Aqui toma los datos 
response = requests.get(channel_url)

#chequea la respuesta previa
soup = BeautifulSoup(response.text, 'html.parser')

#toma el titulo del video y lo escribe en h3
titles = soup.find_all("h3", attrs={"class": "yt-lockup-title"})

#toma el titulo y lo guarda
latest_title = titles[0].a.text

#inicia la notify
toaster = ToastNotifier()

#Muestra la notificación
toaster.show_toast("Ey Jhon acaba de subir un video Nuevo!", latest_title)
