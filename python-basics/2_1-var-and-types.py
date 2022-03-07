#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. 변수, 타입

# Section. 변수

x = 1
y = 2

# 변수 - 값을 가지고 있는 이름 있는 저장공간

# Section. 타입

# 값이 가지고 있는 고유의 종류

# ------------------

# Integer (정수)

x = 1
y = 2

# Float (분수, 소수)

x = 0.1
y = 2/3

# Int와 Float을 같이 써서 사칙연산을 하면 결과값은 Float 타입을 가지고 있음
z = 0.1 + 2
type(z) # float

# Boolean (불리안, 참/거짓)

x = True
y = False

# String (문자열)

x = 'hello'
y = "Bye"

# String 과 Integer 를 섞어서 사칙연산을 할 수 없음
z = 'Hello' + 'Bye' # 'HelloBye'
t = 'Hello' + 1 # Error!

# 이럴때 숫자를 문자열 타입으로 바꾸거나 문자열을 숫자 타입으로 바꾸면 사칙연산 가능
x = 'Hello' + str(1) # 'Hello1'
y = int('1') + 2 # 3