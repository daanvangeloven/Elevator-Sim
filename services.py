import PySimpleGUI as sg

def GetValue(event):
    if (event[0] == "-"):
        return int("-" + event[1])
    else:
       return int(event[0])

def selectFloor():
    print(32)
    chooseFloor = [
        [sg.Text('Choose the floor:')],
        [sg.Button('5', size=(11, 1))],
        [sg.Button('4', size=(11, 1))],
        [sg.Button('3', size=(11, 1))],
        [sg.Button('2', size=(11, 1))],
        [sg.Button('1', size=(11, 1))],
        [sg.Button('0', size=(11, 1))],
        [sg.Button('-1', size=(11, 1))],
        [sg.Button('-2', size=(11, 1))]
    ]
    choosewindow = sg.Window('Choose Floor', chooseFloor)
    print(39)
    event, value = choosewindow.read()
    print(42)
    choosewindow.close()
    return event
