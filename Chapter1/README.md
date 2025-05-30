# CHAPTER 1 파이썬답게 생각하기

## BETTER WAY1 사용중인 파이썬 버전을 알아두라

터미널에서 `--version` 플래그를 사용하여 버전을 확인하는 방법.

```terminal
$ python --version
Python 3.10.12
```

내장 모듈인 sys를 활용하여 버전을 확인하는 방법

```python
# Code
import sys
print(sys.version_info)
print(sys.version)
```

```terminal
# Output
>>>
sys.version_info(major=3, minor=10, micro=12, releaselevel='final', serial=0)
3.10.12 (main, Dec  6 2024, 18:57:45) [Clang 16.0.0 (clang-1600.0.26.3)]
```

### 기억해야 할 내용

- 파이썬 3은 파이썬 최신 버전이며 현재 가장 잘 지원되고 있다. 따라서 프로젝트에서는 파이썬 3을 사용 해야한다.
- 시스템에 있는 파이썬 실행 파일이 원하는 버전인지 확인하라.
- 파이썬 2는 사용하지 말라. 2020년 1월 1일부터 파이썬 2는 더 이상 지원되지 않는다.

## BETTER WAY2 PEP 8 스타일 가이드를 따르라

파이썬 개선 제안(Python Enhancement Proposal) #8, 또는 PEP 8은 파이썬 코드를 어떤 형식으로 작성할지 알려주는 스타일 가이드다.

