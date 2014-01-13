## Term Project: Paint Program
## Fall 2010 (Intro to Computing)
## Made by: Maitreyee Palkar ; mpalkar
## 15-110 Section H
###############################################
## This code can't be copied or used by anyone
###############################################

from Tkinter import *
import base64

def motion(event):
    canvas = event.widget.canvas
    canvas.data["motion"].append((event.x,event.y))
    redrawAll(canvas)

def release(event):
    canvas = event.widget.canvas
    width = canvas.data["width"]
    height = canvas.data["height"]
    motion = canvas.data["motion"]
    last = len(motion)-1
    if(canvas.data["eraser"]==True and event.x>0 and event.x<width-25 and
       event.y>0 and event.y<height-125):
        canvas.data["undoList"].append(["eraser","white",
                                        (event.x-25,event.y-25),
                                        (event.x+25,event.y+25)])
    elif(last>=1):
        leftX = motion[1][0]
        leftY = motion[1][1]
        rightX = motion[last][0]
        rightY = motion[last][1]
        selection = canvas.data["selection"]
        color = canvas.data["fill"]
        if(leftX>0 and leftX<width and leftY>0 and leftY<height-100 and
           rightX>0 and rightX<width and rightY>0 and rightY<height-100):
            canvas.data["undoList"].append([selection,color,
                                            (leftX,leftY),(rightX,rightY)])
    canvas.data["motion"]=[(600,400)]
    redrawAll(canvas)

def keyPressed(event):
    canvas = event.widget.canvas
    if(event.char=="e"):
        canvas.data["eraser"] = True
    else:
        canvas.data["eraser"] = False
        if(event.char=="u"):
            if(len(canvas.data["undoList"])>0):
                canvas.data["undoList"].pop()
        elif(event.char=="n"):
            canvas.data["selection"]="None"
        elif(event.char=="i"):
            canvas.data["undoList"].append(["image","None",(0,0),(0,0)])
        elif(event.char=="l"):
            canvas.data["loadSavedPic"]=True
        elif(event.char=="r"):
            canvas.data["infoFlag"] = False
        elif(event.char=="s"):
            saveImage(canvas)
    redrawAll(canvas)

