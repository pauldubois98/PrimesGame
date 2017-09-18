from primes import *




def game(nbPrimes, mini, maxi):
    nb, li=makeRandNb(nbPrimes, mini, maxi)
    known=[]
    remain=nb
    while remain!=1:
        print("\n\tIn factorizing "+str(nb)+\
              " you still need to factorize "+str(remain))
        fact=input('Enter a factor:')
        try:
            fact=int(fact)
        except:
            print('> Enter an integer, please <')
        if remain%fact==0:
            if fact in li:
                print("{} is a prime factor of {}".format(fact, remain))
                remain=int(remain/fact)
                known.append(fact)
            else:
                print("{} is a factor of {}, but {} is NOT prime"\
                      .format(fact, remain, fact))
        else:
            print("{} is NOT a factor of {}".format(fact, remain))
    print("\n\n\n\n\n\t\t >>> Well done! <<<\n\n\n")
    print('\t'+str(nb), end=' = ')
    for i in known:
        print(i, end=' * ')
    print('1\n\n\n\n')







if __name__=='__main__':
    inp=''
    while inp!='q' and inp!='Q':
        game(7, 0, 15)
        print("Type q to Quit:")
        inp=input()
