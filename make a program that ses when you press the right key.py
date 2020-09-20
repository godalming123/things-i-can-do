from turtle import *
win3 = Screen ()
win3.listen ()
win3.onkeypress (lambda:print("right"), "Right")
while True :
    try :
        win3.update ()
    except :
        break
print ("loop broken sucsesfuly")
