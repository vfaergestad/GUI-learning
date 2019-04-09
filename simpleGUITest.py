import PySimpleGUI as sg

layout = [
    [sg.Text("How many throws do you want to make?")],
    [sg.Input()],
    [sg.Checkbox("Jail"), sg.Checkbox("Community Chest Cards"), sg.Checkbox("Chance Cards")],
    [sg.Checkbox("Triple Dice Jail")]
]

window = sg.Window("Test ass").Layout(layout)
window.Read()

https://pysimplegui.readthedocs.io/tutorial/#adding-a-gui-to-your-program-or-script