def mousePressed(event):
    canvas = event.widget.canvas
    X = event.x
    Y = event.y
    infoLeftX = canvas.data["infoLeftX"]
    infoLeftY = canvas.data["infoLeftY"]
    infoRightX = canvas.data["infoRightX"]
    infoRightY = canvas.data["infoRightY"]
    optionsLeftX = canvas.data["optionLeftX"]
    optionsLeftY = canvas.data["optionLeftY"]
    optionsRightX = canvas.data["optionRightX"]
    optionsRightY = canvas.data["optionRightY"]
    colorsLeftX = canvas.data["colorsLeftX"]
    colorsLeftY = canvas.data["colorsLeftY"]
    colorsRightX = canvas.data["colorsRightX"]
    colorsRightY = canvas.data["colorsRightY"]
    options = canvas.data["options"]
    colors = canvas.data["colors"]
    if((X<infoRightX) and (X>infoLeftX) and
       (Y>infoLeftY) and (Y<infoRightY)):
        canvas.data["infoFlag"] = True
    elif((X<optionsRightX) and (X>optionsLeftX) and
       (Y>optionsLeftY) and (Y<optionsRightY)):
        if(Y<(optionsRightY-(optionsRightY-optionsLeftY)/2)):
            if(X<(optionsRightX-2*(optionsRightX-optionsLeftX)/3)):
                canvas.data["selection"]=options[0][0]
            elif(X>(optionsRightX-2*(optionsRightX-optionsLeftX)/3) and
                 X<(optionsRightX-(optionsRightX-optionsLeftX)/3)):
                canvas.data["selection"]=options[0][1]
            else:
                canvas.data["selection"]=options[0][2]
        else:
            if(X<(optionsRightX-2*(optionsRightX-optionsLeftX)/3)):
                canvas.data["selection"]=options[1][0]
            elif(X>(optionsRightX-2*(optionsRightX-optionsLeftX)/3) and
                 X<(optionsRightX-(optionsRightX-optionsLeftX)/3)):
                canvas.data["selection"]=options[1][1]
            else:
                canvas.data["selection"]=options[1][2]
    elif((X<colorsRightX) and (X>colorsLeftX) and
       (Y>colorsLeftY) and (Y<colorsRightY)):
        if(Y<(colorsRightY-(colorsRightY-colorsLeftY)/2)):
            if(X<(colorsRightX-5*(colorsRightX-colorsLeftX)/6)):
                canvas.data["fill"]=colors[0][0]
            elif(X>(colorsRightX-5*(colorsRightX-colorsLeftX)/6) and
                 X<(colorsRightX-4*(colorsRightX-colorsLeftX)/6)):
                canvas.data["fill"]=colors[0][5]
            elif(X>(colorsRightX-4*(colorsRightX-colorsLeftX)/6) and
                 X<(colorsRightX-3*(colorsRightX-colorsLeftX)/6)):
                canvas.data["fill"]=colors[0][4]
            elif(X>(colorsRightX-3*(colorsRightX-colorsLeftX)/6) and
                 X<(colorsRightX-2*(colorsRightX-colorsLeftX)/6)):
                canvas.data["fill"]=colors[0][3]
            elif(X>(colorsRightX-2*(colorsRightX-colorsLeftX)/6) and
                 X<(colorsRightX-(colorsRightX-colorsLeftX)/6)):
                canvas.data["fill"]=colors[0][2]
            else:
                canvas.data["fill"]=colors[0][1]
        else:
            if(X<(colorsRightX-5*(colorsRightX-colorsLeftX)/6)):
                canvas.data["fill"]=colors[1][0]
            elif(X>(colorsRightX-5*(colorsRightX-colorsLeftX)/6) and
                 X<(colorsRightX-4*(colorsRightX-colorsLeftX)/6)):
                canvas.data["fill"]=colors[1][5]
            elif(X>(colorsRightX-4*(colorsRightX-colorsLeftX)/6) and
                 X<(colorsRightX-3*(colorsRightX-colorsLeftX)/6)):
                canvas.data["fill"]=colors[1][4]
            elif(X>(colorsRightX-3*(colorsRightX-colorsLeftX)/6) and
                 X<(colorsRightX-2*(colorsRightX-colorsLeftX)/6)):
                canvas.data["fill"]=colors[1][3]
            elif(X>(colorsRightX-2*(colorsRightX-colorsLeftX)/6) and
                 X<(colorsRightX-(colorsRightX-colorsLeftX)/6)):
                canvas.data["fill"]=colors[1][2]
            else:
                canvas.data["fill"]=colors[1][1]
    redrawAll(canvas)

def saveImage(canvas):
    undoList = canvas.data["undoList"]
    fileHandler = open("savedImage.txt", "wt") # wt stands for write text
    fileHandler.write(str(undoList)) # write the text
    fileHandler.close() # close the file

def loadSavedImage(canvas):
    fileHandler = open("savedImage.txt", "rt") # rt stands for read text
    text = fileHandler.readlines() # read the entire file into a single string
    fileHandler.close() # close the file
    string = text[0]
    undoList = eval(string)
    canvas.data["savedList"]=undoList

def drawEraser(canvas,centerX,centerY):
    canvas.create_rectangle(centerX-25,centerY-25,centerX+25,centerY+25,
                            fill="white",width=0)

def insertImage(canvas):
    pic = canvas.data["image"]
    canvas.create_image(0,0,anchor=NW,image=pic)

