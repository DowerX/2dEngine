import pygame
from pygame.locals import *
from engine import *

#TODO: finish Game.checkcollisions() (currently it would check twice per frame resulting in two callbacks for both colliders)

class Game():

    frameevents = []
    done = False

    drawables = {}
    colliders = {}

    def __init__(self, name="New Game", windowrect=Vector2(x=800, y=600), 
                fillcolor=pygame.Color(255, 255, 255, 255), clearframe=True):
        self.name = name
        self.fillcolor = fillcolor
        self.windowrect = windowrect
        self.clearframe = clearframe
        self.clock = pygame.time.Clock()
        pygame.init()
        self.screen = pygame.display.set_mode((windowrect.width, windowrect.height), DOUBLEBUF)
        pygame.display.set_caption(name)

    def __del__(self):
        pygame.quit()
        del self

    def mainloop(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.done = True
                    return

            for func in self.frameevents:
                func()

            self.drawframe()
            self.clock.tick()
            pygame.time.wait(10)

    def drawframe(self):
        if self.clearframe:
            self.screen.fill(self.fillcolor, rect=self.windowrect)

        for drawable in self.drawables:
            drawable.draw()

        pygame.display.flip()

    def addframeevent(self, handler):
        self.frameevents.append(handler)

    def removeframeevent(self, handler=None, index=0):
        try:
            if handler == None:
                self.frameevents.remove(self.frameevents[index])
            else:
                self.frameevents.remove()
            return True
        except:
            return False

    def checkcollisions(self):
        for k, v in self.colliders.items():
            for q, w in self.colliders.items():
                if k == w:
                    pass
                else:
                    v.check(w)

#Testing:
if __name__ == "__main__":
    game = Game(name="test", windowrect=pygame.Rect(0,0,1280,720), fillcolor=pygame.Color(150,30,45,255), clearframe=True)

    def title_fps():
        pygame.display.set_caption(f"{game.name} FPS:{int(game.clock.get_fps())}")

    game.addframeevent(title_fps)
    game.mainloop()