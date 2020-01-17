import PySimpleGUI as sg


def GetValue(event):    # this function formats the input to ints
    if event[0] == "-":
        return int("-" + event[1])
    else:
       return int(event[0])


def selectFloor():  # function to get a floor from a new passenger
    # define window layout
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
    # open window and check for input
    choosewindow = sg.Window('Choose Floor', chooseFloor)
    event, value = choosewindow.read()
    choosewindow.close()
    #return input
    return event
