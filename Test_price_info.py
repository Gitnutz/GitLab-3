import price_info as pinfo

print("test_price_info ")

def test_total_cost_shopping():
    result=pinfo.total_cost_shopping()
    
    assert(result==46.75)





def test_cost_of_fruit():
    result=pinfo.cost_of_fruits('watermelon', 2)

    assert(result==13.0)

