import os
import shutil
import tkinter as tk
from tkinter import ttk

def renameFile(path, customName, start_num):
	if not os.path.exists(path):
		os.makedirs(path)
	if len(start_num) < 1:
		start_num = 1
	x = int(start_num)
	newExt = oldExt = os.path.splitext(customName)[1]
	for file in os.listdir(path):	
		y = str(x).rjust(2, '0')
		
		oldExt = os.path.splitext(file)[1]
		OldName = os.fsdecode(file)
		
		
		if newExt != oldExt:
			b = customName.replace(newExt, '')
			newName = b + " " + y + newExt
			old = os.path.join(path, OldName)
			new = os.path.join(path, newName)
		
			os.rename(old, new)
			x-=-1
		else:
			b = customName.replace(oldExt, '')
			newName = b + " " + y + oldExt
			old = os.path.join(path, OldName)
			new = os.path.join(path, newName)
		
			os.rename(old, new)
			x-=-1

		# old = os.path.join(path, OldName)
		# new = os.path.join(path, newName)
		
		# os.rename(old, new)
		# x-=-1

def createFiles(path, fileName, noOfFiles):
	if not os.path.exists(path):
		os.makedirs(path)
	if len(noOfFiles) < 1:
		noOfFiles = 1
	x = int(noOfFiles)
	n = 1
	# y = str(n).rjust(2, '0')
	
	if len(fileName) < 1:
		fileName = "file.txt"

		
	ext = os.path.splitext(fileName)[1]
	b = fileName.replace(ext, '')
	newName = b + " " + str(n) + ext
	pathWithName = os.path.join(path, newName)
	pathWithNameNotExtension = os.path.join(path, b)
	
	with open(pathWithName, "w+") as f:
			pass

	while n < x:
		shutil.copy(pathWithNameNotExtension+" "+str(n)+ext,
					pathWithNameNotExtension+" "+str(n+1)+ext)
		n-=-1
		
	

instruction = """This program renames all file in the given\n directory with the name provided and adds\n a number behind them \n Beware this process cannot be undo'ed \n If you want a space between name and number\n Default starting number is 1"""
createInstruction = """To Create a file/No of Files in a directory\n Use this\n Please Provide Name With a Extension\n 1 File will be created if no number is provided\n Default file name if file 01.txt"""

win = tk.Tk()
win.title("Rename Files")
win.geometry("270x405")

instructionLabel =tk.Label(win, text=instruction)
label = tk.Label(win, text="Directory Path", font=10)
label_1 = tk.Label(win, text="Custom Name", font=10)
label_2 = tk.Label(win, text="Start From", font=10)
entry = tk.Entry(win)
entry_1 = tk.Entry(win)
entry_2 = tk.Entry(win)
button = tk.Button(win, font=20, text="Start", command= lambda: renameFile(entry.get(), entry_1.get(), entry_2.get()))

ttk.Separator(win,orient="horizontal").grid(row=7, columnspan=5, sticky="ew")
createLabel = tk.Label(win, text=createInstruction)
label_3 = tk.Label(win, text="Directory Path", font=10)
label_4 = tk.Label(win, text="Name", font=10)
label_5 = tk.Label(win, text="Number Of Files", font=10)
entry_3 = tk.Entry(win)
entry_4 = tk.Entry(win)
entry_5 = tk.Entry(win)
button_2 = tk.Button(win, font=20, text="Start", command= lambda: createFiles(entry_3.get(), entry_4.get(), entry_5.get()))

instructionLabel.grid(row=0, columnspan=3)
label.grid(row=3, column=0)
label_1.grid(row=4, column=0)
label_2.grid(row=5, column=0)
entry.grid(row=3, column=1, columnspan=2, sticky="N"+"S"+"E"+"W")
entry_1.grid(row=4, column=1, columnspan=2, sticky="N"+"S"+"E"+"W")
entry_2.grid(row=5, column=1, columnspan=2, sticky="N"+"S"+"E"+"W")
button.grid(row=6, column=1, sticky="W")

createLabel.grid(row=8, columnspan=3)
label_3.grid(row=9, column=0)
label_4.grid(row=10, column=0)
label_5.grid(row=11, column=0)
entry_3.grid(row=9, column=1, columnspan=2, sticky="N"+"S"+"E"+"W")
entry_4.grid(row=10, column=1, columnspan=2, sticky="N"+"S"+"E"+"W")
entry_5.grid(row=11, column=1, columnspan=2, sticky="N"+"S"+"E"+"W")
button_2.grid(row=12, column=1, sticky="W")

entry.rowconfigure(0, weight=1)
entry_1.rowconfigure(0, weight=1)
entry_2.rowconfigure(0, weight=1)
entry.columnconfigure(0, weight=1)
entry_1.columnconfigure(0, weight=1)
entry_2.columnconfigure(0, weight=1)

win.mainloop()