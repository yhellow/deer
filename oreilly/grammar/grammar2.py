# def func(num) :
#   return num+1

# nums = [1,2,3,4,5]

# lst = list(map(func,nums))
# print(lst)		# [2,3,4,5,6]

# def mapper(x):
#     return x*x

# xs = [1,2,3,4,5,6]
# mapped = map(mapper, xs)
# print(set(mapped))

# class Puppy :
#   def setName(self,_name) :
#     self.name = _name
  
# myPet = Puppy()
# myPet.setName("꽁별이")
# print(myPet.name)	

# class phones:
#   def os(self, system):
#     self.whatos = system

# iphone = phones()
# iphone.os("ios")
# print(iphone.whatos)

# class Puppy :
#   def __init__(self,_age,name='댕댕이') :
#     self.age = _age
    
# myPet = Puppy(5)
# print("%s, %d세" %(myPet.name,myPet.age))

# class iphone: 
#   def atti(self, gb, os='ios'):
#     self.gbis = gb
#     self.osis = os

# myphone = iphone()
# myphone.atti(128)
# print("my phone runs on %s and is %d gb" %(myphone.osis, myphone.gbis))


# class Chicken :
#   count = 0
#   def __init__(self,_brand='No brand') :
#     self.brand = _brand
#     Chicken.count += 1

# order1 = Chicken('굽네')
# order2 = Chicken('교촌')

# # print(Chicken.count)		# 2
# print(order2.count)		# 2

# class Phones:
#   def whatphone(self,os,gb):
#     self.whatos = os
#     self.whatgb = gb
    
# phone1 = Phones('apple')
# whatphone.os = ios
# whatphone.gb = 128
# phone1 = Phones('samsung')
# whatphone.os = android
# whatphone.gb = 256

# print(phone1.os)


# try : 
#   1/0
#   # raise ZeroDivisionError	# 오류 발생
# except ZeroDivisionError as e :
#   print(e)
# else :
#   print("Success!")