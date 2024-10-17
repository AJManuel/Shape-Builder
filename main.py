from basemod import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


window = tk.Tk()
window.title('Shape Builder')
window.geometry("805x500")
# newShape = Shape('dodecahedron', 'rouge')
# print(newShape.get_colour())

allShapes = ['Sphere','Cone','Cylinder','Triangular Pyramid','Triangular Prism','Square Based Pyramid', 'Torus']
allColours = ['Red', 'Blue', 'Green']

allShapeLabel = tk.Label(master=window, text='Shapes:')
allShapeLabel.grid(column=0,row=0)
allShapeChoices = ttk.Combobox(master=window, values=allShapes)
allShapeChoices.grid(column=1,row=0)

allColourLabel = tk.Label(master=window, text='Colours:')
allColourLabel.grid(column=2, row=0)
allColourChoices = ttk.Combobox(master=window, values=allColours)
allColourChoices.grid(column=3, row=0)



def side0ShapePage():
    radiusText = tk.Label(master=window, text='Radius')
    radiusText.grid(row=2, column=0)

    radiusBox = tk.Entry(master=window, text='test')
    radiusBox.grid(row=3, column=0)

    xCoordText = tk.Label(master=window, text='X Coordinate')
    xCoordText.grid(row=5, column=0)
    xCoordBox = tk.Entry(master=window)
    xCoordBox.grid(row=6, column=0)

    yCoordText = tk.Label(master=window, text='Y Coordinate')
    yCoordText.grid(row=5, column=1)
    yCoordBox = tk.Entry(master=window)
    yCoordBox.grid(row=6, column=1)

    zCoordText = tk.Label(master=window, text='Z Coordinate')
    zCoordText.grid(row=5, column=2)
    zCoordBox = tk.Entry(master=window)
    zCoordBox.grid(row=6, column=2)

    def runShape():
        theColour = allColourChoices.get()
        try:    
            theRadius = float(radiusBox.get())
        except ValueError:
            theRadius = 1
        
        try:
            theXCoord = float(xCoordBox.get())
        except ValueError:
            theXCoord = 0

        try:
            theYCoord = float(yCoordBox.get())
        except ValueError:
            theYCoord = 0

        try: 
            theZCoord = float(zCoordBox.get())
        except ValueError:
            theZCoord = 0
        
        shaping = side0Shape('Sphere',theColour, theRadius, theXCoord, theYCoord, theZCoord)

        getTypeLabelTitle = tk.Label(master=window, text=(f'Type: {shaping.get_type()}'))
        getTypeLabelTitle.grid(row=8, column=0)

        shaping.draw_shape()
        window.destroy()



    drawButton = tk.Button(master=window, text='draw', command=runShape)
    drawButton.grid(row=7, column=0)

def side2ShapePage():
    radiusText = tk.Label(master=window, text='Radius')
    radiusText.grid(row=2, column=0)

    radiusBox = tk.Entry(master=window, text='test')
    radiusBox.grid(row=3, column=0)

    heightText = tk.Label(master=window, text='Height')
    heightText.grid(row=2, column=1)

    heightBox = tk.Entry(master=window, text='tst')
    heightBox.grid(row=3, column=1)

    xCoordText = tk.Label(master=window, text='X Coordinate')
    xCoordText.grid(row=5, column=0)
    xCoordBox = tk.Entry(master=window)
    xCoordBox.grid(row=6, column=0)

    yCoordText = tk.Label(master=window, text='Y Coordinate')
    yCoordText.grid(row=5, column=1)
    yCoordBox = tk.Entry(master=window)
    yCoordBox.grid(row=6, column=1)

    zCoordText = tk.Label(master=window, text='Z Coordinate')
    zCoordText.grid(row=5, column=2)
    zCoordBox = tk.Entry(master=window)
    zCoordBox.grid(row=6, column=2)

    def runShape():
        try:
            theRadius = float(radiusBox.get())
        except ValueError:
            theRadius = 1
        
        try: 
            theHeight = float(heightBox.get())
        except ValueError:
            theHeight = 1

        theColour = allColourChoices.get()
        try:
            theXCoord = float(xCoordBox.get())
        except ValueError:
            theXCoord = 0

        try:
            theYCoord = float(yCoordBox.get())
        except ValueError:
            theYCoord = 0

        try: 
            theZCoord = float(zCoordBox.get())
        except ValueError:
            theZCoord = 0

        shaping = side2Shape('Generalized Cone',theColour, theRadius, theHeight, theXCoord, theYCoord, theZCoord)

        getTypeLabelTitle = tk.Label(master=window, text=(f'Type: {shaping.get_type()}'))
        getTypeLabelTitle.grid(row=8, column=0)

        shaping.draw_shape()
        window.destroy()

    drawButton = tk.Button(master=window, text='draw', command=runShape)
    drawButton.grid(row=7, column=0)

