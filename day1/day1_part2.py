#!/usr/bin/python3

sonar_input_file = open("input_day1.txt", "r")

sonar_input_data = sonar_input_file.readlines()
sonar_data_clean = []

print(sonar_input_data[0])

for item in sonar_input_data:
    sonar_data_clean.append(item.strip())

increase_count=0

for count,value in enumerate(sonar_data_clean):
    if count > 2:
        print(count)
        print(value)
        current_window = sonar_data_clean[count] + sonar_data_clean[count-1] + sonar_data_clean[count-2]
        previous_window = sonar_data_clean[count-1] + sonar_data_clean[count-2] + sonar_data_clean[count-3]
        if current_window > previous_window:
            print(increase_count)
            increase_count=increase_count+1

print(len(sonar_data_clean))

print('The depth increase the following number of times: ',increase_count)
