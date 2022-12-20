import PySimpleGUI as sg
from zip_extractor import extract_archive

label1 = sg.Text("Select File to extract:")
input1 = sg.Input()
choose_but1 = sg.FilesBrowse('choose', key='files', size=10)
label2 = sg.Text("Select Destination Folder:")
input2 = sg.Input()
choose_but2 = sg.FolderBrowse('choose', key='folder', size=10)
extract_but = sg.Button("extract", size=10)
exit_but = sg.Button('exit', size=10,key='exit')
output_txt = sg.Text(key='output', text_color='red')
sg.theme('LightBlue5')
col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_but1], [choose_but2]])
window = sg.Window("ZIP file Extractor", layout=[[col1, col2, col3],
                                                 [extract_but, output_txt], [exit_but]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    archivepath = values['files']
    dest_dir = values['folder']
    extract_archive(archivepath, dest_dir)
    window['output'].update(value='extraction completed!')
    match event:
        case 'exit':
            break

window.close()
