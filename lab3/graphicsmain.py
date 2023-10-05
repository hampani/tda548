from gamemodel import *
from graphics import *

class GameGraphics:
    def __init__(self, game):
        self.game = game

        # open the window
        self.win = GraphWin("Cannon game" , 640, 480, autoflush=False)
        self.win.setCoords(-110, -10, 110, 155)
        
        line = Line(Point(-110, 0), Point(110, 0))
        line.draw(self.win)

        self.draw_cannons = [self.drawCanon(0), self.drawCanon(1)]
        self.draw_scores  = [self.drawScore(0), self.drawScore(1)]
        self.draw_projs   = [None, None]
        self.draw_explosion = None

    def drawCanon(self,playerNr):
        player = self.game.getPlayers()[playerNr]
        cannonSize = self.game.getCannonSize()
        color = player.getColor()
        position = player.getX()

        cannon = Rectangle(Point(position - cannonSize / 2, 0), Point(position + cannonSize / 2, cannonSize))
        cannon.setFill(color)
        cannon.draw(self.win)

        return cannon

    def drawScore(self,playerNr):
        player = self.game.getPlayers()[playerNr]        
        position = player.getX()
        text = Text(Point(position, -5), f"Score: {player.getScore()}")
        text.draw(self.win)
    
        return text

    def fire(self, angle, vel):
        player = self.game.getCurrentPlayer()
        proj = player.fire(angle, vel)

        circle_X = proj.getX()
        circle_Y = proj.getY()


        if self.draw_projs[self.game.getCurrentPlayerNumber()] != None:
            self.draw_projs[self.game.getCurrentPlayerNumber()].undraw()

        circle = Circle(Point(player.getX(), self.game.getCannonSize() / 2), self.game.getBallSize())
        circle.setFill(player.getColor())
        circle.draw(self.win)
     

        while proj.isMoving():
            proj.update(1/50)

            # move is a function in graphics. It moves an object dx units in x direction and dy units in y direction
            circle.move(proj.getX() - circle_X, proj.getY() - circle_Y)

            circle_X = proj.getX()
            circle_Y = proj.getY()

            update(50)

        circle.undraw()
        return proj

    def updateScore(self,playerNr):
        player = self.game.getPlayers()[playerNr]
        self.draw_scores[playerNr].undraw()

        position = player.getX()
        text = Text(Point(position, -5), f"Score: {player.getScore()}")
        text.draw(self.win)

        self.draw_scores[playerNr] = text

    def play(self):
        while True:
            player = self.game.getCurrentPlayer()
            oldAngle,oldVel = player.getAim()
            wind = self.game.getCurrentWind()

            # InputDialog(self, angle, vel, wind) is a class in gamegraphics
            inp = InputDialog(oldAngle,oldVel,wind)
            # interact(self) is a function inside InputDialog. It runs a loop until the user presses either the quit or fire button
            if inp.interact() == "Fire!": 
                angle, vel = inp.getValues()
                inp.close()
            elif inp.interact() == "Quit":
                exit()
            
            player = self.game.getCurrentPlayer()
            other = self.game.getOtherPlayer()
            proj = self.fire(angle, vel)
            distance = other.projectileDistance(proj)

            if distance == 0.0:
                player.increaseScore()
                self.explode(other, player)
                self.updateScore(self.game.getCurrentPlayerNumber())
                self.game.newRound()

            self.game.nextPlayer()
    def explode(self, hitPlayer, shootingPlayer):
        position = hitPlayer.getX()

        radius = self.game.getBallSize()
        while radius < self.game.getCannonSize() * 2:
            circle = Circle(Point(position, self.game.getCannonSize() / 2), radius)
            circle.setFill(shootingPlayer.getColor())
            circle.draw(self.win)

            radius *= 1.1

            update(50)

            circle.undraw()

class InputDialog:
    def __init__ (self, angle, vel, wind):
        self.win = win = GraphWin("Fire", 200, 300)
        win.setCoords(0,4.5,4,.5)
        Text(Point(1,1), "Angle").draw(win)
        self.angle = Entry(Point(3,1), 5).draw(win)
        self.angle.setText(str(angle))
        
        Text(Point(1,2), "Velocity").draw(win)
        self.vel = Entry(Point(3,2), 5).draw(win)
        self.vel.setText(str(vel))
        
        Text(Point(1,3), "Wind").draw(win)
        self.height = Text(Point(3,3), 5).draw(win)
        self.height.setText("{0:.2f}".format(wind))
        
        self.fire = Button(win, Point(1,4), 1.25, .5, "Fire!")
        self.fire.activate()
        self.quit = Button(win, Point(3,4), 1.25, .5, "Quit")
        self.quit.activate()

    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    def getValues(self):
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        return a,v

    def close(self):
        self.win.close()


class Button:

    def __init__(self, win, center, width, height, label):

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0


GameGraphics(Game(11,3)).play()
