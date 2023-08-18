import PySimpleGUI as sg
import eventos

app_title = 'Arapuka v1'
themes = sorted(list(sg.LOOK_AND_FEEL_TABLE.keys()))
sg.ChangeLookAndFeel('DarkBlack')
sg.SetOptions(font='any 11', auto_size_buttons=True, progress_meter_border_depth=0, border_width=1)


# gui design
def create_window():
    # main tab
    layout = [[sg.T('', size=(17, 1)), sg.Text('Arapuka', font='Any 50')],

                [sg.Text('\n\n')],
                [sg.Button('Log', size=(10, 2), pad=(10, 10))],
                [sg.Text('Estados:')],
                # botões dos estados
                [sg.Button('Dormente', size=(10, 2), pad=(10, 10)), sg.Button('Vigilia', size=(10, 2), pad=(10, 10)), sg.Button('Alerta 1', size=(10, 2), pad=(10, 10)), sg.Button('Alerta 2', size=(10, 2), pad=(10, 10)), sg.Button('Suspeito', size=(10, 2), pad=(10, 10))], 
                
                
                [sg.Text('\n\nAções:')],
                #botoes das açoes extras
                [sg.Button('Status', size=(10, 2), pad=(10, 20)), sg.Button('Rd n', size=(10, 2), pad=(10, 20)), sg.Button('Rd n_m', size=(10, 2), pad=(10, 20)), sg.Button('Apagar Memoria', size=(10, 2), pad=(10, 20)), sg.Button('E-mail', size=(10, 2), pad=(10, 20))],
                [sg.Button('Resete', size=(10, 2), pad=(10, 20)), sg.Button('Set RTC', size=(10, 2), pad=(10, 20))],   
                                
            ]



    # window
    return sg.Window(title=app_title, layout=layout, size=(600, 550), icon='arapuka.ico')

window = create_window()

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:   
        break

    elif event == 'Log':
        window.hide()
        eventos.log()
        window.un_hide()

    #Eventos dos Estados
    elif event == 'Dormente':
        window.hide()
        eventos.dormente()
        window.un_hide()

    elif event == 'Vigilia':
        window.hide()
        eventos.vigilia() 
        window.un_hide()  

    elif event == 'Alerta 1':
        window.hide()
        eventos.alerta_1()
        window.un_hide()

    elif event == 'Alerta 2':
        window.hide()
        eventos.alerta_2() 
        window.un_hide()

    elif event == 'Suspeito':
        window.hide()
        eventos.suspeito()
        window.un_hide()

    #Eventos das Ações
    elif event == 'Status':
        window.hide()
        eventos.status()   
        window.un_hide() 

    elif event == 'Rd n':
        window.hide()
        eventos.rd_n()
        window.un_hide()

    elif event == 'Rd n_m':
        window.hide()
        eventos.rd_n_m()  
        window.un_hide() 

    elif event == 'Apagar Memoria':
        window.hide()
        eventos.apagar_memoria()
        window.un_hide()  

    elif event == 'E-mail':
        window.hide()
        eventos.email()
        window.un_hide()

    elif event == 'Resete':
        window.hide()
        eventos.resete()
        window.un_hide()

    elif event == 'Set RTC':
        window.hide()
        eventos.rtc()
        window.un_hide()     

#precisa entrar aqui, porém nao esta entrando
if eventos.update_thread is not None and eventos.update_thread.is_alive():
    eventos.update_thread.join()

window.close()   
