#Forever Alone(FA)
#Metal Slug 2C
#Game,Images,Animation,Keyboard
#The left and right arrow key will make the character move.
#Down Arrow Key will make it jump
#Up Arrow Key will make it aim up
#Z Key will make the character shoot and X key will make character jump

#To win this game you need to kill all the enemies
#*It is optional to save all the villagers. The villagers however, do give you bonus score points.
#You lose when your lives reaches 0

#Problems:

#Next Steps:
#Adding splash screens (To be due by next week)

#Resources Used:
#spritedatabase.net
#spriters-resource.com
#Metal Slug wiki
#arcade.photonstorm.com
#retrogamezone.co.uk/metalslug/

#Sprites, map, ost, music, and character all belong to SNK Playmore
#Sprites Ripped By:
#-Gussprint(Eri Kasamoto's Sprites)
#-MagmaDragon(GameOver Screen)
#AzRaezel(Background)
#Goemar(HUD)


from gamelib import *

game = Game(640,480,"Metal Slug 2 Mission 1 Clone")

sky=Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\Sky.png",game)
dawn=Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\Dawn_Sky.png",game)
dunes=Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\Dunes.png",game)
bk=Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\Sand_Area.png",game)
fg=Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\Sand_Village2.png",game)
castle=Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\Sand_Castle.png",game)
city=Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\Sand_City.png",game)

BGM = Sound("Sounds\\MetalSlug2BGM.wav",1)
Menu = Sound("Sounds\\MetalSlugMenu.wav",2)
MissionStart = Sound("Sounds\\MISSION_START.wav",3)
MissionComplete = Sound("Sounds\\MISSION_COMPLETE.wav",5)
Gameover = Sound("Sounds\\GAME_OVER.wav",6)

bullets=[]
bulletsleft=[]
bulletsup=[]
bulletscrouch=[]

r_bullets=[]
r1_bullets=[]
r2_bullets=[]

s_bullets=[]
s1_bullets=[]
s2_bullets=[]

s3_bullets=[]
s4_bullets=[]
s5_bullets=[]
s6_bullets=[]
s7_bullets=[]
s8_bullets=[]

s9_bullets=[]

rf_bullets=[]
rf1_bullets=[]
rf2_bullets=[]


EriUpperBodyIdle=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_UpperBodyIdle.png",6,game,192/6,28,2)
EriLowerBodyIdle=Image("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_LowerBodyIdle.png",game)

#EriLowerBodyStartRun=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_LowerBodyStartRun.png",2,game,100/4,24,2)
EriLowerBodyLoopRun=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_LowerBodyLoopRun.png",12,game,360/12,26,2)
EriUpperBodyLoopRun=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_UpperBodyLoopRun.png",12,game,384/12,29,2)

EriLowerBodyLoopRunLeft=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_LowerBodyLoopRunLeft.png",12,game,360/12,26,2)
EriUpperBodyLoopRunLeft=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_UpperBodyLoopRunLeft.png",12,game,384/12,29,2)

EriUpperBodyJump=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_UpperBodyJump.png",6,game,186/6,27,2)
EriLowerBodyJump=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_LowerBodyJump.png",11,game,264/11,30,2)

EriCrouchIdle=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_CrouchIdle.png",6,game,210/6,28,2)
EriUpperBodyUpIdle=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_UpperBodyUpIdle.png",6,game,180/6,24,2)

EriShooting=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_Shooting.png",10,game,540/10,27,0.5)#Shooting is upper body only
EriShootingLeft=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_ShootingLeft.png",10,game,540/10,27,0.5)
EriShootingUp=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_ShootingUp.png",10,game,31,620/10,0.5)
EriCrouchShoot=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_CrouchShoot.png",10,game,550/10,29,0.5)

EriDeath=Animation("Game_Images\\Metal_Slug\\Eri_Kasamoto\\Eri_Death_Sh.png",18,game,882/18,36,2)

RebelRifleIdle=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Rifle_Idle.png",4,game,160/4,38,2)
RebelRifleLoopRun=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Rifle_LoopRun.png",12,game,504/12,38,2)
RebelRifleShoot=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Rifle_Shoot.png",38,game,84,1862/38,2)

RebelRifleShoot1=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Rifle_Shoot.png",38,game,84,1862/38,2)
RebelRifleShoot2=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Rifle_Shoot.png",38,game,84,1862/38,2)

RebelBiker=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Biker.png",3,game,198/3,54,2)

Rifleman=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Rifleman.png",17,game,1105/17,40,2)
Rifleman1=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Rifleman.png",17,game,1105/17,40,2)
Rifleman2=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Rifleman.png",17,game,1105/17,40,2)

RebelShield=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_Idle.png",6,game,210/6,39,2)
RebelShield1=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_Idle.png",6,game,210/6,39,2)
RebelShield2=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_Idle.png",6,game,210/6,39,2)
RebelShield3=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_Idle.png",6,game,210/6,39,2)
RebelShieldShoot=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_Shoot.png",10,game,420/10,44,2)
RebelShieldShoot1=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_Shoot.png",10,game,420/10,44,2)

RebelShieldDown=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_IdleDown.png",6,game,270/6,48,2)
RebelShieldDownShoot=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_ShootDown.png",10,game,480/10,42,2)
RebelShieldDownShoot1=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_ShootDown.png",10,game,480/10,42,2)

RebelShieldDownShoot2=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_ShootDown.png",10,game,480/10,42,2)
RebelShieldDownShoot3=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_ShootDown.png",10,game,480/10,42,2)
RebelShieldDownShoot4=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_ShootDown.png",10,game,480/10,42,2)
RebelShieldDownShoot5=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_ShootDown.png",10,game,480/10,42,2)
RebelShieldDownShoot6=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_ShootDown.png",10,game,480/10,42,2)
RebelShieldDownShoot7=Animation("Game_Images\\Metal_Slug\\Rebel_Soldiers\\Shield_ShootDown.png",10,game,480/10,42,2)

VillagerCaptured=Animation("Game_Images\\Metal_Slug\\NPC\\VillagerCaptured.png",37,game,1628/37,48,2)
VillagerCaptured1=Animation("Game_Images\\Metal_Slug\\NPC\\VillagerCaptured.png",37,game,1628/37,48,2)
#VillagerWalkLeft=Animation("Game_Images\\Metal_Slug\\NPC\\VillagerWalkLeft.png",12,game,408/12,40,2)
VillagerTied=Animation("Game_Images\\Metal_Slug\\NPC\\VillagerTied.png",8,game,296/8,27,2)
VillagerTied1=Animation("Game_Images\\Metal_Slug\\NPC\\VillagerTied.png",8,game,296/8,27,2)
VillagerTied2=Animation("Game_Images\\Metal_Slug\\NPC\\VillagerTied.png",8,game,296/8,27,2)
VillagerGiveLeft=Animation("Game_Images\\Metal_Slug\\NPC\\VillagerGiveLeft.png",39,game,2106/39,40,2)
VillagerGiveLeft1=Animation("Game_Images\\Metal_Slug\\NPC\\VillagerGiveLeft.png",39,game,2106/39,40,2)
VillagerGiveLeft2=Animation("Game_Images\\Metal_Slug\\NPC\\VillagerGiveLeft.png",39,game,2106/39,40,2)
VillagerGiveLeft3=Animation("Game_Images\\Metal_Slug\\NPC\\VillagerGiveLeft.png",39,game,2106/39,40,2)
VillagerGiveLeft4=Animation("Game_Images\\Metal_Slug\\NPC\\VillagerGiveLeft.png",39,game,2106/39,40,2)

