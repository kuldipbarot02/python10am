# def test(a,b,c,d):
#     print("A :",a,"B :",b,"C :",c,"D :",d)
# test(1,2,3,4)

def test(a=10,b=20,c=30,d=40):  # in this function value change only right to left

    print("A :",a,"B :",b,"C :",c,"D :",d)
test(1,2,3,4)
test(1,2,3)
test(1,2)
test(1)
test()
test(a=200,c=300)