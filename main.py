import model.conbination as fc
import model.student_Info as si

number_list, status = si.student_info('data/students_list.xlsx')
# print(number_list, status)

conbination = fc.find_combination(number_list, status, 5, 4)

conbination.calc()