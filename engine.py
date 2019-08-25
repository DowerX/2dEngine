import math

class Vector2():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Circle():
    def __init__(self, radius=1, center=Vector2(x=0, y=0)):
        self.radius = radius
        self.center = center

class Drawable():
    def __init__(self, function, resources={}, id=None):
        self.function = function
        self.resources = resources

    def draw(self):
        self.function()

class Collider():
    def __init__(self, type, rect=None, circle=None, callbacks=[], id=None):
        self.id = id
        self.rect = rect
        self.circle = circle
        self.callbacks = callbacks

    def collision(self, other):
        for func in self.callbacks:
            func(self, other)

    def callcallbacks(self, other):
        for func in self.callbacks:
            func(other)

        for func in other.callbacks:
            func(self)

    def check(self, other):
        if not self.rect == None:
            if not other.rect == None:
                self.rectcheck(other)
            else:
                self.mixedcheck(other)
        else:
            if not other.rect == None:
                self.mixedcheck(other)
            else:
                self.circlecheck(other)

    def rectcheck(self, other):
        if (self.rect.x < other.rect.x + other.rect.width and
            self.rect.x + self.rect.width > other.rect.x and
            self.rect.y < other.rect.y + other.rect.height and
            self.rect.y + self.rect.height > other.rect.y):

            self.callcallbacks(other)

            return True
        else:
            return False

    def mixedcheck(self, other):
        pass
    
    def circlecheck(self, other):
        dx = self.circle.center.x - other.circle.center.x
        dy = self.circle.center.y - other.circle.center.y

        if math.sqrt(dx * dx + dy * dy) < self.circle.radius + other.circle.radius:
            self.callcallbacks(other)
            return True
        else:
            return False