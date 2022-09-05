# hospital-data-analysis
## What it is
A hospital has a large file of patient data.  They would like to know some statistics based off patient data, however it would take a person a very long time to do
this and they would be prone to error.  My job is to create a GUI which allows a user to get the (average cost per year life lived), (average cost to treat a patient),
(average number of months until death), (average age of patient at death).  This data will be saved to a file for later viewing.

## How it works
This script is created using python and the tkinter, numpy, and matplotlib libraries.  I broke it down in to a few primary functions calculateAverages(file parser),
graphing, GUI entering the initial file location, and lastly the GUI section for handling the data the user is interested.

## The Program
When first opening the app the first GUI has a prompt for the user.  UI and UX were under high consideration for this program.
If a file location is entered incorrectly then the appropriate error message will be displayed.

![GUI_screen1_prompt](https://user-images.githubusercontent.com/52471959/188481614-437c3c26-45c3-4f69-9dd1-8a8ef184a8a5.png)
![GUI_screen1_incorrect_location](https://user-images.githubusercontent.com/52471959/188481551-0348f55d-1997-414a-ac37-97e451397dab.png)

Once a correct file location is entered a second screen will be displayed for the user to check the information they are 
interested in.  If they do not want some of the data they have the option to not check the box and that information will
be withheld.

![GUI_screen2_correct_loc](https://user-images.githubusercontent.com/52471959/188481832-f40f747d-3328-444a-933d-dc73ac8b5148.png)
![GUI_screen2_avg_display](https://user-images.githubusercontent.com/52471959/188481969-95a05a03-d790-4ecd-a38a-77ec3321b048.png)

The histograms were added as a way to visualize the overall data that is being analyzed.  All the analysis is in the 
form of averages.  Therefore, a histogram is a great tool to allow a user to understand the data they are looking at 
quickly.

![GUI_screen2_histo](https://user-images.githubusercontent.com/52471959/188482045-fdca00d4-0aa3-4cfd-9607-2423566d378b.png)
![histo_2](https://user-images.githubusercontent.com/52471959/188482110-c66da60f-9043-45ed-bc48-335fe4fffb27.png)
![histo_3](https://user-images.githubusercontent.com/52471959/188482097-cd985a38-a622-48c4-8cda-68c4bd85363d.png)

The user has a choice of saving the data to a file in the same directory.

![saved_data_to_file](https://user-images.githubusercontent.com/52471959/188482188-adbf1194-eb0e-4a1e-9275-6ef93846828c.png)

The program has to parse this file to find the relavant data and convert the units of data to the requested format of year or
month and then average it.

![file_information](https://user-images.githubusercontent.com/52471959/188481464-911daa53-26e2-4982-a657-a1ec940d85e7.png)
