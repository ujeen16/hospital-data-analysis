#by Eugene Ayotte on 6/22/2022


def calculate_averages(file_location):
    file = open( file_location, "r" )
    lines = file.readlines()
    file.close()

    total_starting_age = 0
    total_surviving_age = 0
    total_treatment_cost = 0
    num_of_patients = 0
    for line in lines:
        # loop through the current line in file and separate "words" by the spaces in the line
        my_words = line.split()
        for i in range(len(my_words)):
            # age: is unique word which indicates the age of the patient is the next "word"
            if my_words[i] == "age:":
                starting_age = float(my_words[i + 1])
                total_starting_age += starting_age
                num_of_patients += 1
            elif my_words[i] == "LMs":
                surviving_age = float(my_words[i + 1])
                total_surviving_age += surviving_age
                treatment_cost = float(my_words[i + 5])
                total_treatment_cost += treatment_cost

    # two decimal places of precision as a string for potential writing to a file
    avg_treatment_cost = "{:.2f}".format(total_treatment_cost / num_of_patients)
    avg_cost_per_year_life = "{:.2f}".format((total_treatment_cost / total_surviving_age) * 12)
    avg_num_months_to_death = "{:.2f}".format(total_surviving_age / num_of_patients)
    avg_month_age_at_death = "{:.2f}".format((total_starting_age + total_surviving_age) / num_of_patients)

    my_averages = (avg_cost_per_year_life, avg_treatment_cost, avg_num_months_to_death, avg_month_age_at_death)

    return my_averages


# if the user indicated interest in given data then display it
def display_averages(cur_averages, data_interest):
    if data_interest[0] != "0":
        print(cur_averages[0], "average cost per year of life lived")
    if data_interest[1] != "0":
        print(cur_averages[1], " average cost to treat a patient")
    if data_interest[2] != "0":
        print(cur_averages[2], " average number of months until death")
    if data_interest[3] != "0":
        print(cur_averages[3], " average age of patient at death")


# 0=avg_cost_per_year_life 1=avg_treatment_cost 2=avg_num_months_to_death 3=avg_month_age_at_death
# save any data user indicates interest in to a separate file in same directory as the file of patient data
# new_file removes the file name and replaces it with the file name of new file
def save_averages(cur_averages, data_interest, cur_file_loc):
    new_file_loc = cur_file_loc[:cur_file_loc.rfind("\\") + 1] + "resultingAverages.txt"
    with open(new_file_loc, 'w') as fh:
        fh.write("patient averages\n--------------------\n")
        if data_interest[0] != "0":
            fh.write(cur_averages[0] + " average cost per year of life lived" + "\n")
        if data_interest[1] != "0":
            fh.write(cur_averages[1] + " average cost to treat a patient" + "\n")
        if data_interest[2] != "0":
            fh.write(cur_averages[2] + " average number of months until death" + "\n")
        if data_interest[3] != "0":
            fh.write(cur_averages[3] + " month averaged age of patient at death" + "\n")
    fh.close()


# three main steps 1) get file location of the patient data and calculate data 2) determine the data user is interested in and display
# 3) ask if user would like to save the data to a file and do so if they wish
def main():
    file_loc = input("please enter the file location of the data to be analysed:\n")
    # "C:\\Users\\Ujeen\\Desktop\\hospitalSampleAverages.txt"
    cur_averages = calculate_averages(file_loc)

    data_of_interest = input("four types of data are available \n1)average cost per year of life lived 2)average cost to treat a patient\n"
                             "3)average number of months until death 4)average age of patient at death\n "
                            "type either a 1 or a 0 for each type of data where a 1 indicates to find the average\n"
                             " and 0 indicates not to find an average. please put a space between each input\n").split()
    display_averages(cur_averages, data_of_interest)

    save_to_file = input("would you like to save this data to a text file 'resultingAverages' in current directory?\n"
                         "type 1 if yes 0 if no\n")
    if save_to_file != "0":
        save_averages(cur_averages, data_of_interest, file_loc)


main()