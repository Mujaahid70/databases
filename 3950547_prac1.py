#3950547 - Mujaahid Abrahams
import pandas as pd

crimeStats = pd.read_csv("SouthAfricaCrimeStats_v2.csv")
crimeStats.head()

def yearSplit(inp2):
    year = inp2.split("-")
    year1 = int(year[0])
    year2 = int(year[1])
    count = year2 - year1
    nextyear = year1
    yearlist = []
    for i in range (count):
        nextyear += 1
        yearlist.append(str(year1)+"-"+str(nextyear))
        year1 += 1

    return yearlist

def yearErrorCheck(year):
    yeees = ["2005-2006","2006-2007","2007-2008","2008-2009","2009-2010","2010-2011","2011-2012","2012-2013","2013-2014","2014-2015","2015-2016"]
    if (("-" in year)):
        yearlist = yearSplit(year)
        both = set(yeees) & set(yearlist)
        count = len(yearlist)
        temp = 0
        for i in range(count):
            if yearlist[i] in both:
                temp +=1
        if(temp==count):
            return True
    else:
        return False
    return False

def provinceErrorCheck(pro):
    provinces = ["Eastern Cape", "Free State","Gauteng","Kwazulu/Natal", "Limpopo","Mpumalanga","Northen Cape","North West","Western Cape"]
    for i in range(len(provinces)):
        if(provinces[i] == pro):
            return True
    return False

def stationErrorCheck(sta):
    stations = crimeStats.drop_duplicates(subset="Station")
    stations = stations.Station
    if True in (stations[0::] == sta):
        return True
   

    return False

#i tried this but it no work
# def categoryErrorCheck(cat):
#     category = crimeStats.drop_duplicates(subset="Category")
#     category = category.Category
#     print(category[0::] == cat)
#     if True in (category[0::] == cat):
#         print("xxxxxxxxxxxxxxxxxxxxxx")
#         return True
    
#     return False

#question2
def question2():

    inp1 = "Western Cape"
    inp2 = "2005-2016"
    inp1 = input("enter specific provience: ")
    inp2 = input("enter the year period of for report on total amount of crimes (eg, 2004-2015): ")

    yearlist = yearSplit(inp2)

    crime = crimeStats[crimeStats.Province == inp1]
    crime  = crime.loc[0::, yearlist]

    total= 0
    for i in range(len(yearlist)):
        total+=crime[yearlist[i]].sum()

    print("Total incidence for "+inp1+"for year"+inp2+"is:"+str(total))
#end of question2

#question3
def question3():
    sta = "Cape Town Central"
    year = "2005-2015"

    sta = input("Enter station: ")
    year = input("enter year in the form '2005-2015':")

    while(yearErrorCheck(year) == False):
        year = input("enter valid year in the form '2005-2015':")

    while(stationErrorCheck(sta) == False):
        sta = input("Enter vaild station: ")
    yearlist = yearSplit(year)
    stations = crimeStats[crimeStats.Station == sta]
    stations = stations.loc[0::, yearlist]

    total = 0
    for i in range (len(yearlist)):
        total += stations[yearlist[i]].sum()
    
    print("Total indicidents in "+sta+": "+str(total))
#end of question3

#question4
def question4():
    cat = "Truck hijacking"
    year = "2005-2007"

    #please remove the comment below token for user input on pro,year,cat 
    #year = input("Enter spicific year(s) in the form '2005-2015':")
    #cat = input("Enter Category: ")

    while(yearErrorCheck(year) == False):
        year = input("enter valid year in the form '2005-2015':")
    
    truck = crimeStats[crimeStats.Category == cat]
    yearlist = yearSplit(year)
    truck = truck.loc[0:: , yearlist]
    total = 0
    for i in range(len(yearlist)):
        total += truck[yearlist[i]].sum()

    print(cat+" incidences is: "+str(total))
#end of question4

#question5
def question5():
    year = "2009-2010"
    cat = "Arson"
    stalist = ["Boitekong","Ngodwana"]

    #please remove the comment below token for user input on year, cat, stationlist, and for-loop 
    #year = input("enter year in the form '2005-2015':")
    #cat = input("enter catergory: ")
    #num = input("how many stations do you want? ")
    # stalist = []
    # for i in range(num):
    #     stalist = stalist.append(input("Station name: "))
    while(yearErrorCheck(year) == False):
        year = input("enter valid year in the form '2005-2015':")
    arson = crimeStats[(crimeStats.Category == cat) & (crimeStats.Station.isin(stalist))]
    yearlist = yearSplit(year)
    arson = arson.loc[0::, yearlist]
    print(cat+" in " +str(stalist)+": "+str(arson.count()))
