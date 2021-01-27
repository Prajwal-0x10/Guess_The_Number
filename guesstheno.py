import random
from tkinter import *
import os
root = Tk()
root.geometry('700x600')
root.resizable(0, 0)
root.title('Guess The Number')
Label(root, text='Guess the Number', font='arial 20 bold').pack()
Label(root, text=':- an3rdone', font='arial 10 ').pack()

Choice = IntVar()
Name = StringVar()
guess_taken1=IntVar()
Result=StringVar()
guess_taken=IntVar()
guess_taken.set(10)
guess_taken1.set(guess_taken.get())
Result.set('Guess the no between 1 to 100')


number = random.randint(1, 100)


def find():
    guess_taken1.set(guess_taken.get())
    if 10>=guess_taken.get()>0  :
        if  number>Choice.get():
            Result.set('your guess is low')
            guess_taken.set(guess_taken.get()-1)
            guess_taken1.set(guess_taken.get())
        elif Choice.get() > number:
            Result.set('your guess is high')
            guess_taken.set(guess_taken.get() - 1)
            guess_taken1.set(guess_taken.get())
        elif Choice.get() == number:
            Result.set('boo-yeah! you guessed th correct number in {chance_taken} chances '.format(chance_taken=11-guess_taken.get()))
    else:
        Result.set("game over you lost")


def restart():
    number = random.randint(1, 100)
    Result.set("Guess a number between 1 to 100 ")
    guess_taken.set(10)
    guess_taken1.set(guess_taken.get())
ent1 = Entry(root, textvariable=Choice, width=3,
             font=('Ubuntu', 50), relief=GROOVE)
ent1.place(relx=0.5, rely=0.3, anchor=CENTER)

ent2 = Entry(root, textvariable=Result, width=50,
             font=('Courier', 15), relief=GROOVE)
ent2.place(relx=0.5, rely=0.7, anchor=CENTER)

ent3 = Entry(root, text=guess_taken1, width=2,
             font=('Ubuntu', 24), relief=GROOVE)
ent3.place(relx=0.61, rely=0.85, anchor=CENTER)

msg = Label(root, text='Guess a number between 1 to 100 ',
            font=("Courier", 25), relief=GROOVE)
msg.place(relx=0.5, rely=0.17, anchor=CENTER)

msg2 = Label(root, text='Remaninig Guesses',
             font=("Courier", 25), relief=GROOVE)
msg2.place(relx=0.3, rely=0.85, anchor=CENTER)

try_no = Button(root, width=8, text='TRY', font=(
    'Courier', 25), command=find, relief=GROOVE)
try_no.place(relx=0.5, rely=0.5, anchor=CENTER)

stop = Button(root, text='stop', width=40, command=root.destroy,
                 bg="red", activebackground="red", relief=GROOVE)
stop.place(relx=0.25, rely=1, anchor=S)

reset = Button(root, text='Restart', width=40, command=restart,
                 bg="red", activebackground="red", relief=GROOVE)
reset.place(relx=0.75, rely=1, anchor=S)




root.mainloop()
