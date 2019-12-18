import random


def setup():
    size(400,500)
    background(0)
    noLoop()
    
def rect_gray():
    fill(129, 135, 128)
    rect(0,20,400,480)
    
def rect_blue():
    fill(41, 90, 227)
    rect(10,30,380,470) 
    
def rect_red():  
    x=10
    y=30
    fill (219,29,29)
    for i in range(10):
       # for j in range(8):
        rect(x,y,380/10,30)
        x=x+380/10
        noLoop
        
    translate(0,y)
    noLoop  
    
def snow():
    #rect(1,1,2,2) 
    for i in range(100):        
        rect(random.randint(0,400),random.randint(0,500),5,5)
        fill(255, 1.0)
        
      
def draw():
     rect_gray()  
     rect_blue() 

     y=30
     rect_red()
     for j in range(7):
         y=(y*j)
         rect_red()
        
         snow()
    
        
    
   
    
    
    