[영문판](https://peps.python.org/pep-0008/)
[국문판](https://wikidocs.net/7896)

### 공백

- 탭 대신 스페이스를 사용해 들여쓰기하라.

```python
# Yes:
def function():
    return True

# No:
def function():
 return True  # 탭 사용
```

- 문법적으로 중요한 들여쓰기에는 4칸 스페이스를 사용하라.

```python
# Yes:
def outer():
    def inner():
        print('4칸 들여쓰기')

# No:
def outer():
  def inner():
      print('2칸 또는 불규칙한 들여쓰기')
```

- 라인 길이는 79개 문자 이하여야 한다.

```python
# Yes:
long_string = (
    "이렇게 긴 문자열은 "
    "여러 줄로 나누어 작성합니다."
)

# No:
long_string = "이렇게 긴 문자열을 한 줄에 모두 작성하면 가독성이 떨어지고 PEP 8 가이드라인에도 맞지 않습니다."
```

- 긴 식을 다음 줄에 이어서 쓸 경우에는 일반적인 들여쓰기보다 4 스페이스를 더 들여써야 한다.

```python
# Yes:
def long_function_name(
        parameter1, parameter2,
        parameter3):
    print(parameter1)

# No:
def long_function_name(
    parameter1, parameter2,
    parameter3):
    print(parameter1)
```

- 파일 안에서 각 함수와 클래스 사이에는 빈 줄을 두 줄 넣어라.

```python
# Yes:
class FirstClass:
    pass


class SecondClass:
    pass

# No:
class FirstClass:
    pass
class SecondClass:
    pass
```

- 클래스 안에서 메서드와 메서드 사이에는 빈 줄을 한 줄 넣어라.

```python
# Yes:
class MyClass:
    def method1(self):
        pass

    def method2(self):
        pass

# No:
class MyClass:
    def method1(self):
        pass
    def method2(self):
        pass
```

- 딕셔너리에서 키와 콜론 사이에는 공백을 넣지 않고, 한 줄 안에 키와 값을 같이 넣는 경우에는 콜론 다음에 스페이스를 하나 넣는다.

```python
# Yes:
d = {'key': 'value'}

# No:
d = {'key' : 'value'}
d = {'key':'value'}
```

- 변수 대입에서 = 전후에는 스페이스를 하나씩만 넣는다.

```python
# Yes:
x = 1

# No:
x=1
x    =    1
```

- 타입 표기를 덧붙이는 경우에는 변수 이름과 콜론 사이에 공백을 넣지 않도록 주의하고, 콜론과 타입 정보 사이에는 스페이스를 하나 넣어라.

```python
# Yes:
name: str = "김철수"
age: int = 25

# No:
name : str = "김철수"
age:int = 25
```

### 명명 규약

- 함수, 변수, 애트리뷰트는 `lowercase_underscore`처럼 소문자와 밑줄을 사용한다.

```python
# Yes:
def calculate_total():
    student_count = 10
    total_score = 95.5

# No:
def calculateTotal():
    studentCount = 10
    TotalScore = 95.5
```

- 보호돼야 하는 인스턴스 애트리뷰트는 일반적인 애트리뷰트 이름 규칙을 따르되, `_leading_underscore`처럼 밑줄로 시작한다.

```python
# Yes:
class Person:
    def __init__(self):
        self._private_data = "민감한 정보"

# No:
class Person:
    def __init__(self):
        self.privateData = "민감한 정보"
```

- private 인스턴스 애트리뷰트는 일반적인 애트리뷰트 이름 규칙을 따르되, `__leading_underscore`처럼 밑줄 두 개로 시작한다.

```python
# Yes:
class BankAccount:
    def __init__(self):
        self.__account_number = "123-456-789"

# No:
class BankAccount:
    def __init__(self):
        self._account_number = "123-456-789"
        self.private_number = "123-456-789"
```

- 클래스는 `CapitalizedWord`처럼 여러 단어를 이어 붙이되, 각 단어의 첫 글자를 대문자로 만든다.

```python
# Yes:
class StudentProfile:
    pass

class DatabaseConnection:
    pass

# No:
class student_profile:
    pass

class databaseConnection:
    pass
```

- 모듈 수준의 상수는 `ALL_CAPS`처럼 모든 글자를 대문자로 하고 단어와 단어 사이에 밑줄로 연결한 형태를 사용한다.

```python
# Yes:
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 60

# No:
maxConnections = 100
default_timeout = 60
```

- 클래스에 들어 있는 인스턴스 메서드는 호출 대상 객체를 가리키는 첫 번째 인자의 이름으로 반드시 self를 사용해야 한다.

```python
# Yes:
class Person:
    def update_name(self, new_name):
        self.name = new_name

# No:
class Person:
    def update_name(this, new_name):
        this.name = new_name
```

- 클래스 메서드는 클래스를 가리키는 첫 번째 인자의 이름으로 반드시 cls를 사용해야 한다.

```python
# Yes:
class Person:
    @classmethod
    def from_birth_year(cls, year):
        return cls(2024 - year)

# No:
class Person:
    @classmethod
    def from_birth_year(klass, year):
        return klass(2024 - year)
```

### 식과 문장

- 긍정적인 식을 부정하지 말고 부정을 내부에 넣어라.

```python
# Yes:
if a is not b:
    print("a와 b는 다른 객체입니다")

# No:
if not a is b:
    print("a와 b는 다른 객체입니다")
```

- 빈 컨테이너나 시퀀스를 검사할 때는 길이를 0과 비교하지 말라.

```python
# Yes:
if not items:
    print("리스트가 비어있습니다")

# No:
if len(items) == 0:
    print("리스트가 비어있습니다")
```

- 비어 있지 않은 컨테이너나 시퀀스를 검사할 때도 길이가 0보다 큰지 비교하지 말라.

```python
# Yes:
if items:
    print("리스트에 항목이 있습니다")

# No:
if len(items) > 0:
    print("리스트에 항목이 있습니다")
```

- 한 줄짜리 if 문이나 한 줄짜리 for, while 루프, 한 줄짜리 except 복합문을 사용하지 말라.

```python
# Yes:
if user.is_active:
    print("활성화된 사용자입니다")
    send_welcome_email()

# No:
if user.is_active: print("활성화된 사용자입니다"); send_welcome_email()

# Yes:
for item in items:
    process_item(item)
    update_status(item)

# No:
for item in items: process_item(item); update_status(item)
```

- 식을 한 줄 안에 다 쓸 수 없는 경우, 식을 괄호로 둘러싸고 줄바꿈과 들여쓰기를 추가해서 읽기 쉽게 만들라.

```python
# Yes:
total = (
    first_number +
    second_number +
    third_number
)

# No:
total = first_number + second_number + third_number  # 너무 길어서 가독성이 떨어짐
```

- 여러 줄에 걸쳐 식을 쓸 때는 줄이 계속된다는 표시를 하는 \ 문자보다는 괄호를 사용하라.

```python
# Yes:
long_string = (
    "이것은 매우 긴 문자열입니다. "
    "여러 줄에 걸쳐 작성할 수 있습니다. "
    "가독성이 좋아집니다."
)

# No:
long_string = "이것은 매우 긴 문자열입니다. " \
              "여러 줄에 걸쳐 작성할 수 있습니다. " \
              "가독성이 좋아집니다."
```

### 임포트

- import 문을 항상 파일 맨 앞에 위치시켜라.

```python
# Yes:
import os
import sys

def process_data():
    pass

# No:
def process_data():
    pass

import os  # 잘못된 위치
import sys  # 잘못된 위치
```

- 모듈을 임포트할 때는 절대적인 이름을 사용하고, 현 모듈의 경로에 상대적인 이름을 사용하지 말라.

```python
# Yes:
from my_package.submodule import MyClass

# No:
import MyClass  # 모듈의 전체 경로를 명시하지 않음
```

- 반드시 상대적인 경로로 임포트해야 하는 경우에는 `from . import foo`처럼 명시적인 구문을 사용하라.

```python
# Yes:
from . import sibling_module
from .sibling_module import some_function

# No:
import sibling_module  # 상대 경로를 명시하지 않음
```

- 임포트를 적을 때는 표준 라이브러리 모듈, 서드 파티 모듈, 직접 만든 모듈 순서로 섹션을 나눠라.

```python
# Yes:
# 표준 라이브러리
import os
import sys
from datetime import datetime

# 서드 파티 라이브러리
import pandas as pd
import requests

# 로컬 모듈
from my_package import utils
from my_package.models import User

# No:
import pandas as pd
import os
from my_package import utils
import requests
import sys
```

각 섹션 내에서는 알파벳 순서로 정렬하는 것이 좋습니다

```python
# Yes:
# 표준 라이브러리
import datetime
import os
import sys

# 서드 파티 라이브러리
import pandas as pd
import requests

# No:
# 표준 라이브러리
import sys
import os
import datetime
```

### 기억해야 할 내용

- 파이썬 코드를 작성할 때는 항상 파이썬 개선 제안 #8 스타일 가이드를 따르라.
- 큰 파이썬 커뮤니티와 공통된 스타일을 공유하면 다른 사람과 협력할 때 도움이 된다.
- 일관성 있는 스타일을 사용하면 나중에 자신이 작성한 코드를 직접 수정할 때도 더 수월해진다.

## BETTER WAY3 bytes와 str의 차이를 알아두라

파이썬에는 문자열 데이터의 시퀀스를 표현하는 두 가지 타입이 있다. 바로 `bytes`와 `str`이다.

`bytes` 타입의 인스턴스에는 부호가 없는 8바이트 데이터가 그대로 들어간다.

```python
a = b'h\x65llo'
print(list(a))
print(a)
```

```terminal
>>>
[104, 101, 108, 108, 111]
b'hello'
```

`str` 인스턴스에는 사람이 사용하는 언어의 문자를 표현하는 [유니코드 코드 포인트](https://developer.mozilla.org/ko/docs/Glossary/Code_point)가 들어 있다.

```python
a = 'a\u0300 propos'
print(list(a))
print(a)
```

```terminal
>>>
['a', '̀', ' ', 'p', 'r', 'o', 'p', 'o', 's']
à propos
```

중요한 사실은 `str` 인스턴스에는 직접 대응하는 이진 인코딩이 없고 `bytes`에는 직접 대응하는 텍스트 인코딩이 없다는 점이다. 유니코드 데이터를 이진 데이터로 변환하려면 `str`의 `encode` 메서드를 호출해야 하고, 이진 데이터를 유니코드 데이터로 변환하려면 `bytes`의 `decode` 메서드를 호출해야 한다.

파이썬 프로그램을 작성할 때 유니코드 데이터를 인코딩하거나 디코딩하는 부분을 인터페이스의 가장 먼 경계 지점에 위치시켜라. 이런 방식을 **유니코드 샌드위치**라고 부른다.

```python
# 나쁜 예시 (인코딩/디코딩이 중간에 섞여있음)
def process_text(text):
    # 입력이 바이트인지 문자열인지 불명확
    if isinstance(text, bytes):
        text = text.decode('utf-8')
    
    # 중간 처리 과정에서 인코딩/디코딩이 섞임
    processed = text.encode('ascii', errors='ignore')
    return processed.decode('ascii')

# 좋은 예시 (유니코드 샌드위치)
def process_text(text):
    # 1. 입력을 즉시 유니코드로 디코딩
    if isinstance(text, bytes):
        text = text.decode('utf-8')
    
    # 2. 내부 처리 (모든 처리는 유니코드 문자열로)
    processed = text.lower()
    processed = processed.replace(' ', '_')
    
    # 3. 출력 직전에 인코딩
    return processed.encode('utf-8')
```

문자를 표현하는 타입이 둘로 나뉘어 있기 때문에 두 타입을 변환해주고 입력 값이 코드가 원하는 값과 일치하는지 확신하기 위해 종종 두 가지 도우미 함수가 필요하다.

```python
# 항상 str을 반환하는 함수
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # str 인스턴스

print(repr(to_str(b'foo')))
print(repr(to_str('bar')))
print(repr(to_str(b'\xed\x95\x9c'))) # UTF-8에서 한글은 3바이트임
```

```terminal
>>>
'foo'
'bar'
'한'
```

```python
# 항상 bytes를 반환하는 함수
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value # bytes 인스턴스

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))
print(repr(to_bytes('한글')))
```

```terminal
>>>
b'foo'
b'bar'
b'\xed\x95\x9c\xea\xb8\x80'
```

`bytes`와 `str`을 파이썬에서 다룰 때 꼭 기억해야 할 두 가지 문제점이 있다.

- `bytes`와 `str`이 똑같이 작동하는 것처럼 보이지만 각각의 인스턴스는 서로 호환되지 않기 때문에 전달 중인 문자 시퀀스가 어떤 타입 인지를 항상 잘 알고 있어야 한다는 점이다. 예를 들어 `bytes`와 `str`끼리 `+`연산, `>`연산, `%`연산을 사용할 수 없다(예상과 다르게 작동한다).

- 파일 핸들과 관련한 연산들이 디폴트로 유니코드 문자열을 요구하고 이진 바이트 문자열을 요구하지 않는다는 것이다. 파일 읽기/쓰기 모드인 `r`, `w`는 기본값이 시스템 디폴트 인코딩이다.

  ```python
    # 1. 텍스트 파일 읽기/쓰기 (기본값)
    with open('text.txt', 'w') as f:
        f.write('안녕하세요')  # OK
        # f.write(b'안녕하세요')  # Error

    with open('text.txt', 'r') as f:
        content = f.read()  # str 타입으로 반환

    # 2. 바이너리 파일 읽기/쓰기
    with open('binary.dat', 'wb') as f:
        f.write(b'Hello')  # OK
        # f.write('Hello')  # Error

    with open('binary.dat', 'rb') as f:
        content = f.read()  # bytes 타입으로 반환

    # 3. 인코딩 명시적으로 전달
    with open('file.txt', 'w', encoding='utf-8') as f:
        f.write('안녕')  # UTF-8로 인코딩되어 저장
  ```

### 기억해야 할 내용

- `bytes`에는 8비트 값의 시퀀스가 들어 있고, `str`에는 유니코드 코드 포인트의 시퀀스가 들어 있다.
- 처리할 입력이 원하는 문자 시퀀스인지 확실히 하려면 도우미 함수를 사용하라.
- `bytes`와 `str` 인스턴스를 (>, ==, +, %와 같은) 연산자에 섞어서 사용할 수 없다.
- 이진 데이터를 파일에서 읽거나 파일에 쓰고 싶으면 항상 이진 모드 ('rb'나 'wb')로 파일을 열어라.
- 유니코드 데이터를 파일에서 읽거나 파일에 쓰고 싶을때는 시스템 디폴트 인코딩에 주의하라. 인코딩 차이로 놀라고 싶지 않으면 `open`에 `encoding` 파라미터를 명시적으로 전달하라.

## BETTER WAY4 C 스타일 형식 문자열을 str.format과 쓰기보다는 f-문자열을 통한 인터폴레이션을 사용하라

파이썬은 사용자 인터페이스, 명령줄 유틸리티 메시지, 파일과 소켓에 데이터를 쓰는 등 문자열을 많이 사용한다.

**형식화**는 미리 정의된 문자열에 데이터 값을 끼워 넣어서 원하는 형식으로 출력하는 것을 의미한다. 파이썬에서는 언어에 내장된 기능과 표준 라이브러리를 통해 네 가지 형식화 방법을 제공한다.

### % 연산자

```python
a = 0b10111011
b = 0xc5f
print('이진수 %d, 십육진수 %d' % (a, b))
```

```terminal
>>>
이진수 187, 십육진수 3167
```

형식 지정자의 문법은 C의 printf 함수에서 비롯된 것이다. 하지만 파이썬에서 C 스타일 형식 문자열을 사용하는 데는 네 가지 문제점이 있다.

첫 번째 문제점은 형식화 식에서 오른쪽에 있는 tuple 내 데이터 값의 순서를 바꾸거나 값의 타입을 바꾸면 타입 변환이 불가능하므로 오류가 발생한다는 점이다.

```python
# 문제 1: 순서나 타입이 맞지 않으면 오류 발생
key = 'my_var'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)  # 정상
print(formatted)  # my_var     = 1.23

# 순서를 바꾸면 오류 발생
formatted = '%-10s = %.2f' % (value, key)  # TypeError: must be real number, not str

# 타입을 바꾸면 오류 발생
formatted = '%-10s = %.2f' % (key, '1.234')  # TypeError: must be real number, not str
```

두 번째 문제점은 형식화를 하기 전에 값을 살짝 변경해야 한다면 식을 읽기가 매우 어려워진다는 점이다.

```python
# 문제 2: 값을 수정해야 할 때 가독성이 떨어짐
pantry = [
    ('아보카도', 1.0),
    ('바나나', 2.5),
    ('사과', 3.0)
]

# C 스타일 형식화 - 가독성이 떨어짐
for item in pantry:
    print('%-10s = %.1f' % (item[0], item[1] * 1.2))  # 20% 가격 인상
```

세 번째 문제점은 형식화 문자열에서 같은 값을 여러 번 사용하고 싶다면 튜플에서 같은 값을 여러 번 반복해야 한다는 점이다.

```python
# 문제 3: 같은 값을 반복해서 사용해야 함
name = 'Python'
formatted = 'Hello, %s! Welcome to %s. %s is a great language.' % (name, name, name)
print(formatted)  # Hello, Python! Welcome to Python. Python is a great language.
```

마지막 문제점은 형식화 식에 딕셔너리를 사용하면 문장이 번잡스러워진다는 것이다.

```python
# 문제 4: 딕셔너리 사용 시 문장이 복잡해짐
data = {
    'name': 'Python',
    'version': '3.9',
    'year': 2020
}
formatted = '%(name)s %(version)s was released in %(year)d' % data
print(formatted)  # Python 3.9 was released in 2020
```

### 내장 함수 format

내장 함수 `format`은 단일 값을 형식화할 때 유용하다.

```python
# 기본 사용법
x = 1234.5678
print(format(x, '0.2f'))  # '1234.57'
print(format(x, '>10.1f'))  # '   1234.6'

# 천 단위 구분자
print(format(1234567, ','))  # '1,234,567'

# 진수 변환
print(format(42, 'b'))  # '101010' (이진수)
```

### str.format 메서드

`str` 타입에 새로 추가된 `format` 메서드를 호출하면 여러 값에 대해 한꺼번에 이 기능을 적용할 수 있다.

```python
# 위치 기반 인자
print('{} {} {}'.format('파이썬', '최고', '언어'))  # '파이썬 최고 언어'

# 키워드 인자
print('{name}는 {age}살입니다.'.format(name='홍길동', age=25))  # '홍길동는 25살입니다.'

# 딕셔너리 언패킹
data = {'name': '홍길동', 'age': 25}
print('{name}는 {age}살입니다.'.format(**data))  # '홍길동는 25살입니다.'

# 인덱스 기반
key = 'my_var'
value = 1.234
formatted = '{1} = {0}'.format(key, value)
print(formatted)
```

```terminal
>>>
1.234 = my_var
```

위치 인덱스를 사용하면 format에 넘기는 인자의 순서를 바꾸지 않아도 형식화 문자열을 사용해 형식화한 값의 출력 순서를 변경할 수 있다. 그리고 키워드 인자를 사용하면 `format`에 넘기는 인자에 값을 여러 번 반복할 필요가 없다.

하지만 `format` 메서드도 앞에서 설명한 두 번째 문제점은 해결하지 못한다.

```python
for i, (item, count) in enumerate(pantry):
    old_style = '#%d: %s = %d' % (
        i + 1,
        item.title(),
        count * 1.2
    )

    new_style = '#{}: {:<10s} = {}'.format(
        i + 1,
        item.title(),
        count * 1.2
    )
    
    assert old_style == new_style
```

C 스타일 형식화와 새로운 형식화는 가독성 면에서 거의 차이가 없으며, 둘 다 읽기에 좋지 않다.

이런 단점 때문에 웬만하면 `str.format` 메서드를 사용하지 말 것을 권한다.


### f-문자열

Python 3.6부터 도입된 f-문자열은 가장 현대적이고 읽기 쉬운 문자열 형식화 방법입니다.

```python
# 기본 사용법
name = '파이썬'
version = 3.10
print(f'{name} {version}')  # '파이썬 3.10'

# 표현식 사용
x, y = 10, 20
print(f'{x} + {y} = {x + y}')  # '10 + 20 = 30'

# 딕셔너리 사용
data = {'name': '홍길동', 'age': 25}
print(f'{data["name"]}는 {data["age"]}살입니다.')  # '홍길동는 25살입니다.'

# 조건부 표현식
age = 20
print(f'당신은 {"성인" if age >= 20 else "미성년자"}입니다.')  # '당신은 성인입니다.'

# repr 문자열
formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)

# 여러 형식화 길이 차이 비교
f_string = f'{key:<10} = {value:.2f}'

c_tuple  = '%-10s = %.2f' % (key, value)

str_args = '{:<10} = {:.2f}'.format(key, value)

str_kw   = '{key:<10} = {value:.2f}'.format(key=key,
                                            value=value)

c_dict   = '%(key)-10s = %(value).2f' % {'key': key,
                                         'value': value}
```

f-문자열이 제공하는 표현력, 간결성, 명확성을 고려할 때 파이썬 프로그래머가 사용할 수 있는 형식화 옵션 중에서 f-문자열이 가장 좋은 선택이다.

### 기억해야 할 내용

- % 연산자를 사용하는 C 스타일 형식화 문자열은 여러 가지 단점과 번잡성이라는 문제가 있다.
- `str.format` 메서드는 형식 지정자 [미니 언어](https://docs.python.org/3/library/string.html#format-specification-mini-language)에서 유용한 개념 몇 가지를 새로 제공했다. 하지만 이를 제외하면 str.format 메서드도 C 스타일 형식 문자열의 문제점을 그대로 가지고 있으므로, 가능하면 피하는 것이 좋다.
- f-문자열은 값을 문자열 안에 넣는 새로운 구문으로, C 스타일 형식화 문자열의 가장 큰 문제점을 해결해준다.
- f-문자열은 간결하지만, 위치 지정자 안에 임의의 파이썬 식을 직접 포함시킬 수 있으므로 매우 강력하다.

## BETTER WWAY5 복잡한 식을 쓰는 대신 함수를 작성하라

파이썬은 문법이 간결하므로 상단한 로직이 들어가는 식도 한 줄로 매우 쉽게 작성할 수 있다. 예를 들어 URL의 질의 문자열을 구문 분석하고 싶다고 하자. 여기서 각 질의 문자열(query string) 파라미터는 정수 값을 표현한다.

```python
from urllib.parse import parse_qs

my_values = parse_qs('빨강=5&초록=0&투명도=', 
                     keep_blank_values=True)
print(repr(my_values))
```

```terminal
>>>
{'빨강': ['5'], '초록': ['0'], '투명도': ['']}
```

query string에는 여러 값이 들어 있고, 일부는 값이 하나만 들어 있으며, 일부는 이름은 있지만 값이 비어 있고, 일부는 아예 없을 수도 있다. 결과 딕셔너리에 get 메서드를 사용하면 상황에 따라 다른 값이 반환된다.

```python
print('빨강:', my_values.get('빨강'))
print('초록:', my_values.get('초록'))
print('투명도:', my_values.get('투명도'))
``` 

```terminal
>>>
빨강: ['5']
초록: ['']
투명도: None
```

파라미터가 없거나 비어있을 경우 0이 디폴트 값으로 대입되면 좋을 것이다. 이런 로직을 처리하기 위해 `if` 식(expression)을 사용하면 좋을 것이다. 다음 각 식은 왼쪽의 하위 식이 `False`인 경우 모두 `or` 연산자 오른쪽의 하위 식 값으로 계산된다.

```python
red = my_values.get('빨강', [''])[0] or 0
green = my_values.get('초록', [''])[0] or 0
opacity = my_values.get('투명도', [''])[0] or 0

print(f'빨강: {red!r}, 초록: {green!r}, 투명도: {opacity!r}')
```

```terminal
>>>
빨강: '5', 초록: 0, 투명도: 0
```

하지만 이 식은 읽기 어려운 데다 우리가 원하는 모든 기능을 제공하지도 못한다. 우리는 모든 파라미터 값을 정수로 변환해서 즉시 수식에 활용하길 바란다. 그렇게 하려면 각 식을 int 내장 함수로 감싸서 문자열을 정수로 구문 분석해야 한다.

```python
red = int(my_values.get('빨강', [''])[0] or 0)
green = int(my_values.get('초록', [''])[0] or 0)
opacity = int(my_values.get('투명도', [''])[0] or 0)
```

현재 이 코드는 너무 읽기 어렵고, 시각적 잡음이 많다. 즉, 코드를 이해하기 쉽지 않으므로, 코드를 새로 읽는 사람이 이 식이 실제로 어떤 일을 하는지 이해하기 위해 너무 많은 시간을 투자해야 한다.

파이썬에는 코드를 간결하게 유지하면서 이런 경우를 명확하게 표현할 수 있는 `if/else` 조건식(또는 삼항 조건식)이 있다.

```python
red_str = my_values.get('빨강', [''])
red = int(red_str[0]) if red_str[0] else 0
```

이 코드가 더 좋다. 또한, 덜 복잡한 경우라면 `if/else` 조건식이 코드를 아주 명확하게 해줄 것이다. 하지만 앞의 예제는 다음과 같이 여러 줄로 나눠 쓴 완전한 `if/else` 문보다는 아직 덜 명확하다.

```python
red_str = my_values.get('빨강', [''])
if red_str[0]:
    red = int(red_str[0])
else:
    red = 0
```

이 로직을 반복 적용하려면 (이 예제처럼 단지 두세 번에 불과할지라도) 꼭 도우미 함수를 작성해야 한다.

```python
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default
```

도우미 함수 호출을 사용해 작성한 코드는 앞에서 본 복잡한 버전이나 두 줄로 나눠 쓴 `if/else` 문보다 명확하다.

```python
red = get_first_int(my_values, '빨강')
```

식이 복잡해지기 시작하면 바로 식을 더 작은 조각으로 나눠서 로직을 도우미 함수로 옮길지 고려해야 한다. 복잡한 식을 표현할 수 있는 파이썬의 함축적인 문법이 이런 지저분한 코드를 만들어내지 않도록 하라. '반복하지 말라(Don't Repeat Yourself)'는 뜻의 DRY 원칙을 따르라.

### 기억해야 할 내용

- 파이썬 문법을 사용하면 아주 복잡하고 읽기 어려운 한 줄짜리 식을 쉽게 작성할 수 있다.
- 복잡한 식을 도우미 함수로 옮겨라. 특히 같은 로직을 반복해 사용할 때는 도우미 함수를 꼭 사용하라.
- boolean 연산자 `or`나 `and`를 식에 사용하는 것보다 `if/else` 식을 쓰는 편이 더 가독성이 좋다.

## BETTER WAY6 인덱스를 사용하는 대신 대입을 사용해 데이터를 언패킹하라

파이썬에는 값으로 이뤄진 불변 순서쌍을 만들어낼 수 있는 tuple 내장 타입이 있다.

```python
snack_calories = {
    '감튀': 510,
    '치즈퐁듀': 220,
    '치즈볼': 150,
}
items = tuple(snack_calories.items())
print(items)
```

```terminal
>>>
(('감튀', 510), ('치즈퐁듀', 220), ('치즈볼', 150))
```

튜플에 있는 값은 숫자 인덱스를 사용해 접근할 수 있다.

```python
item = ('호박엿', '식혜')
first = item[0]
second = item[1]
print(first, '&', second)
``` 

```terminal
>>>
호박엿 & 식혜
```

일단 튜플이 만들어지면, 인덱스를 통해 새 값을 대입해서 튜플을 변경할 수는 없다.

```python
item = ('호박엿', '식혜')
item[0] = '치즈퐁듀'
```

```terminal
>>>
Traceback ...
TypeError: 'tuple' object does not support item assignment
```

파이썬에는 **언패킹** 구문이 있다. 언패킹 구문을 사용하면 한 문장 안에서 여러 값을 대입할 수 있다.

```python
item = ('호박엿', '식혜')
first, second = item
print(first, '&', second)
```

```terminal
>>>
호박엿 & 식혜
```

언패킹은 튜플 인덱스를 사용하는 것보다 시각적인 잡음이 적다. 리스트, 시퀀스, 인터러블 안에 여러 계층으로 이터러블이 들어간 경우 등 다양한 패턴을 언패킹 구문에 사용할 수 있다.

파이썬 초보자는 언패킹을 사용하면 임시 변수를 정의하지 않고도 값을 맞바꿀 수 있다는 사실에 놀랄지도 모른다.

```python
a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)
```

```terminal
>>>
1 2
2 1
```

어떻게 이런 맞바꾸기가 가능한지 살펴보자. 파이썬은 오른쪽 할당 식을 먼저 계산한다. 그 결과 값이 이름이 없는 새로운 tuple에 저장된다. 그 후 대입문의 좌항에 있는 언패킹 패턴을 통해 이 튜플의 값이 좌항의 변수에 할당된다.

언패킹의 용례 중에서 또 한 가지 쓸모 있는 것으로 for 루프 또는 그와 비슷한 다른 요소의 대상인 리스트의 원소를 언패킹하는 것이 있다. 비교를 위해 먼저 언패킹을 사용하지 않고 간식이 들어있는 `list`에 대해 이터레이션하는 코드를 살펴보자.

```python
snacks = [('베이컨', 350), ('도넛', 240), ('머핀', 190)]
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f'#{i+1}: {name} = {calories} 칼로리')
```

```terminal
>>>
#1: 베이컨 = 350 칼로리
#2: 도넛 = 240 칼로리
#3: 머핀 = 190 칼로리
```

잘 작동하지만 잡음이 많다. snacks 구조 내부의 깊숙한 곳에 있는 데이터를 인덱스로 찾으려면 코드가 길어진다. 이런 경우 언패킹을 사용하면 코드가 훨씬 명확해진다.

```python
for rank, (name, calories) in enumerate(snacks, 1):
    print(f'#{rank}: {name} = {calories} 칼로리')
```

```terminal
>>>
#1: 베이컨 = 350 칼로리
#2: 도넛 = 240 칼로리
#3: 머핀 = 190 칼로리
```

이런 식의 루프가 필요할 때는 이 방법이 파이썬다운 방식이다. 코드가 더 짧고 이해하기도 쉽다. 일반적으로는 인덱스를 사용해 무언가에 접근할 필요가 전혀 없다.

### 기억해야 할 내용

- 파이썬은 한 문장 안에서 여러 값을 대입할 수 있는 언패킹이라는 특별한 문법을 제공한다.
- 파이썬 언패킹은 일반화돼 있으므로 모든 이터러블에 적용할 수 있다. 그리고 이터러블이 여러 계층으로 내포된 경우에도 언패킹을 적용할 수 있다.
- 인덱스를 사용해 시퀀스 내부에 접근하는 대신 언패킹을 사용해 시각적인 잡음을 줄이고 코드를 더 명확하게 만들라.

## BETTER WAY7 range보다는 enumerate를 사용하라

`range` 내장 함수는 어떤 정수 집합을 이터레이션하는 루프가 필요할 때 유용하다

```python
from random import randint

random_bits = 0
for i in range(32):
    if randint(0, 32) & 1:
        random_bits |= 1 << i

print(bin(random_bits))
```

```terminal
>>>
0b10101010101010101010101010101010
```

문자열로 이뤄진 `list`처럼 이터레이션할 대상 데이터 구조가 있으면 이 시퀀스에 대해 바로 루프를 돌 수 있다.

```python
flavor_list = ['바닐라', '초콜릿', '피칸', '딸기']
for flavor in flavor_list:
    print(f'{flavor} 맛있어요!')
```

```terminal
>>>
바닐라 맛있어요!
초콜릿 맛있어요!
피칸 맛있어요!
딸기 맛있어요!
```

리스트를 이터레이션하면서 리스트의 몇 번째 원소를 처리 중인지 알아야 할 때가 있다. 이 때 `range`를 사용하는 방법도 있다.

```python
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i+1}: {flavor}')
```

```terminal
>>>
1: 바닐라
2: 초콜릿
3: 피칸
4: 딸기
```

그러나 이 코드는 list의 길이를 알아야 하고, 인덱스를 사용해 배열 원소에 접근해야 한다. 이렇게 단계가 여러 개이므로 코드를 읽기 어렵다.

파이썬은 이런 문제를 해결할 수 있는 `enumerate` 내장 함수를 제공한다. `enumerate`는 이터레이터를 지연 계산 제너레이터로 감싼다. 이 이터레이터는 원래 이터레이터의 각 원소와 해당 원소의 인덱스를 tuple로 묶은 값을 하나씩 생성한다.

```python
it = enumerate(flavor_list)
print(next(it))
print(next(it))
```

```terminal
>>>
(0, '바닐라')
(1, '초콜릿')
```

`enumerate`가 넘겨주는 각 쌍을 for 문에서 간결하게 언패킹할 수 있다.

```python
for i, flavor in enumerate(flavor_list):
    print(f'{i+1}: {flavor}')
```

```terminal
>>>
1: 바닐라
2: 초콜릿
3: 피칸
4: 딸기
```

`enumerate`의 두 번째 파라미터로 어디부터 수를 세기 시작할지 지정할 수 있다.

```python
for i, flavor in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')
```

```terminal
>>>
1: 바닐라
2: 초콜릿
3: 피칸
4: 딸기
```

### 기억해야 할 내용

- `enumerate`를 사용하면 이터레이터에 대해 루프를 돌면서 이터레이터에서 가져오는 원소의 인덱스까지 얻는 코드를 간결하게 작성할 수 있다.
- `range`에 대해 루프를 돌면서 시퀀스의 원소를 인덱스로 가져오기보다는 `enumerate`를 사용하라.
- `enumerate`의 두 번째 파라미터로 시작 인덱스를 지정할 수 있다(기본값은 0이다).