def drawImage(canvas,selection,color,(leftX,leftY),(rightX,rightY)):
    width = canvas.data["width"]
    height = canvas.data["height"]
    if(selection=="None"):
        canvas.create_rectangle(0,0,width,height-100,fill=color,width=0)
    elif(selection=="Line"):
        canvas.create_line(leftX,leftY,rightX,rightY,fill=color,width=2)
    elif(selection=="Oval"):
        canvas.create_oval(leftX,leftY,rightX,rightY,fill=color,width=1)
    elif(selection=="Rectangle"):
        canvas.create_rectangle(leftX,leftY,rightX,rightY,fill=color,width=1)
    elif(selection=="Arc"):
        canvas.create_arc(leftX,leftY,rightX,rightY,style=ARC,outline=color,
                          start=180,extent=180,width=2)
    elif(selection=="Triangle"):
        canvas.create_polygon(leftX,rightY,rightX-(rightX-leftX)/2,leftY,
                              rightX,rightY,fill=color,width=1)
    elif(selection=="Pentagon"):
        canvas.create_polygon(leftX+(rightX-leftX)/4,rightY,leftX,
                              leftY+(rightY-leftY)/3,rightX-(rightX-leftX)/2,
                              leftY,rightX,leftY+(rightY-leftY)/3,
                              rightX-(rightX-leftX)/4,rightY,
                              fill=color,width=1)
    elif(selection=="image"):
        insertImage(canvas)
    elif(selection=="eraser"):
        drawEraser(canvas,leftX+25,leftY+25)

def drawPicture(canvas):
    undoList = canvas.data["undoList"]
    for element in range(len(undoList)):
        selection = undoList[element][0]
        color = undoList[element][1]
        (leftX,leftY) = undoList[element][2]
        (rightX,rightY) = undoList[element][3]
        drawImage(canvas,selection,color,(leftX,leftY),(rightX,rightY))

def drawSavedPic(canvas):
    loadSavedImage(canvas)
    savedList = canvas.data["savedList"]
    for element in range(len(savedList)):
        selection = savedList[element][0]
        color = savedList[element][1]
        (leftX,leftY) = savedList[element][2]
        (rightX,rightY) = savedList[element][3]
        drawImage(canvas,selection,color,(leftX,leftY),(rightX,rightY))

def drawInfo(canvas):
    width = canvas.data["width"]
    height = canvas.data["height"]
    info = """Thanks for using the modified paint program!\n\n
    This program has many basic features such as undo but lacks some
    such as fill.
    To draw any of the shapes, press the left mouse button and slide
    accross. The image will be created with the end location as the
    bottom right and the start location as the top left.
    When no shape is selected, this action results in a background color.
    Pressing "n" on the keyboard allows for no shape to be selected.
    Once a shape is drawn with a color, its color can't be changed.
    All actions can be undone. Pressing "u" on the keyboard undoes
    the last action.
    To use the eraser, press "e" on the keyboard. Only one square can
    be erased at one time.
    To insert an image, press "i" on the keyboard. The image can't be
    resized or relocated. The image must be a .gif file saved in the
    same folder as this program with the name "image.gif"
    To diplay a saved picture, press "l" on the keyboard. The image
    must be saved previously using the same program.
    To save a picture, press "s" on the keyboard. Images saved using
    this program can be reopened using only this program.
    Saving and loading previous images can't be undone.
    To exit the instructions, press "r" on the keyboard.\n\n
    Created By: Maitreyee Palkar [Fall 2010]"""
    canvas.create_rectangle(0,0,width,height,width=0,fill="pink")
    canvas.create_text(width/2,height/2,text=info,justify=CENTER,
                       font=("Times New Roman",15))

