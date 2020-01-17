import PySimpleGUI as sg
import time
from services import GetValue, selectFloor

CurrentFloor = 0
chosenFloor = []
callFloor = []
passengers= 0
sg.theme("DarkAmber")

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
    if len(chosenFloor) == 0 and len(callFloor) == 0:
        event, values = window.read()
        if len(event) > 0:
            callFloor.append(GetValue(event))
    while len(chosenFloor) > 0 or len(callFloor) > 0:
        print("48")
        # Go to chosen floors first
        if len(chosenFloor) > 0:
            print("51")
            if chosenFloor[0] < CurrentFloor:
                window[str(CurrentFloor)].update("")
                CurrentFloor -= 1;
                window[str(CurrentFloor)].update("O")
            elif chosenFloor[0] > CurrentFloor:
                window[str(CurrentFloor)].update("")
                CurrentFloor += 1;
                window[str(CurrentFloor)].update("O")
        # Go to called floors 2nd
        else:
            print("62")
            if callFloor[0] < CurrentFloor:
                window[str(CurrentFloor)].update("")
                CurrentFloor -= 1;
                window[str(CurrentFloor)].update("O")
            elif callFloor[0] > CurrentFloor:
                window[str(CurrentFloor)].update("")
                CurrentFloor += 1;
                window[str(CurrentFloor)].update("O")
        print("71")
        if (CurrentFloor in callFloor) or (CurrentFloor in chosenFloor):
            print("75")
            if CurrentFloor in callFloor:
                print("81")
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

        window['PassengerCounter'].update(passengers)
        event, values = window.Read(timeout=1000, timeout_key="__TIMEOUT__")
        if event != "__TIMEOUT__":
            time.sleep(0.5)
            callFloor.append(GetValue(event))
        if event == 'Exit':
            window.close()
    time.sleep(1)
