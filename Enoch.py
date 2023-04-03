import PySimpleGUI as sg
import qrcode

# Define the layout of the PySimpleGUI window
layout = [
    [sg.Text('Enter data to encode:')],
    [sg.Input(key='-DATA-')],
    [sg.Button('Generate QR code'), sg.Button('Exit')],
    [sg.Text('', key='-STATUS-')],
]

# Create the PySimpleGUI window
window = sg.Window('QR Code Generator', layout)

# Event loop to process "Generate QR code" button and "Exit" button clicks
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):  # If user closes window or clicks "Exit" button
        break
    if event == 'Generate QR code':
        data = values['-DATA-']
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save("qr_code.png")
        window['-STATUS-'].update('QR code generated!')

# Close the PySimpleGUI window
window.close()