#end of question5

#question6
def question6():
    year = "2014-2015"

    #please remove the comment below token for user input on year
    #year = input("enter year in the form '2005-2015':"")

    while(yearErrorCheck(year) == False):
        year = input("enter valid year in the form '2005-2015':")

    highest_index = crimeStats[year].idxmax()
    crime = crimeStats.loc[highest_index].at["Category"]
    print("This highest type of crime in 2014 to 2015 is "+str(crime))
    #question6 end

    #question 7
def question7():
    sta = "Nongoma"

    #please remove the comment below token for user input on Station
    #sta = input("Please enter a station: ")

    while(stationErrorCheck(sta) == False):
        sta = input("Enter valid station: ")

    area = crimeStats[(crimeStats.Station == sta)]
    year = crimeStats.columns[3::]
    lowest = area[year[0]].sum()
    lowestyear = ""
    for i in range (len(year)-1):
        temp_val = area[year[i+1]].sum()
        if(lowest > temp_val ):
            lowest = temp_val
            lowestyear = year[i]
        elif(lowest == temp_val):
            lowestyear = lowestyear+" and "+year[i]+" have the same values"
    
    print("Highest period of crime:"+lowestyear)
#end of question7

#question8

def question8():
    #Method to find which stations of a specified province,year and category
    #has 0 crimes commited#
    #pro = province
    #year, is the range of years you would like to check. Note that this can be a range eg, 2005-2015
    #cat = Category

    pro = "North West"
    cat = "Attempted murder"
    year = "2008-2009"

    #please remove the comment below token for user input on pro,year,cat 
    #pro = input("Enter Spicific province: ")
    #year = input("Enter spicific year(s) in the form '2005-2015':")
    #cat = input("Enter Category: ")

    while(yearErrorCheck(year) == False):
        year = input("enter valid year in the form '2005-2015':")

    while(provinceErrorCheck(pro) == False):
        pro = input("Enter valid SOUTH AFRICAN province: ")

    zero_stations = crimeStats[crimeStats.Province == pro]
    yearlist = ["Station","Category"]
    yearlist = yearlist+yearSplit(year)
    zero_stations = zero_stations.loc[0::, yearlist]
    zero_stations = zero_stations[(zero_stations["2008-2009"] == 0) & (zero_stations.Category == cat)]
    print(zero_stations)
#end of question8

#question9
def question9():
    year = "2005-2015"
    pro = "Gauteng"
    sta = "Jhb Central"

    #please remove the comment below token for user input on pro,year,sta 
    # year = input("enter year in the form '2005-2015':")
    # sta = input("enter valid station: ")
    # pro = input("enter valid province: ")

    while(yearErrorCheck(year) == False):
        year = input("enter valid year in the form '2005-2015':")   
    while(provinceErrorCheck(pro) == False):
        pro = input("Enter valid SOUTH AFRICAN province: ") 
    while(stationErrorCheck(sta) == False):
        sta = input("Enter valid station: ")

    yearlist = yearSplit(year)
    indcidence = crimeStats[(crimeStats.Province == pro) & (crimeStats.Station == sta)]
    indcidence = indcidence.loc[0::, yearlist]

    total = 0
    for i in range(len(yearlist)):
        total +=indcidence[i::].sum()
    print("The total indiences that occured in "+pro+" within station "+sta+" during each year is:\n"+str(total))

#end of question9


inp = -1
while not(inp == 0):
    inp = input("Select an option (enter the number only, eg. 4):\n" + "1 - display the data as in question 1\n" +  "2 - Question 2\n" + 
    "3 - Question 3\n" + "4 - Question 4\n" + "5 - Question 5\n" + "6 - Question 6\n" + "7 - Question 7\n" + "8 - Question 8\n" + "9 - Special :) Question\n" + 
    "0 - Exit\n:")
    inp = int(inp)
    if inp == 1:  
        print(crimeStats)
    elif inp == 2: 
        question2()
    elif inp == 3: 
        question3()
    elif inp == 4: 
        question4()
    elif inp == 5: 
        question5()
    elif inp == 6: 
        question6()
    elif inp == 7: 
        question7()
    elif inp == 8: 
        question8()
    elif inp == 9: 
        question9()
