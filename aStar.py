import pygame
import spritesheet
import button
from sys import exit
pygame.init()


screen_width=961
screen_height=780
SCREEN = pygame.display.set_mode((1200, 850),pygame.SRCALPHA)
SCREEN.fill('#463f3a')
BLACK=(0,0,0)
pygame.display.set_caption('A* Pathfinder')
clock = pygame.time.Clock()
font1=pygame.font.Font('font1/font1.ttf', 40)
font=pygame.font.Font('font1/font1.ttf', 50)

button_sheet_image=pygame.image.load('buttons/new_buttons.png').convert_alpha()
button_sheet=spritesheet.SpriteSheet(button_sheet_image)

reset_image=button_sheet.get_image(7,36,18,18,5,(BLACK))
reset_button=button.Button(600+20,20,reset_image,1)

start_image=button_sheet.get_image(7,4,18,18,5,(BLACK))
start_button=button.Button(600+20,750,start_image,1)

exit_image=button_sheet.get_image(39,36,18,18,5,(BLACK))
exit_button=button.Button(600-(10*9),750,exit_image,1)

back_image=button_sheet.get_image(39,4,18,18,5,(BLACK))
back_button=button.Button(600-(10*9),20,back_image,1)

home_image=pygame.image.load('pictures/intro.png').convert_alpha()
# home_image=pygame.transform.scale(home_image,(530,350))

home_image_1_1=pygame.image.load('pictures/1.1.png').convert_alpha()
home_image_1_2=pygame.image.load('pictures/1.2.png').convert_alpha()
home_image_1_3=pygame.image.load('pictures/1.3.png').convert_alpha()
home_image_1_4=pygame.image.load('pictures/1.4.png').convert_alpha()
home_image_2_1=pygame.image.load('pictures/2.1.png').convert_alpha()
home_image_2_2=pygame.image.load('pictures/2.2.png').convert_alpha()
home_image_2_3=pygame.image.load('pictures/2.3.png').convert_alpha()
home_image_2_4=pygame.image.load('pictures/2.4.png').convert_alpha()
home_image_3_1=pygame.image.load('pictures/3.1.png').convert_alpha()
home_image_3_2=pygame.image.load('pictures/3.2.png').convert_alpha()
home_image_3_3=pygame.image.load('pictures/3.3.png').convert_alpha()
home_image_3_4=pygame.image.load('pictures/3.4.png').convert_alpha()

home_image_1_1=pygame.transform.scale(home_image_1_1,(600,450))
home_image_1_2=pygame.transform.scale(home_image_1_2,(600,450))
home_image_1_3=pygame.transform.scale(home_image_1_3,(600,450))
home_image_1_4=pygame.transform.scale(home_image_1_4,(600,450))
home_image_2_1=pygame.transform.scale(home_image_2_1,(600,450))
home_image_2_2=pygame.transform.scale(home_image_2_2,(600,450))
home_image_2_3=pygame.transform.scale(home_image_2_3,(600,450))
home_image_2_4=pygame.transform.scale(home_image_2_4,(600,450))
home_image_3_1=pygame.transform.scale(home_image_3_1,(600,450))
home_image_3_2=pygame.transform.scale(home_image_3_2,(600,450))
home_image_3_3=pygame.transform.scale(home_image_3_3,(600,450))
home_image_3_4=pygame.transform.scale(home_image_3_4,(600,450))

home_images=[home_image_1_1,home_image_1_2,home_image_1_3,home_image_1_4,home_image_2_1,home_image_2_2,home_image_2_3,home_image_2_4,home_image_3_1,home_image_3_2,home_image_3_3,home_image_3_4]


