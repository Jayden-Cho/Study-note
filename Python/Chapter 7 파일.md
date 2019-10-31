# Chapter 7 파일

#### 텍스트 파일?

연속적으로 연결되어 있는 줄글들의 집합.

<br>

#### open()

open() 함수를 통해 파일을 열 수 있다.

- open() 함수는 handle을 반환하고, handle은 파일에 대한 작업을 수행하기위해 사용됨.
- handle은 텍스트가 파일 형태, 메모리에 저장된 문자열의 형태, 웹사이트에 존재하는 형태와 같이 다른 방식으로 저장되어 있는 텍스트를 처라하는 표준화된 방식.
  - 많은 양의 문자 파일을 한번에 읽어 발생할 수 있는 성능의 문제를 점진적으로 읽어 방지함.

~~~python
# open('파일명.형식', '모드 선택')
fhand = open('hello.txt', 'r')
# 모드에서는 w 또는 r 두 가지 선택 가능.
# w는 파일 작성, r은 파일 읽기.
~~~

<br>

#### 개행 문자

개행 문자는 '\n'. 

- '\n'도 하나의 문자로 여겨짐.

~~~python
s1 = 'Hello World!'
print(len(s1))    # 12
s2 = 'Hello\nWorld!'
print(len(s2))    # 12
~~~

<br>

#### 파일 핸들

파일 핸들은 순서가 있고 연속적으로 구성된 텍스트 파일을 한줄한줄 읽어 나가게 됨.

~~~python
fhand = open('Hamlet.txt')

for line in fhand:
  print(line)

# 한 줄씩 띄워져서 출력됨.
~~~

<br>

#### 파일 라인 수 세기

~~~python
fhand = open('Hamlet.txt')
count = 0

for line in fhand:
  count = count + 1
print('Line Count: ', count)
~~~

<br>

#### 파일 전체 읽기

*read()* 함수를 통해 단일한 하나의 문장으로 읽어 들어올 수도 있음. 각 문장에 대한 구분은 개행문자로 구분됨.

~~~python
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp)) # 한 문장에 있는 단어의 개수를 출력.
print(inp[:20]) # 첫 20개의 단어를 출력.
~~~

<br>

#### 파일 내용 검색하기

문자열과 내장 함수를 통해 특정 문자열로 시작하는 문자 찾을 수 있음.

~~~python
fhand = open('mbox-short.txt')
for line in fhand:
  # startswith()함수로 특정 문자열을 검색할 수 있음.
  if line.startswith('From: '):
    print(line)
~~~

문제는 결과값들이 한 줄씩 띄워져 출력됨.

- print() 함수로 출력되면서 개행 문자가 계속해서 추가되기 때문.
- 새로운 라인은 공백으로 인식되므로 해당 부분을 제거하게 되면 개행 문자 삭제 가능.
  - rstrip() 함수로 오른쪽 공백 제거.

~~~python
fhand = open('mbox-short.txt')
for line in fhand:
  line = line.rstrip() # 오른쪽 공백 제거
  if line.startswith('From: '):
    print(line)
~~~

<br>

#### 파일 이름 입력 받기

잘못된 파일명을 입력했을 때 처리방법을 생각해봐야.

~~~python
fname = input("Enter the file name: ")
try:
  fhand = open(fname)
except:
  print('File cannot be opened: ', fname)
  quit()

count =. 
for line in fhand:
  if line.startswith('Subject:'):
    conut = count + 1
  print('There were',count,'subject lines in', fname)
~~~

