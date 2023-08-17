import PySimpleGUI as sg
import threading
import folium
from selenium import webdriver
import os

map_window_open = False

def exibir_mapa(latitude, longitude):
    global map_window_open

    m = folium.Map(location=[latitude, longitude], zoom_start=16)
    folium.Marker([latitude, longitude]).add_to(m)

    map_filename = 'map.html'
    m.save(map_filename)

    image_filename = 'map_screenshot.png'
    capture_screenshot(map_filename, image_filename)

    os.remove(map_filename)

    # if map_window_open:
    #     sg.PopupAnimated(None)
    #     map_window.close()

    criar_janela_mapa(image_filename)
    map_window_open = True

def capture_screenshot(url, output_filename):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get('file://' + os.path.abspath(url))
    driver.save_screenshot(output_filename)

    driver.quit()

def criar_janela_mapa(image_filename):
    layout_mapa = [[sg.Image(filename=image_filename)]]
    map_window = sg.Window('Mapa', layout_mapa, finalize=True)

    while True:
        event, values = map_window.read()

        if event == sg.WINDOW_CLOSED:
            break

    map_window.close()

def main():
    sg.theme('LightGrey1')

    layout = [
        [sg.Text('Latitude:'), sg.InputText(key='latitude')],
        [sg.Text('Longitude:'), sg.InputText(key='longitude')],
        [sg.Button('Mostrar no Mapa'), sg.Button('Sair')],
    ]

    window = sg.Window('Exemplo de Mapa com Folium', layout, resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break
        elif event == 'Mostrar no Mapa':
            latitude = values['latitude']
            longitude = values['longitude']

            if latitude and longitude:
                try:
                    latitude = float(latitude)
                    longitude = float(longitude)

                    thread = threading.Thread(target=exibir_mapa, args=(latitude, longitude))
                    thread.start()

                except ValueError:
                    sg.popup_error('Digite valores válidos para Latitude e Longitude.')

    window.close()

if __name__ == '__main__':
    main()

'''
-15.890327
-047.763727
'''