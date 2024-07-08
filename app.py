"""
this application manage a diamonds
"""
from enum import Enum 
import pandas as x 
fileDimonds = 'filename.csv'
tempp =x.pandas.read_csv(fileDimonds)
diamond =[]

class Menu(Enum): #wich q to answer
    QA =1
    QB =2
    QC =3
    QD =4
    QE =5
    QF =6
    QG =7
    EXIT=0

def display_menu():
    for action in Menu:
        print(f'{action.value} -  {action.name}')
    return Menu(int( input("your selection?")))    
    


# csv file
def load_file():
    dataa =pandas.read_csv(fileDimonds)
    data.append(dataa)


# def read_csv_and_split(filename):
    #with open(filename, 'r') as f:
       # lines = f.readlines()
       # return [line.split(',') for line in lines]



# highest diamond price
def qa():
    max = tempp['price'].max()
    print("the highest price is: ",max)

# average diamond price
def qb(): 
    total =tempp['price'].sum()
    sumItems = tempp['price'].count()
    print("Average diamond price: " , total / sumItems)

# cut diamonds Ideal
def qc(): 
    result=tempp[tempp['cut'] == 'Ideal']    
    count = result.shape[0]
    print("Number of Ideal cut diamonds: ",count)

#Number of different diamond colors
def qd(): 
   saver = tempp['color'].unique()
   number = len(saver) 
   n = pandas.unique(tempp['color'])
   print("Number of colors: ",number + n)

# Premium cut diamonds
def qe(): 
    medianC = tempp[tempp['cut'] == 'Premium']['carat'].median()
    print("Colors is: ",medianC)

# The average Carat for the chosen cut is:
def qf(): 
  avg = tempp.groupby('cut')['carat'].mean()
  print(f"Average carat for  type: \n{avg}")

    
def qg(): pass

    



if __name__ =='__main__':
    while True:
        user_selection =display_menu()
        if user_selection == Menu.EXIT: exit()
        if user_selection == Menu.QA : qa()
        if user_selection == Menu.QB : qb() 
        if user_selection == Menu.QC : qc()
        if user_selection == Menu.QD : qd()
        if user_selection == Menu.QE : qe()
        if user_selection == Menu.QF : qf()
        if user_selection == Menu.QG : qg()       