def side3ShapePage():
    radiusText = tk.Label(master=window, text='Radius')
    radiusText.grid(row=2, column=0)

    radiusBox = tk.Entry(master=window, text='test')
    radiusBox.grid(row=3, column=0)

    heightText = tk.Label(master=window, text='Height')
    heightText.grid(row=2, column=1)

    heightBox = tk.Entry(master=window, text='tst')
    heightBox.grid(row=3, column=1)

    xCoordText = tk.Label(master=window, text='X Coordinate')
    xCoordText.grid(row=5, column=0)
    xCoordBox = tk.Entry(master=window)
    xCoordBox.grid(row=6, column=0)

    yCoordText = tk.Label(master=window, text='Y Coordinate')
    yCoordText.grid(row=5, column=1)
    yCoordBox = tk.Entry(master=window)
    yCoordBox.grid(row=6, column=1)

    zCoordText = tk.Label(master=window, text='Z Coordinate')
    zCoordText.grid(row=5, column=2)
    zCoordBox = tk.Entry(master=window)
    zCoordBox.grid(row=6, column=2)

    def runShape():
        try:
            theRadius = float(radiusBox.get())
        except ValueError:
            theRadius = 1
        
        try:
            theHeight  = float(heightBox.get())
        except ValueError:
            theHeight = 1
        
        theColour = allColourChoices.get()

        try:
            theXCoord = float(xCoordBox.get())
        except ValueError:
            theXCoord = 0

        try:
            theYCoord = float(yCoordBox.get())
        except ValueError:
            theYCoord = 0

        try: 
            theZCoord = float(zCoordBox.get())
        except ValueError:
            theZCoord = 0
        shaping = side3Shape('Cylinder',theColour, theRadius, theHeight, theXCoord, theYCoord, theZCoord)

        getTypeLabelTitle = tk.Label(master=window, text=(f'Type: {shaping.get_type()}'))
        getTypeLabelTitle.grid(row=8, column=0)

        shaping.draw_shape()
        window.destroy()

    drawButton = tk.Button(master=window, text='draw', command=runShape)
    drawButton.grid(row=7, column=0)


def side4ShapePage():
    edgeText = tk.Label(master=window, text='Edge')
    edgeText.grid(row=2, column=0)

    edgeBox = tk.Entry(master=window, text='test')
    edgeBox.grid(row=3, column=0)

    xCoordText = tk.Label(master=window, text='X Coordinate')
    xCoordText.grid(row=5, column=0)
    xCoordBox = tk.Entry(master=window)
    xCoordBox.grid(row=6, column=0)

    yCoordText = tk.Label(master=window, text='Y Coordinate')
    yCoordText.grid(row=5, column=1)
    yCoordBox = tk.Entry(master=window)
    yCoordBox.grid(row=6, column=1)

    zCoordText = tk.Label(master=window, text='Z Coordinate')
    zCoordText.grid(row=5, column=2)
    zCoordBox = tk.Entry(master=window)
    zCoordBox.grid(row=6, column=2)

    def runShape():
        try:
            theRadius = float(edgeBox.get())
        except ValueError:
            theRadius = 1

        theColour = allColourChoices.get()

        try:
            theXCoord = float(xCoordBox.get())
        except ValueError:
            theXCoord = 0

        try:
            theYCoord = float(yCoordBox.get())
        except ValueError:
            theYCoord = 0

        try: 
            theZCoord = float(zCoordBox.get())
        except ValueError:
            theZCoord = 0
        shaping = side4Shape('Triangular Pyramid',theColour, theRadius, theXCoord, theYCoord, theZCoord)

        getTypeLabelTitle = tk.Label(master=window, text=(f'Type: {shaping.get_type()}'))
        getTypeLabelTitle.grid(row=8, column=0)

        shaping.draw_shape()
        window.destroy()

    drawButton = tk.Button(master=window, text='draw', command=runShape)
    drawButton.grid(row=7, column=0)

