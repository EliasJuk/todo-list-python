from PySimpleGUI import PySimpleGUI as sg

tarefas = []

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('ADICIONE UMA TAREFA', justification='center',size=(40,1), font=('Arial', 10, 'bold'))],
    [sg.Text('TAREFA:', font=('Arial', 10, 'bold')), sg.Input(key='tarefa',size=(25,1)), sg.Button(button_text='ADD', key="save", size=(8,1) )],
    [sg.Listbox(values=tarefas, size=(46, 16), key="items")],
    [sg.Button('Remover', size=(20, 1)), sg.Button('Editar', size=(20, 1))]
]

# Janela
janela = sg.Window('todo-list', layout)

# Eventos
while True:
  eventos = janela.read()
  if eventos == sg.WINDOW_CLOSE:
    break