import random as r 
n=r.randrange(11)
try=0
print("Guess any number b/w 1 to 10")
while try<5:
    ans =input(">")
    try+=1
    if try>3:
        print("Hint is available")
        ch=input("Do you want hint(yes/no) ")
        if ch==yes:
            hint=n%2
            if hint==0:
                print("number is even")
            else:
                print("number is odd")
        else:

    if ans==n:
        print("you win")
        win=True
else:
    print("You loss")
    print("Number was ",n)
if win=True:
    try=0
    print("Do you want to play the next level")
    level2=input("(yes/no) ")
    if level2==yes:
        while try<3:
            n=r.randrange(11)
            ans=input(">")
            try+=1
            if try>1:
            
                ch=input("Hint is available(yes/no) ")
                if ch==yes:
                    for x in range(2,n+1):
                        t=n%x
                        if x!=n and t==0:
                            print("number is prime number")
                        else:
                            print("number is not a prime number")
                else:
            if ans==n:
                print("you win")
        else:
            print("you lose")
            print("Number was",n)
                