class Tile(pygame.sprite.Sprite):
    def __init__(self,width,length,x,y):
        super().__init__()
        self.length=length
        self.width=width
        self.image=pygame.Surface((width,length))
        self.image.fill('#463f3a')
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.already_changed=False
        self.h=0
        self.g=0
        self.f=0
        self.predecessor=None
        #user-clicked tiles
        self.start_node=False
        self.end_node=False
        self.obstacle_node=False
        #neighboring tiles
        self.right_tile=None
        self.left_tile=None
        self.up_tile=None
        self.down_tile=None
        #neighboring diagonals
        self.north_east_tile=None
        self.south_east_tile=None
        self.north_west_tile=None
        self.south_west_tile=None
        pygame.draw.rect(self.image, ('#bcb8b1'), self.image.get_rect(), 2) #border
    def get_surrounding_tiles(self):
         #data for surrounding tiles
         self.right_x=self.rect.x+40
         self.right_y=self.rect.y

         self.left_x=self.rect.x-40
         self.left_y=self.rect.y

         self.up_y=self.rect.y-40
         self.up_x=self.rect.x

         self.down_y=self.rect.y+40
         self.down_x=self.rect.x

         self.north_e_x=self.rect.x+40
         self.north_e_y=self.rect.y-40

         self.south_e_x=self.rect.x+40
         self.south_e_y=self.rect.y+40

         self.north_w_x=self.rect.x-40
         self.north_w_y=self.rect.y-40
         
         self.south_w_x=self.rect.x-40
         self.south_w_y=self.rect.y+40   
         
         #for loop to find each neighboring tile
         for tile in grid:
            if tile.rect.x==self.right_x and tile.rect.y==self.right_y:
                self.right_tile=tile
            elif tile.rect.x==self.left_x and tile.rect.y==self.left_y:
                self.left_tile=tile
            elif tile.rect.x==self.up_x and tile.rect.y==self.up_y:
                self.up_tile=tile
            elif tile.rect.x==self.down_x and tile.rect.y==self.down_y:
                self.down_tile=tile
            elif tile.rect.x==self.north_e_x and tile.rect.y==self.north_e_y:
                self.north_east_tile=tile
            elif tile.rect.x==self.south_e_x and tile.rect.y==self.south_e_y:
                self.south_east_tile=tile
            elif tile.rect.x==self.north_w_x and tile.rect.y==self.north_w_y:
                self.north_west_tile=tile
            elif tile.rect.x==self.south_w_x and tile.rect.y==self.south_w_y:
                self.south_west_tile=tile
               
    def calculate_heuristics(self):
        global goal_tile
        self.dx = abs(self.rect.x - goal_tile.rect.x)
        self.dy = abs(self.rect.y - goal_tile.rect.y)
        h = 1 * (self.dx + self.dy) + (1.4 - 2 * 1) * min(self.dx, self.dy)
        self.h=h

    def calculate_g_cost(self):
        dx = abs(self.predecessor.rect.x-self.rect.x)
        dy = abs(self.predecessor.rect.y-self.rect.y)
        sum = 1 * (dx + dy) + (1.4 - 2 * 1) * min(dx,dy)
        self.g=sum
        pointer=self.predecessor
        while pointer.predecessor!=None:
            sum+=pointer.g
            pointer=pointer.predecessor
        return sum
        
grid=pygame.sprite.Group()

def draw_tiles(surface):
    grid.draw(surface)
    
def draw_borders():
    for tile in grid:
        pygame.draw.rect(tile.image, ('#bcb8b1'), tile.image.get_rect(), 2)

def instatiateTiles():
    for y in range(0,17):
        for x in range(0,24):
            tile=Tile(40,40,x*40+120,y*40+150)
            grid.add(tile)

def check_collision(xpos,ypos):
    for tile in grid:
        if tile.rect.collidepoint(xpos,ypos):
            return tile
    return None
def color_key_tiles(state,tile):
        if state==0:
            tile.image.fill('#ffe548')
            tile.start_node=True
        elif state==1:
            tile.image.fill((103,167,100))
            tile.end_node=True
        elif (state>1) and (tile.start_node==False) and (tile.end_node==False) and (tile.obstacle_node==False):
            tile.image.fill('#fdf8e1')
            tile.obstacle_node=True
    
