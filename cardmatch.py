from Tkinter import *
##-L3110216
##Card match game
##Christian Jensen
deck=Tk()
deck.title("Card Match")
deck.configure(bg="black")
from random import *
cards=[]
for x in range(1,14):
    cards.append(PhotoImage(file="images/cards_%s.gif"%(str(x))))
cardback=PhotoImage(file="images/Back.gif")
carddeck=[]
for x in cards:
    carddeck.append(Button(deck,image=x,width=74,height=114,borderwidth=0,padx=0,pady=0))
saved={}#empity dict
value1=0
value2=0
flipped=0
clicked=0
def click(args):
    global clicked    
    global flipped
    global value1
    global value2
    row=args[0]
    column=args[1]
    saved=args[2]
    button=args[3]
    if button.cget('image')=='pyimage14': 
        clicked+=1
        flipped+=1
        button.config(image=saved[(row,column)])
        if flipped==3:
            if value1.cget('image')!=value2.cget('image'):
                value1.config(image=cardback)
                value2.config(image=cardback)
            flipped=1
        if flipped==2:
            value2=button
        if flipped==1:
            value1=button
###Shuffle    
def cshuffle():
    global flipped
    global clicked
    clicked=0
    flipped=0
    ##Deck 1
    sdeck=[]
    cards2=cards[:]#slice copy
    for x in range(1,14):
        tmp1=cards2[-1]
        card=choice(cards2)
        tmp2=card
        sdeck.append(tmp2)
        cards2.remove(card)
    carddeck2=[]
    for x in sdeck:
        carddeck2.append(Button(deck,image=x,width=74,height=114,borderwidth=0,padx=0,pady=0))
    ##Deck 2
    sdeck=[]
    cards3=cards[:]
    for x in range(1,14):
        tmp1=cards3[-1]
        card=choice(cards3)
        tmp2=card
        sdeck.append(tmp2)
        cards3.remove(card)
    carddeck3=[]
    for x in sdeck:
        carddeck3.append(Button(deck,image=x,width=74,height=114,borderwidth=0,padx=0,pady=0))
    ##Both decks
    allcarddecks=(carddeck2,carddeck3)
    rowco=[]
    for x in xrange(13):
        rowco.append([{'row':0,'column':x},{'row':1,'column':x}])
    
    for x in allcarddecks:
        for y in x:
            rowcochoice1=choice(rowco)
            rowcochoice2=choice(rowcochoice1)
            saved[(rowcochoice2['row'],rowcochoice2['column'])]=y.cget('image')#saves image to row/col value
            y.config(image=cardback)
            y.grid(rowcochoice2)
            y.config(command=lambda i=(rowcochoice2['row'],rowcochoice2['column'],saved,y):click(i[:]))
            rowcochoice1.remove(rowcochoice2)
            if not len(rowcochoice1):
                rowco.remove(rowcochoice1)
button_1=Button(deck,text="Shuffle",command=cshuffle)
button_1.grid(row=4, column=6)
deck.mainloop()
