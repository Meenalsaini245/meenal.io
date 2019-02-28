# n = int(input("enter the number"))
# for i in range(n-1,-1,-1):
#     for j in range(n-i-1,-1,-1):
#         print("   ", end="")
#     for j in range((i*2)+1,-1,-1):
#         print(" * ",end="")
#     print()


# def find_name(l, name):
#      return l[index(l, lambda item: item["name"] == name)]


# import re
# def find_string(clg_name):
#     with open('script.txt') as file:
#         matcher = re.compile('.*'+clg_name.lower()+'.*')
#         for each_entry in file:
#             if matcher.match(each_entry.lower()):
#                 i,j,k= each_entry.split('|')
#                 print('|'.join([j,i,k]),end="")

# if __name__=='__main__':
#     clg_name=""
#     while clg_name!="exit":
#         clg_name=input("enter string:")
#         find_string(clg_name)
#         print('Type "exit" to quit')

# class employee:
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.email = first + "." +last + '@gmail.com'
#         self.pay = pay
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

# emp1 = employee('meenal','saini',60000)
# emp2 = employee('priya',"sai",7000)



# print(emp1.fullname())               
# print(employee.fullname(emp2))   

# list1=[[2,3,4,],[5,4,8],[9,2,6]]
# for i in list1:
#     print(i)
# for i in rows:
#     for j in column:

# person = {'name': 'meenal','age':25}
# sentence = 'my name is {0[name]} and my age is {1[age]}'.format(person,person)
# print(sentence)

# class person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age


import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass

    def move (self, dirnx,dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

class snake(object):
    def __init__(self,color,pos):
        pass

    def move(self):
        pass

    def reset(self,pos):
        pass

    def addcube(self):
        pass

    def draw(self, surface):
        pass

def drawgrid(w, rows, surface):
    sizebtwn= w//rows
    x= 0
    y=0
    for i in range(rows):
        x = x + sizebtwn
        y = y + sizebtwn

        pygame.draw.line(surface,(255,255,255),(x,0),(x,w))
        pygame.draw.line(Surface,(255,255,255),(0,y),(w,y))
    

def redrawwindow(surface):
    global rows,width
    surface.fill(0,0,0)
    drawgrid(width,rows,surface)
    pygame.display.update()

def randomsnack(rows, items):
    pass

def messagebox(subject, content):
    pass

def main():
    global width,rows
    width = 500
    height = 500
    rows = 20
    win = pygame.display.setmode(width,width)
    a = snake((255,0,0),(10,10))
    flag = True
    clock = pygame.time.clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawwindow(win)