def color_neighbors(map,visit_map,current_tile):
    for key in map:
        if (not(map[key]==None)) and (not(map[key] in visit_map)) and (not(map[key] in obstacle_group)):
            map[key].predecessor=current_tile
            map[key].image.fill((110,103,98))
            map[key].calculate_heuristics()
            curr_g_cost=map[key].calculate_g_cost()
            map[key].f=map[key].h+curr_g_cost
            # print(key,' :f = ',map[key].f,' = ',map[key].h,' + ',curr_g_cost)

def get_valid_tile(neighboring_tiles,visited):
    for key in neighboring_tiles:
        if neighboring_tiles[key]!=None and not(neighboring_tiles[key] in obstacle_group) and not(neighboring_tiles[key] in visited):
            # print('valid tile set to :',neighboring_tiles[key].rect.x,neighboring_tiles[key].rect.y)
            return neighboring_tiles[key]
    return None

def check_frontiers(current_lowest_tile,frontiers,visited):
    lowest_f = current_lowest_tile
    for tile in frontiers:
        if tile in visited:
            frontiers.remove(tile)
        else:
            if tile.f<current_lowest_tile.f :
                # print('theres a lower f cost in the frontier',tile.rect.x,tile.rect.y,'with : ',tile.f)
                if tile.f<lowest_f.f:
                    lowest_f=tile
    return lowest_f

def find_least_f(unvisited):
    lowest_f = unvisited[0]
    for tile in unvisited:
        if tile.f<lowest_f.f:
            lowest_f=tile
    # print('lowest f in unvisited : ', lowest_f.rect.x,lowest_f.rect.y, 'with f = ',lowest_f.f)
    return lowest_f

def show_path(current_tile):
    current_tile.image.fill('#89fc00')
    while current_tile.predecessor!=None and current_tile.predecessor.start_node!=True:
        current_tile.predecessor.image.fill('#89fc00')
        current_tile=current_tile.predecessor



def a_star_pathfind(current_tile):
    visited=[]
    unvisited=[]
    frontiers=[]
    unvisited.append(current_tile)

    while len(unvisited)>0:
        current_tile=find_least_f(unvisited)
        current_tile.get_surrounding_tiles()
        neighboring_tiles={
            'right':current_tile.right_tile,
            'left':current_tile.left_tile,
            'up':current_tile.up_tile,
            'down':current_tile.down_tile,
            'north_e':current_tile.north_east_tile,
            'south_e':current_tile.south_east_tile,
            'north_w':current_tile.north_west_tile,
            'south_w':current_tile.south_west_tile
        }
        color_neighbors(neighboring_tiles,visited,current_tile)

        current_lowest_tile=get_valid_tile(neighboring_tiles,visited)
        if current_lowest_tile==None:
            if(len(frontiers)>0):
                current_lowest_tile=frontiers[0]
                current_lowest_tile=check_frontiers(current_lowest_tile,frontiers,visited)
            else:
                return   
        elif current_lowest_tile==goal_tile:
            goal_tile.image.fill((103,167,100))
            # current_tile.image.fill((20,250,80))
            show_path(current_tile)
            return
        for key in neighboring_tiles:
            if not(neighboring_tiles[key]==None) and neighboring_tiles[key].f<current_lowest_tile.f and not(neighboring_tiles[key] in visited) and not(neighboring_tiles[key] in obstacle_group):
                current_lowest_tile=neighboring_tiles[key]
                if current_lowest_tile==goal_tile:
                    show_path(current_lowest_tile)
                    goal_tile.image.fill((103,167,100))
                    return
            if not(neighboring_tiles[key]==None) and not(neighboring_tiles[key] in visited) and not(obstacle_group.has(neighboring_tiles[key])) and not(neighboring_tiles[key] in frontiers):
                frontiers.append(neighboring_tiles[key])

        current_lowest_tile=check_frontiers(current_lowest_tile,frontiers,visited)
        # print('best_step = ' ,current_lowest_tile.rect.x,current_lowest_tile.rect.y)
        current_lowest_tile.image.fill((181,99,97))

        unvisited.remove(current_tile)
        visited.append(current_tile)
        current_tile=current_lowest_tile
        unvisited.append(current_tile)


