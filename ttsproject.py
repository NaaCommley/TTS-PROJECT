import PySimpleGUI as sg
import pyttsx3

speaker = pyttsx3.init()

layout = [
    [sg.Text('Enter your text:', text_color='black', background_color='#8e9791'),
    sg.InputText(key='-INPUT-'),
    sg.Text('Select a voice:'),
    sg.Radio('Male', "RADIO1", default=True, key='-MALE-', text_color='black', background_color='blue'),
    sg.Radio('Female', "RADIO1", key='-FEMALE-', text_color='black', background_color='#ffe599'),
    ],
     
    [sg.Text('Volume: '),
     sg.Slider(key='-VOLUME-',range=(0,10), size=(18, 15), orientation='horizontal')],
    [sg.Button('Speak'), sg.Button('Exit')]
]

window = sg.Window('TEXT TO SPEECH APP', layout, background_color= '#dc9bad')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Speak':
        #Initialize the pyttsx3 engine
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        volume = engine.getProperty('volume')
        set_volume = values['-VOLUME-']
        # Get the text from the input box
        text = values['-INPUT-']

        voices = engine.getProperty('voices')

        # Set the voice type
        if values['-MALE-']:
            engine.setProperty('voice', voices[0].id)
        elif values['-FEMALE-']:
            engine.setProperty('voice', voices[1].id)

        engine.setProperty('volume', set_volume)
        engine.say(text)

        engine.runAndWait()


window.close()



