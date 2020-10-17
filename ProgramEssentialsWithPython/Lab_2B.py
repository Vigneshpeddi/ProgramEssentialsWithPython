#Week 2 Day 2: Lab #2B Vignesh Peddi 1/25/19
#This program follows the flowchart from Lab #2B
#Step 1 of Flowchart: START
#"Start" represents your starting comments
#Step 2 of Flowchart: PROCESS -filesize_megabits-
filesize_megabits = ((45*5.6)*1000)*8 
#Step 3 of FLowchart: PROCESS -upload_speed-
upload_speed = 100
#Step 4 of Flowchart: PROCESS -time_seconds-
time_seconds = filesize_megabits/upload_speed
#Step 5 of Flowchat: PROCESS -time_minutes-
time_minutes = time_seconds/60
#Step 5 of Flowchart: OUTPUT -time_minutes-
print("It will take {0:.0f} minutes to upload 45 videos with an average file size of 5.6gb with an upload speed of {1:.0f}mbps".format(time_minutes, upload_speed))
