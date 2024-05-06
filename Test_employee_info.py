import employee_info as einfo
print("Test_employee_info")

def test_get_employees_by_age_range():
 
    result=einfo.get_employees_by_age_range(1,99)

    assert(result==einfo.employee_data)



def test_calculate_average_salary():

    result=einfo.calculate_average_salary()

    assert(result==60166.666666666664)

def test_get_employees_by_dept():

    test_data = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    result=einfo.get_employees_by_dept("Sales")

    assert(result==test_data)