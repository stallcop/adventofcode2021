#!/usr/bin/python3

sonar_input_file = open("input_day1.txt", "r")

sonar_input_data = sonar_input_file.readlines()
sonar_data_clean = []

print(sonar_input_data[0])

for item in sonar_input_data:
    sonar_data_clean.append(item.strip())

for item in sonar_data_clean:
    int(item)

def method1():
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
    return increase_count

def method2():
    debug_list = [zip(sonar_data_clean,sonar_data_clean[1:],sonar_data_clean[2:])]
    print(debug_list)
    sum_list = [sum([int(x) for x in sonar_tuple]) for sonar_tuple in zip(sonar_data_clean,sonar_data_clean[1:],sonar_data_clean[2:])]
    #sum_list = [sum(sonar_tuple) for sonar_tuple in zipped_list]
    compare_list = [currentNum < nextNum for currentNum, nextNum in zip(sum_list,sum_list[1:])]

    return sum(compare_list)

print(len(sonar_data_clean))

print('The depth increase the following number of times: ',method1())
print('The depth increase according to our second calculation method: ',method2())

