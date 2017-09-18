from random import choice


def primeRange(mini, maxi):
    ###fonding primes
    #init
    l=[True for i in range(maxi)]
    #case 0 & 1
    l[0], l[1]=False, False
    #extraction of the primes numbers
    for a in range (2,int(maxi/2)+1):
        if l[a]:
            for i in range (a*a,maxi,a):
                if l[i]==1:
                    l[i]=False
    
    ###put all primes in a list
    final=[]
    for i in range (mini,maxi):
        if l[i]:
            final.append(i)
    
    return final

def makeRandNb(nbPrimes, mini, maxi):
    li=[]
    primes=primeRange(mini, maxi)
    nb=1
    for i in range(nbPrimes):
        new=choice(primes)
        li.append(new)
        nb*=new
    
    return (nb, li)



##########################################################################




from primes import *
from tkinter import *

class Game(Frame):
    #init
    def __init__(self, root=None, nbPrimes=6, mini=0, maxi=20):
        #class init
        Frame.__init__(self, root, padx=10, pady=10)

        ##game var
        self.nb, self.li=makeRandNb(nbPrimes, mini, maxi)
        self.known=[]
        self.remain=self.nb
        #options
        self.nbPrimes=nbPrimes
        self.mini=mini
        self.maxi=maxi
        self.tries=0

        ##options
        #options frame
        self.op=Frame(self, bd=5, relief='ridge')
        #info about options label
        self.opLab=Label(self.op, text='{} primes factors between {} and {}'\
              .format(self.nbPrimes, self.mini, self.maxi))
        self.opLab.grid(column=0, row=0, columnspan=3)
        #button "new game"
        Button(self.op, text='New Game', bg='green', fg='white',\
               activeforeground='green', activebackground='white',\
               command=self.newGame).grid(column=1, row=1)
        Button(self.op, text='Rules', bg='grey', fg='white',\
               activeforeground='grey', activebackground='white',\
               command=self.rules).grid(column=0, row=1)
        Button(self.op, text='More', bg='black', fg='white',\
               activeforeground='black', activebackground='white',\
               command=self.about).grid(column=2, row=1)
        #nbPrimes
        self.nbPrimesVar=StringVar()
        self.nbPrimesVar.set(self.nbPrimes)
        self.nbPrimesEntr=Entry(self.op, textvariable=self.nbPrimesVar, width=8)
        self.nbPrimesEntr.grid(column=2, row=2)
        self.nbPrimesEntr.bind('<Return>', self.upDateOptions)
        Label(self.op, text='Number of factors:').grid(column=0, row=2, \
                                                       sticky='e', columnspan=2)
        #minimum val for primes
        self.miniVar=StringVar()
        self.miniVar.set(self.mini)
        self.miniEntr=Entry(self.op, textvariable=self.miniVar, width=8)
        self.miniEntr.grid(column=2, row=3)
        self.miniEntr.bind('<Return>', self.upDateOptions)
        Label(self.op, text='Minimum value of the factors:').grid(column=0, \
                                                            row=3, columnspan=2)
        #maximum value for primes
        self.maxiVar=StringVar()
        self.maxiVar.set(self.maxi)
        self.maxiEntr=Entry(self.op, textvariable=self.maxiVar, width=8)
        self.maxiEntr.grid(column=2, row=4)
        self.maxiEntr.bind('<Return>', self.upDateOptions)
        Label(self.op, text='Maximum value of the factors:').grid(column=0, \
                                                            row=4, columnspan=2)

        #pack options
        self.op.pack()

        
        ##graph var
        #nb
        self.labNb=Label(self, text='Factorize: '+str(self.nb), \
                         font=('Times', '24', 'bold'))
        self.labNb.pack()
        #remain
        self.labRemain=Label(self, text='Remaining: '+str(self.remain), \
                         font=('Times', '20', 'italic'))
        self.labRemain.pack()
        #partial fact
        self.labFact=Label(self, text=str(self.nb)+" = ", fg='orange',\
                         font=('Times', '18'), wraplength=300)
        self.labFact.pack()
        
        #entr
        self.fact=StringVar()
        self.entr=Entry(self, font=('Times', '20'), textvariable=self.fact)
        self.entr.pack()
        self.entr.bind('<Return>', self.tryFact)

        
        #pack itself
        self.pack()

    #start a new game
    def newGame(self, event=None):
        self.tries=0
        self.nb, self.li=makeRandNb(self.nbPrimes, self.mini, self.maxi)
        self.known=[]
        self.remain=self.nb
        self.upDate()

    #make a try
    def tryFact(self, event=None):
        try:
            fact=int(self.fact.get())
        except:
            self.entr.config(bg='red')
        else:
            self.tries+=1
            if self.remain%fact==0:
                if fact in self.li:
                    self.entr.config(bg='light green')
                    self.fact.set('')
                    self.remain=int(self.remain/fact)
                    self.known.append(fact)
                    self.upDate()
                else:
                    self.entr.config(bg='light blue')
            else:
                self.entr.config(bg='light yellow')



    #update the display
    def upDate(self, event=None):
        self.labRemain.config(text='Remaining: '+str(self.remain))
        self.labNb.config(text='Favtorize: '+str(self.nb))
        partFact=str(self.nb)+" = "
        for i in range(0, len(self.known)):
            partFact+=str(self.known[i])
            partFact+='* '
        if self.remain==1:
            partFact=partFact[:-2]
            self.labRemain.config(text='Remaining: DONE!')
            self.win()
        self.labFact.config(text=partFact)

    #winner window
    def win(self, event=None):
        winWindow=Toplevel(None, bg='gold')
        winWindow.title('WINNER!')
        Label(winWindow, text='WINNER!', fg='red', bg='gold',\
              font=('Helvetica', '28', 'bold')).pack()
        Label(winWindow, text='You factorized:', fg='black', bg='gold',\
              font=('Helvetica', '18')).pack()
        partFact=str(self.nb)+" = "
        for i in range(0, len(self.known)):
            partFact+=str(self.known[i])
            partFact+='* '
        partFact=partFact[:-2]
        Label(winWindow, text=partFact, fg='dark red', bg='gold',\
              font=('Helvetica', '24', 'italic')).pack()
        Label(winWindow, text='with {} tries ({} fails)'.format(self.tries, \
              self.tries-len(self.known)), fg='black', bg='gold', \
              font=('Helvetica', '18')).pack()

    #rules window
    def rules(self, event=None):
        winWindow=Toplevel(None, bg='silver')
        Label(winWindow, text='The prime factorization game!', fg='red', \
              bg='silver', font=('Times', '28', 'bold')).pack()
        rules="""\n\
This "game" is made for (crazy) math students.\n\n\
The goal is to factorize a number, that is generated \n\
at random using the options that you give about the \n\
numbres of primes factors that you want, and the seize \n\
of these primes factors.\n\n\
The winner window is made to be able to take a picture \n\
of it, and compare with others students ;)\n\n\
Have fun !\n\
"""
        Label(winWindow, text=rules, fg='white', \
              bg='silver', font=('Times', '14')).pack()

    #about window
    def about(self, event=None):
        winWindow=Toplevel(None, bg='black')
        Label(winWindow, text='More informations about us:', fg='white', \
              bg='black', font=('Times', '20', 'bold')).pack()
        more="""\n\
   This game was created by Yohance Osborne, and\n\
programmed by Paul Dubois,  bolth  in  1st  year  in\n\
UCL (University College of London).\n\n\
This game is coded in Python 3 & tkinter\n\n\n\
\t\t\t\t#the unknown"""
        Label(winWindow, text=more, fg='white', justify='left',\
              bg='black', font=('Times', '14')).pack()
    
    #update the options
    def upDateOptions(self, event=None):
        #nbPrimes
        try:
            self.nbPrimes=int(self.nbPrimesVar.get())
        except:
            self.nbPrimesVar.set(self.nbPrimes)
        #mini. val. of primes
        try:
            self.mini=int(self.miniVar.get())
        except:
            self.miniVar.set(self.mini)
        #mini. val. of primes
        try:
            self.maxi=int(self.maxiVar.get())
        except:
            self.maxiVar.set(self.maxi)
        #info about options label
        self.opLab.config(text='{} primes factors between {} and {}'\
              .format(self.nbPrimes, self.mini, self.maxi))
        #new options => new game
        self.newGame()




if __name__=='__main__':
    fen=Tk()
    fen.title('> Prim Fact. Game <')
    game=Game(fen)
    
    fen.mainloop()
