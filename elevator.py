#!/usr/bin/env python

"""
This is the control system for an elevator. The elevator class implements graphically
the movement of an elevator in the 5 floors building.

"""

import pygame, sys
from pygame import display, draw, event, mouse, Surface
from pygame.locals import *
import threading

    
#our game object class
class elevator:
    inc = 0
    num_pisos = 5
    door_state = "open"
    index_img = 0
    images =["ascensor_a.png","ascensor_2.png","ascensor_1.png","ascensor_c.png"]
    c_blanco = (255, 255,255)  #blanco
    c_verde = (128, 255,128)    #verde
    cont =0;
    button_ext = 0
    button_int = 0
    last_floor = 0

    def __move_and_draw_all_game_objects(self):
        # mueve el ascensor
        if self.motor != "stop" or self.door_state == "closing" or self.door_state == "opening":
            self.screen.blit(self.background, (0, 0))
            self.position = self.position.move(0,self.inc)
            self.screen.blit(self.ascensor, self.position)
        # control de puertas
        if self.door_state == "closing":
            self.cont+=1
            if self.cont % 10 == 0:
                if self.index_img < 3:
                    self.index_img = self.index_img +1
                    self.ascensor = pygame.image.load(self.images[self.index_img]).convert()
                else:
                    self.door_state = "close"
        elif self.door_state == "opening":
            self.cont+=1
            if self.cont % 10 == 0:
                if self.index_img >0:
                    self.index_img = self.index_img -1
                    self.ascensor = pygame.image.load(self.images[self.index_img]).convert()
                else:
                    self.door_state = "open"
        pygame.display.update()
        pygame.time.delay(50)
        

    def destroy(self):
        pygame.quit()
        sys.exit()
            
    def __init__(self, caption):
        pygame.init()
        self.screen = pygame.display.set_mode((1024,768), pygame.FULLSCREEN)
        pygame.display.set_caption(caption)
        self.background = pygame.image.load('edificio.png').convert()
        self.screen.blit(self.background, (0, 0))        #draw the background
        self.ascensor = pygame.image.load(self.images[self.index_img]).convert()
        self.position = self.ascensor.get_rect()
        self.position = self.position.move(155,650)
        self.screen.blit(self.ascensor, self.position)
        #Botonera
        self.botonera = pygame.image.load('botonera.png').convert()
        self.screen.blit(self.botonera, (770, 5))
        #Botones de piso
        for x in range(0,5):
            draw.circle(self.screen, (255, 255,255), (817, 720-x*58), 13)
            font = pygame.font.SysFont("comicsansms", 30)
            text = font.render(("F"+str(x+1)), True, (255, 255,255))
            #rect = text.rect()
            #screen.fill((255, 255, 255))
            self.screen.blit(text, (850, 700-x*58))

        #numero de piso
        self.set_floor_indicator(0)
            
        self.buttons = [False] * self.num_pisos

        #indicadores
        self.set_mov_indicator("stop")
        
        #init
        self.motor = "stop"
        self.inc = 0
        pygame.display.update()
        '''threads = list()
        t = threading.Thread(target=self.execute)
        threads.append(t)
        t.start()'''


    #Public function
    def set_motor(self, mov):
        if mov == "up":
            self.inc = -1
        elif mov == "down":
            self.inc = 1
        elif mov == "stop":
            self.inc = 0
        else:
            return
        self.motor = mov

    def get_motor(self):
        return self.motor

    def set_door(self, state):
        if (self.door_state == "close") and (state == "open"):
            self.door_state = "opening"
        elif (self.door_state == "open") and (state == "close"):
            self.door_state = "closing"

    def get_door(self):
        return self.door_state
        
    def get_floor(self):
        piso =(650 - self.position.top)/156.0
        return piso+1

    def set_floor_indicator(self, floor):
        if floor == self.last_floor:
            return
        font = pygame.font.SysFont("consolas", 70)
        text = font.render(str(floor), True, (128, 255,128))
        rect = ((0, 0),(100,70))
        bg_text = self.botonera.subsurface(rect)
        self.screen.blit(bg_text, (770, 5))
        self.screen.blit(text, (805, 20))
        self.last_floor = floor

    def set_mov_indicator(self, mov):
        if mov == "stop":
            triangle_up = pygame.draw.polygon(self.screen,self.c_blanco,[(974, 24), (951, 44), (998, 44)],0)
            triangle_down = pygame.draw.polygon(self.screen,self.c_blanco,[(974, 76), (951, 58), (998, 58)],0)
        elif mov == "up":
            triangle_up = pygame.draw.polygon(self.screen,self.c_verde,[(974, 24), (951, 44), (998, 44)],0)
        elif mov == "down":
            triangle_down = pygame.draw.polygon(self.screen,self.c_verde,[(974, 76), (951, 58), (998, 58)],0)

    def get_button_call(self):
        state = self.button_ext
        self.button_ext = 0
        return state

    def get_button_int(self):
        state = self.button_int
        self.button_int = 0
        return state

    def set_light_call(self, key, state):
        key = key-1
        if key < 0 or key > 4:
            return
        if state == "off":
            draw.circle(self.screen, self.c_blanco, (817, 720-key*58), 13)
        elif state == "on":
            draw.circle(self.screen, self.c_verde, (817, 720-key*58), 13)

    def set_light_int(self, key, state):
        key = key-1
        if key < 0 or key > 4:
            return
        if state == "off":
            draw.circle(self.screen, self.c_blanco, (820, 349-key*58), 13)
        elif state == "on":
            draw.circle(self.screen, self.c_verde, (820, 349-key*58), 13)  
        

    def execute(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                 pygame.quit()
                 sys.exit()
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = mouse.get_pos()
            #print (mouse_pos)
            for x in range(0,5):
                rect1 = pygame.Rect(800,327-x*58,39,38)
                rect2 = pygame.Rect(800,707-x*58,39,38)
                if rect1.collidepoint(mouse_pos) == True:
                    self.button_int = x+1
                elif rect2.collidepoint(mouse_pos) == True:
                    self.button_ext = x+1
            
        
        if( pygame.key.get_pressed()[pygame.K_F1] != 0 ):
            self.button_ext = 1
        elif( pygame.key.get_pressed()[pygame.K_F2] != 0 ):
            self.button_ext = 2
        elif( pygame.key.get_pressed()[pygame.K_F3] != 0 ):
            self.button_ext = 3
        elif( pygame.key.get_pressed()[pygame.K_F4] != 0 ):
            self.button_ext = 4
        elif( pygame.key.get_pressed()[pygame.K_F5] != 0 ):
            self.button_ext = 5
        elif( pygame.key.get_pressed()[pygame.K_1] != 0 ):
            self.button_int = 1
        elif( pygame.key.get_pressed()[pygame.K_2] != 0 ):
            self.button_int = 2
        elif( pygame.key.get_pressed()[pygame.K_3] != 0 ):
            self.button_int = 3
        elif( pygame.key.get_pressed()[pygame.K_4] != 0 ):
            self.button_int = 4
        elif( pygame.key.get_pressed()[pygame.K_5] != 0 ):
            self.button_int = 5
        elif( pygame.key.get_pressed()[pygame.K_ESCAPE] != 0 ):
            pygame.quit()
            sys.exit()
        self.__move_and_draw_all_game_objects()
        
        
        


