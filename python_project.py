import speech_recognition as sr     # import the library
import tkinter as tk



global text                         #text is declared globally
text='abc'                          
r = sr.Recognizer()                 # initialize recognizer

'''def speak():'''
with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
    print("Speak Anything :")
    audio = r.listen(source)        # listen to the source
    print('Done')


    try:
        text=r.recognize_google(audio)
        print("You said : "+ text)
    except sr.UnknownValueError:
        print("Google Web recognition is unable to recognize the audio")

print("Enter your choice you want to perform : ")
x = input("1.Write 2.Append ")

'''def write():'''
if x=='1':
    file=open("D:\\Python\\first.txt","w")
    file.write(f'{text}')
    file.close()

'''def append():'''
if x=='2':
    file=open("D:\\Python\\first.txt","a")
    file.write(f'{text}')
    file.close()

 
'''
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button1 = tk.Button(frame, 
                   text="Write", 
                   command=write)
button1.pack(side=tk.LEFT)
button2 = tk.Button(frame,
                   text="Append",
                   command=append)
button2.pack(side=tk.LEFT)
button3 = tk.Button(frame, 
                   text="Speak", 
                   command=speak)
button3.pack(side=tk.LEFT)
t=tk.Text(root,height=50,width=100)
t.pack()
t.insert(tk.END,"Output : ", +text)
root.mainloop()
'''
    
