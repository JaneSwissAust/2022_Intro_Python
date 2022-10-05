def clear_screen():
    print("----------------------------------------------------")
    print("                 clear screen")
    print("----------------------------------------------------")

    import os
    os.system('cls')



def play_list_rating():
    print("----------------------------------------------------")
    print("                python course exercises UNIL ")
    print("")
    print("                week 1 ")
    print("")
    print("")
    print("----------------------------------------------------")
    print("----------------------------------------------------")
    print("Exercise 1: write a while loop to display the values of the rating of an album playlist stored in the list PlayListRatings. If the score is less than 6, exit the loop. ")
    print("----------------------------------------------------")


    playListRating =[10, 9.5,10, 8, 7.5, 5, 10, 10]

    indx=0
    while indx<len(playListRating):
        if playListRating[indx]<6: break
        else:
            print(playListRating[indx])
        indx +=1

def play_list_rating2():
    print("")
    print("----------------------------------------------------")
    print("Exercise 2: ")
    print("----------------------------------------------------")
    print("rewrite with a for loop")
    print("----------------------------------------------------")
    playListRating =[10, 9.5,10, 8, 7.5, 5, 10, 10]


    for indx in range(len(playListRating)):
        if playListRating[indx]<6:
            break
        else:
            print(playListRating[indx])
        


def colored_squares():
    print("")
    print("----------------------------------------------------")
    print("Exercise 3: ")
    print("----------------------------------------------------")
    print("              print out a list")
    print("----------------------------------------------------")

    squares=[]
    for index, color in enumerate(["red", "yellow", "green","purple", "blue"]):
        squares.append(color)
    print(squares)


def file_handling():
    print("")
    print("----------------------------------------------------")
    print("Exercise 4a: ")
    print("----------------------------------------------------")
    print("         create and write to a file")
    print("----------------------------------------------------")
    import os

    fhandler= open('ans.txt', 'w+', encoding="utf-8") 
    fhandler.seek(0)
    print(fhandler.read())
    fhandler.close()


    with open('ans1.txt', 'w+', encoding="utf-8") as fhandler:
        print(fhandler.read())
        fhandler.write('This is my first i/O exercise\n')
    #   print('hello1')
        fhandler.seek(0)
        print(fhandler.read())
        fhandler.seek(0)
        print(fhandler.readlines())
    #   print('hello2')
        os.system('type ans1.txt')
    #   print('hello3')
    fhandler.close()


#import csv
#import netCDF4
#import pickle
#import pandas as pd
#import xarray as xr
#import numpy as np

def file_handling2():
    print("\n")
    print("----------------------------------------------------")
    print("Exercise 4b: ")
    print("----------------------------------------------------")
    print("         create and write more to a file")
    print('         print to screen')
    print("----------------------------------------------------")
    import math
    import os
    
    with open('ans2.txt','w+',encoding="utf-8") as fhandler:   
        fhandler.seek(0)
    #    print(fhandler.readlines())
        firstline=f'I have just learnt that pi is approximately {math.pi:.4f}\n'
        secondline='writing this to the file\n'
        thirdline='this is a piece of cake\n'   
        fhandler.writelines([firstline, secondline, thirdline])
        fhandler.seek(0)
        print(fhandler.readlines())
        print('\n')
        fhandler.seek(0)    
        print(fhandler.read())
        os.system('type ans2.txt')
    fhandler.close()    
    
    
    
def tabular_files():
    print("\n")
    print("----------------------------------------------------")
    print("Exercise 5: ")
    print("----------------------------------------------------")
    print("         create and write to a TABULAR file")
    print('         print to screen')
    import csv
    import numpy as np
    import pooch
    import urllib.request
    import pandas as pd
    import os


    url = 'https://unils-my.sharepoint.com/:x:/g/personal/tom_beucler_unil_ch/ETDZdgCkWbZLiv_LP6HKCOAB2NP7H0tUTLlP_stknqQHGw?e=2lFo1x'

    datafile = pooch.retrieve('https://unils-my.sharepoint.com/:x:/g/personal/tom_beucler_unil_ch/ETDZdgCkWbZLiv_LP6HKCOAB2NP7H0tUTLlP_stknqQHGw?download=1',known_hash='c7676360997870d00a0da139c80fb1b6d26e1f96050e03f2fed75b921beb4771')


    row=[]
    with open(datafile, 'r') as fh:
        reader = csv.reader(fh)
        for info in reader:
            row.append(info)
           # print(info)
    fh.close()



def output_monthindices(month=None):
    
#    print("This function takes a string month as input e.g., January")
#    print("and outputs the first and last indices of that month")

    import csv
    import numpy as np
    import pooch
    import urllib.request
    import pandas as pd
    import os

    row=[]
      
    test = [rowobj[1].split(' ')[0].split('-')[1] for rowobj in row[1:]]
    truefalse = []
    for obj in test:
        if obj==month:
            truefalse.append(obj)
        else:
            truefalse.append(np.nan)
    return pd.Series(truefalse).first_valid_index(),pd.Series(truefalse).last_valid_index()


    Jan_index = output_monthindices(month='01')
    Feb_index = output_monthindices(month='02')
    Mar_index = output_monthindices(month='03')

    print(Jan_index)
    print(Feb_index)
    print(Mar_index)


    savefile = ['jan.csv','feb.csv','mar.csv'] # List containing the filenames
    indices = [Jan_index, Feb_index, Mar_index]
    for i in range(len(indices)):
      with open(savefile[i],'w') as fh:
        writer = csv.writer(fh)
        for indx in range(indices[i][0],indices[i][1]):
          writer.writerow(row[indx])
          print(row[indx])



def main():
    clear_screen()
    play_list_rating()
    play_list_rating2()
    colored_squares()
    file_handling() 
    file_handling2()
    tabular_files()
    output_monthindices(month=None)
    
    
main()
