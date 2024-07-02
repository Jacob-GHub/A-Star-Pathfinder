import pygame

class Button():
    def __init__(self,x,y,image,scale):
        width=image.get_width()
        height=image.get_width()
        self.image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
    def draw(self,surface):
        surface.blit(self.image,(self.rect.x,self.rect.y))
    def wasClicked(self):
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            # print('button clicked')
            return True
        else:
            return False
    def collides(self):
        pos=pygame.mouse.get_pos()
        print(self.rect.collidepoint(pos))
        return (self.rect.collidepoint(pos))