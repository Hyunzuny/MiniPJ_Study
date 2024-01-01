programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again.",
"Loop": "A sequence of instructions that is continually repeated until a certain condition is reached.",
}

#value 불러오기
# k = programming_dictionary['Bug']
# print(k)


# #딕셔너리 추가.
programming_dictionary['Key'] = 'oooooooooo'
print(programming_dictionary)

# #딕셔너리 통째로 삭제
# programming_dictionary = {}
# print(programming_dictionary)

# #딕셔너리 수정
# programming_dictionary['Bug'] = 'hahaha'
# print(programming_dictionary)

# for key in programming_dictionary:
#     print(key) #key
#     print(programming_dictionary[key]) #value


# #key - list
# travel_loge ={
#     "France": {"citis_visited":["Paris","Lille",'Dijon'], 'total': 12},
#     "Korea" : {"citis_visited":['속초', '강릉', '양양'], "total" : 4}, 
# }

# #list - dick
# travel_loge =[
#     {
#         "country":"France", 
#         "citis_visited":["Paris","Lille",'Dijon'], 
#         'total': 12
#         },
#     {
#         "country":"Korea", 
#         "citis_visited":['속초', '강릉', '양양'], 
#         "total" : 4
#         }, 
# ]
