from pygame import *
from random import randint
mixer.init()
mixer.music.load('song.mp3')
mixer.music.play()
wn = display.set_mode((700,500))
clock = time.Clock()
display.set_caption("Шутер")
background = transform.scale(image.load("сіній сіній.png"),(700,500))
background_kill = transform.scale(image.load("огурец убійцо.jpg"),(700,500))
background_2 = transform.scale(image.load("оранжевій.jpg"),(700,500))

FPS = 60
font.init()
font1 = font.Font(None,36)
score = 0

lose = 0
class GameSprite(sprite.Sprite):
    def __init__(self,pl_image,pl_x,pl_y,size_x,size_y,pl_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(pl_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
        self.speed = pl_speed
        self.size_x = size_x
    def reset(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    
    def update(self):
        keys = key.get_pressed()
        #[K_a,K_k]
        #назва списку[номер елементу]
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700 - self.size_x:
            self.rect.x += self.speed
class Enemy(GameSprite):
    def update(self):
        global lose

        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -50
            self.rect.x = randint(80,620)
            self.speed = randint(1,5)

game = True
finish = False

pirat= Player("ДЖЕК.png",300,320,80,180,5)

skymbrias = sprite.Group()
skymbria = Enemy("СКУМБРІЯ.png",30,30,80,80,3)
skymbrias.add(skymbria)


gymynkul= Enemy("гумункул.png",300,330,160,380,3)

ogyrogs = sprite.Group()
ogyrog=Enemy("огурок.png",30,320,80,80,3)
ogyrogs.add(ogyrog)


taburets = sprite.Group()
taburet=Enemy("табурет-removebg-preview.png",100,0,80,80,3)
taburets.add(taburet)

pityxs = sprite.Group()
pityx=Enemy("петух-removebg-preview (2).png",100,0,80,80,3)
pityxs.add(pityx)
pityx=Enemy("петух-removebg-preview (2).png",100,0,80,80,3)
pityxs.add(pityx)
level1 =1
level2 = 0 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        # elif e.type == KEYDOWN:
        #     if e.key == K_SPACE:
        #         rocket.fire()
    if  level1:
        wn.blit(background,(0,0))
        text_score = font1.render("скумрія: " + str(score),1,(255,255,255))
        wn.blit(text_score,(10,20))
        text_lose = font1.render("огурок: " + str(lose),1,(255,255,255))
        wn.blit(text_lose,(10,50))
        pirat.reset()
        pirat.update()
        gymynkul.reset()
        skymbria.reset()
        skymbria.update()
        ogyrog.reset()
        ogyrog.update()
   

        collis_fish = sprite.spritecollide(pirat,skymbrias,True)
        if collis_fish:
            skymbria = Enemy("СКУМБРІЯ.png",randint(80,620),-30,80,80,3)
            skymbrias.add(skymbria)
            score +=1

        collis_ogyrog = sprite.spritecollide(pirat,ogyrogs,True)
        if collis_ogyrog:
            ogyrog=Enemy("огурок.png",randint(80,620),-30,80,80,3)
            ogyrogs.add(ogyrog)
            lose += 1

        if lose > 3:
            wn.blit(background_kill,(0,0))
        if score > 0:
            level1 = 0 
            level2 = 1
            lose=0
            score = 0
            wn.blit(background_2,(0,0))

            time.delay(1000)
            
    if level2 :            
            wn.blit(background_2,(0,0))  
            text_score = font1.render("табуретки: " + str(score),1,(255,255,255))
            wn.blit(text_score,(10,20))
            text_lose = font1.render("петух: " + str(lose),1,(255,255,255))
            wn.blit(text_lose,(10,50))   
            taburet.reset()
            pirat.reset()
            pirat.update()
            taburet.reset()
            taburet.update()
            pityxs.draw(wn)
            pityxs.update()

            
            collis_pityx = sprite.spritecollide(pirat,pityxs,True)
            if collis_pityx :
                lose += 1
                if lose< 10:
                    pityx=Enemy("петух-removebg-preview (2).png",randint(80,620),-30,80,80,3)
                    pityxs.add(pityx)
                if lose ==2:
                    for i in range(30):
                        pityx=Enemy("петух-removebg-preview (2).png",randint(80,620),randint(-80,-20),80,80,3)
                        pityxs.add(pityx)

            collis_taburet = sprite.spritecollide(pirat,taburets,True)
            if collis_taburet:
                taburet=Enemy("табурет-removebg-preview.png",randint(80,620),-30,80,80,3)
                taburets.add(taburet)
                score += 1


            

        
    clock.tick(FPS)
    display.update()








