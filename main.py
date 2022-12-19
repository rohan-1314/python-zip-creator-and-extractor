import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select Files to compress: ")
input1 = sg.Input()
choose_but1 = sg.FileBrowse('choose', key='files')
label2 = sg.Text("Select Destination Folder: ")
input2 = sg.Input()
choose_but2 = sg.FolderBrowse('choose', key='folder')
compress_but = sg.Button("compress")
exit_but = sg.Button('exit')
output_txt = sg.Text(key='output',text_color='red')
window = sg.Window("File Compressor", layout=[[label1, input1, choose_but1],
                                              [label2, input2, choose_but2],
                                              [compress_but, output_txt], [exit_but]],
                                                font=('Helvetica', 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values['files'].split(';')
    folder_path = values['folder']
    make_archive(filepaths, folder_path)
    window['output'].update(value='compression completed!')
    match event:
        case 'exit':
            break

window.close()
