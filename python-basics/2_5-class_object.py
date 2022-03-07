#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. 클래스, 오브젝트
class Person:
  name = "워니"

  def say_hello(self):
    print("안녕 나는 " + self.name)

p = Person()

class Person:
  def __init__(self, name):
    self.name = name

  def say_hello(self):
    print("안녕 나는 " + self.name)

p = Person("워니")
p.say_hello()

class Person:
  def __init__(self, name, hometown):
    self.name = name
    self.hometown = hometown

  def say_hello(self, to_name):
    print("안녕 나는 " + self.name + "반가워, " + to_name)

  def introduce(self):
    print("나는 " + self.name + " 이고, 내 고향은 " + self.hometown + " 이야")

# 상속

class Artist(Person):
  def draw(self, title):
    print("나는 곧 다음 작품을 그릴거에요. 작품 이름은 " + title)

class Programmer(Person):
  def code(self, language):
    print("나는 다음 프로젝트는 " + language + "로 코딩 할거에요")

artist = Artist("워니", "창원")
programmer = Programmer("민수", "울산")