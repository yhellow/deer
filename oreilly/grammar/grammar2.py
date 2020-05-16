# def func(num) :
#   return num+1

# nums = [1,2,3,4,5]

# lst = list(map(func,nums))
# print(lst)		# [2,3,4,5,6]

def mapper(x):
    return x*x

xs = [1,2,3,4,5,6]
mapped = map(mapper, xs)
print(set(mapped))
