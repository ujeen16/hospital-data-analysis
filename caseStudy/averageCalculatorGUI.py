from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

# this function takes a file location and searches for data specified by two key strings
# 'age:' and 'LMs'. if file format changes or data requested changes then this function needs
# to be adjusted.
def calculateAverages(fileLocation):
    # prepare file to be iterated through
    file = open(fileLocation, "r")
    lines = file.readlines()
    file.close()
    # initialize data we need to calculate averages
    totalStartingAge = 0
    totalSurvivingAge = 0
    totalTreatmentCost = 0
    numOfPatients = 0
    # values for histogram
    initialAgeOfPatients = []
    totalTreatmentCostOfPatients = []
    totalSurvivingAgeOfPatients = []
    # loop through every line
    for line in lines:
        # loop through the current line in file and separate "words" by the spaces in the line
        myWords = line.split()
        for i in range(len(myWords)):
            # age: is unique word which indicates the age of the patient is the next "word"
            # this occurs nowhere except for in the line of the data we are interested in
            # occurs once patient so count the num of patients and adjust total starting age here
            if myWords[i] == "age:":
                startingAge = float(myWords[i + 1])
                initialAgeOfPatients.append(startingAge//12)
                totalStartingAge += startingAge
                numOfPatients += 1
            # this occurs once at the end of a patients data. adjust the total surviving age and
            # the total treatment cost with this line
            elif myWords[i] == "LMs":
                survivingAge = float(myWords[i + 1])
                totalSurvivingAgeOfPatients.append(survivingAge//12)
                totalSurvivingAge += survivingAge
                treatmentCost = float(myWords[i + 5])
                totalTreatmentCostOfPatients.append(treatmentCost)
                totalTreatmentCost += treatmentCost
    # with these four pieces of data we are able to calculate all desired averages
    # two decimal places of precision as a string for potential writing to a file
    avgTreatmentCost = "{:.2f}".format(totalTreatmentCost / numOfPatients)
    avgCostPerYearLife = "{:.2f}".format((totalTreatmentCost / totalSurvivingAge) * 12)
    avgNumMonthsToDeath = "{:.2f}".format(totalSurvivingAge / numOfPatients)
    avgMonthAgeAtDeath = "{:.2f}".format((totalStartingAge + totalSurvivingAge) / numOfPatients)
    # rather than returning four values just place them in a container
    myAverages = (avgCostPerYearLife, avgTreatmentCost, avgNumMonthsToDeath, avgMonthAgeAtDeath)
    histoData = [initialAgeOfPatients, totalTreatmentCostOfPatients, totalSurvivingAgeOfPatients]

    return (myAverages, histoData)


# used to visualize the base data used to calculate averages
def graph(values):
    initialAgeArray = np.array(values[0])
    totalCostArray = np.array(values[1])
    totalSurvivingAgeArray = np.array(values[2])

    bins = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    plt.hist(initialAgeArray, bins=bins)
    plt.xticks(bins)
    plt.title('Initial Age')
    plt.ylabel('number of patients')
    plt.xlabel('age (years)')
    plt.show()

    bins = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]
    plt.hist(totalCostArray, bins=bins)
    plt.xticks(bins)
    plt.title('Total Cost')
    plt.ylabel('number of patients')
    plt.xlabel('monetary cost in dollars')
    plt.show()

    bins = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    plt.hist(totalSurvivingAgeArray, bins=bins)
    plt.xticks(bins)
    plt.title('Surviving Age')
    plt.ylabel('number of patients')
    plt.xlabel('age (years)')
    plt.show()

    '''
    plt.scatter(initialAgeArray, totalCostArray)
    plt.title('no relationship between age and cost for treatment')
    plt.ylabel('monetary cost in dollars')
    plt.xlabel('age (years)')
    plt.show()
    '''


# example of a file location "C:\\Users\\Ujeen\\Desktop\\hospitalSampleAverages.txt"
def enteredFileLocation():
    try:
        # need the average values by parsing the file. if an error occurs then throw exception and
        # don't open second screen. curAverages and curFileLoc are global so they may be accessed in
        # screen 3
        global curAverages
        global histData
        curAverages, histData = calculateAverages(e.get())
        global curFileLoc
        curFileLoc = e.get()
        screen2 = Toplevel()
        screen2.title("Data Averages: data of interest")
        # Display the data of interest here the user indicates with a check mark if they are interested
        # in particular data or saving data to a file. appropriate messages are displayed for user
        # there input is saved as a global so screen two has their choices in scope
        label = Label(screen2, text="check the boxes if you're interested in that data").pack()
        global var0, var1, var2, var3, var4, var5
        var0, var1, var2, var3, var4, var5 = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
        check0 = Checkbutton(screen2, text="average cost per year of life lived", variable=var0).pack()
        check1 = Checkbutton(screen2, text="average cost to treat a patient", variable=var1).pack()
        check2 = Checkbutton(screen2, text="average number of months until death", variable=var2).pack()
        check3 = Checkbutton(screen2, text="averaged age of patient at death(in months)", variable=var3).pack()
        check4 = Checkbutton(screen2, text="would you like to save this data to a text file 'resultingAverages'\nin the same directory as file entered", variable=var4).pack()
        check5 = Checkbutton(screen2, text="would you like a histogram to visualize the data sources", variable=var5).pack()
        # activates screen 3 enteredDataOfInterest function
        inputButton = Button(screen2, text="Enter", command=enteredDataOfInterest).pack()
    except FileNotFoundError:
        errorMessage.set("No file was found in this location")
    except OSError:
        errorMessage.set("No file was found in this location")
    except ZeroDivisionError:
        errorMessage.set("Incorrect file or format 'age:' expected but not found")


# final screen displaying results of the data that the user indicated interest in
# with check marks in screen 2. Also will save that same data to a file in the same
# directory as the source data given in screen one. file will be
# 'prevFileDirectory\resultingAverages.txt'
def enteredDataOfInterest():
    screen3 = Toplevel()
    screen3.title("Data Averages: resulting Statistics")
    lbl = Label(screen3, text="Averages\n" + "-" * 30).pack()
    if var0.get():
        label0 = Label(screen3, text=curAverages[0] + " average cost per year of life lived").pack()
    if var1.get():
        label1 = Label(screen3, text=curAverages[1] + " average cost to treat a patient").pack()
    if var2.get():
        label2 = Label(screen3, text=curAverages[2] + " average number of months until death").pack()
    if var3.get():
        label3 = Label(screen3, text=curAverages[3] + " averaged age of patient at death(in months)").pack()
    if var4.get():
        new_file_loc = curFileLoc[:curFileLoc.rfind("\\") + 1] + "resultingAverages.txt"
        with open(new_file_loc, 'w') as fh:
            fh.write("patient averages\n--------------------\n")
            if var0.get():
                fh.write(curAverages[0] + " average cost per year of life lived" + "\n")
            if var1.get():
                fh.write(curAverages[1] + " average cost to treat a patient" + "\n")
            if var2.get():
                fh.write(curAverages[2] + " average number of months until death" + "\n")
            if var3.get():
                fh.write(curAverages[3] + " averaged age of patient at death(in months)" + "\n")
        fh.close()
    if var5.get():
        graph(histData)


# program begins here at the first of three windows this one will require the user to input a file location
# after entering file location they must click enter button and then logic continues to the enteredFileLocation function
root = Tk()
root.title("Data Averages: file location")

# entry field for button
e = Entry(root, width=150, borderwidth=5)
e.pack()
e.insert(0, "enter file location of patient data here. In windows type double backslash '\\\\' rather than a single '\\'")

# there will be a blank line under the entry field and this will be blank unless an invalid file location
# is entered. then it will display an error message errorMessage value will be changed to display the message
errorMessage = StringVar()
errorMessage.set("")
errorLabel = Label(root, textvariable=errorMessage).pack()

# button activating screen two if no error
myButton = Button(root, text="Enter", command=enteredFileLocation)
myButton.pack()


root.mainloop()