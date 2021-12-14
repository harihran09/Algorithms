import tkinter as tk
from tkinter import *

def mapto(z,y):
    return (600/y)*z

a=[]
n=int(input('Enter the size of list'))
print('Enter the elements')
for i in range(n):
    a=a+[int(input())]
print(a)
    
pad=5
width=30
space=10
    
root=Tk()
root.title('Basic tkinter line')
root.geometry('{}x{}+0+0'.format(root.winfo_screenwidth(),(root.winfo_screenheight()-100)))
cw=1000              #canvas width
ch=1000               #canvas height
canvas=Canvas(root,width=cw,height=ch)
canvas.place(x=0,y=0)
print(root.winfo_screenwidth())
print(root.winfo_screenheight())
print(root.winfo_width())
print(root.winfo_height())

x_start=pad
x_end=x_start+width
y_start=(root.winfo_screenheight()-120)

for i in range(n):
    
    y_end=y_start-mapto(a[i],max(a))
    canvas.create_rectangle(x_start,y_start,x_end,y_end,fill='#ff0000',outline='#000000',width=1)
    x_start=x_start+width+space
    x_end=x_start+width
    


            
        
    

for i in range(n-1):
    for j in range(n-i-1):
        x_start=pad
        x_end=x_start+width
        for k in range(n-i):
            
            y_end=y_start-mapto(a[k],max(a))
        
            if(k==j or k==j+1):
                canvas.create_rectangle(x_start,y_start,x_end,y_end,fill='#ffff00',outline='#000000',width=1)
            else:
                canvas.create_rectangle(x_start,y_start,x_end,y_end,fill='#ff0000',outline='#000000',width=1)
            x_start=x_start+width+space
            x_end=x_start+width
        for x in range(k+1,n):
            
            y_end=y_start-mapto(a[x],max(a))
            
            canvas.create_rectangle(x_start,y_start,x_end,y_end,fill='#ff00ff',outline='#000000',width=1)
            
            x_start=x_start+width+space
            x_end=x_start+width     

        canvas.update()
        canvas.after(250)
        
        canvas.delete(ALL)

        
        if(a[j]>a[j+1]):
            a[j]=a[j]+a[j+1]
            a[j+1]=a[j]-a[j+1]
            a[j]=a[j]-a[j+1]
            x_start=pad
            x_end=x_start+width
            for k in range(n-i):
        
                y_end=y_start-mapto(a[k],max(a))
                
                if(k==j or k==j+1):
                    canvas.create_rectangle(x_start,y_start,x_end,y_end,fill='#ffff00',outline='#000000',width=1)
                else:
                    canvas.create_rectangle(x_start,y_start,x_end,y_end,fill='#ff0000',outline='#000000',width=1)
                x_start=x_start+width+space
                x_end=x_start+width
            for x in range(k+1,n):
                y_end=y_start-mapto(a[x],max(a))
                
                canvas.create_rectangle(x_start,y_start,x_end,y_end,fill='#ff00ff',outline='#000000',width=1)
                
                x_start=x_start+width+space
                x_end=x_start+width

            
            canvas.update()
            canvas.after(750)
            canvas.delete(ALL)
            
x_start=pad
x_end=x_start+width
y_start=(root.winfo_screenheight()-120)

for i in range(n):
    
    y_end=y_start-mapto(a[i],max(a))
    canvas.create_rectangle(x_start,y_start,x_end,y_end,fill='#ff00ff',outline='#000000',width=1)
    x_start=x_start+width+space
    x_end=x_start+width
        
        
            
        
        
       
        

print(a)

root.update_idletasks()
root.mainloop()


