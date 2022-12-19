import PySimpleGUI as sg

label1 = sg.Text("Select Files to compress: ")
input1 = sg.Input()
choose_but1 = sg.FileBrowse()
label2 = sg.Text("Select Destination Folder: ")
input2 = sg.Input()
choose_but2 = sg.FolderBrowse()
compress_but = sg.Button("compress")
window = sg.Window("File Compressor", layout=[[label1, input1, choose_but1],
                                              [label2, input2, choose_but2],
                                              [compress_but]])
window.read()
window.close()