def side5ShapePrismPage():
    sideLengthText = tk.Label(master=window, text='Triangle Length')
    sideLengthText.grid(row=2, column=0)

    sideLengthBox = tk.Entry(master=window, text='test')
    sideLengthBox.grid(row=3, column=0)

    heightText = tk.Label(master=window, text='Height')
    heightText.grid(row=2, column=1)

    heightBox = tk.Entry(master=window, text='tst')
    heightBox.grid(row=3, column=1)

    lengthText = tk.Label(master=window, text="Rectangle Length")
    lengthText.grid(row=2, column=2)

    lengthBox = tk.Entry(master=window, text='fsdsdfg')
    lengthBox.grid(row=3,column=2)

    baseAreaText = tk.Label(master=window, text='Base Area')
    baseAreaText.grid(row=2, column=3)

    baseAreaBox = tk.Entry(master=window, text='sdfs')
    baseAreaBox.grid(row=3, column=3)

    xCoordText = tk.Label(master=window, text='X Coordinate')
    xCoordText.grid(row=5, column=0)
    xCoordBox = tk.Entry(master=window)
    xCoordBox.grid(row=6, column=0)

    yCoordText = tk.Label(master=window, text='Y Coordinate')
    yCoordText.grid(row=5, column=1)
    yCoordBox = tk.Entry(master=window)
    yCoordBox.grid(row=6, column=1)

    zCoordText = tk.Label(master=window, text='Z Coordinate')
    zCoordText.grid(row=5, column=2)
    zCoordBox = tk.Entry(master=window)
    zCoordBox.grid(row=6, column=2)

    def runShape():
        try: 
            theSideLength = float(sideLengthBox.get())
        except ValueError:
            theSideLength = 1
        
        try:
            theHeight  = float(heightBox.get())
        except ValueError:
            theHeight = 1

        try:   
            theRectangleLength = float(lengthBox.get())
        except ValueError:
            theRectangleLength = 1

        try:
            theBaseArea = float(baseAreaBox.get())
        except ValueError:
            theBaseArea = 1

        theColour = allColourChoices.get()
        try:
            theXCoord = float(xCoordBox.get())
        except ValueError:
            theXCoord = 0

        try:
            theYCoord = float(yCoordBox.get())
        except ValueError:
            theYCoord = 0

        try: 
            theZCoord = float(zCoordBox.get())
        except ValueError:
            theZCoord = 0
        shaping = side5ShapePrism('Triangular Prism',theColour, theSideLength, theRectangleLength, theBaseArea, theHeight, theXCoord, theYCoord, theZCoord)

        getTypeLabelTitle = tk.Label(master=window, text=(f'Type: {shaping.get_type()}'))
        getTypeLabelTitle.grid(row=8, column=0)

        shaping.draw_shape()
        window.destroy()

    drawButton = tk.Button(master=window, text='draw', command=runShape)
    drawButton.grid(row=7, column=0)

def side5ShapePyramidPage():
    baseEdgeText = tk.Label(master=window, text='Base Edge Length')
    baseEdgeText.grid(row=2, column=0)

    baseEdgeBox = tk.Entry(master=window, text='test')
    baseEdgeBox.grid(row=3, column=0)

    heightText = tk.Label(master=window, text='Height')
    heightText.grid(row=2, column=1)

    heightBox = tk.Entry(master=window, text='tst')
    heightBox.grid(row=3, column=1)

    xCoordText = tk.Label(master=window, text='X Coordinate')
    xCoordText.grid(row=5, column=0)
    xCoordBox = tk.Entry(master=window)
    xCoordBox.grid(row=6, column=0)

    yCoordText = tk.Label(master=window, text='Y Coordinate')
    yCoordText.grid(row=5, column=1)
    yCoordBox = tk.Entry(master=window)
    yCoordBox.grid(row=6, column=1)

    zCoordText = tk.Label(master=window, text='Z Coordinate')
    zCoordText.grid(row=5, column=2)
    zCoordBox = tk.Entry(master=window)
    zCoordBox.grid(row=6, column=2)

    def runShape():
        try:
            theEdge = float(baseEdgeBox.get())
        except ValueError:
            theEdge = 1
        
        try:
            theHeight  = float(heightBox.get())
        except ValueError:
            theHeight = 1

        try:
            theXCoord = float(xCoordBox.get())
        except ValueError:
            theXCoord = 0

        try:
            theYCoord = float(yCoordBox.get())
        except ValueError:
            theYCoord = 0

        try: 
            theZCoord = float(zCoordBox.get())
        except ValueError:
            theZCoord = 0
        theColour = allColourChoices.get()
        shaping = side5ShapePyramid('Square Based Pyramid',theColour, theEdge, theHeight, theXCoord, theYCoord, theZCoord)

        getTypeLabelTitle = tk.Label(master=window, text=(f'Type: {shaping.get_type()}'))
        getTypeLabelTitle.grid(row=8, column=0)

        shaping.draw_shape()
        window.destroy()

    drawButton = tk.Button(master=window, text='draw', command=runShape)
    drawButton.grid(row=7, column=0)

