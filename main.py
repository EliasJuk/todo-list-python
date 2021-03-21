from PySimpleGUI import PySimpleGUI as sg

tarefas = []

# Layout
sg.theme('dark grey 6')
layout = [
  [sg.Text('ADICIONE UMA TAREFA', justification='center',size=(40,1), font=('Arial', 10, 'bold'))],
  [sg.Text('TAREFA:', font=('Arial', 10, 'bold')), sg.Input(key='todo_item',size=(26,1)), sg.Button(button_text='add', key='add_item', size=(8,1) )],
  [sg.Listbox(values=tarefas, size=(46, 16), key='listbox_items')],
  [sg.Button('Remover', size=(20, 1)), sg.Button('Editar', size=(20, 1))]
]

# Janela
janela = sg.Window('todo-list', layout)

# Eventos
while True:
	event, values = janela.Read()
	if event == 'add_item':
		tarefas.append(values['todo_item']) #Adiciona a valor contido em todo_item no array tarefas
		janela.FindElement('listbox_items').Update(values=tarefas) #Atualiza o conteudo contido na listbox
		janela.Element('todo_item').Update(value=[]) #Limpa o valor contido no input text
	elif event == 'Remover':
		tarefas.remove(values['listbox_items'][0]) #Remove item selecionado da lista no array
		janela.FindElement('listbox_items').Update(values=tarefas) #Atualiza o conteudo contido na listbox
	elif event == 'Editar':
		item_selected = values['listbox_items'][0] #Pega o valor do item seleciona e salva na variavel item_selected
		tarefas.remove(values['listbox_items'][0]) #Remove o item selecionado da lista
		janela.FindElement('listbox_items').Update(values=tarefas) #Atualiza o conteudo contido na listbox
		janela.FindElement('todo_item').Update(value=item_selected) #Coloca o valor de item_selected dentro do input
	elif event == None:
		break