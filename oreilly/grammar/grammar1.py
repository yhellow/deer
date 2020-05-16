intValue = int('1')
print(type(intValue))

value = input()
value = input("Input a value : ")
value = float(input())
print (value)
print("Hello Python")
print("1+1=",2)

v = input("put in name: ")
print (v, 'lol')

str3 = """Hello   
World""" 
print (str3)

str1[0] == 'f'
str1[0:3] == 'fir'
str1[0:-2] == 'fir'
str1[:4] == 'firs'
str1[:0] == 'first'
str1[:-1] == 'firs'
# str1[]

\\ escape \
\' 
\"
\n # new line
\b # backspace
\t # tab

name = "리아"
greeting = "안녕하세요 %s입니다" %name
introduce = "%d 세이고 키는 %.1f cm입니다" %(100, 200)
percent = "100%" # 100% ??

sth = 'random'
dice = 6
sentence = "what kind of dice is fair? %s and how many numbers are there? %d" %(sth,dice)
sentence = "what kind of dice is fair? %s and how many numbers are there? %.1f" %(sth,dice)
=== sentence1 = "what kind of dice is fair? %s and how many numbers are there? %d" %('random', 6)

introduce2 = "{age} 세,{height} cm입니다".format(age=10,height=100.0)
greeting2 = "안녕하세요 {name:*<7}입니다".format(name=name)
introduce3 = "키는 {height:_^10.1f}입니다".format(height=191.124)

intro = "i am {age} live in {place}, and like {fruit}".format(age=5, place= 'brooklyn', fruit='tomatoes')
print(intro )

t = True and False
t = True or False

str1 = " helloWorld "
len(str1)    # 글자 총 개수 반환
str1.count('com')  # 인자의 문자열과 같은 문자 개수 반환
str2 = str1.strip()  # 문자열 양쪽 공백 제거한 문자열 반환
str2 = str1.lstrip()  # 왼쪽 공백제거한 문자열 반환
str2 = str1.rstrip()   # 오른쪽 공백제거한 문자열 반환
print(str1.startswith(str2))  # 접두사로 붙어있는지 확인

string = "          likewise    "
print(string.startswith(''))

copy = '%s'%str1
print(copy)
copy2 = str1[:-2]
print(copy2)

list1 = [1, 2, 3, 'sdf', ['a','b', True]]
list2 = [0,5]

print(list1[2:4])   # [3, 'sdf']
print(list1+list2)  # [1, 2, 3, 'sdf', ['a','b', True], 0, 5]
print(list*2)       # [0,5,0,5]
del list1[3:5]  # list == [1,2,3]

_list = ['b','c','d','a']

_list.append('x') # 맨뒤에 넣기
_list.pop()   # 맨뒤에 빼기
_list.index('a')  # 요소의 인덱스 반환 (없으면 에러)
_list.remove('a') # 같은 요소(첫번째 나오는) 삭제
_list.extend(otherList) # 리스트에 다른 리스트 넣기
_list.sort()
_list.reverse()
_list.index('x')
_list.count('c')

dic = {'name':'lion', 'age':'1'}
dic2 = dict(name='lion',age=1)
print(dic2)

dic['sex'] = 'male'
del dic['sex']
dic.clear()
print(dic)

dic['sex'] = 'male'  # 추가
del dic['name']
dic.clear()
print(dic.get('name')) # 'lion'
print (dic)
t = 'name' in dic # True
print(t)
l = dic.items()  # [('name','lion),('age','1')]
print(l)

tup = (1,2,3,"hi",['a','b'])
sameTup = 1,2,3,"hi",['a','b']  # 소괄호 안넣어도 된다
oneTup = 1,   #  (1)   뒤에 컴마 넣어야 함 (단순 변수와 차이를 주기 위해?)

tutle = 1,2,3,4,5, [9,8]
tutle[5][0] = 7
print(tutle[-1])
tup[0] = 10  # 리스트와 달리 바꾸기 불가능
tup[4][1] = 'c'  # 바꾸기 가능

greeting = "Hi man"
g0 = set(greeting)  # {'H','i',' ','m','a','n'}
g1 = set([1,2,3])   # {1, 2, 3}
# 리스트,딕셔너리,튜플 모두 적용가능

greet = "a set of strings"
sgreet = set(greet)
sgreet.add('b','m')
print(sgreet)
why = [1,2,3]
swhy = set(why)
print(why)

one = g0 & g1  # 교집합
two = g0 | g1  # 합집합
three = g0 - g1  # 차집합

g0.add('!')
g1.update([4, 5, 6])  # 여러개 값 추가
g0.remove(' ')
print(g0)

i =2
while i <= 10 :
  print(i)
  i += 1

for문
for i in range(10):
#   print(i)          # 1 2 3 4 5 6 7 8 9

for i in range(startint, endint, stepint) :
#   print(i)          # 1 2 3 4 5 6 7 8 9

for i in range(0, 11, 2):
    print(i)

리스트
list1 = ['a','b','c']
for i in range(len(list1)) :
  print(list1[i])	# a b c

lost = [1,2,3]
for i in range(len(lost)):
    print(lost[i])
  
for ch in list1 :
  print(ch)		#a b c 

# 딕셔너리
dic = {'A':'Kim', 'B':'Park'}
for key,val in dic.items() :
  print(key, val, end='/')  # print 함수 인자 end
  							# A Kim/Park B/

i = 4
if i == 0 :
  print('zero')
elif i % 2 == 0 :
  print('even')
else :
  print('odd')

i = 5
if i == 0:
    print('zero')
elif i%2==0:
    print('even number')
else:
    print('odd number')
  
리스트, 튜플, 문자열
li = [1, 2, 3, 4, 'hello', 'bye']
if 4 in li :
  print('li has 4')
else :
  print('No 4')

def funcName(a, b) :
  return a+b
print(funcName(1,2))

def funcName(*value) :
  print(value)		# [1,2,3,4,5,6]
  for i in value :
    print(i, end=', ')

num = 1
def func() :
  print(num)
  global num
  num = -1
  
func()
print(num)	  # -1