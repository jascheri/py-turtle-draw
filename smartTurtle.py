class smartTurtle(Turtle):
    """
    smartTurtle extends the Turtle class with the ability to draw houses and a street of houses
    """
    
    def setHouseWidth(self, _houseWidth):
        """
        setHouseWidth() sets the default house width for the turtle
        """
        self.houseWidth = _houseWidth
    
    def makeRectangle(self, width, height):
        """
        makeRectangle() creates a rectangle from the current location of the turtle of the sizes specified in the paramaters
        """
        for i in range(0, 4):
            self.turnRight()
            if (i == 0) or (i == 2):
                self.forward(width)
            else:
                self.forward(height)
    
    def makeRoof(self, width):
        """
        makeRoof() adds a roof to the current position.  Must start at top left corner of the house
        """
        self.turn(30)
        self.forward(width)
        self.turn(120)
        self.forward(width)
    
    def makeHouse(self, width, height):
        """
        makeHouse() makes a house at the current position of specified width and height
        """
        self.makeRectangle(width, height)
        self.makeRoof(width)
    
    def makeStreet(self, x, y, numberOfHouses):
        """
        makeStreet() creates a street of houses starting at x, y 
        """
        self.penUp()
        self.moveTo(x,y)
        self.turn(0)
        for i in range(0, numberOfHouses):
            self.turn(int(0.0 - self.getHeading()))
            self.penUp()
            self.moveTo(int(x+(self.houseWidth*i)),y)
            self.penDown()
            self.makeHouse(self.houseWidth, self.houseWidth)

def createAStreet(_houseWidth, _houseYPos, _numberOfHouses):
    """
    createAStreet() creates a world, smartTurtle and a street of houses based on passed paramaters
    
    Paramaters:
        houseWidth: How wide the houses should be
        houseYPos: The Y position of the houses
        numberOfHouses: The number of houses that should display
    """
    #Calculates the width and height of the world to fit the houses appropriately.
    if _houseYPos < _houseWidth:
        _houseYPos = _houseWidth
    worldWidth = _numberOfHouses * _houseWidth
    worldHeight = _houseYPos + _houseWidth + 50
    
    myWorld = World(worldWidth, worldHeight)
    turtle = smartTurtle(myWorld)
    turtle.setHouseWidth(_houseWidth)
    turtle.makeStreet(0, _houseYPos, _numberOfHouses)

"""
Executes my program.  all 3 variables can be changed with successful results :)
Parameters: houseWidth, houseYPos, numberOfHouses
"""
#createAStreet(50, 100, 5)
#createAStreet(150, 100, 20)
createAStreet(150, 200, 10)






