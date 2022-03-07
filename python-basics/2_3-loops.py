#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. 반복문

# 5번 같은 코드 반복하기
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")

# 만약 코드가 더 복잡하다면?
x = 1
y = 2
z = (x + y) * z
print("z", z)

x = 1
y = 2
z = (x + y) * z
print("z", z)

x = 1
y = 2
z = (x + y) * z
print("z", z)

x = 1
y = 2
z = (x + y) * z
print("z", z)

x = 1
y = 2
z = (x + y) * z
print("z", z)

# 이걸 반복문으로 나타낸다면?

# 첫번째 방법: for loop

for x in range(5):
  print("Hello World")

# 두번째 방법: while loop

i = 0
while i < 5:
  print("Hello World")

# for loop 을 쓰는 다양한 방법

# 1. 10번 반복을 해야할때
for i in range(10):
  print(i)

# 2. 리스트의 엘레먼트를 하나씩 엑세스 할때
x = ['철수', '영희', '찰스']
for name in x:
  print(name)

# 반복문에 다양한 조건을 붙일 수 있음
import time
while 1 > 0:
  print("Hello World")
  time.sleep(1)

while True:
  print("Hello World")
  time.sleep(1)

