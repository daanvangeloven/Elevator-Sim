import PySimpleGUI as sg
import time
from services import GetValue, selectFloor

# Initialize variables for global scope
CurrentFloor = 0        # Current floor of the elevator
chosenFloor = []        # List of all the floors that people have chosen
callFloor = []          # List of floors where people have called an elevator
passengers = 0         # Amount of passengers currently in the elevator

sg.theme("DarkAmber")

# Defining the layout for the main display
mainLayout = [
    [sg.Text('Current \n position:'), sg.Text('Call elevator:', justification="right")],
    [sg.T('', key='5', size=(5, 1)), sg.Button('5', size=(11, 1))],
    [sg.T('', key='4', size=(5, 1)), sg.Button('4', size=(11, 1))],
    [sg.T('', key='3', size=(5, 1)), sg.Button('3', size=(11, 1))],
    [sg.T('', key='2', size=(5, 1)), sg.Button('2', size=(11, 1))],
    [sg.T('', key='1', size=(5, 1)), sg.Button('1', size=(11, 1))],
    [sg.T('O', key='0', size=(5, 1)), sg.Button('0', size=(11, 1))],
    [sg.T('', key='-1', size=(5, 1)), sg.Button('-1', size=(11, 1))],
    [sg.T('', key='-2', size=(5, 1)), sg.Button('-2', size=(11, 1))],
    [sg.Exit(), sg.T('Passengers: '), sg.T('0', key='PassengerCounter')]]
window = sg.Window('Elevator', mainLayout)

while True:
    # Check if the elevator is idle
    if len(chosenFloor) == 0 and len(callFloor) == 0:
        event, values = window.read()
        if len(event) > 0:
            callFloor.append(GetValue(event))
    while len(chosenFloor) > 0 or len(callFloor) > 0:
        # Go to chosen floors first
        if len(chosenFloor) > 0:
            if chosenFloor[0] < CurrentFloor:
                window[str(CurrentFloor)].update("")
                CurrentFloor -= 1;
                window[str(CurrentFloor)].update("O")
            elif chosenFloor[0] > CurrentFloor:
                window[str(CurrentFloor)].update("")
                CurrentFloor += 1;
                window[str(CurrentFloor)].update("O")
        # Go to called floors after all chosen floors are gone
        else:
            if callFloor[0] < CurrentFloor:
                window[str(CurrentFloor)].update("")
                CurrentFloor -= 1;
                window[str(CurrentFloor)].update("O")
            elif callFloor[0] > CurrentFloor:
                window[str(CurrentFloor)].update("")
                CurrentFloor += 1;
                window[str(CurrentFloor)].update("O")
        # Check if the elevator is on a desired floor
        if (CurrentFloor in callFloor) or (CurrentFloor in chosenFloor):
            # check if a new passenger enters the elevator
            if CurrentFloor in callFloor:
                try:
                    chosenFloor.append(GetValue(selectFloor()))
                    passengers += 1
                except:
                    pass
            try:
                callFloor.remove(CurrentFloor)
            except:
                pass
            try:
                chosenFloor.remove(CurrentFloor)
                passengers -= 1
            except:
                pass
        # Update passenger count
        window['PassengerCounter'].update(passengers)
        # Wait for input for 1 second then continue
        event, values = window.Read(timeout=1000, timeout_key="__TIMEOUT__")
        if event != "__TIMEOUT__":
            time.sleep(0.5)
            callFloor.append(GetValue(event))
        if event == 'Exit':
            window.close()
    time.sleep(1)
