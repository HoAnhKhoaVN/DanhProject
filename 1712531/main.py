# -*- coding: utf-8 -*-
from tkinter import *
import numpy as np

def printData(firstName, lastName):
    print(firstName)
    print(lastName)
    root.destroy()


def isExist(path,i,j):
  if([i,j] in path):
    return True
  return False

def isSubstitution(X,Y):
  return X[0]+1==Y[0] and X[1]+1== Y[1]

def isDeletion(X,Y):
  return X[0]==Y[0] and X[1]+1==Y[1]

def Alignment(path,s1,s2):
  left=[]
  right=[]
  for i in range(len(path)-1,0,-1):
    if(isSubstitution(path[i], path[i-1])):
      left.append(s1[path[i][0]].upper())
      right.append(s2[path[i][1]].upper())
    elif(isDeletion(path[i], path[i-1])):
      left.append("*")
      right.append(s2[path[i][1]].upper())
    else:
      right.append("*")
      left.append(s1[path[i][0]].upper())
  return left, right

def display_table(table,lst,path,s1,s2): 
    # Copy sang mang mới
    total_rows = len(lst)+1
    total_columns = len(lst[0])+1
    
    X=np.full((total_rows, total_columns),fill_value=0,dtype=object)
    # Thêm tên ở dòng
    for i in range(2,total_columns):
        X[0,i]=s2[i-2]
        e = Entry(table, width=3, fg='black',bg="blue",
                          font=('Arial',16,'bold')) 
        e.grid(row=0, column=i) 
        e.insert(END,X[0][i])    
        
        
    # Thêm tên ở cột
    for i in range(2,total_rows):
        X[i,0]=s1[i-2]
        e = Entry(table, width=3, fg='black',bg="blue",
                          font=('Arial',16,'bold')) 
        e.grid(row=i, column=0) 
        e.insert(END,X[i][0])    
        
    for i in range(1, total_rows):
        for j in range(1, total_columns):
            X[i,j]=lst[i-1,j-1]
    # find total number of rows and 
    # columns in list 
    # code for creating table
    for i in range(1,total_rows): 
        for j in range(1,total_columns): 
            if([i-1,j-1] in path):
                e = Entry(table, width=3, fg='black',bg="red",
                          font=('Arial',16,'bold')) 
            else:
                e = Entry(table, width=3, fg='black', 
                               font=('Arial',16,'bold')) 
            e.grid(row=i, column=j) 
            e.insert(END,X[i][j])    
            
    # Alignment
#    e= Entry(table,width=10, fg="red", font=("Arial", 16, 'bold'))
#    e.insert(END,"\nAlignment\n")
    align=Tk()
    # Thực hiện căn lề
    left,right=Alignment(path,s1,s2)
    
    space=np.full((len(right)),fill_value="|", dtype=object)
    # Hiện ra man hình
    for i in range(len(left)):
        e = Entry(align, width=3, fg='black',
                          font=('Arial',16,'bold')) 
        e.grid(row=0, column=i) 
        e.insert(END,left[i])
        
    for i in range(len(space)):
        e = Entry(align, width=3, fg='black',
                          font=('Arial',16,'bold')) 
        e.grid(row=1, column=i) 
        e.insert(END,space[i])
            
    for i in range(len(right)):
        e = Entry(align, width=3, fg='black',
                          font=('Arial',16,'bold')) 
        e.grid(row=2, column=i) 
        e.insert(END,right[i])
        
    
def isDuplicated(x,y):
  if(x==y):
    return 0
  else:
    return 2

def create_table(s1,s2):
  n=len(s1)
  m=len(s2)
  matrix=np.zeros((n+1,m+1), dtype=np.int64)
  for i in range(n+1):
    matrix[i,0]=i

  for i in range(m+1):
    matrix[0,i]=i

  for i in range(1,n+1):
    for j in range(1,m+1):
      matrix[i,j]=min(matrix[i-1,j]+1,matrix[i,j-1]+1,matrix[i-1,j-1]+isDuplicated(s1[i-1],s2[j-1]))

  return matrix


def trace(n,m,D ,path,s1,s2):
  if(n==0) and (m==0):
    return path
  deletion= D[n-1,m]+1
  insertion= D[n,m-1]+1
  substitution= D[n-1,m-1]+isDuplicated(s1[n-1], s2[m-1])
  if(substitution==D[n,m]):
    path.append([n-1,m-1])
    return trace(n-1,m-1,D,path,s1,s2)  

  if(deletion==D[n,m]):
    path.append([n-1,m])
    return trace(n-1,m,D,path,s1,s2)

  if(insertion==D[n,m]):
    path.append([n,m-1])
    return trace(n,m-1,D,path,s1,s2)
  
def process():
    table=Tk()
    s1= entry1.get()
    s2 = entry2.get()
    D=create_table(s1,s2)
    
    path=trace(len(s1),len(s2),D,[],s1,s2)
    path=[[len(s1),len(s2)]]+ path
    t=display_table(table,D,path,s1,s2)
    #table.mainloop()
    
### MAIN ###
# Cài 

root = Tk()  # create windown
#Label 1
label1 = Label(root,text = 'Enter string 1:')
label1.pack()

entry1 = Entry(root, width = 30)
entry1.pack()

label3 = Label(root, text="Enter string 2:")
label3.pack()

entry2 = Entry(root, width = 30)
entry2.pack()

#
button1 = Button(root, text = 'Min Edit Distance')
button1.pack() 
button1.config(command = process)

root.mainloop()