Banana=Image("Game_Images\\Metal_Slug\\Items\\Banana.png",game)
Chicken=Animation("Game_Images\\Metal_Slug\\Items\\CookedChicken.png",43,game,1204/43,32,2)
CannedFood=Image("Game_Images\\Metal_Slug\\Items\\CannedFood.png",game)
Poo=Animation("Game_Images\\Metal_Slug\\Items\\Poo.png",6,game,126/6,30,2)
Medal=Animation("Game_Images\\Metal_Slug\\Items\\Medal.png",21,game,441/21,20,2)

Bar=Image("Game_Images\\Metal_Slug\\Font\\HUD\\bar.png",game)
leftbox=Image("Game_Images\\Metal_Slug\\Font\\HUD\\left_box.png",game)
rightbox=Image("Game_Images\\Metal_Slug\\Font\\HUD\\right_box.png",game)
box=Image("Game_Images\\Metal_Slug\\Font\\HUD\\box.png",game)
arms=Image("Game_Images\\Metal_Slug\\Font\\HUD\\arms.png",game)
infinite=Image("Game_Images\\Metal_Slug\\Font\\HUD\\infinite.png",game)

GameOver=Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\MS_Game_Over_Screen.png",game)
GameOver.resizeTo(game.width,game.height)

Victory=Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\BlackBKG.png",game)
Victory.resizeTo(game.width,game.height)

#Title Screen
TitleScreen=Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\MS_Title_Screen.png",game)
TitleScreen.resizeTo(game.width,game.height)
TitleScreen.draw()
Menu.play()
game.update(1)
game.wait(K_SPACE)

Instructions=Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\Instructions.png",game)
Instructions.draw()
game.update(0.05)


city.resizeTo(city.width*2,city.height*2)
city.moveTo(bk.x+5220,bk.y-32)

castle.resizeTo(castle.width*2,castle.height*2)
castle.moveTo(bk.x+2930,bk.y-16)

fg.resizeTo(fg.width*2,fg.height*2)
fg.moveTo(1850,216)

bk.moveTo(fg.x-1632,fg.y+50)
bk.resizeTo(bk.width*2,bk.height*2)

dunes.resizeTo(dunes.width*2,dunes.height*2)
dunes.moveTo(bk.x-50,bk.y-40)

dawn.resizeTo(dawn.width*3,dawn.height*3)
dawn.moveTo(bk.x+6000,bk.y-122)

sky.resizeTo(sky.width*3,sky.height*3)
sky.moveTo(bk.x+500,bk.y-122)

EriUpperBodyIdle.resizeBy(100)
EriUpperBodyIdle.moveTo(EriUpperBodyIdle.x,EriUpperBodyIdle.y+95)

EriLowerBodyIdle.resizeBy(100)
EriLowerBodyIdle.moveTo(EriUpperBodyIdle.x-5,EriUpperBodyIdle.y+24)

#EriLowerBodyStartRun.resizeBy(100)
EriLowerBodyLoopRun.resizeBy(100)
EriUpperBodyLoopRun.resizeBy(100)

EriLowerBodyLoopRunLeft.resizeBy(100)
EriUpperBodyLoopRunLeft.resizeBy(100)

EriUpperBodyJump.resizeBy(100)
EriLowerBodyJump.resizeBy(100)

EriShooting.resizeBy(100)
EriShootingLeft.resizeBy(100)
EriShootingUp.resizeBy(100)
EriCrouchShoot.resizeBy(100)

EriUpperBodyUpIdle.resizeBy(100)
EriCrouchIdle.resizeBy(100)

EriDeath.resizeBy(100)

H_Ammo=1

E_Ammo=1 #RebelRifle
E1_Ammo=1 #ShieldDown
E2_Ammo=1 #Rifleman
E3_Ammo=1 #ShieldShoot
E4_Ammo=1 #Rifleman1
E5_Ammo=1 #ShieldDown1
E6_Ammo=1 #RebelRifle1
E7_Ammo=1 #ShieldDown2
E8_Ammo=1 #ShieldDown3
E9_Ammo=1 #ShieldDown4
E10_Ammo=1 #ShieldDown5
E11_Ammo=1 #ShieldDown6
E12_Ammo=1 #ShieldDown7
E13_Ammo=1 #Rifleman2
E14_Ammo=1 #RebelRifle2
E15_Ammo=1 #ShieldShoot1

Give=1 #Captured
Give1=1 #Tied
Give2=1 #Captured1
Give3=1 #Tied1
Give4=1 #Tied2

Lives=3

Enemies=21

Bgm=1
Start=1
TimeoutGO=1
TimeoutV=1

jumping = False
landed = False
factor = 1

RebelRifleIdle.resizeBy(100)
RebelRifleLoopRun.resizeBy(100)
RebelRifleShoot.resizeBy(100)

RebelRifleShoot1.resizeBy(100)
RebelRifleShoot2.resizeBy(100)

RebelBiker.resizeBy(100)

RebelShield.resizeBy(100)
RebelShield1.resizeBy(100)
RebelShield2.resizeBy(100)
RebelShield3.resizeBy(100)
RebelShieldShoot.resizeBy(100)
RebelShieldShoot1.resizeBy(100)

RebelShieldDownShoot.resizeBy(100)
RebelShieldDownShoot1.resizeBy(100)
RebelShieldDownShoot2.resizeBy(100)
RebelShieldDownShoot3.resizeBy(100)
RebelShieldDownShoot4.resizeBy(100)
RebelShieldDownShoot5.resizeBy(100)
RebelShieldDownShoot6.resizeBy(100)
RebelShieldDownShoot7.resizeBy(100)

Rifleman.resizeBy(100)
Rifleman1.resizeBy(100)
Rifleman2.resizeBy(100)

RebelRifleIdle.moveTo(800,EriLowerBodyIdle.y-14)
RebelRifleShoot1.moveTo(2700,EriLowerBodyIdle.y-14)
RebelRifleShoot2.moveTo(3745,EriLowerBodyIdle.y-14)

RebelShield.moveTo(720,EriLowerBodyIdle.y-14)
RebelShield1.moveTo(2230,EriLowerBodyIdle.y-14)
RebelShield2.moveTo(3320,EriLowerBodyIdle.y-14)
RebelShield3.moveTo(3685,EriLowerBodyIdle.y-14)
RebelShieldDownShoot.moveTo(2000,EriLowerBodyIdle.y-167)
RebelShieldShoot.moveTo(1500,EriLowerBodyIdle.y-18)
RebelShieldShoot1.moveTo(4300,EriLowerBodyIdle.y-18)
RebelShieldDownShoot1.moveTo(2500,EriLowerBodyIdle.y-167)

RebelShieldDownShoot2.moveTo(3115,EriLowerBodyIdle.y-198)
RebelShieldDownShoot3.moveTo(3170,EriLowerBodyIdle.y-198)
RebelShieldDownShoot4.moveTo(3225,EriLowerBodyIdle.y-198)#LeftEnd
RebelShieldDownShoot5.moveTo(3490,EriLowerBodyIdle.y-198)
RebelShieldDownShoot6.moveTo(3545,EriLowerBodyIdle.y-198)
RebelShieldDownShoot7.moveTo(3600,EriLowerBodyIdle.y-198)