def drawColors(canvas):
    width = canvas.data["width"]
    height = canvas.data["height"]
    colors = canvas.data["colors"]
    leftX = width/1.65
    leftY = height-70
    rightX = width-50
    rightY = height-20
    canvas.create_rectangle(leftX,leftY,rightX,rightY,fill="white")    
    canvas.create_rectangle(leftX,leftY,rightX-5*(rightX-leftX)/6,rightY-(rightY-leftY)/2,
                       fill=colors[0][0])
    canvas.create_rectangle(rightX-(rightX-leftX)/6,leftY,rightX,rightY-(rightY-leftY)/2,
                       fill=colors[0][1])
    canvas.create_rectangle(rightX-2*(rightX-leftX)/6,leftY,rightX-(rightX-leftX)/6,rightY-(rightY-leftY)/2,
                       fill=colors[0][2])
    canvas.create_rectangle(rightX-3*(rightX-leftX)/6,leftY,rightX-2*(rightX-leftX)/6,rightY-(rightY-leftY)/2,
                       fill=colors[0][3])
    canvas.create_rectangle(rightX-4*(rightX-leftX)/6,leftY,rightX-3*(rightX-leftX)/6,rightY-(rightY-leftY)/2,
                       fill=colors[0][4])
    canvas.create_rectangle(rightX-5*(rightX-leftX)/6,leftY,rightX-4*(rightX-leftX)/6,rightY-(rightY-leftY)/2,
                       fill=colors[0][5])
    canvas.create_rectangle(leftX,rightY-(rightY-leftY)/2,rightX-5*(rightX-leftX)/6,rightY,
                       fill=colors[1][0])
    canvas.create_rectangle(rightX-(rightX-leftX)/6,rightY-(rightY-leftY)/2,rightX,rightY,
                       fill=colors[1][1])
    canvas.create_rectangle(rightX-2*(rightX-leftX)/6,rightY-(rightY-leftY)/2,rightX-(rightX-leftX)/6,rightY,
                       fill=colors[1][2])
    canvas.create_rectangle(rightX-3*(rightX-leftX)/6,rightY-(rightY-leftY)/2,rightX-2*(rightX-leftX)/6,rightY,
                       fill=colors[1][3])
    canvas.create_rectangle(rightX-4*(rightX-leftX)/6,rightY-(rightY-leftY)/2,rightX-3*(rightX-leftX)/6,rightY,
                       fill=colors[1][4])
    canvas.create_rectangle(rightX-5*(rightX-leftX)/6,rightY-(rightY-leftY)/2,rightX-4*(rightX-leftX)/6,rightY,
                       fill=colors[1][5])
    canvas.data["colorsLeftX"]=leftX
    canvas.data["colorsLeftY"]=leftY
    canvas.data["colorsRightX"]=rightX
    canvas.data["colorsRightY"]=rightY

def drawSelections(canvas):
    width = canvas.data["width"]
    height = canvas.data["height"]
    option = canvas.data["selection"]
    Fill = canvas.data["fill"]
    if(Fill!="black"):Color="black"
    else:Color="white"
    if(option!="None"):
        canvas.create_rectangle(width/2,height-70,width/1.75,
                                height-20,fill=Color)
        drawImage(canvas,option,Fill,((width/2)-.5,height-70-.5),
                  ((width/1.75)-.5,height-20-.5))
    else:
        canvas.create_rectangle(width/2,height-70,width/1.75,
                                height-20,fill=Fill)
        Text="Option:\n"+option
        textX = (width/2)+((width/1.75)-(width/2))/2
        textY = (height-70)+((height-20)-(height-70))/2
        canvas.create_text(textX,textY,justify=CENTER,text=Text,fill=Color)