start_tile=None
goal_tile=None
obstacle_group=pygame.sprite.Group()

def find_key_tiles():
    for tile in grid:
        if tile.start_node==True:
            global start_tile
            start_tile=tile
        elif tile.end_node==True:
            global goal_tile
            goal_tile=tile
        elif tile.obstacle_node==True:
            global obstacle_group
            obstacle_group.add(tile)

instatiateTiles()#create all tile sprites

start_message = font.render('Please click your starting point',True,'#f9dc5c')
start_message_rect = start_message.get_rect(center = (600,50))

goal_message = font.render('Please click your goal point',True,'#2b9348')
goal_message_rect = goal_message.get_rect(center = (600,50))

border_message = font.render('Please click to create your obstacle(s)',True,'#fdf8e1')
border_message_rect = border_message.get_rect(center = (600,50))

space_message = font.render('Press Space when ready to path-find',True,'#fdf8e1')
space_message_rect = space_message.get_rect(center = (600,50))

intro_message = font1.render('This is an A* path-finding visualization tool',True,'#fdf8e1')
intro_message_rect = intro_message.get_rect(center = (600,50))

intro_sub_message = font.render('You must select a start and goal point, represented by:',True,'#fdf8e1')
intro_sub_message_rect = intro_sub_message.get_rect(center = (600,120))

obs_message=font.render('You may also place multiple obstacles, represented by: ',True,'#fdf8e1')
obs_message_rect = obs_message.get_rect(center = (600,180))

def display_start_screen():
    SCREEN.fill(('#463f3a'))
    SCREEN.blit(home_image,(20,-5))
    # SCREEN.blit(intro_message,intro_message_rect)
    # SCREEN.blit(intro_sub_message,intro_sub_message_rect)
    # SCREEN.blit(obs_message,obs_message_rect)
    exit_button.draw(SCREEN)
    start_button.draw(SCREEN)

start_screen=True

# SCREEN.blit(start_message,start_message_rect)
back=False
clicks=0
path_found=False
restart=False
start_time=0
curr_image=0
tile_placing=False
while True:
    if restart:
        clicks=0
        # obstacle_group.clear()
        obstacle_group.empty()
        # grid.clear()
        grid.empty()
        instatiateTiles()
        start_tile=None
        goal_tile=None
        path_found=False
        restart=False
        tile_placing=True
        if back:
            tile_placing=False
            start_screen=True
            back=False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if (start_button.wasClicked()):
                start_screen=False
                tile_placing=True
            elif (exit_button.wasClicked()):
                pygame.quit()
                exit()
            elif (reset_button.wasClicked()):
                  restart=True
                  break
            elif (back_button.wasClicked()):
                restart=True
                back=True
                break
            elif tile_placing:
                xpos=(pygame.mouse.get_pos()[0])
                ypos=(pygame.mouse.get_pos()[1])
                key_tile=check_collision(xpos,ypos)
                if key_tile != None:
                    color_key_tiles(clicks,key_tile)
                    clicks+=1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and clicks>1:
            find_key_tiles()
            a_star_pathfind(start_tile)
            path_found=True
    if not(start_screen):
        SCREEN.fill('#463f3a')
        if path_found:
            reset_button.draw(SCREEN)
            back_button.draw(SCREEN)
        else:
            if clicks==0:
                SCREEN.blit(start_message,start_message_rect)
            elif clicks==1:
                SCREEN.blit(goal_message,goal_message_rect)
            elif clicks==2:
                SCREEN.blit(border_message,border_message_rect)
            elif clicks>2 and not(path_found):
                SCREEN.blit(space_message,space_message_rect)
    
        draw_tiles(SCREEN)
        draw_borders()
    else:
        start_time+=1
        if start_time>=60:
            curr_image+=1
            start_time=-1
        if curr_image>=12:
            curr_image=0
        display_start_screen()
        SCREEN.blit(home_images[curr_image],(550,220))
        tile_placing=False
    pygame.display.update()
    clock.tick(60)