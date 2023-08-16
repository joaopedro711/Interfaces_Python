import PySimpleGUI as sg
import folium
from selenium import webdriver
import os

#precisa ter o ChromeDriver instalado

def main():
    sg.theme('LightGrey1')

    layout = [
        [sg.Text('Latitude:'), sg.InputText(key='latitude')],
        [sg.Text('Longitude:'), sg.InputText(key='longitude')],
        [sg.Button('Mostrar no Mapa'), sg.Button('Sair')],
        [sg.Image(filename='', key='map_image')],
    ]

    window = sg.Window('Exemplo de Mapa com Folium', layout, resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Sair':
            os.remove(image_filename) 
            break
        elif event == 'Mostrar no Mapa':
            latitude = values['latitude']
            longitude = values['longitude']

            if latitude and longitude:
                try:
                    latitude = float(latitude)
                    longitude = float(longitude)

                    m = folium.Map(location=[latitude, longitude], zoom_start=16)
                    folium.Marker([latitude, longitude]).add_to(m)

                    map_filename = 'map.html'
                    m.save(map_filename)

                    image_filename = 'map_screenshot.png'
                    capture_screenshot(map_filename, image_filename)

                    window['map_image'].update(image_filename)

                    os.remove(map_filename)  # Remove o arquivo HTML gerado

                except ValueError:
                    sg.popup_error('Digite valores válidos para Latitude e Longitude.')

    window.close()

def capture_screenshot(url, output_filename):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get('file://' + os.path.abspath(url))
    driver.save_screenshot(output_filename)

    driver.quit()

if __name__ == '__main__':
    main()
