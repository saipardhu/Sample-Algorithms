import os
from random import shuffle
from termcolor import colored

path =os.path.abspath("C:/Users/Pardhu/Downloads/Songs")
songs=os.listdir(path)
shuffle(songs)
index=0
size=len(songs)
song = songs[index]
played=[]
# print(colored("Hello", "red",attrs=['dark','bold']))
print(colored("Current Song: ","red",attrs=['dark','bold']),song)
os.startfile(path + "//" + song)
played.append(song)

while index<(size):
    # song = songs[index]
    # print(song)
    # os.startfile(path + "//" + song)
    choice=input("Enter choice: ")
    if(choice=='N' or choice=='n'):
        index = index + 1
        song=(songs[index])
        print(colored("Current Song: ", "red", attrs=['dark', 'bold']), song)
        os.startfile(path + "//" + song)
        index + 1
        played.append(song)
        # continue
    elif(choice=="R" or choice=='r'):
        song = (songs[index])
        print(colored("Current Song: ", "red", attrs=['dark', 'bold']), song)
        os.startfile(path + "//" + song)
        # continue
    elif(choice=="D" or choice=="d"):
        print(played)

# os.startfile(path+"//"+songs[0])
# for song in songs:
#     print(song)
#     #os.startfile(path+"//"+song)
#     sleep()


