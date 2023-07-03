import pandas as pd
import numpy as np
import model.conbination as fc
import model.student_Info as si

num_same_group, status, student_list = si.student_info('data/students_list.xlsx')
# print(number_list, status)

conbination = fc.find_combination(num_same_group, status, 5, 4)
#conbination.calc()
group_result, belong_result = conbination.calc()

n_list = student_list.to_numpy()

group_list = []

list = [0] * 3
for group, member in group_result.items():
    list[0] = group
    for i in member:
        list[1] = n_list[i][0]
        list[2] = n_list[i][1]
        group_list.append(list.copy())
        
group_pd = pd.DataFrame(group_list,  columns=['group', 'number', 'nickname'])

student_list['suggestion'] = belong_result

with pd.ExcelWriter('suggestion.xlsx') as writer:
    group_pd.to_excel(writer, index=False, sheet_name='group')
    student_list.to_excel(writer, index=False, sheet_name='belong')