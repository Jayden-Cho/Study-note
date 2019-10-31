# Chapter 6 문자열

#### in을 논리 연산자로 사용하기

~~~python
fruit = 'banana'
print('n' in fruit)
# True로 출력됨.
print('m' in fruit)
# False로 출력됨.
~~~



 #### Strip 메소드

- *lstrip()*: 왼쪽 공백 제거
- *rstrip()*: 오른쪽 공백 제거
- *strip()*: 양쪽 공백 제거



#### 시작 문자열 찾기

~~~python
line = 'Please have a nice day'
print(line.startswith('Please'))
# True 출력됨.
print(line.startswith('p'))
# False 출력됨: 대소문자 구분
~~~



## Exercise: Parsing Strings

~~~python
str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
print(ipos)
# result: 18

piece = str[ipos:]
print(piece)
# result: ': 0.8475'

piece = str[ipos+2:]
print(piece)
# result: '0.8475' --> string value

value = float(piece)
print(value)
# result: 0.8475 --> float value
~~~



## Quiz

~~~python
words = 'Connect Foundation'

if 'F' in words:
    words.lower()
    words[7] = '&'
else:
    print(words)
print(words)
# result: TypeError: 'str' object does not support item assignment
~~~

- 파이썬은 문자열을 변경할 수 없음. 인덱스로 참조한 위치에 대입하려고 하면 에러.
  - 다른 문자열이 필요하면 조합해 새로 만들어야 함.