Rifleman.moveTo(2250,EriLowerBodyIdle.y-14)
Rifleman1.moveTo(1560,EriLowerBodyIdle.y-14)
Rifleman2.moveTo(3380,EriLowerBodyIdle.y-14)

RebelBiker.moveTo(1650,EriLowerBodyIdle.y-14)
RebelBiker.setSpeed(12,90)

VillagerCaptured.resizeBy(75)
VillagerCaptured.moveTo(1000,EriLowerBodyIdle.y-14)
VillagerTied.resizeBy(100)
VillagerTied.moveTo(4250,EriLowerBodyIdle.y)
VillagerCaptured1.moveTo(4200,EriLowerBodyIdle.y-14)
VillagerCaptured1.resizeBy(75)
VillagerTied1.resizeBy(100)
VillagerTied1.moveTo(2900,EriLowerBodyIdle.y)
VillagerTied2.resizeBy(100)
VillagerTied2.moveTo(4150,EriLowerBodyIdle.y)
VillagerGiveLeft.resizeBy(100)#Captured
VillagerGiveLeft1.resizeBy(100)#Tied
VillagerGiveLeft2.resizeBy(100)#Captured1
VillagerGiveLeft3.resizeBy(100) #Tied1
VillagerGiveLeft4.resizeBy(100)

Banana.resizeBy(100)
Chicken.resizeBy(75)
CannedFood.resizeBy(100)
Poo.resizeBy(50)
Medal.resizeBy(75)

Bar.resizeBy(100)
Bar.moveTo(80,40)
leftbox.resizeBy(100)
leftbox.moveTo(180,22)
rightbox.resizeBy(100)
rightbox.moveTo(242,22)
box.resizeBy(100)
box.moveTo(211,39)
arms.resizeBy(100)
arms.moveTo(205,22)
infinite.moveTo(arms.x+5,arms.y+16)