def drawOptions(canvas):
    width = canvas.data["width"]
    height = canvas.data["height"]
    options = canvas.data["options"]
    leftX = width/5
    leftY = height-70
    rightX = width/2.15
    rightY = height-20
    canvas.create_rectangle(leftX,leftY,rightX,rightY,fill="yellow",width=2)
    canvas.create_line(rightX-(rightX-leftX)/3,leftY,rightX-(rightX-leftX)/3,
                       rightY,width=2)
    canvas.create_line(rightX-2*(rightX-leftX)/3,leftY,rightX-2*(rightX-leftX)/3,
                       rightY,width=2)
    canvas.create_line(leftX,rightY-(rightY-leftY)/2,rightX,rightY-(rightY-leftY)/2,
                       width=2)
    canvas.create_arc(leftX+5,leftY+5,rightX-2*(rightX-leftX)/3-5,rightY-(rightY-leftY)/2-5,
                      style=ARC,start=180,extent=180)
    canvas.create_text(leftX+20,leftY+5,anchor=NW,justify=CENTER,
                       text=options[0][0])
    canvas.create_text(rightX-2*(rightX-leftX)/3+10,leftY+5,anchor=NW,
                       justify=CENTER,text=options[0][1])
    canvas.create_text(rightX-(rightX-leftX)/3+10,leftY+5,anchor=NW,
                       justify=CENTER,text=options[0][2])
    canvas.create_text(leftX+10,rightY-(rightY-leftY)/2+5,anchor=NW,
                       justify=CENTER,text=options[1][0])
    canvas.create_text(rightX-2*(rightX-leftX)/3+10,rightY-(rightY-leftY)/2+5,
                       anchor=NW,justify=CENTER,text=options[1][1])
    canvas.create_text(rightX-(rightX-leftX)/3+10,rightY-(rightY-leftY)/2+5,
                       anchor=NW,justify=CENTER,text=options[1][2])
    canvas.data["optionLeftX"]=leftX
    canvas.data["optionLeftY"]=leftY
    canvas.data["optionRightX"]=rightX
    canvas.data["optionRightY"]=rightY

def drawButton(canvas):
    width = canvas.data["width"]
    height = canvas.data["height"]
    infoButtonLeftX = width/16
    infoButtonLeftY = height-70
    infoButtonRightX = width/6
    infoButtonRightY = height-20
    canvas.create_rectangle(infoButtonLeftX,infoButtonLeftY,infoButtonRightX,
                            infoButtonRightY,fill="gold")
    Text = "Click\nfor\nInstructions"
    canvas.create_text(infoButtonLeftX+10,infoButtonLeftY,
                       text=Text,anchor=NW,justify=CENTER)
    canvas.data["infoLeftX"]=infoButtonLeftX
    canvas.data["infoLeftY"]=infoButtonLeftY
    canvas.data["infoRightX"]=infoButtonRightX
    canvas.data["infoRightY"]=infoButtonRightY

def drawPaintArea(canvas):
    width = canvas.data["width"]
    height = canvas.data["height"]
    canvas.create_rectangle(0,0,width,height-100,fill="white",width=0)

def redrawAll(canvas):
    canvas.delete(ALL)
    if(canvas.data["infoFlag"]==False):
        drawPaintArea(canvas)
        drawButton(canvas)
        drawSelections(canvas)
        drawOptions(canvas)
        drawColors(canvas)
        if(canvas.data["loadSavedPic"]==True):
            drawSavedPic(canvas)
        drawPicture(canvas)
    else:
        drawInfo(canvas)

def init(canvas):
    canvas.data["undoList"]=[]
    canvas.data["selection"]="None"
    canvas.data["fill"]="white"
    canvas.data["infoFlag"]=False
    canvas.data["options"]=[["Arc","Triangle","Pentagon"],
                            ["Line","Oval","Rectangle"]]
    canvas.data["colors"]=[["black","red","pink","brown","blue","purple"],
                           ["white","yellow","orange","green","cyan","grey"]]
    canvas.data["motion"]=[(600,400)]
    pic = PhotoImage(file="image.gif")
    canvas.data["image"]=pic
    canvas.data["eraser"]=False
    canvas.data["savedList"]=[]
    canvas.data["loadSavedPic"]=False
    redrawAll(canvas)

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    root = Tk()
    Width = 800
    Height = 650
    canvas = Canvas(root, width=Width, height=Height,background="grey")
    canvas.pack()
    root.resizable(width=0, height=0) #makes it unresizeable
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    canvas.data["width"] = Width
    canvas.data["height"] = Height
    init(canvas)
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<B1-Motion>",motion)
    root.bind("<ButtonRelease-1>",release)
    root.bind("<Key>", keyPressed)
##    timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
