# my_list = ["Wall", "Door", "Window", "Glass", "Mirror", "Kitchen"]
# # my_list_1 = list()
#
# # print(my_list_1)
# print(my_list)
# print(my_list[0])
# print(my_list[-1])
# print(my_list[2:])#from the second index to last
# print(my_list[:2]) #till second index
# print(my_list[2:3]) #incluse second and exclude 3
# print(my_list[::2])#freom zero to include second
# print(my_list[2::])#freom second to last
# print(my_list[::-1]) # reverse but also include first from reverse
# print(my_list[2:4:2]) #print every second and include second until exclude four


# my_list = ["Hello", "World", "Python", "Snake", "Captain"]
# print(my_list)

#Popoular functions for lists
# numbers  =  [12,8,23,13,76,34,89,54]
# print(len(numbers))  #gives the length of the list
# print(sorted(numbers)) # returns the sorted list
# print(max(numbers))   # returns the max number from the list
# print(min(numbers))    # returns the min numbers from the list
# print(sum(numbers))    # returns the sum of all elements from the list



#popular methods in the list


# my_New_List_01 = ["Shahzad", "Danish", "Iram", "Saira","Malik"]
# my_New_List_02 = ["Sajid", "Rehana"]
# print(my_New_List_01)
# my_New_List_01.extend(my_New_List_02) #joins two lists together
# print(my_New_List_01)
# my_New_List_01.append("Hussani") #add new element in list
# print(my_New_List_01)
# my_New_List_01.sort()  #sort the list alphabetically
# print(my_New_List_01)
# my_New_List_01.count("Hussani") #count how many a value is repeated
# print(my_New_List_01.count("Rehana"))
# my_New_List_01.remove("Iram")  #remove the certain emenet from the list
# print(my_New_List_01)
# my_New_List_01.insert(2,"Iram") #insert the new element in requitred index nymber
# print(my_New_List_01)
# my_New_List_01.pop() #pop the last inserted or last indexed element from the list by default
# print(my_New_List_01)
# my_New_List_01.pop(0) # pop the zero indexed element from the list
# print(my_New_List_01)
# my_New_List_01.reverse() #reverse the original list not a copy unlike the (::-1)
# print(my_New_List_01)
# my_New_List_02.clear()  #clear the list
# print(my_New_List_02)
# my_New_List_01 = []  #same clear the list
# print(my_New_List_01)
# y = my_New_List_01.copy() # gonna create an independent copy


#Nested Lists
points = [[0,1,2],
          [3,4,5],
          [6,7,8]
    ]
point1 = points[1]
print(points) #or
print(points[1][2]) #the second index list and the  index 3rd element
print(point1)