def torusPage():
    minorRadiusText = tk.Label(master=window, text='Minor Radius')
    minorRadiusText.grid(row=2, column=0)

    minorRadiusBox = tk.Entry(master=window, text='test')
    minorRadiusBox.grid(row=3, column=0)

    majorRadiusText = tk.Label(master=window, text='Major Radius')
    majorRadiusText.grid(row=2, column=1)

    majorRadiusBox = tk.Entry(master=window, text='tst')
    majorRadiusBox.grid(row=3, column=1)

    xCoordText = tk.Label(master=window, text='X Coordinate')
    xCoordText.grid(row=5, column=0)
    xCoordBox = tk.Entry(master=window)
    xCoordBox.grid(row=6, column=0)

    yCoordText = tk.Label(master=window, text='Y Coordinate')
    yCoordText.grid(row=5, column=1)
    yCoordBox = tk.Entry(master=window)
    yCoordBox.grid(row=6, column=1)

    zCoordText = tk.Label(master=window, text='Z Coordinate')
    zCoordText.grid(row=5, column=2)
    zCoordBox = tk.Entry(master=window)
    zCoordBox.grid(row=6, column=2)

    def runShape():
        try:
            theMajor = float(minorRadiusBox.get())
        except ValueError:
            theMajor = 2

        try:
            theMinor  = float(majorRadiusBox.get())
        except ValueError:
            theMinor = 1
        try:
            theXCoord = float(xCoordBox.get())
        except ValueError:
            theXCoord = 0

        try:
            theYCoord = float(yCoordBox.get())
        except ValueError:
            theYCoord = 0

        try: 
            theZCoord = float(zCoordBox.get())
        except ValueError:
            theZCoord = 0
        theColour = allColourChoices.get()
        shaping = torusShape('Torus',theColour, theMajor, theMinor, theXCoord, theYCoord, theZCoord)

        getTypeLabelTitle = tk.Label(master=window, text=(f'Type: {shaping.get_type()}'))
        getTypeLabelTitle.grid(row=8, column=0)

        shaping.draw_shape()
        window.destroy()

    drawButton = tk.Button(master=window, text='draw', command=runShape)
    drawButton.grid(row=7, column=0)

def checkShape():
    currentShape = allShapeChoices.get()
    currentColour = allColourChoices.get()
    if currentShape == 'Sphere' and (currentColour == 'Red' or currentColour == 'Blue' or currentColour == 'Green'):
        side0ShapePage()
    elif currentShape == 'Cone' and (currentColour == 'Red' or currentColour == 'Blue' or currentColour == 'Green'):
        side2ShapePage()
    elif currentShape == 'Cylinder' and (currentColour == 'Red' or currentColour == 'Blue' or currentColour == 'Green'):
        side3ShapePage()
    elif currentShape == 'Triangular Pyramid' and (currentColour == 'Red' or currentColour == 'Blue' or currentColour == 'Green'):
        side4ShapePage()
    elif currentShape == 'Triangular Prism' and (currentColour == 'Red' or currentColour == 'Blue' or currentColour == 'Green'):
        side5ShapePrismPage()
    elif currentShape == 'Square Based Pyramid' and (currentColour == 'Red' or currentColour == 'Blue' or currentColour == 'Green'):
        side5ShapePyramidPage()
    elif currentShape == 'Torus' and (currentColour == 'Red' or currentColour == 'Blue' or currentColour == 'Green'):
        torusPage()
    else: 
        messagebox.showinfo("ERROR", "Thats not what I asked")

submitShapeChoice = tk.Button(master=window, text='submit', command=checkShape)
submitShapeChoice.grid(column=0, row=1)

window.mainloop()