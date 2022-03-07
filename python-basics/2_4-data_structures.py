#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. 자료 구조

# Section. List (배열)

# 사용법

x = []
x = list()
print(x)
x = [[1,2],[3,4]] # nested list

x = [1,2,3]
x.append(4)
x.append(5)
x.pop()
print(x)

       #0     1     2      3     4   - zero based index
x = ["철수","영희","토마스","민혜","민수"]
print(x[4])

# 사용 용도
# 1. 여러개의 엘레먼트를 담고 싶을때
# 2. 엘레멘트를 순서대로 담고 싶을때
# 3. 변수 안에 있는 내용물을 바꿀거 같을때

# tuple (튜플)
x = tuple()
x = (1,2,3,4,5)
x = ((1,2), (3,4))
x = ("철수", "영희")
x[0] = "민수"

# list = 내용물을 바꿀 수 있는 자료구조: mutable 뮤터블
# tuple = 내용물을 바꿀 수 없는 자료구조: immutable 임뮤터블

# Set (세트)
x = set()
x.add(1)
x.add(2)
x = {1,2}

x = set(("민수","철수","영희"))
x[0] = "민혜"

# 1. 순서가 뒤죽박죽이 될 수 있다
# 2. Set 는 immutable - 내용물을 바꿀 수 없음
# 3. 어떤 내용물이 있는지 확인하는게 빠르다

x = set((1,2,3,4,5,6,7))
print(7 in x)

# Dictionary (딕셔너리, 사전, 해쉬 테이블)
x = {}
x = dict()

# Key, Value
x["이름"] = "민수"
x["나이"] = 20
x["위치"] = "한국"

# 1. 순서가 뒤죽박죽일 수 있다
# 2. key 에 해당되는 값을 나중에 불러오고 싶을때
# 3. 어떤 Key가 자료 구조안에 들어있는지 빨리 알고 싶을때

# list vs tuple
# list: mutable (내용물을 바꿀 수 있다)
# tuple: immutable (내용물을 바꿀 수 없다)

# set vs dictionary
# set: key-value 가 필요 없고 key 만 필요할때
# dictionary: key-value 가 필요할때

# list + tuple vs set + dictionary

# list + tuple:
# 1) ordered - 순서가 정해져있다 - 내용물이 자료구조에 들어간 순서대로 저장된다
# 2) 멤버쉽 검색이 느리다

# set + dictionary:
# 1) unordered - 내용물이 자료구조에 들어간 순서대로 저장되지 않을 수 있다
# 2) 멤버쉽 검색이 빠르다
