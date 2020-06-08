import requests
from bs4 import BeautifulSoup
import urllib #Guardar de manera muy sencilla las imágenes que queramos jalarnos



def run():
    for i in range(1, 5):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic')

        image_url = image_container.find('img')['src'] #Encontrar la etiqueta img y acceder a su atributo source
        image_name = image_url.split('/')[-1] #obtener una referencia al nombre de la imagen para poderla guardar: guardarla con el nombre original - Aquí obtenemos la referencia a la última diagonal de la url | Con -1 inmediatamente accedemos al último elemento de una lista
        print('Descargando la imagen {}'.format(image_name))
        urllib.request.urlretrieve('https:{}'.format(image_url), image_name) #El primer parámetro  es la url de dónde se encuentra la imagen, el segundo parámetro es el nombre de la imagen


if __name__ == '__main__':
    run()