while not game.over:
    game.processInput()
    BGM.play()
    sky.draw()
    dawn.draw()
    dunes.draw()
    bk.draw()
    fg.draw()
    castle.draw()
    city.draw()
    Bar.draw()
    leftbox.draw()
    rightbox.draw()
    box.draw()
    arms.draw()
    infinite.draw()

    RebelBiker.move()



    EriLowerBodyIdle.draw()
    EriUpperBodyIdle.draw()
    EriLowerBodyIdle.visible=True
    EriUpperBodyIdle.visible=True

    RebelRifleIdle.draw()
    RebelShield.draw()
    RebelShieldShoot.draw()
    RebelShieldShoot1.draw()
    RebelShieldDownShoot.draw()
    Rifleman.draw()
    Rifleman1.draw()
    RebelShieldDownShoot1.draw()
    RebelRifleShoot1.draw()
    RebelRifleShoot2.draw()
    RebelShield1.draw()
    RebelShield2.draw()
    RebelShield3.draw()
    Rifleman2.draw()

    RebelShieldDownShoot2.draw()
    RebelShieldDownShoot3.draw()
    RebelShieldDownShoot4.draw()
    RebelShieldDownShoot5.draw()
    RebelShieldDownShoot6.draw()
    RebelShieldDownShoot7.draw()
    VillagerCaptured.draw()
    VillagerTied.draw()
    VillagerCaptured1.draw()
    VillagerTied1.draw()
    VillagerTied2.draw()

    Start-=0.1

    if Start>0:
        MissionStart.play()

    if not keys.Pressed[K_RIGHT]:
        EriUpperBodyLoopRun.visible=False
        EriLowerBodyLoopRun.visible=False

    if not keys.Pressed[K_LEFT]:
        EriUpperBodyLoopRunLeft.visible=False
        EriLowerBodyLoopRunLeft.visible=False

    if not keys.Pressed[K_UP]:
        EriUpperBodyUpIdle.visible=False

    if not keys.Pressed[K_DOWN]:
        EriCrouchIdle.visible=False

    if keys.Pressed[K_RIGHT] and city.x-EriUpperBodyIdle.x>=1200 and Lives>0:
        #EriLowerBodyStartRun.visible=True
        #EriLowerBodyStartRun.moveTo(EriLowerBodyIdle.x+3,EriLowerBodyIdle.y)
        EriLowerBodyIdle.makeVisible(0)
        EriLowerBodyLoopRun.moveTo(EriLowerBodyIdle.x-5,EriLowerBodyIdle.y)
        EriLowerBodyLoopRun.visible=True
        EriUpperBodyIdle.makeVisible(0)
        EriUpperBodyLoopRun.moveTo(EriLowerBodyIdle.x+3,EriLowerBodyIdle.y-24)
        EriUpperBodyLoopRun.visible=True
        #EriLowerBodyStartRun.visible=False
        city.x-=6
        castle.x-=6
        fg.x-=6
        bk.x-=3
        dunes.x-=2
        dawn.x-=6
        sky.x-=1
        RebelRifleIdle.x-=6
        RebelShield.x-=6
        RebelShieldDownShoot.x-=6
        Rifleman.x-=6
        Rifleman1.x-=6
        Rifleman2.x-=6
        RebelShieldShoot.x-=6
        RebelShieldShoot1.x-=6
        RebelShieldDownShoot1.x-=6
        RebelRifleShoot1.x-=6
        RebelRifleShoot2.x-=6
        RebelShield1.x-=6
        RebelShield2.x-=6
        RebelShield3.x-=6
        RebelShieldDownShoot2.x-=6
        RebelShieldDownShoot3.x-=6
        RebelShieldDownShoot4.x-=6
        RebelShieldDownShoot5.x-=6
        RebelShieldDownShoot6.x-=6
        RebelShieldDownShoot7.x-=6
        VillagerCaptured.x-=6
        VillagerTied.x-=6
        VillagerCaptured1.x-=6
        VillagerTied1.x-=6
        VillagerTied2.x-=6

    elif keys.Pressed[K_LEFT] and city.x-EriUpperBodyIdle.x<=5350 and Lives>0:
        EriLowerBodyIdle.makeVisible(0)
        EriLowerBodyLoopRunLeft.moveTo(EriLowerBodyIdle.x-5,EriLowerBodyIdle.y)
        EriLowerBodyLoopRunLeft.visible=True
        EriUpperBodyIdle.makeVisible(0)
        EriUpperBodyLoopRunLeft.moveTo(EriLowerBodyIdle.x-12,EriLowerBodyIdle.y-24)
        EriUpperBodyLoopRunLeft.visible=True
        city.x+=6
        castle.x+=6
        fg.x+=6
        bk.x+=3
        dunes.x+=2
        dawn.x+=6
        sky.x+=1
        RebelRifleIdle.x+=6
        RebelShield.x+=6
        RebelShieldDownShoot.x+=6
        Rifleman.x+=6
        Rifleman1.x+=6
        Rifleman2.x+=6
        RebelShieldShoot.x+=6
        RebelShieldShoot1.x+=6
        RebelShieldDownShoot1.x+=6
        RebelRifleShoot1.x+=6
        RebelRifleShoot2.x+=6
        RebelShield1.x+=6
        RebelShield2.x+=6
        RebelShield3.x+=6
        RebelShieldDownShoot2.x+=6
        RebelShieldDownShoot3.x+=6
        RebelShieldDownShoot4.x+=6
        RebelShieldDownShoot5.x+=6
        RebelShieldDownShoot6.x+=6
        RebelShieldDownShoot7.x+=6
        VillagerCaptured.x+=6
        VillagerTied.x+=6
        VillagerCaptured1.x+=6
        VillagerTied1.x+=6
        VillagerTied2.x+=6

    elif keys.Pressed[K_UP] and Lives>0:
        EriUpperBodyIdle.makeVisible(0)
        EriUpperBodyUpIdle.moveTo(EriLowerBodyIdle.x+4,EriLowerBodyIdle.y-32)
        EriUpperBodyUpIdle.visible=True

    elif keys.Pressed[K_DOWN] and Lives>0:
        EriLowerBodyIdle.makeVisible(0)
        EriCrouchIdle.moveTo(EriLowerBodyIdle.x,EriLowerBodyIdle.y)
        EriCrouchIdle.visible=True
        EriUpperBodyIdle.makeVisible(0)
        

    if keys.Pressed[K_LEFT] and keys.Pressed[K_z] and H_Ammo>=0.5 and Lives>0:
        EriUpperBodyIdle.makeVisible(0)
        EriUpperBodyLoopRunLeft.visible=False
        EriShootingLeft.moveTo(EriLowerBodyIdle.x-34,EriLowerBodyIdle.y-26)

    elif keys.Pressed[K_UP] and keys.Pressed[K_z] and H_Ammo>=0.5 and Lives>0:
        EriUpperBodyIdle.makeVisible(0)
        EriUpperBodyUpIdle.visible=False
        EriShootingUp.moveTo(EriLowerBodyIdle.x,EriLowerBodyIdle.y-70)

    elif keys.Pressed[K_DOWN] and keys.Pressed[K_z] and H_Ammo>=0.5 and Lives>0:
        EriUpperBodyIdle.makeVisible(0)
        EriCrouchIdle.visible=False
        EriCrouchShoot.moveTo(EriLowerBodyIdle.x+20,EriLowerBodyIdle.y)

    elif keys.Pressed[K_z] and H_Ammo>=0.5 and Lives>0:
        EriUpperBodyIdle.makeVisible(0)
        EriUpperBodyLoopRun.visible=False
        EriShooting.moveTo(EriLowerBodyIdle.x+26,EriLowerBodyIdle.y-26)
        EriShooting.visible=True

    if keys.Pressed[K_LEFT] and keys.Pressed[K_z] and H_Ammo>=1 and Lives>0:
        bulletsleft.append(Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\Pistol_Bullet_F.png",game))
        bulletsleft[len(bulletsleft)-1].moveTo(EriShootingLeft.x-60,EriShootingLeft.y)
        H_Ammo-=0.5

    elif keys.Pressed[K_UP] and keys.Pressed[K_z] and H_Ammo>=1 and Lives>0:
        bulletsup.append(Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\Pistol_Bullet_U.png",game))
        bulletsup[len(bulletsup)-1].moveTo(EriShootingUp.x,EriShootingUp.y-26)
        H_Ammo-=0.5

    elif keys.Pressed[K_DOWN] and keys.Pressed[K_z] and H_Ammo>=1 and Lives>0:
        bulletscrouch.append(Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\Pistol_Bullet_F.png",game))
        bulletscrouch[len(bulletscrouch)-1].moveTo(EriCrouchShoot.x+60,EriCrouchShoot.y)
        H_Ammo-=0.5

    elif keys.Pressed[K_z] and H_Ammo>=1 and Lives>0:
        bullets.append(Image("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\Pistol_Bullet_F.png",game))
        bullets[len(bullets)-1].moveTo(EriShooting.x+60,EriShooting.y)
        H_Ammo-=0.5


    if EriLowerBodyIdle.y < 354 and EriUpperBodyIdle.y<374:
        landed = False

    else:
        landed = True

    if jumping:
        EriLowerBodyIdle.y-=27 * factor
        EriUpperBodyIdle.y-=27 * factor
        factor *= .90
        landed = False
        if factor < .18:
            jumping = False
            factor = 1

    if keys.Pressed[K_x] and landed and not jumping and Lives>0:
        jumping = True

    if not landed:
        EriLowerBodyIdle.y+=9
        EriUpperBodyIdle.y+=9

    

    for b in bullets:
        b.resizeTo(20,10)
        b.setSpeed(10,270)
        b.move()

        if b.isOffScreen("right") or b.x-EriUpperBodyIdle.x>=300:
            b.visible=False

        if b.collidedWith(RebelRifleIdle) or b.collidedWith(RebelRifleShoot):
            RebelRifleIdle.visible=False
            RebelRifleShoot.visible=False
            b.visible=False
            game.score+=100

        if b.collidedWith(VillagerCaptured):
            VillagerCaptured.visible=False
            b.visible=False
            game.score+=50

        if b.collidedWith(RebelBiker):
            RebelBiker.health-=40
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShield):
            RebelShield.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldDownShoot):
            RebelShieldDownShoot.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldShoot):
            RebelShieldShoot.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldShoot1):
            RebelShieldShoot1.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelRifleShoot1):
            RebelRifleShoot1.visible=False
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShield1):
            RebelShield1.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShield2):
            RebelShield2.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelRifleShoot2):
            RebelRifleShoot2.visible=False
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShield3):
            RebelShield3.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(VillagerCaptured1):
            VillagerCaptured1.visible=False
            b.visible=False
            game.score+=50

    for b in bulletsleft:
        b.resizeTo(20,10)
        b.setSpeed(10,90)
        b.move()

        if b.isOffScreen("left") or EriUpperBodyIdle.x-b.x>=310:
            b.visible=False

        if b.collidedWith(RebelRifleIdle) or b.collidedWith(RebelRifleShoot):
            RebelRifleIdle.visible=False
            RebelRifleShoot.visible=False
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelBiker):
            RebelBiker.health-=40
            b.visible=False
            game.score+=100

        if b.collidedWith(VillagerCaptured):
            VillagerCaptured.visible=False
            b.visible=False
            game.score+=50

        if b.collidedWith(RebelShield):
            RebelShield.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldShoot):
            RebelShieldShoot.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldShoot1):
            RebelShieldShoot1.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelRifleShoot1):
            RebelRifleShoot1.visible=False
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShield1):
            RebelShield1.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShield2):
            RebelShield2.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelRifleShoot2):
            RebelRifleShoot2.visible=False
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShield3):
            RebelShield3.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(VillagerCaptured1):
            VillagerCaptured1.visible=False
            b.visible=False
            game.score+=50


    for b in bulletscrouch:
        b.resizeTo(20,10)
        b.setSpeed(10,270)
        b.move()

        if b.isOffScreen("right") or b.x-EriUpperBodyIdle.x>=300:
            b.visible=False

        if b.collidedWith(RebelRifleIdle) or b.collidedWith(RebelRifleShoot):
            RebelRifleIdle.visible=False
            RebelRifleShoot.visible=False
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelBiker):
            RebelBiker.health-=40
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShield):
            RebelShield.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(VillagerCaptured):
            VillagerCaptured.visible=False
            b.visible=False
            game.score+=50

        if b.collidedWith(Rifleman):
            Rifleman.visible=False
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldShoot):
            RebelShieldShoot.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldShoot1):
            RebelShieldShoot1.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(Rifleman1):
            Rifleman1.visible=False
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelRifleShoot1):
            RebelRifleShoot1.visible=False
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShield1):
            RebelShield1.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(Rifleman2):
            Rifleman2.visible=False
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShield2):
            RebelShield2.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelRifleShoot1):
            RebelRifleShoot1.visible=False
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShield3):
            RebelShield3.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelRifleShoot2):
            RebelRifleShoot2.visible=False
            b.visible=False
            game.score+=100

        if b.collidedWith(VillagerTied):
            VillagerTied.visible=False
            b.visible=False
            game.score+=50

        if b.collidedWith(VillagerCaptured1):
            VillagerCaptured1.visible=False
            b.visible=False
            game.score+=50

        if b.collidedWith(VillagerTied1):
            VillagerTied1.visible=False
            b.visible=False
            game.score+=50

        if b.collidedWith(VillagerTied2):
            VillagerTied2.visible=False
            b.visible=False
            game.score+=50

    for b in bulletsup:
        b.resizeTo(10,20)
        b.setSpeed(10,360)
        b.move()

        if b.isOffScreen("top"):
            b.visible=False

        if b.collidedWith(RebelShieldDownShoot):
            RebelShieldDownShoot.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldDownShoot1):
            RebelShieldDownShoot1.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldDownShoot2):
            RebelShieldDownShoot2.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldDownShoot3):
            RebelShieldDownShoot3.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldDownShoot4):
            RebelShieldDownShoot4.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldDownShoot5):
            RebelShieldDownShoot5.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldDownShoot6):
            RebelShieldDownShoot6.health-=20
            b.visible=False
            game.score+=100

        if b.collidedWith(RebelShieldDownShoot7):
            RebelShieldDownShoot7.health-=20
            b.visible=False
            game.score+=100



    if H_Ammo<1:
        H_Ammo+=0.05

    if RebelRifleIdle.x-EriUpperBodyIdle.x<=340:
        RebelRifleIdle.visible=False
        RebelRifleShoot.moveTo(RebelRifleIdle.x-36,RebelRifleIdle.y-11)
        E_Ammo-=0.009755

    if RebelRifleIdle.x-EriUpperBodyIdle.x<=340 and E_Ammo>=1:
        r_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        r_bullets[len(r_bullets)-1].moveTo(RebelRifleShoot.x-20,RebelRifleShoot.y-12)
        
    for r in r_bullets:
        r.resizeTo(10,10)
        r.setSpeed(6,90)
        r.move()

        if keys.Pressed[K_RIGHT]:
            r.x-=6

        if r.collidedWith(EriUpperBodyIdle)or r.collidedWith(EriUpperBodyLoopRun) or r.collidedWith(EriUpperBodyLoopRunLeft) or r.collidedWith(EriLowerBodyIdle) or r. collidedWith(EriLowerBodyLoopRun) or r.collidedWith(EriLowerBodyLoopRunLeft) or r.collidedWith(EriCrouchIdle):
            Lives-=1
            r.visible=False

        if r.isOffScreen("left"):
            r.visible=False

    if RebelBiker.collidedWith(EriLowerBodyIdle) or RebelBiker.collidedWith(EriLowerBodyLoopRun) or RebelBiker.collidedWith(EriLowerBodyLoopRunLeft) or RebelBiker.collidedWith(EriCrouchIdle) or RebelBiker.collidedWith(EriCrouchShoot):
        Lives-=1
        RebelBiker.visible=False

    if RebelShieldDownShoot.x-EriUpperBodyIdle.x<=300:
        E1_Ammo-=0.0095

    if RebelShieldDownShoot.x-EriUpperBodyIdle.x<=300 and E1_Ammo>=1:
        s_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        s_bullets[len(s_bullets)-1].moveTo(RebelShieldDownShoot.x-20,RebelShieldDownShoot.y+20)

    for s in s_bullets:
        s.resizeTo(10,10)
        s.setSpeed(6,180)
        s.move()

        if keys.Pressed[K_RIGHT]:
            s.x-=6

        elif keys.Pressed[K_LEFT]:
            s.x+=6

        if s.collidedWith(EriUpperBodyIdle)or s.collidedWith(EriUpperBodyLoopRun) or s.collidedWith(EriUpperBodyLoopRunLeft) or s.collidedWith(EriLowerBodyIdle) or s. collidedWith(EriLowerBodyLoopRun) or s.collidedWith(EriLowerBodyLoopRunLeft) or s.collidedWith(EriCrouchIdle):
            Lives-=1
            s.visible=False

        if s.isOffScreen("bottom"):
            s.visible=False

    if Rifleman.x-EriUpperBodyIdle.x<=320:
        E2_Ammo-=0.0097

    if Rifleman.x-EriUpperBodyIdle.x<=320 and E2_Ammo>=1:
        rf_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        rf_bullets[len(rf_bullets)-1].moveTo(Rifleman.x-20,Rifleman.y)

    for r in rf_bullets:
        r.resizeTo(10,10)
        r.setSpeed(6,90)
        r.move()

        if keys.Pressed[K_RIGHT]:
            r.x-=6

        if r.collidedWith(EriUpperBodyIdle)or r.collidedWith(EriUpperBodyLoopRun) or r.collidedWith(EriUpperBodyLoopRunLeft) or r.collidedWith(EriLowerBodyIdle) or r. collidedWith(EriLowerBodyLoopRun) or r.collidedWith(EriLowerBodyLoopRunLeft) or r.collidedWith(EriCrouchIdle):
            Lives-=1
            r.visible=False

        if r.isOffScreen("left"):
            r.visible=False

    if RebelShieldShoot.x-EriUpperBodyIdle.x<=320:
        E3_Ammo-=0.0095

    if RebelShieldShoot.x-EriUpperBodyIdle.x<=320 and E3_Ammo>=1:
        s1_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        s1_bullets[len(s1_bullets)-1].moveTo(RebelShieldShoot.x-20,RebelShieldShoot.y-20)

    for s in s1_bullets:
        s.resizeTo(10,10)
        s.setSpeed(6,90)
        s.move()

        if keys.Pressed[K_RIGHT]:
            s.x-=6

        if s.collidedWith(EriUpperBodyIdle)or s.collidedWith(EriUpperBodyLoopRun) or s.collidedWith(EriUpperBodyLoopRunLeft) or s.collidedWith(EriLowerBodyIdle) or s. collidedWith(EriLowerBodyLoopRun) or s.collidedWith(EriLowerBodyLoopRunLeft) or s.collidedWith(EriCrouchIdle):
            Lives-=1
            s.visible=False

        if s.isOffScreen("left"):
            s.visible=False

    if Rifleman1.x-EriUpperBodyIdle.x<=320:
        E4_Ammo-=0.0097

    if Rifleman1.x-EriUpperBodyIdle.x<=320 and E4_Ammo>=1:
        rf1_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        rf1_bullets[len(rf1_bullets)-1].moveTo(Rifleman1.x-20,Rifleman1.y)

    for r in rf1_bullets:
        r.resizeTo(10,10)
        r.setSpeed(6,90)
        r.move()

        if keys.Pressed[K_RIGHT]:
            r.x-=6

        if r.collidedWith(EriUpperBodyIdle)or r.collidedWith(EriUpperBodyLoopRun) or r.collidedWith(EriUpperBodyLoopRunLeft) or r.collidedWith(EriLowerBodyIdle) or r. collidedWith(EriLowerBodyLoopRun) or r.collidedWith(EriLowerBodyLoopRunLeft) or r.collidedWith(EriCrouchIdle):
            Lives-=1
            r.visible=False

        if r.isOffScreen("left"):
            r.visible=False

    if RebelShieldDownShoot1.x-EriUpperBodyIdle.x<=300:
        E5_Ammo-=0.0095

    if RebelShieldDownShoot1.x-EriUpperBodyIdle.x<=300 and E5_Ammo>=1:
        s2_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        s2_bullets[len(s2_bullets)-1].moveTo(RebelShieldDownShoot1.x-20,RebelShieldDownShoot1.y+20)

    for s in s2_bullets:
        s.resizeTo(10,10)
        s.setSpeed(6,180)
        s.move()

        if keys.Pressed[K_RIGHT]:
            s.x-=6

        elif keys.Pressed[K_LEFT]:
            s.x+=6

        if s.collidedWith(EriUpperBodyIdle)or s.collidedWith(EriUpperBodyLoopRun) or s.collidedWith(EriUpperBodyLoopRunLeft) or s.collidedWith(EriLowerBodyIdle) or s. collidedWith(EriLowerBodyLoopRun) or s.collidedWith(EriLowerBodyLoopRunLeft) or s.collidedWith(EriCrouchIdle):
            Lives-=1
            s.visible=False

        if s.isOffScreen("bottom"):
            s.visible=False

    if RebelRifleShoot1.x-EriUpperBodyIdle.x<=340:
        E6_Ammo-=0.009755

    if RebelRifleShoot1.x-EriUpperBodyIdle.x<=340 and E6_Ammo>=1:
        r1_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        r1_bullets[len(r1_bullets)-1].moveTo(RebelRifleShoot1.x-20,RebelRifleShoot1.y-12)
        
    for r in r1_bullets:
        r.resizeTo(10,10)
        r.setSpeed(6,90)
        r.move()

        if keys.Pressed[K_RIGHT]:
            r.x-=6

        if r.collidedWith(EriUpperBodyIdle)or r.collidedWith(EriUpperBodyLoopRun) or r.collidedWith(EriUpperBodyLoopRunLeft) or r.collidedWith(EriLowerBodyIdle) or r. collidedWith(EriLowerBodyLoopRun) or r.collidedWith(EriLowerBodyLoopRunLeft) or r.collidedWith(EriCrouchIdle):
            Lives-=1
            r.visible=False

        if r.isOffScreen("left"):
            r.visible=False

    if RebelShieldDownShoot2.x-EriUpperBodyIdle.x<=300:
        E7_Ammo-=0.0095

    if RebelShieldDownShoot2.x-EriUpperBodyIdle.x<=300 and E7_Ammo>=1:
        s3_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        s3_bullets[len(s3_bullets)-1].moveTo(RebelShieldDownShoot2.x-20,RebelShieldDownShoot2.y+20)

    for s in s3_bullets:
        s.resizeTo(10,10)
        s.setSpeed(6,180)
        s.move()

        if keys.Pressed[K_RIGHT]:
            s.x-=6

        elif keys.Pressed[K_LEFT]:
            s.x+=6

        if s.collidedWith(EriUpperBodyIdle)or s.collidedWith(EriUpperBodyLoopRun) or s.collidedWith(EriUpperBodyLoopRunLeft) or s.collidedWith(EriLowerBodyIdle) or s. collidedWith(EriLowerBodyLoopRun) or s.collidedWith(EriLowerBodyLoopRunLeft) or s.collidedWith(EriCrouchIdle):
            Lives-=1
            s.visible=False

        if s.isOffScreen("bottom"):
            s.visible=False

    if RebelShieldDownShoot3.x-EriUpperBodyIdle.x<=300:
        E8_Ammo-=0.0095

    if RebelShieldDownShoot3.x-EriUpperBodyIdle.x<=300 and E8_Ammo>=1:
        s4_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        s4_bullets[len(s4_bullets)-1].moveTo(RebelShieldDownShoot3.x-20,RebelShieldDownShoot3.y+20)

    for s in s4_bullets:
        s.resizeTo(10,10)
        s.setSpeed(6,180)
        s.move()

        if keys.Pressed[K_RIGHT]:
            s.x-=6

        elif keys.Pressed[K_LEFT]:
            s.x+=6

        if s.collidedWith(EriUpperBodyIdle)or s.collidedWith(EriUpperBodyLoopRun) or s.collidedWith(EriUpperBodyLoopRunLeft) or s.collidedWith(EriLowerBodyIdle) or s. collidedWith(EriLowerBodyLoopRun) or s.collidedWith(EriLowerBodyLoopRunLeft) or s.collidedWith(EriCrouchIdle):
            Lives-=1
            s.visible=False

        if s.isOffScreen("bottom"):
            s.visible=False

    if RebelShieldDownShoot4.x-EriUpperBodyIdle.x<=300:
        E9_Ammo-=0.0095

    if RebelShieldDownShoot4.x-EriUpperBodyIdle.x<=300 and E9_Ammo>=1:
        s5_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        s5_bullets[len(s5_bullets)-1].moveTo(RebelShieldDownShoot4.x-20,RebelShieldDownShoot4.y+20)

    for s in s5_bullets:
        s.resizeTo(10,10)
        s.setSpeed(6,180)
        s.move()

        if keys.Pressed[K_RIGHT]:
            s.x-=6

        elif keys.Pressed[K_LEFT]:
            s.x+=6

        if s.collidedWith(EriUpperBodyIdle)or s.collidedWith(EriUpperBodyLoopRun) or s.collidedWith(EriUpperBodyLoopRunLeft) or s.collidedWith(EriLowerBodyIdle) or s. collidedWith(EriLowerBodyLoopRun) or s.collidedWith(EriLowerBodyLoopRunLeft) or s.collidedWith(EriCrouchIdle):
            Lives-=1
            s.visible=False

        if s.isOffScreen("bottom"):
            s.visible=False

    if RebelShieldDownShoot5.x-EriUpperBodyIdle.x<=300:
        E10_Ammo-=0.0095

    if RebelShieldDownShoot5.x-EriUpperBodyIdle.x<=300 and E10_Ammo>=1:
        s6_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        s6_bullets[len(s6_bullets)-1].moveTo(RebelShieldDownShoot5.x-20,RebelShieldDownShoot5.y+20)

    for s in s6_bullets:
        s.resizeTo(10,10)
        s.setSpeed(6,180)
        s.move()

        if keys.Pressed[K_RIGHT]:
            s.x-=6

        elif keys.Pressed[K_LEFT]:
            s.x+=6

        if s.collidedWith(EriUpperBodyIdle)or s.collidedWith(EriUpperBodyLoopRun) or s.collidedWith(EriUpperBodyLoopRunLeft) or s.collidedWith(EriLowerBodyIdle) or s. collidedWith(EriLowerBodyLoopRun) or s.collidedWith(EriLowerBodyLoopRunLeft) or s.collidedWith(EriCrouchIdle):
            Lives-=1
            s.visible=False

        if s.isOffScreen("bottom"):
            s.visible=False

    if RebelShieldDownShoot6.x-EriUpperBodyIdle.x<=300:
        E11_Ammo-=0.0095

    if RebelShieldDownShoot6.x-EriUpperBodyIdle.x<=300 and E11_Ammo>=1:
        s7_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        s7_bullets[len(s7_bullets)-1].moveTo(RebelShieldDownShoot6.x-20,RebelShieldDownShoot6.y+20)

    for s in s7_bullets:
        s.resizeTo(10,10)
        s.setSpeed(6,180)
        s.move()

        if keys.Pressed[K_RIGHT]:
            s.x-=6

        elif keys.Pressed[K_LEFT]:
            s.x+=6

        if s.collidedWith(EriUpperBodyIdle)or s.collidedWith(EriUpperBodyLoopRun) or s.collidedWith(EriUpperBodyLoopRunLeft) or s.collidedWith(EriLowerBodyIdle) or s. collidedWith(EriLowerBodyLoopRun) or s.collidedWith(EriLowerBodyLoopRunLeft) or s.collidedWith(EriCrouchIdle):
            Lives-=1
            s.visible=False

        if s.isOffScreen("bottom"):
            s.visible=False

    if RebelShieldDownShoot7.x-EriUpperBodyIdle.x<=300:
        E12_Ammo-=0.0095

    if RebelShieldDownShoot7.x-EriUpperBodyIdle.x<=300 and E12_Ammo>=1:
        s8_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        s8_bullets[len(s8_bullets)-1].moveTo(RebelShieldDownShoot7.x-20,RebelShieldDownShoot7.y+20)

    for s in s8_bullets:
        s.resizeTo(10,10)
        s.setSpeed(6,180)
        s.move()

        if keys.Pressed[K_RIGHT]:
            s.x-=6

        elif keys.Pressed[K_LEFT]:
            s.x+=6

        if s.collidedWith(EriUpperBodyIdle)or s.collidedWith(EriUpperBodyLoopRun) or s.collidedWith(EriUpperBodyLoopRunLeft) or s.collidedWith(EriLowerBodyIdle) or s. collidedWith(EriLowerBodyLoopRun) or s.collidedWith(EriLowerBodyLoopRunLeft) or s.collidedWith(EriCrouchIdle):
            Lives-=1
            s.visible=False

        if s.isOffScreen("bottom"):
            s.visible=False

    if Rifleman2.x-EriUpperBodyIdle.x<=320:
        E13_Ammo-=0.0097

    if Rifleman2.x-EriUpperBodyIdle.x<=320 and E13_Ammo>=1:
        rf2_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        rf2_bullets[len(rf2_bullets)-1].moveTo(Rifleman2.x-20,Rifleman2.y)

    for r in rf2_bullets:
        r.resizeTo(10,10)
        r.setSpeed(6,90)
        r.move()

        if keys.Pressed[K_RIGHT]:
            r.x-=6

        if r.collidedWith(EriUpperBodyIdle)or r.collidedWith(EriUpperBodyLoopRun) or r.collidedWith(EriUpperBodyLoopRunLeft) or r.collidedWith(EriLowerBodyIdle) or r. collidedWith(EriLowerBodyLoopRun) or r.collidedWith(EriLowerBodyLoopRunLeft) or r.collidedWith(EriCrouchIdle):
            Lives-=1
            r.visible=False

        if r.isOffScreen("left"):
            r.visible=False

    if RebelRifleShoot2.x-EriUpperBodyIdle.x<=320:
        E14_Ammo-=0.0097

    if RebelRifleShoot2.x-EriUpperBodyIdle.x<=320 and E14_Ammo>=1:
        r2_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        r2_bullets[len(r2_bullets)-1].moveTo(RebelRifleShoot2.x-20,RebelRifleShoot2.y-12)

    for r in r2_bullets:
        r.resizeTo(10,10)
        r.setSpeed(6,90)
        r.move()

        if keys.Pressed[K_RIGHT]:
            r.x-=6

        if r.collidedWith(EriUpperBodyIdle)or r.collidedWith(EriUpperBodyLoopRun) or r.collidedWith(EriUpperBodyLoopRunLeft) or r.collidedWith(EriLowerBodyIdle) or r. collidedWith(EriLowerBodyLoopRun) or r.collidedWith(EriLowerBodyLoopRunLeft) or r.collidedWith(EriCrouchIdle):
            Lives-=1
            r.visible=False

        if r.isOffScreen("left"):
            r.visible=False

    if RebelShieldShoot1.x-EriUpperBodyIdle.x<=320:
        E15_Ammo-=0.0095

    if RebelShieldShoot1.x-EriUpperBodyIdle.x<=320 and E15_Ammo>=1:
        s9_bullets.append(Animation("Game_Images\\Metal_Slug\\Metal_Slug_2\\Sprites\\E_Bullet.png",2,game,8,8,1))
        s9_bullets[len(s9_bullets)-1].moveTo(RebelShieldShoot1.x-20,RebelShieldShoot1.y-20)

    for s in s9_bullets:
        s.resizeTo(10,10)
        s.setSpeed(6,90)
        s.move()

        if keys.Pressed[K_RIGHT]:
            s.x-=6

        if s.collidedWith(EriUpperBodyIdle)or s.collidedWith(EriUpperBodyLoopRun) or s.collidedWith(EriUpperBodyLoopRunLeft) or s.collidedWith(EriLowerBodyIdle) or s. collidedWith(EriLowerBodyLoopRun) or s.collidedWith(EriLowerBodyLoopRunLeft) or s.collidedWith(EriCrouchIdle):
            Lives-=1
            s.visible=False

        if s.isOffScreen("left"):
            s.visible=False

    if RebelBiker.health<=0 or RebelBiker.isOffScreen("left"):
        RebelBiker.visible=False

    if RebelShield.health<=0:
        RebelShield.visible=False

    if RebelShieldDownShoot.health<=0:
        RebelShieldDownShoot.visible=False

    if RebelShieldShoot.health<=0:
        RebelShieldShoot.visible=False

    if RebelShieldShoot1.health<=0:
        RebelShieldShoot1.visible=False

    if RebelShieldDownShoot1.health<=0:
        RebelShieldDownShoot1.visible=False

    if RebelShield1.health<=0:
        RebelShield1.visible=False

    if RebelShieldDownShoot2.health<=0:
        RebelShieldDownShoot2.visible=False

    if RebelShieldDownShoot3.health<=0:
        RebelShieldDownShoot3.visible=False

    if RebelShieldDownShoot4.health<=0:
        RebelShieldDownShoot4.visible=False

    if RebelShieldDownShoot5.health<=0:
        RebelShieldDownShoot5.visible=False

    if RebelShieldDownShoot6.health<=0:
        RebelShieldDownShoot6.visible=False

    if RebelShieldDownShoot7.health<=0:
        RebelShieldDownShoot7.visible=False

    if RebelShield2.health<=0:
        RebelShield2.visible=False

    if RebelShield3.health<=0:
        RebelShield3.visible=False


    if VillagerCaptured.visible==False:
        VillagerGiveLeft.moveTo(VillagerCaptured.x,VillagerCaptured.y)
        VillagerGiveLeft.draw(False)
        Give-=0.05

    if Give<0:
        Give=0

    if Give==0:
        Banana.moveTo(VillagerGiveLeft.x-30,VillagerGiveLeft.y+18)

    if Banana.collidedWith(EriLowerBodyIdle) or Banana.collidedWith(EriLowerBodyLoopRun) or Banana.collidedWith(EriLowerBodyLoopRunLeft) or Banana.collidedWith(EriCrouchIdle):
        Banana.visible=False
        game.score+=50

    if VillagerTied.visible==False:
        VillagerGiveLeft1.moveTo(VillagerTied.x,VillagerTied.y-4)
        VillagerGiveLeft1.draw(False)
        Give1-=0.05

    if Give1<0:
        Give1=0

    if Give1==0:
        Chicken.moveTo(VillagerGiveLeft1.x-30,VillagerGiveLeft1.y+8)

    if Chicken.collidedWith(EriLowerBodyIdle) or Chicken.collidedWith(EriLowerBodyLoopRun) or Chicken.collidedWith(EriLowerBodyLoopRunLeft) or Chicken.collidedWith(EriCrouchIdle):
        Chicken.visible=False
        game.score+=150

    if VillagerCaptured1.visible==False:
        VillagerGiveLeft2.moveTo(VillagerCaptured1.x,VillagerCaptured1.y)
        VillagerGiveLeft2.draw(False)
        Give2-=0.05

    if Give2<0:
        Give2=0

    if Give2==0:
        CannedFood.moveTo(VillagerGiveLeft2.x-30,VillagerGiveLeft2.y+18)

    if CannedFood.collidedWith(EriLowerBodyIdle) or CannedFood.collidedWith(EriLowerBodyLoopRun) or CannedFood.collidedWith(EriLowerBodyLoopRunLeft) or CannedFood.collidedWith(EriCrouchIdle):
        CannedFood.visible=False
        game.score+=50

    if VillagerTied1.visible==False:
        VillagerGiveLeft3.moveTo(VillagerTied1.x,VillagerTied1.y-4)
        VillagerGiveLeft3.draw(False)
        Give3-=0.05

    if Give3<0:
        Give3=0

    if Give3==0:
        Poo.moveTo(VillagerGiveLeft3.x-30,VillagerGiveLeft3.y+18)

    if Poo.collidedWith(EriLowerBodyIdle) or Poo.collidedWith(EriLowerBodyLoopRun) or Poo.collidedWith(EriLowerBodyLoopRunLeft) or Poo.collidedWith(EriCrouchIdle):
        Poo.visible=False
        game.score+=25

    if VillagerTied2.visible==False:
        VillagerGiveLeft4.moveTo(VillagerTied2.x,VillagerTied2.y-4)
        VillagerGiveLeft4.draw(False)
        Give4-=0.05

    if Give4<0:
        Give4=0

    if Give4==0:
        Medal.moveTo(VillagerGiveLeft4.x-30,VillagerGiveLeft4.y+18)

    if Medal.collidedWith(EriLowerBodyIdle) or Medal.collidedWith(EriLowerBodyLoopRun) or Medal.collidedWith(EriLowerBodyLoopRunLeft) or Medal.collidedWith(EriCrouchIdle):
        Medal.visible=False
        game.score+=75
        

    if RebelRifleShoot.visible==False:
        E_Ammo=0

    if RebelShieldDownShoot.visible==False:
        E1_Ammo=0

    if Rifleman.visible==False:
        E2_Ammo=0

    if RebelShieldShoot.visible==False:
        E3_Ammo=0

    if Rifleman1.visible==False:
        E4_Ammo=0

    if RebelShieldDownShoot1.visible==False:
        E5_Ammo=0

    if RebelRifleShoot1.visible==False:
        E6_Ammo=0

    if RebelShieldDownShoot2.visible==False:
        E7_Ammo=0

    if RebelShieldDownShoot3.visible==False:
        E8_Ammo=0

    if RebelShieldDownShoot4.visible==False:
        E9_Ammo=0

    if RebelShieldDownShoot5.visible==False:
        E10_Ammo=0

    if RebelShieldDownShoot6.visible==False:
        E11_Ammo=0

    if RebelShieldDownShoot7.visible==False:
        E12_Ammo=0

    if Rifleman2.visible==False:
        E13_Ammo=0

    if RebelRifleShoot2.visible==False:
        E14_Ammo=0

    if RebelShieldShoot1.visible==False:
        E15_Ammo=0

    if E_Ammo<1:
        E_Ammo+=0.01

    if E1_Ammo<1:
        E1_Ammo+=0.01

    if E2_Ammo<1:
        E2_Ammo+=0.01

    if E3_Ammo<1:
        E3_Ammo+=0.01

    if E4_Ammo<1:
        E4_Ammo+=0.01

    if E5_Ammo<1:
        E5_Ammo+=0.01

    if E6_Ammo<1:
        E6_Ammo+=0.01

    if E7_Ammo<1:
        E7_Ammo+=0.01

    if E8_Ammo<1:
        E8_Ammo+=0.01

    if E9_Ammo<1:
        E9_Ammo+=0.01

    if E10_Ammo<1:
        E10_Ammo+=0.01

    if E11_Ammo<1:
        E11_Ammo+=0.01

    if E12_Ammo<1:
        E12_Ammo+=0.01

    if E13_Ammo<1:
        E13_Ammo+=0.01

    if E14_Ammo<1:
        E14_Ammo+=0.01

    if E15_Ammo<1:
        E15_Ammo+=0.01

    if RebelRifleShoot.visible==False and RebelShieldDownShoot.visible==False and Rifleman.visible==False and RebelShieldShoot.visible==False and Rifleman1.visible==False and RebelShieldDownShoot1.visible==False and RebelRifleShoot1.visible==False and RebelShieldDownShoot2.visible==False and RebelShieldDownShoot3.visible==False and RebelShieldDownShoot4.visible==False and RebelShieldDownShoot5.visible==False and RebelShieldDownShoot6.visible==False and RebelShieldDownShoot7.visible==False and Rifleman2.visible==False and RebelRifleShoot2.visible==False and RebelBiker.visible==False and RebelShield.visible==False and RebelShield1.visible==False and RebelShield2.visible==False and RebelShield3.visible==False and RebelShieldShoot1.visible==False:
        TimeoutV-=0.05

    if TimeoutV<0:
        TimeoutV=0

    if TimeoutV==0:
        game.over=True

    if Lives<=0:
        EriDeath.moveTo(EriLowerBodyIdle.x,EriLowerBodyIdle.y)
        EriDeath.draw(False)
        EriLowerBodyIdle.visible=False
        EriUpperBodyIdle.visible=False
        EriCrouchIdle.visible=False
        EriShooting.visible=False
        EriUpperBodyLoopRun.visible=False
        EriLowerBodyLoopRun.visible=False
        EriUpperBodyLoopRunLeft.visible=False
        EriLowerBodyLoopRunLeft.visible=False
        EriCrouchShoot.visible=False
        EriUpperBodyUpIdle.visible=False
        EriShootingUp.visible=False
        TimeoutGO-=0.05

    if TimeoutGO<0:
        TimeoutGO=0

    if TimeoutGO==0:
        game.over=True

    game.drawText("1UP="+str (Lives), 38, 48, Font(white,20,black,'Silom.ttf'))
    game.drawText(""+str (game.score), 100, 10, Font(white,24,black,'SilomBol.ttf'))

    game.update(20)

if TimeoutV==0:
    #Victory.draw()
    game.drawText("MISSION COMPLETE!",200,80,Font(white,26,black,'chicago.ttf'))
    game.drawText("RESULT",280,120,Font(white,24,black,'chicago.ttf'))
    game.drawText("Lives Left  "+str(Lives),120,180,Font(white,24,black,'chicago.ttf'))
    game.drawText("Score  "+str(game.score),120,220,Font(white,24,black,'chicago.ttf'))
    game.drawText("Press [SPACE] to Exit",420,420)
    
    MissionComplete.play()

if TimeoutGO==0:
    Gameover.play()
    GameOver.draw()

game.update(20)
game.wait(K_SPACE)
game.quit()



###CREDITS: LZ (For Helping With Graphics)
