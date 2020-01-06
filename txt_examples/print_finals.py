#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Txt files as a input
# Random amount of CRNs for each student
# First input courses.txt
# Student ID CourseCRN, split with " "
# Same student ID can be enrolled in different courses so 

# Second input can be finals.txt or finals2.txt
# CourseCRN    CourseName    Date    Time split with "\t"

# Ask for input until user writes correct input

# Firstly sort exams according to their date then their time

# First output: Final exam schedule of student with ID "studentID":

# Then, at each other line of the output, your program should display 3 pieces of information: (1) course name, (2) exam date and (3) exam time
# (1) (2) (3) can be printed with format method. Seperate with '\t': print(..., sep=',')

# If a course doesn't have final exam your program will print the CRN numbers of the courses for which there are no final exams.
# Courses without a final exam: courseCRN1, courseCRN2, …, courseCRNN
def DateForSort(item):
    date = "".join(x for x in item[1].split("."))
    hour = "".join(x for x in item[2].split(":"))
    
    return (date + hour)

def FinalScheduler():
    file1 = input("Please enter filename for the courses list: ")
    file2 = input("Please enter filename for the finals list: ")
    #student_id = input("Please enter a student ID: ")

    #student_ids = []
    courseCRN = []
    courseCRN2 = []
    crn_finals = {}
    studentnCourses = {}
    
    #dict = {'key':1}
    
    #for key in dict:
    #    print(key)
    
    f1 = open(file1)
    
    lines1 = f1.readlines()
    f1.close()

    for i in lines1: # Take students courses into the dictionary

        vars = i.split()
        if vars[0] not in studentnCourses:
            studentnCourses[vars[0]] = []
        for j in range(len(vars) - 1):
            courseCRN = vars[j + 1]
            studentnCourses[vars[0]].append(courseCRN)

    f2 = open(file2)

    lines2 = f2.readlines()
    f2.close()

    for x in lines2: # Take CRNs course name, exam date and times into the dictionary

        vars = x.split()
        if vars[0] not in crn_finals:
            crn_finals[vars[0]] = []
        for k in range(len(vars)-1):
            courseCRN2 = vars[k + 1]
            crn_finals[vars[0]].append(courseCRN2)
    #print("CRN Finals: ",crn_finals)
    
    # Pull data from dictionary and print out
    noFinal = []
    haveFinal = []
    
    while True:
        student_id = input("Please enter a student ID: ")
        if student_id in studentnCourses: # Data comes
            print("Final exam schedule of student with ID {}:".format(student_id))
            #crn_finals_sorted = sorted(crn_finals.items(), key=lambda x: x[studentnCourses[student]][1])
            
            for crn in studentnCourses[student_id]:
                try:
                    haveFinal.append(crn_finals[crn])
                except KeyError:
                    noFinal.append(crn)
            
            haveFinal.sort(key = DateForSort)
            #print(haveFinal)

            for final in haveFinal:
                
                print("%s\t%s\t%s" % (final[0],final[1],final[2]))

            if noFinal != []:
                print("Courses without a final exam:",end=" ")
                print(", ".join(noFinal),)
                break
            else:
                break
        
        else:
            print("There is no student with ID {}".format(student_id))
            continue
        
if __name__ == '__main__':
    
    FinalScheduler()
