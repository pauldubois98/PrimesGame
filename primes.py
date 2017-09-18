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

if __name__=='__main__':
    #test of the module
    print(primeRange(0, 10))
    print(primeRange(10, 50))
    print()
    for i in range(5):
        print(makeRandNb(10,0,100))






