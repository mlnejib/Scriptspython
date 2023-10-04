#nom="nejib"
prenom="mla"
college="bois de boulogne"
#print("bonjour Mr {}  {} du college {} ".format(nom,prenom,college))
#print(nom[2:4])
#print(college[-8:-1])
#print(college.split()[-1])
print(college[::-1])


def dire(message,age,nom):
    print("Mr {} votre age est {} et votre message {}".format(nom,age,message))


dire("yo bro",42,"sam")