
import numpy as np

npArray = np.array([1000,2000,3000,4000,5000])

productWithCharge = npArray ** 2;
# [200,200,200,200,2000]
print(productWithCharge)


# [] + value or np.add()
# [] - value or np.subtract()
# [] / value or np.divide()
# [] * value or np.multiply()
# [] % value or np.mod(array,value)
# [] ** value or np.pow(array,3)


# [] + [] or np.add()
# [] - [] or np.subtract()
# [] / [] or np.divide()
# [] * [] or np.multiply()


productArray = np.array([   
                                [49,59,69],
                                [79,89,99]
                        ])
discountArray = np.array([ [ 10,11,13],[15,20,35]])

finalPriceArray = productArray - discountArray
# print(finalPriceArray)


# amount with gst => 18% => * 1.18
# only gst amount => 18% => * 0.18

# print(finalPriceArray * 1.18)
# print(finalPriceArray * 0.18)



npArray = np.array([217,125,171,283,144,237,118,235])
sqrtArray = np.sqrt(npArray)
# print(sqrtArray)


sqrtArray = np.array([14.73091986, 11.18033989, 13.07669683, 16.82260384, 
                      12.00 , 15.3948043, 10.86278049, 15.32970972])

roundArray = np.round(sqrtArray,2)
print(roundArray)

print(np.floor(roundArray))
print(np.ceil(roundArray))