from tkinter import *

root = Tk()

t = Text(root, height=10, width=30)
t.pack()


quote = """Hamelet: o be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take Arms against a Sea of troubles,
And by opposing end them: to die, to sleep
No more; and by a sleep, to say we end
The heart-ache, and the thousand natural shocks
That Flesh is heir to? 'Tis a consummation
Devoutly to be wished. To die, to sleep,
To sleep, perchance to Dream; aye, there's the rub,
For in that sleep of death, what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause. There's the respect
That makes Calamity of so long life:
For who would bear the Whips and Scorns of time,
The Oppressor's wrong, the proud man's Contumely,
The pangs of disprized Love, the Law’s delay,
The insolence of Office, and the spurns
That patient merit of the unworthy takes,
When he himself might his Quietus make
With a bare Bodkin? Who would Fardels bear, [F: these Fardels]
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscovered country, from whose bourn
No traveller returns, puzzles the will,
And makes us rather bear those ills we have,
Than fly to others that we know not of.
Thus conscience doth make cowards of us all,
And thus the native hue of Resolution
Is sicklied o'er, with the pale cast of Thought,
And enterprises of great pitch and moment, [F: pith]
With this regard their Currents turn awry, [F: away]
And lose the name of Action. Soft you now,
The fair Ophelia? Nymph, in thy Orisons
Be all my sins remember'"""

t.insert(END, quote)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# mylist = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=t.yview)


root.mainloop()