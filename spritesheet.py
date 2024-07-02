import pygame

class SpriteSheet():
    def __init__(self,image):
        self.sheet = image
    
    def get_image(self,x,y,width,height,scale,color):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet,(0,0),(x,y,width,height))
        image=pygame.transform.scale(image,(width*scale,height*scale))
        image.set_colorkey(color)

        return image