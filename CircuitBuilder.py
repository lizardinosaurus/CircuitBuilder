#all of the built in python modules used are imported here
import pygame
import os
import sys
import types
import sqlite3
import ctypes



#connects the program to the circuitdata database
conn = sqlite3.connect("circuitdata.db")
cursor = conn.cursor()

#initialises pygame and font function
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Lucida sans', 16)
bigfont = pygame.font.SysFont('Lucida sans', 46)

#sets up the pygame window with the resolution of hight and width 
WIDTH, HEIGHT = 2560, 1440
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
# uses the ctypes module to fill up the entire screen no matter the resolution or aspect ratio
if sys.platform == "win32":
    HWND = pygame.display.get_wm_info()['window']
    SW_MAXIMIZE = 3
    ctypes.windll.user32.ShowWindow(HWND, SW_MAXIMIZE)
pygame.display.set_caption("Circuit builder")

#the FPS value is used in the main window to determine how many times the program should run per second
FPS = 165
clock = pygame.time.Clock()

# takes an image from the assets folder and converts it into a sprite
def makesprite(imagepng, width, height):
    image = pygame.image.load(os.path.join('assets', imagepng)).convert_alpha() # uses the os function to load the image from the assests folder
    sprite = pygame.transform.scale(image, (width, height)) # converts the image into a sprite
    return sprite

#sets up a cemra group for tracking the positon of the "camera"
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()


component_list = pygame.sprite.Group() # sets the component list as all component sprites
camera_group = CameraGroup() # sets a cameragroup variable to match the main CameraGroup



#imports all assests from the assets folder and converts them into sprites with a specific size using the makesprite function 
AMMETER_W = makesprite('ammeter_w.png', 70, 30)
AMMETER = makesprite('ammeter.png', 30, 30)
BULB_W = makesprite('bulb_w.png', 70, 30)
BULB = makesprite('bulb.png', 30, 30)
BULB_POWERED = makesprite('bulb_powered.png', 30, 30)
CELL_W = makesprite('cell_w.png', 60, 40)
CELL = makesprite('cell.png', 20, 40)
DIODE_W = makesprite('diode_w.png', 60, 25)
DIODE = makesprite('diode.png', 20, 25)
FUSE_W = makesprite('fuse_w.png', 100, 20)
FUSE = makesprite('fuse.png', 60, 20)
FUSE_BROKEN = makesprite('fuse_broken.png', 60, 20)
LED_W = makesprite('led_w.png', 70, 30)
LED = makesprite('led.png', 30, 30)
LED_POWERED = makesprite('led_powered.png', 30, 30)
RESISTOR_W = makesprite('resistor_w.png', 100, 20)
RESISTOR = makesprite('resistor.png', 60, 20)
SWITCH_W = makesprite('switch_w.png', 80, 15)
SWITCH_OPEN = makesprite('switch_open.png', 40, 15)
SWITCH_CLOSED = makesprite('switch_closed.png', 40, 10)
SWITCH_OPEN = makesprite('switch_open.png', 40, 10)
VOLTMETER_W = makesprite('voltmeter_w.png', 70, 30)
VOLTMETER = makesprite('voltmeter.png', 30, 30)

COMPTRAY = makesprite('comptray.png', 250, 350)
COMPTRAYrect = COMPTRAY.get_rect(x=0, y=40)
DELETEBUTTON = makesprite('deletebutton.png', 200, 50)
DELETEBUTTONrect = DELETEBUTTON.get_rect(x=15, y=400)
smalldelete = makesprite('smalldelete.jpeg', 75, 23)
smalldeleteblue = makesprite('smalldeleteblue.jpeg', 75, 23)
positiveterminal = makesprite('positiveterminal.jpeg', 75, 44)
positiveterminalblue = makesprite('positiveterminalblue.jpeg', 75, 44)
negativeterminal = makesprite('negativeterminal.jpeg', 75, 44)
negativeterminalblue = makesprite('negativeterminalblue.jpeg', 75, 44)
setres = makesprite('setres.jpeg', 75, 44)
setvolts = makesprite('setvolts.png', 75, 75)
setvoltsblue = makesprite('setvoltsblue.png', 75, 75)
toggle = makesprite('toggle.png', 75, 75)
toggleblue = makesprite('toggleblue.png', 75, 75)
setamps = makesprite('setamps.png', 75, 75)
setampsblue = makesprite('setampsblue.png', 75, 75)
setresblue = makesprite('setresblue.jpeg', 75, 44)
deletearrow = makesprite('delete.jpeg', 75, 23)
connectwire = makesprite('connectwire.jpeg', 75, 44)
wires = makesprite('wires.jpeg', 75, 22)
comp = makesprite('component.jpeg', 75, 22)
compblue = makesprite('componentblue.jpeg', 75, 22)
rotatebutton = makesprite('rotate.jpeg', 75, 21)
rotateblue = makesprite('rotateblue.jpeg', 75, 21)
connectp = makesprite('connectp.jpeg', 75, 66)
connectn = makesprite('connectn.jpeg', 75, 66)
connectpblue = makesprite('connectpblue.jpeg', 75, 66)
connectnblue = makesprite('connectnblue.jpeg', 75, 66)
greensq = makesprite('greensq.png', 5, 5)
redsq = makesprite('redsq.png', 5, 5)
play = makesprite('play.jpeg', 50, 50)
playrect = play.get_rect(x=1400, y=-2)
pause = makesprite('pause.jpeg', 50, 50)
field = makesprite('textbox.jpeg', 500, 150)
ok = makesprite('ok.jpeg', 60, 20)
okrect = ok.get_rect(x=1125, y=465)
cancel = makesprite('cancel.jpeg', 60, 20)
cancelrect = cancel.get_rect(x=900, y=465)
voltbox = makesprite('voltage.jpeg', 500, 150)
ampbox = makesprite('ampbox.png', 500, 150)

#============================================ main program functions ==========================================================
# all the functions for the program will be defined in this space

def draw_window():
    WIN.blit(COMPTRAY, comprect(COMPTRAY, 0,40))
    WIN.blit(AMMETER_W, comprect(AMMETER_W, 23,265))
    WIN.blit(BULB_W, comprect(BULB_W, 23,130))
    WIN.blit(CELL_W, comprect(CELL_W, 25,70))
    WIN.blit(DIODE_W, comprect(DIODE_W, 28,200))
    WIN.blit(FUSE_W, comprect(FUSE_W, 60,330))
    WIN.blit(LED_W, comprect(LED_W, 130,198))
    WIN.blit(RESISTOR_W, comprect(RESISTOR_W, 110,79))
    WIN.blit(SWITCH_W, comprect(SWITCH_W, 125,136))
    WIN.blit(VOLTMETER_W, comprect(VOLTMETER_W, 130,265))
    WIN.blit(DELETEBUTTON, comprect(DELETEBUTTON, 15, 400))
    WIN.blit(play, comprect(play, 1400, -2))

# defines the rectangle for a given component
def comprect(component, tlx, tly):
    comprect = component.get_rect() # gets the rectangle value for a sprite
    comprect.topleft = (tlx, tly) # sets the topleft value to coordinates entered
    return comprect 

#detects when a component in the tray is clicked and creates a sprite for it
def drag_and_drop_check(self, Component, componenttype, id_count):
    try:
        if (self.collidepoint(pygame.mouse.get_pos())) and (leftclick == True): # detects if a component in the tray is clicked
                cursor.execute("INSERT INTO tblcomponents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (((id_count)-1), componenttype, mx, my, 0, 0, 0, 0, 0, 0, 0, 0, 0, False, 0, 0, False,0 ,0, 0)) # adds the new component to the databse
                conn.commit()
                id_count = int(id_count) + 1 #increments id_count by 1
                component_list.add(Component(mx, my, camera_group, 0, 0, False)) # adds the component to the component_list
                Component.clicked = True # sets component to clicked
                return id_count # returns the new id
        else:
            return id_count # returns the same id if component isnt clicked
    # runs the same function with id_count as 1 if the program is unable to detrmine its value
    except TypeError:
        if (self.collidepoint(pygame.mouse.get_pos())) and (leftclick == True): # detects if a component in the tray is clicked
                cursor.execute("INSERT INTO tblcomponents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (0, componenttype, mx, my, 0, 0, 0, 0, 0, 0, 0, 0, 0, False, 0, 0, False, 0, 0, 0)) # adds the new component to the databse
                conn.commit()
                id_count = 2 #increments id_count by 1
                component_list.add(Component(mx, my, camera_group, 0, 0, False)) #adds the component to the component_list
                Component.clicked = True # sets component to clicked
                return id_count # returns the new id
        else:
            return id_count # returns the same id if component isnt clicked
        
                
# makes the clicked component follow the mouse
def drag_component():
   for component in component_list: # initiates a list of every component
        if component.clicked == True: # checks if the component is clciked
            global collidecheck
            collidecheck = True # lets the program know a component is being dragged
            mx, my = pygame.mouse.get_pos() # finds the mouse position
            # constantly updates the components x and y cooridinates to be the same as the mouses
            component.rect.x = mx-(component.rect.width/2)
            component.rect.y = my-(component.rect.height/2)
            
# checks if a component is clicked on
def check_clicked():
    for component in component_list: # initiates a list of all components
            if pygame.Rect(component).collidepoint(pygame.mouse.get_pos()): # checks if the component is clicked
                # sets the components value to clicked and lets the program know it has been clicked on
                collidecheck = True
                component.clicked = True
                break # ends the loop
            
# lets the program know the component is no longer being dragged
def drop_component():
    global collidecheck
    collidecheck = False
    # sets clicked to false for all components
    for component in component_list:
        component.clicked = False

#updates a components location in the database
def updatepos():    
        count = 0
        cursor.execute('SELECT compID FROM tblcomponents ORDER BY compID') # selcts compID from tblcomponents
        data = cursor.fetchall()
        for component in component_list: # initiates a loop of every component
            idnumber = data[count][0] # stores the compID of that component
            # stores its positon
            originx = component.rect.x
            originy = component.rect.y
            # updates the components position in the databas
            cursor.execute("UPDATE tblcomponents SET xpos=?, ypos=?, resistance=?, voltage=?, uniquestate=? WHERE compID=?", (originx, originy, component.resistance, component.voltage, component.uniquestate, idnumber) )
            conn.commit()
            count += 1
            
# moves all the components when the user drags on the screen
def cameraoffsetcheck():
    try:
        counter = -1
        # takes all of the x and y value for every component from the database
        cursor.execute('SELECT xpos FROM tblcomponents ORDER BY compID')
        xposdata = cursor.fetchall()
        cursor.execute('SELECT ypos FROM tblcomponents ORDER BY compID')
        yposdata = cursor.fetchall()
        for component in component_list: # initiates a loop for every component
            counter += 1
            # finds the components relative distance from the mouse
            offsetx = int(xposdata[counter][0]) - startpos[0]
            offsety = int(yposdata[counter][0]) - startpos[1]
            if (pygame.mouse.get_pressed(3)[0] == True) and (collidecheck == False) and (COMPTRAYrect.collidepoint(pygame.mouse.get_pos()) == False): # detects if the mouse is clicking on empty space
                # updates all components to ensure there relative distance to the mouse remains the same as the mouse is moved around
                component.rect.x = pygame.mouse.get_pos()[0] + offsetx
                component.rect.y = pygame.mouse.get_pos()[1] + offsety
    except IndexError: # stops the program crashing if the database is empty
        pass


# deletes all components when the deltebutton is clicked
def deletecheck():
    if (DELETEBUTTONrect.collidepoint(pygame.mouse.get_pos()) == True)  and (collidecheck == False): # checks if the deltebutton is clicked
        for component in component_list: # initiates a loop for all components
            # delets the sprites for all components
            component.kill()
            global id_count
            id_count = 1
        # empties the entire database
        cursor.execute('DELETE FROM tblcomponents')
        cursor.execute('DELETE FROM tblpositiveconnections')
        cursor.execute('DELETE FROM tblnegativeconnections')
        conn.commit()
        id_count = 1

#rotate a component
def rotate(component, idnumber):

        # updates the components rotation in the database and sets it to 0 if it reashes -360 degrees
        cursor.execute("UPDATE tblcomponents SET rotation=rotation + ? WHERE compID=?", (-90, idnumber) )
        cursor.execute("UPDATE tblcomponents SET rotation=? WHERE rotation=?", (0, -360) )
        
# sets all the components rotation to 0 but doesnt update the database
def unrotate():
    counter = -1
    cursor.execute('SELECT rotation FROM tblcomponents ORDER BY compID')
    data = cursor.fetchall()
    for component in component_list: # initiates a loop for all components
        counter += 1
        altered_image =  component.image = pygame.transform.rotate(component.image, 360+data[counter][0]) # sets the image rotation to 360 + the value in the database
        drawn_image = altered_image # altered_image() is whatever changes you're making to the image before it's drawn
        image_location = drawn_image.get_rect(center=component.rect.center) #returns the Surface's rect with rect.center set to the center of the object
        component.image, component.rect = (drawn_image, image_location)
 
# detects if a component is rightclicked and saves its idnumber
def dropdown():
    global showmenu, saveid, wait, dbid
    count = 0
    # selects compID from the database
    cursor.execute('SELECT compID FROM tblcomponents ORDER BY compID')
    data = cursor.fetchall()
    for component in component_list: # initialises a loop for all components
        idnumber = data[count][0] # sets idnumber to the compID value in the database
        count += 1
        if (pygame.mouse.get_pressed(3)[2] == True) and (component.rect.collidepoint(pygame.mouse.get_pos()) == True): # detects if a component is rightclicked
            # saves the components id number and database id as well as sets showmenu to true to allow the program to know the menu should be presented
            showmenu = True
            saveid = count-1
            wait = True
            dbid = idnumber

# adds red and green dots to show positive nd negative terminals of every component
def redgreen():
    try:
        # selects all data drom the components table
        cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
        maindata = cursor.fetchall()
        count = 0
        for component in component_list:# initialises a loop for all components
            # detects the rotation of the component by checking the database and draws the dots in the correct place depending on that rotation
            if maindata[count][12] == 0:
                WIN.blit(greensq, comprect(greensq, component.rect.midright[0]-2, component.rect.midright[1]-2))
                WIN.blit(redsq, comprect(redsq, component.rect.midleft[0]-2, component.rect.midleft[1]-2))
            if maindata[count][12] == -90:
                WIN.blit(greensq, comprect(greensq, component.rect.midbottom[0]-2, component.rect.midbottom[1]-2))
                WIN.blit(redsq, comprect(redsq, component.rect.midtop[0]-2, component.rect.midtop[1]-2))
            if maindata[count][12] == -180:
                WIN.blit(greensq, comprect(greensq, component.rect.midleft[0]-2, component.rect.midleft[1]-2))
                WIN.blit(redsq, comprect(redsq, component.rect.midright[0]-2, component.rect.midright[1]-2))
            if maindata[count][12] == -270:
                WIN.blit(greensq, comprect(greensq, component.rect.midtop[0]-2, component.rect.midtop[1]-2))
                WIN.blit(redsq, comprect(redsq, component.rect.midbottom[0]-2, component.rect.midbottom[1]-2))
            count +=1
    except IndexError: # stops the program crashing if the database is empty
        pass
# creates the dropdown menu when the component is rightclicked
def presentmenu(text):
    try:
         global showmenu, wait, hover, textbox, textbox2, textbox3
        
         
         if showmenu == True: # checks if the compoennt has been rightclicked from dropdown()
             wait = True
             sr = True
             sv = True
             ss = True
             sf = True
             # draws the 3 main menu buttons
             WIN.blit(rotatebutton, comprect(rotatebutton, mx+10, my+33))
             WIN.blit(deletearrow, comprect(deletearrow, mx+10, my+10))
             WIN.blit(connectwire, comprect(connectwire, mx+10, my+54))
            

             # creates the coords of all the buttons
             dx = mx+10
             dy = my+10
             rx = mx+10
             ry = my+33
             px = mx+10
             py = my+54
             nx = mx+10
             ny = my+120

            # ctreates rectangles for all the buttons
             comp1rect = comp.get_rect(x=dx+75, y=dy)
             deletearrowrect = deletearrow.get_rect(x=dx, y=dy)
             rotatebuttonrect = rotatebutton.get_rect(x=rx, y=ry)
             connectwirerect = connectwire.get_rect(x=px, y=py)
             wiresrect = wires.get_rect(x=dx+75, y=dy+22)
             negativeterminalrect = negativeterminal.get_rect(x=dx+150, y=dy+22)
             positiveterminalrect = positiveterminal.get_rect(x=dx+150, y=dy+66)
             negativeterminal2rect = negativeterminal.get_rect(x=dx+75, y=dy+44)
             positiveterminal2rect = positiveterminal.get_rect(x=dx+75, y=dy+88)
             setresrect = setres.get_rect(x=dx, y=dy+88)

         # selects all data from tblcomponents and saves it to data
         cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
         data = cursor.fetchall()
         if data[saveid][1] == "Resistor":
             if sr == True:
                 WIN.blit(setres, comprect(setres, mx+10, my+98))
             if (setresrect.collidepoint(pygame.mouse.get_pos()) == True): # detects if the rotate button is hovered over
                 wait = True
                 WIN.blit(setresblue, comprect(setresblue, dx, dy+88)) # places a blue version of the button over the original
                 if (pygame.mouse.get_pressed(3)[0] == True):  # detects if the button is clciked
                     sr = False
                     textbox = True
                     if showmenu == True:
                         text =  ""
         if data[saveid][1] == "Cell": # checks if the component type is a cell
             if sv == True:
                 WIN.blit(setvolts, comprect(setres, mx+10, my+82)) # displays the set voltage button in the dropdown menu
             if (setresrect.collidepoint(pygame.mouse.get_pos()) == True): # detects if the setvoltage button is hovered over
                 wait = True
                 WIN.blit(setvoltsblue, comprect(setresblue, dx, dy+73)) # places a blue version of the button over the original
                 if (pygame.mouse.get_pressed(3)[0] == True):  # detects if the button is clciked
                     sv = False
                     textbox2 = True
                     if showmenu == True:
                         text =  ""
         if data[saveid][1] == "Fuse": # checks if the component type is a Fuse
             if sf == True:
                 WIN.blit(setamps, comprect(setres, mx+10, my+82)) # displays the set voltage button in the dropdown menu
             if (setresrect.collidepoint(pygame.mouse.get_pos()) == True): # detects if the setvoltage button is hovered over
                 wait = True
                 WIN.blit(setampsblue, comprect(setresblue, dx, dy+73)) # places a blue version of the button over the original
                 if (pygame.mouse.get_pressed(3)[0] == True):  # detects if the button is clciked
                     sf = False
                     textbox3 = True
                     if showmenu == True:
                         text =  ""
         if data[saveid][1] == "Switch": # checks if the component type is a switch
             cursor.execute('SELECT compID FROM tblpositiveconnections ORDER BY compID') # selcts compID from tblcomponents
             if ss == True:
                 WIN.blit(toggle, comprect(setres, mx+10, my+82))
             if (setresrect.collidepoint(pygame.mouse.get_pos()) == True): # detects if the rotate button is hovered over
                 wait = True
                 WIN.blit(toggleblue, comprect(setresblue, dx, dy+73)) # places a blue version of the button over the original
                 if (pygame.mouse.get_pressed(3)[0] == True):  # detects if the button is clciked
                     ss = False
                     # detects if the unique state of the switch is true or false
                     state = component_list.sprites()[saveid].uniquestate
                     # changes the current state of the switch
                     if state == False:
                         component_list.sprites()[saveid].uniquestate = True
                         cursor.execute("UPDATE tblpositiveconnections SET ignore=? WHERE compID=?", (False, dbid) )
                         conn.commit()
                     if state == True:
                         component_list.sprites()[saveid].uniquestate = False
                         cursor.execute("UPDATE tblpositiveconnections SET ignore=? WHERE compID=?", (True, dbid) )
                         conn.commit()
                         
                         

                     
             
         if (rotatebuttonrect.collidepoint(pygame.mouse.get_pos()) == True): # detects if the rotate button is hovered over
            wait = True
            WIN.blit(rotateblue, comprect(rotateblue, rx, ry)) # places a blue version of the button over the original 
            if (pygame.mouse.get_pressed(3)[0] == True):  # detects if the rotate button is clciked
               rotate(component_list.sprites()[saveid], dbid) # calls the rotate function 

            
         if (deletearrowrect.collidepoint(pygame.mouse.get_pos()) == True) or (comp1rect.collidepoint(pygame.mouse.get_pos()) == True) or (wiresrect.collidepoint(pygame.mouse.get_pos()) == True) or (negativeterminalrect.collidepoint(pygame.mouse.get_pos()) == True) or (positiveterminalrect.collidepoint(pygame.mouse.get_pos()) == True): # detects if the delete button or any of its sub buttons are hovered over
            wait = True
            # draws the sub buttons of the delete button, component and wires
            WIN.blit(comp, comprect(comp, dx+75, dy))
            WIN.blit(wires, comprect(comp, dx+75, dy+22))
            if (comp1rect.collidepoint(pygame.mouse.get_pos()) == True): # detects if the component button is hovered over
                WIN.blit(compblue, comprect(compblue, dx+75, dy)) # draws a blue component button over the original
                if (pygame.mouse.get_pressed(3)[0] == True): # detects if the component button is clicked
                    component_list.sprites()[saveid].kill() # deletes the sprite of the component that is selected
                    # deletes all instances of the selected component from all tables in the database
                    cursor.execute('SELECT * FROM tblcomponents')
                    cursor.execute('DELETE FROM tblcomponents WHERE "compID"=(?)', (dbid,))
                    cursor.execute('SELECT * FROM tblpositiveconnections')
                    cursor.execute('DELETE FROM tblpositiveconnections WHERE "compID"=(?)', (dbid,))
                    cursor.execute('DELETE FROM tblpositiveconnections WHERE "positiveterminalconnectedto"=(?)', (dbid,))
                    cursor.execute('SELECT * FROM tblnegativeconnections')
                    cursor.execute('DELETE FROM tblnegativeconnections WHERE "compID"=(?)', (dbid,))
                    cursor.execute('DELETE FROM tblnegativeconnections WHERE "negativeterminalconnectedto"=(?)', (dbid,))
                    conn.commit()
            if (wiresrect.collidepoint(pygame.mouse.get_pos()) == True) or (negativeterminalrect.collidepoint(pygame.mouse.get_pos()) == True) or (positiveterminalrect.collidepoint(pygame.mouse.get_pos()) == True): # detects if the wire option in the delte menu is hovered over
                # draws the neagtive and positive terminal buttons on the screen nex to the wires button
                WIN.blit(negativeterminal, comprect(negativeterminal, dx+150, dy+22))
                WIN.blit(positiveterminal, comprect(positiveterminal, dx+150, dy+66))
                if (negativeterminalrect.collidepoint(pygame.mouse.get_pos()) == True): # detects if the negative terminal button is hovered over
                    WIN.blit(negativeterminalblue, comprect(negativeterminalblue, dx+150, dy+22)) # draws a blue negative terminal button over the original
                    if (pygame.mouse.get_pressed(3)[0] == True): # detects if the negative terminal button is clicked
                        # deletes all instances of the negative connections of the selected component in the database
                        cursor.execute('SELECT * FROM tblnegativeconnections')
                        cursor.execute('DELETE FROM tblnegativeconnections WHERE "compID"=(?)', (dbid,))
                        cursor.execute('SELECT * FROM tblpositiveconnections')
                        cursor.execute('DELETE FROM tblpositiveconnections WHERE "positiveterminalconnectedto"=(?)', (dbid,))
                        conn.commit()
                if (positiveterminalrect.collidepoint(pygame.mouse.get_pos()) == True): # detects if the positive terminal button is hovered over
                    WIN.blit(positiveterminalblue, comprect(positiveterminalblue, dx+150, dy+66)) # draws a blue positive terminal button over the original
                    if (pygame.mouse.get_pressed(3)[0] == True): # detects if the positive terminal button is clicked
                        # deletes all instances of the negative connections of the selected component in the database
                        cursor.execute('SELECT * FROM tblpositiveconnections')
                        cursor.execute('DELETE FROM tblpositiveconnections WHERE "compID"=(?)', (dbid,))
                        cursor.execute('SELECT * FROM tblnegativeconnections')
                        cursor.execute('DELETE FROM tblnegativeconnections WHERE "negativeterminalconnectedto"=(?)', (dbid,))
                        conn.commit()
                    

            

         if (connectwirerect.collidepoint(pygame.mouse.get_pos()) == True) or (negativeterminal2rect.collidepoint(pygame.mouse.get_pos()) == True) or (positiveterminal2rect.collidepoint(pygame.mouse.get_pos()) == True):# detects if the mouse is over the connectwire button or any of its sbu buttons
            wait = True
            # displays positive and negative terminal buttons
            WIN.blit(negativeterminal, comprect(negativeterminal, dx+75, dy+44))
            WIN.blit(positiveterminal, comprect(positiveterminal, dx+75, dy+88))
            if (negativeterminal2rect.collidepoint(pygame.mouse.get_pos()) == True): # detects if the negative terminal button is hovered over
                    WIN.blit(negativeterminalblue, comprect(negativeterminalblue, dx+75, dy+44)) # draws a blue negative terminal button over the original
                    hover = True
                    if (pygame.mouse.get_pressed(3)[0] == True): # detects if the neagtive terminal button is clicked
                        # allows the negativeconnect function to run
                        global nconnectcheck
                        nconnectcheck = True
            if (positiveterminal2rect.collidepoint(pygame.mouse.get_pos()) == True): # detects if the positive terminal button is hovered over
                    WIN.blit(positiveterminalblue, comprect(positiveterminalblue, dx+75, dy+88)) # draws a blue positive terminal button over the original
                    hover = True
                    if (pygame.mouse.get_pressed(3)[0] == True): # detects if the positive terminal button is clicked
                        # allows the positiveconnect function to run
                        global pconnectcheck
                        pconnectcheck = True

         # sets up a textbox for the use to enter value for the resistance of the resistor   
         if textbox == True:
             WIN.blit(field, comprect(field, 800,350))# sets up the text field
             text_surface = bigfont.render(text, False, (0, 0, 0)) # creates a surface for the text
             WIN.blit(text_surface, (845, 382)) # places the text in the textbox
             # places the ok and cancel buttons in the textbox
             WIN.blit(ok, comprect(ok, 1125, 465))
             WIN.blit(cancel, comprect(cancel, 900, 465))
             # detects if the cancel or ok buttons are clicked
             if (cancelrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                 textbox = False
             if (okrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                 component_list.sprites()[saveid].resistance = float(text)
                 textbox = False

             return text # returns the value of the text
            
         # sets up a textbox for the use to enter value for the maximum current for the fuse  
         if textbox3 == True:
             WIN.blit(ampbox, comprect(field, 800,350))# sets up the text field
             text_surface = bigfont.render(text, False, (0, 0, 0)) # creates a surface for the text
             WIN.blit(text_surface, (845, 382)) # places the text in the textbox
             # places the ok and cancel buttons in the textbox
             WIN.blit(ok, comprect(ok, 1125, 465))
             WIN.blit(cancel, comprect(cancel, 900, 465))
             # detects if the cancel or ok buttons are clicked
             if (cancelrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                 textbox3 = False
             if (okrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                 component_list.sprites()[saveid].resistance = float(text)
                 textbox3 = False

             return text # returns the value of the text
            
         # sets up a textbox for the use to enter value for the voltage of the cell  
         if textbox2 == True:
             WIN.blit(voltbox, comprect(voltbox, 800,350))# sets up the text field
             text_surface = bigfont.render(text, False, (0, 0, 0)) # creates a surface for the text
             WIN.blit(text_surface, (845, 382)) # places the text in the textbox
             # places the ok and cancel buttons in the textbox
             WIN.blit(ok, comprect(ok, 1125, 465))
             WIN.blit(cancel, comprect(cancel, 900, 465))
             # detects if the cancel or ok buttons are clicked
             if (cancelrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                 textbox2 = False
             if (okrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                 component_list.sprites()[saveid].voltage = float(text)
                 textbox2 = False

             return text # returns the value of the text
         else:
             return text # returns the value of the text
         

             


    except: # stops the program crashing when the database is empty
        # sets up a textbox for the use to enter value for the resistance of the resistor   
        if textbox == True:
             WIN.blit(field, comprect(field, 800,350))# sets up the text field
             text_surface = bigfont.render(text, False, (0, 0, 0)) # creates a surface for the text
             WIN.blit(text_surface, (845, 382)) # places the text in the textbox
             # places the ok and cancel buttons in the textbox
             WIN.blit(ok, comprect(ok, 1125, 465))
             WIN.blit(cancel, comprect(cancel, 900, 465))
             # detects if the cancel or ok buttons are clicked
             if (cancelrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                 textbox = False
             if (okrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                 component_list.sprites()[saveid].resistance = float(text)
                 textbox = False
             return text # returns the value of the text
            
        # sets up a textbox for the use to enter value for the maximum current for the fuse    
        if textbox3 == True:
             WIN.blit(ampbox, comprect(field, 800,350))# sets up the text field
             text_surface = bigfont.render(text, False, (0, 0, 0)) # creates a surface for the text
             WIN.blit(text_surface, (845, 382)) # places the text in the textbox
             # places the ok and cancel buttons in the textbox
             WIN.blit(ok, comprect(ok, 1125, 465))
             WIN.blit(cancel, comprect(cancel, 900, 465))
             # detects if the cancel or ok buttons are clicked
             if (cancelrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                 textbox3 = False
             if (okrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                 component_list.sprites()[saveid].resistance = float(text)
                 textbox3 = False

             return text # returns the value of the text

        # sets up a textbox for the use to enter value for the voltage of the cell  
        if textbox2 == True:
             WIN.blit(voltbox, comprect(voltbox, 800,350))# sets up the text field
             text_surface = bigfont.render(text, False, (0, 0, 0)) # creates a surface for the text
             WIN.blit(text_surface, (845, 382)) # places the text in the textbox
             # places the ok and cancel buttons in the textbox
             WIN.blit(ok, comprect(ok, 1125, 465))
             WIN.blit(cancel, comprect(cancel, 900, 465))
             # detects if the cancel or ok buttons are clicked
             if (cancelrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                 textbox2 = False
             if (okrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                 component_list.sprites()[saveid].voltage = float(text)
                 textbox2 = False

             return text # returns the value of the text
        else:
             return text # returns the value of the text


# adds all of the positive terminal data to the database when 2 components are connected
def positiveconnect():
   try:
        global pconnectcheck, wincolour
        wincolour = 255, 216, 216 # sets the window to red
        fail = True
        count = 0
        count2 = 0
        # selects necessary data from tblcomponents and tblpositiveconnections
        cursor.execute('SELECT compID FROM tblcomponents ORDER BY compID')
        data = cursor.fetchall()
        cursor.execute('SELECT * FROM tblpositiveconnections ORDER BY compID')
        connectdata = cursor.fetchall()
        for component in component_list: # initiates a loop for all components in the databse
            idnumber = data[count][0] # sets idnumber to the compid value in tblcomponents
            count += 1
            if (pygame.mouse.get_pressed(3)[0] == True) and (component.rect.collidepoint(pygame.mouse.get_pos()) == True): # detects if a component is clicked 
                fail = False
                for row in connectdata:
                    if (connectdata[count2][1] == dbid) and (connectdata[count2][2] == idnumber): # detects if the clicked component was the original one selected in the dropdown menu
                        pconnectcheck = False
                        fail = True
                    count2 += 1
                # if fail is true meaning a new component was clicked all relevant terminal data is added to the database
                if fail == False:  
                    cursor.execute("INSERT INTO tblpositiveconnections VALUES (NULL, ?, ?, ?, ?)", (dbid, idnumber, 0, False)) # inserts original component - new component in tblpositiveconnections
                    cursor.execute("INSERT INTO tblnegativeconnections VALUES (NULL, ?, ?, ?)", (idnumber, dbid, 0)) # inserts new component - original component in tblneagtiveconnections
                    pconnectcheck = False
                    wincolour = 241, 241, 250 # sets the window back to the original colour
                    # selects all data from tblpositiveconnections
                    cursor.execute('SELECT * FROM tblpositiveconnections')
                    data = cursor.fetchall()
                    loopcount = -1
                    connectcount = 0
                    for item in data: # loops for all lines in tblcomponents
                        loopcount += 1
                        # detects how many times the component appears and sets the connectamount variable to that value
                        if data[loopcount][1] == dbid:
                            connectcount += 1 
                            cursor.execute("UPDATE tblpositiveconnections SET connectamount=? WHERE compID=?", (connectcount, dbid) ) # updates the database with how many connections the component has
                            conn.commit()
                    # identifies amount of negative connections using the same method as the positive terminal counter
                    cursor.execute('SELECT * FROM tblnegativeconnections')
                    data = cursor.fetchall()
                    loopcount = -1
                    connectcount = 0
                    for item in data:
                        loopcount += 1
                        if data[loopcount][1] == idnumber:
                            connectcount += 1
                            cursor.execute("UPDATE tblnegativeconnections SET connectamount=? WHERE compID=?", (connectcount, idnumber) )
                            conn.commit()
            # cancels the function if the screen is clicked while not hovering over a component
            if (pygame.mouse.get_pressed(3)[0] == True) and (component.rect.collidepoint(pygame.mouse.get_pos()) == False) and (md == True):
                pconnectcheck = False
                wincolour = 241, 241, 250
   except IndexError: # stops the program crashing if the database is empty
        pass
#7
def negativeconnect():
    try:
        global nconnectcheck, wincolour
        wincolour = 255, 216, 216 # sets the window to red
        fail = True
        count = 0
        count2 = 0
        # selects necessary data from tblcomponents and tblnegativeconnections
        cursor.execute('SELECT compID FROM tblcomponents ORDER BY compID')
        data = cursor.fetchall()
        cursor.execute('SELECT * FROM tblnegativeconnections ORDER BY compID')
        connectdata = cursor.fetchall()
        for component in component_list: # initiates a loop for all components in the databse
            idnumber = data[count][0] # sets idnumber to the compid value in tblcomponents
            count += 1
            if (pygame.mouse.get_pressed(3)[0] == True) and (component.rect.collidepoint(pygame.mouse.get_pos()) == True): # detects if a component is clicked 
                fail = False
                for row in connectdata:
                    if (connectdata[count2][1] == dbid) and (connectdata[count2][2] == idnumber): # detects if the clicked component was the original one selected in the dropdown menu
                        pconnectcheck = False
                        fail = True
                    count2 += 1
                # if fail is true meaning a new component was clicked all relevant terminal data is added to the database
                if fail == False:  
                    cursor.execute("INSERT INTO tblnegativeconnections VALUES (NULL, ?, ?, ?)", (dbid, idnumber, 0)) # inserts original component - new component in tblnegativeconnections
                    cursor.execute("INSERT INTO tblpositiveconnections VALUES (NULL, ?, ?, ?, ?)", (idnumber, dbid, 0, False))  # inserts new component - original component in tblpositiveconnections
                    nconnectcheck = False
                    wincolour = 241, 241, 250 # sets the window back to the original colour
                    # selects all data from tblnegativeconnections
                    cursor.execute('SELECT * FROM tblnegativeconnections')
                    data = cursor.fetchall()
                    loopcount = -1
                    connectcount = 0
                    for item in data: # loops for all lines in tblcomponents
                        loopcount += 1
                        # detects how many times the component appears and sets the connectamount variable to that value
                        if data[loopcount][1] == dbid:
                            connectcount += 1
                            cursor.execute("UPDATE tblnegativeconnections SET connectamount=? WHERE compID=?", (connectcount, dbid) ) # updates the database with how many connections the component has
                            conn.commit()
                    # identifies amount of negative connections using the same method as the negative terminal counter
                    cursor.execute('SELECT * FROM tblpositiveconnections')
                    data = cursor.fetchall()
                    loopcount = -1
                    connectcount = 0
                    for item in data:
                        loopcount += 1
                        if data[loopcount][1] == idnumber:
                            connectcount += 1
                            cursor.execute("UPDATE tblpositiveconnections SET connectamount=? WHERE compID=?", (connectcount, idnumber) )
                            conn.commit()
            # cancels the function if the screen is clicked while not hovering over a component
            if (pygame.mouse.get_pressed(3)[0] == True) and (component.rect.collidepoint(pygame.mouse.get_pos()) == False) and (md == True):
                nconnectcheck = False
                wincolour = 241, 241, 250
            
    except IndexError: # stops the program crashing if the database is empty
        pass
    
# draws all the wires for positive connections
def pconnections():
    try:
        # selects all necessary data
        cursor.execute('SELECT * FROM tblpositiveconnections ORDER BY compID')
        data = cursor.fetchall()
        cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
        maindata = cursor.fetchall()
        count = 0
        count2 = 0
        count3 = 0
        for row in data: # creates a loop for all the lines in the connection table
            origin = data[count][1]
            connection = data[count][2]
            count+=1
            count2 = 0
            for component in component_list: # starts a loop for every componenet
                compid = maindata[count2][0]
                if compid == origin: # detects if the origin component matches an id in the table
                    # creates a list ctypes with a value of 0 - 3 depending on the components rotation
                    if maindata[count2][12] == 0: 
                        sx = maindata[count2][8]
                        sy = maindata[count2][9]
                        ctype = [0]
                    if maindata[count2][12] == -90:
                        sx = maindata[count2][6]
                        sy = maindata[count2][7]
                        ctype = [1]
                    if maindata[count2][12] == -180:
                        sx = maindata[count2][4]
                        sy = maindata[count2][5]
                        ctype = [2]
                    if maindata[count2][12] == -270:
                        sx = maindata[count2][10]
                        sy = maindata[count2][11]
                        ctype = [3]
                    count3 = 0
                    for component in component_list:
                        if connection == maindata[count3][0]:  # detects if the connecting component matches an id in the table
                            # appends to list ctypes with a value of 0 - 3 depending on the components rotation
                            if maindata[count3][12] == 0: 
                                ex = maindata[count3][4]
                                ey = maindata[count3][5]
                                ctype.append(0)
                            if maindata[count3][12] == -90:
                                ex = maindata[count3][10]
                                ey = maindata[count3][11]
                                ctype.append(1)
                            if maindata[count3][12] == -180:
                                ex = maindata[count3][8]
                                ey = maindata[count3][9]
                                ctype.append(2)
                            if maindata[count3][12] == -270:
                                ex = maindata[count3][6]
                                ey = maindata[count3][7]
                                ctype.append(3)
                            # depending on tha values in ctypes the program will draw the most suitable turining at points using functions of the components x and y cooridinates 
                            if ctype == [0, 1]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (ex, sy), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, sy), (ex, ey), (3))
                            if ctype == [1, 0]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, ey), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, ey), (ex, ey), (3))
                            if ctype == [0, 3]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (ex, sy), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, sy), (ex, ey), (3))
                            if ctype == [2, 1]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (ex, sy), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, sy), (ex, ey), (3))
                            if ctype == [1, 2]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, ey), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, ey), (ex, ey), (3))
                            if ctype == [3, 0]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, ey), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, ey), (ex, ey), (3))
                            if ctype == [3, 2]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, ey), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, ey), (ex, ey), (3))
                            if ctype == [2, 3]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (ex, sy), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, sy), (ex, ey), (3))
                            if ctype == [3, 3]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, (sy+ey)/2), (ex, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, (sy+ey)/2), (ex, ey), (3))
                            if ctype == [1, 1]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, (sy+ey)/2), (ex, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, (sy+ey)/2), (ex, ey), (3))
                            if ctype == [1, 3]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, (sy+ey)/2), (ex, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, (sy+ey)/2), (ex, ey), (3))
                            if ctype == [3, 1]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, (sy+ey)/2), (ex, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, (sy+ey)/2), (ex, ey), (3))
                            if ctype == [0, 0]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), ((sx+ex)/2, sy), (3))
                                pygame.draw.line(WIN, (0,0,0), ((sx+ex)/2, sy), ((sx+ex)/2, ey), (3))
                                pygame.draw.line(WIN, (0,0,0), ((sx+ex)/2, ey), (ex, ey), (3))
                            if ctype == [0, 2]:
                                 if sx > ex:
                                    pygame.draw.line(WIN, (0,0,0), (sx, sy), ((sx+50), sy), (3))
                                    pygame.draw.line(WIN, (0,0,0), (sx+50, sy), ((sx+50), ey), (3))
                                    pygame.draw.line(WIN, (0,0,0), ((sx+50), ey), (ex, ey), (3))
                            if ctype == [2, 0]:
                                if sx < ex:
                                    pygame.draw.line(WIN, (0,0,0), (sx, sy), ((sx-50), sy), (3))
                                    pygame.draw.line(WIN, (0,0,0), (sx-50, sy), ((sx-50), ey), (3))
                                    pygame.draw.line(WIN, (0,0,0), ((sx-50), ey), (ex, ey), (3))
                            if ctype == [2, 2]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), ((sx+ex)/2, sy), (3))
                                pygame.draw.line(WIN, (0,0,0), ((sx+ex)/2, sy), ((sx+ex)/2, ey), (3))
                                pygame.draw.line(WIN, (0,0,0), ((sx+ex)/2, ey), (ex, ey), (3))
                        count3+=1
                count2+=1          
        
    except IndexError:
        pass
#7           
def nconnections():
    try:
        # selects all necessary data
        cursor.execute('SELECT * FROM tblnegativeconnections ORDER BY compID')
        data = cursor.fetchall()
        cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
        maindata = cursor.fetchall()
        count = 0
        count2 = 0
        count3 = 0
        for row in data: # creates a loop for all the lines in the connection table
            origin = data[count][1]
            connection = data[count][2]
            count+=1
            count2 = 0
            for component in component_list: # starts a loop for every componenet
                compid = maindata[count2][0]
                if compid == origin: # detects if the origin component matches an id in the table
                    # creates a list ctypes with a value of 0 - 3 depending on the components rotation
                    if maindata[count2][12] == 0:
                        sx = maindata[count2][4]
                        sy = maindata[count2][5]
                        ctype = [0]
                    if maindata[count2][12] == -90:
                        sx = maindata[count2][10]
                        sy = maindata[count2][11]
                        ctype = [1]
                    if maindata[count2][12] == -180:
                        sx = maindata[count2][8]
                        sy = maindata[count2][9]
                        ctype = [2]
                    if maindata[count2][12] == -270:
                        sx = maindata[count2][6]
                        sy = maindata[count2][7]
                        ctype = [3]
                    count3 = 0
                    for component in component_list:
                        if connection == maindata[count3][0]: # detects if the connecting component matches an id in the table
                            # appends to list ctypes with a value of 0 - 3 depending on the components rotation
                            if maindata[count3][12] == 0:
                                ex = maindata[count3][8]
                                ey = maindata[count3][9]
                                ctype.append(0)
                            if maindata[count3][12] == -90:
                                ex = maindata[count3][6]
                                ey = maindata[count3][7]
                                ctype.append(1)
                            if maindata[count3][12] == -180:
                                ex = maindata[count3][4]
                                ey = maindata[count3][5]
                                ctype.append(2)
                            if maindata[count3][12] == -270:
                                ex = maindata[count3][10]
                                ey = maindata[count3][11]
                                ctype.append(3)
                             # depending on tha values in ctypes the program will draw the most suitable turining at points using functions of the components x and y cooridinates 
                            if ctype == [0, 1]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (ex, sy), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, sy), (ex, ey), (3))
                            if ctype == [1, 0]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, ey), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, ey), (ex, ey), (3))
                            if ctype == [0, 3]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (ex, sy), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, sy), (ex, ey), (3))
                            if ctype == [2, 1]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (ex, sy), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, sy), (ex, ey), (3))
                            if ctype == [1, 2]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, ey), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, ey), (ex, ey), (3))
                            if ctype == [3, 0]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, ey), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, ey), (ex, ey), (3))
                            if ctype == [3, 2]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, ey), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, ey), (ex, ey), (3))
                            if ctype == [2, 3]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (ex, sy), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, sy), (ex, ey), (3))
                            if ctype == [3, 3]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, (sy+ey)/2), (ex, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, (sy+ey)/2), (ex, ey), (3))
                            if ctype == [1, 1]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, (sy+ey)/2), (ex, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, (sy+ey)/2), (ex, ey), (3))
                            if ctype == [1, 3]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, (sy+ey)/2), (ex, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, (sy+ey)/2), (ex, ey), (3))
                            if ctype == [3, 1]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), (sx, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (sx, (sy+ey)/2), (ex, (sy+ey)/2), (3))
                                pygame.draw.line(WIN, (0,0,0), (ex, (sy+ey)/2), (ex, ey), (3))
                            if ctype == [0, 0]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), ((sx+ex)/2, sy), (3))
                                pygame.draw.line(WIN, (0,0,0), ((sx+ex)/2, sy), ((sx+ex)/2, ey), (3))
                                pygame.draw.line(WIN, (0,0,0), ((sx+ex)/2, ey), (ex, ey), (3))
                            if ctype == [0, 2]:
                                if sx < ex:
                                    pygame.draw.line(WIN, (0,0,0), (sx, sy), ((sx-50), sy), (3))
                                    pygame.draw.line(WIN, (0,0,0), (sx-50, sy), ((sx-50), ey), (3))
                                    pygame.draw.line(WIN, (0,0,0), ((sx-50), ey), (ex, ey), (3))
                            if ctype == [2, 0]:
                                if sx > ex:
                                    pygame.draw.line(WIN, (0,0,0), (sx, sy), ((sx+50), sy), (3))
                                    pygame.draw.line(WIN, (0,0,0), (sx+50, sy), ((sx+50), ey), (3))
                                    pygame.draw.line(WIN, (0,0,0), ((sx+50), ey), (ex, ey), (3))
                            if ctype == [2, 2]:
                                pygame.draw.line(WIN, (0,0,0), (sx, sy), ((sx+ex)/2, sy), (3))
                                pygame.draw.line(WIN, (0,0,0), ((sx+ex)/2, sy), ((sx+ex)/2, ey), (3))
                                pygame.draw.line(WIN, (0,0,0), ((sx+ex)/2, ey), (ex, ey), (3))
                        count3+=1
                count2+=1          
        
    except IndexError:
        pass
              
            

# sets all components to unpowered
def reset():    
        count = 0
        # selects compid from tblcomponents and saves it do data
        cursor.execute('SELECT compID FROM tblcomponents ORDER BY compID')
        data = cursor.fetchall()
        for component in component_list: # initiates a loop of every component
            # sets the components powered value to flase in the database
            idnumber = data[count][0]
            cursor.execute("UPDATE tblcomponents SET powered=? WHERE compID=?", (False, idnumber) )
            conn.commit()
            count += 1

# stores coordinates of all faces of a components   
def wirecoords():
    try:
        count = 0
        # selects compid from tblcomponents and saves it do data
        cursor.execute('SELECT compID FROM tblcomponents ORDER BY compID')
        data = cursor.fetchall()
        for component in component_list: # initiates a loop of all components
            idnumber = data[count][0]
            # stores all the needed face coordinates of the component
            cursor.execute("UPDATE tblcomponents SET midleftx=?, midlefty=?, midbottomx=?, midbottomy=?, midrightx=?, midrighty=?, midtopx=?, midtopy=? WHERE compID=?", (component.rect.midleft[0], component.rect.midleft[1], component.rect.midbottom[0], component.rect.midbottom[1], component.rect.midright[0], component.rect.midright[1], component.rect.midtop[0], component.rect.midtop[1], idnumber) )
            conn.commit()
            count += 1
    except IndexError:
        pass

# detetcs if the playbutton is clicked
def playbutton():
            if (playrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                runstate = True
                return runstate
            return False

#detects if the pause button is clicked
def pausebutton():
            if (playrect.collidepoint(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed(3)[0] == True):
                runstate = False
                reset()
                return runstate
            return True
                


def check_powered(cellislist):
        count = -1
        level = 1
        # selects all data from tblcomponents and saves it to data
        cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
        data = cursor.fetchall()
        for component in component_list: # initialises a loop of all components
            count += 1
            if data[count][1] == "Cell": # detects if a component is a cell
                # saves its id to cellid and appends it to cellidlist
                cellid = data[count][0]
                cellidlist.append(cellid)
        while cellidlist != []: # runs the loop for all cells in cellidlist
            # takes the first value of cellidlist, saves it to cellid then removes it from the list
            cellid = cellidlist[0]
            connectedcomp = cellid
            cellidlist.pop(0)
            # selects all values from tblpositiveconnections and saves it to data
            cursor.execute('SELECT * FROM tblpositiveconnections ORDER BY compID')
            data = cursor.fetchall()
            # defines all the variables needed by the function
            count = -1
            branches = []
            cycles = 0
            compcount = 999999
            rangevalue = 0
            empty = False
            total = 0
            while total <= len(component_list): # runs the command untill a loop has been powered for the number of components
                rangevalue += 1
                count += 1
                if cycles >= len(component_list) or empty == True: # runs when a branch is empty or all components have been powered
                    # searches the list branches and sets the connected comp to the count stored there + amount of times it appears in the list
                    cycles = 0
                    temp = compcount
                    compcount = branches[0]
                    connections = 0
                    for comp in branches:
                        if comp == compcount:
                            connections +=1
                    connectedcomp = data[compcount+connections][2]
                    # resets all variables and removes one instance of the index 0 value from branches
                    connections = 0
                    branches.pop(0)
                    count = 0
                    empty = False

                if (data[count][1] == connectedcomp) and (data[count][4] == False): # checks if the selected item from the databse is the same as then connectedcomp
                        
                    cycles += 1
                    if data[count][3] >= 2: # detects if the component has 2 or more connections
                        level = 2
                        if (count not in branches) and (count != compcount):
                            # appends the component to branches for all of its connections so the program can bo back to the split later on
                            for i in range(data[count][3]-1):
                                branches.append(count)

                    cursor.execute('SELECT * FROM tblnegativeconnections ORDER BY compID')
                    negdata = cursor.fetchall()
                    for line in negdata:
                        if line[1] == data[count][2]:
                            if line[3] >= 2:
                                level = 0
                        
                    count2 = -1
                    # checks if a component has no other component connected to its positive terminal
                    empty = True
                    for lines in data:
                        count2 += 1
                        if data[count][2] == data[count2][1]:
                            empty = False
                    
                    connectedcomp = data[count][2] # sets the connectedcomp to the next component in the circuit
                    count = -1
                    if connectedcomp == cellid: # checks if the current connectedcomp is equal to the original cellid
                        # runst the same code above but poweres all the components as they are selected
                        # defines all the variables needed by the function
                        total += 1
                        count = -1
                        empty = False
                        cursor.execute('SELECT * FROM tblpositiveconnections ORDER BY compID')
                        data = cursor.fetchall()
                        branches = []
                        cycles = 0
                        compcount = 999999
                        while total <= len(component_list): # runs the command untill a loop has been powered for the number of components
                            count += 1
                            if cycles >= len(component_list) or empty == True: # runs when a branch is empty or all components have been powered
                            # searches the list branches and sets the connected comp to the count stored there + amount of times it appears in the list
                                cycles = 0
                                temp = compcount
                                compcount = branches[0]
                                connections = 0
                                for comp in branches:
                                    if comp == compcount:
                                        connections +=1
                                connectedcomp = data[compcount+connections][2]
                                # resets all variables and removes one instance of the index 0 value from branches
                                connections = 0
                                branches.pop(0)
                                count = 0
                                empty = False


                            if (data[count][1] == connectedcomp) and (data[count][4] == False): # checks if the selected item from the databse is the same as then connectedcomp
                                cycles += 1
                                if data[count][3] >= 2:
                                    if (count not in branches) and (count != compcount):
                                        for i in range(data[count][3]-1):
                                            branches.append(count)

                                count2 = -1
                                empty = True
                                for lines in data:
                                    count2 += 1
                                    if (data[count][2] == data[count2][1]):
                                        empty = False

        
                                
                                cursor.execute("UPDATE tblcomponents SET powered=? WHERE compID=?", (True, connectedcomp) )
                                conn.commit()
                                

                                if (empty == True):
                                    ended = data[count][1]
                                    count3 = -1
                                    for i in range(len(component_list)**2):
                                        count3 += 1
                                        if data[count3][1] == ended:
                                            if data[count3][3] >= 2:
                                                break
                                            cursor.execute("UPDATE tblcomponents SET powered=? WHERE compID=?", (False, ended) )
                                            conn.commit()
                                            count3 = -1
                                            count4 = -1
                                            for i in range(len(component_list)**2):
                                                count4 += 1
                                                if data[count4][2] == ended:
                                                    ended = data[count4][1]
                                                    count4 = -1
                                                    break
                                                    
                                    
                        
                                connectedcomp = data[count][2]
                                if connectedcomp == cellid:
                                    total += 1
                                count = -1

            
            
        
                  
                                
                                    
def power_components():
    count = -1
    cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
    data = cursor.fetchall()
    for component in component_list:
        if data[count][1] != ("Switc"):  
            count += 1
            if data[count][16] == False:
                component.image = component.originalimage
            if data[count][16] == True:
                component.image = component.closedimage
            if data[count][13] == True and data[count][16] == False:
                    component.image = component.poweredimage
            cursor.execute("UPDATE tblcomponents SET rotation=? WHERE rotation=?", (0, -360) )
            if data[count][12] == 0:
                altered_image =  component.image = pygame.transform.rotate(component.image, 0)
                drawn_image = altered_image # altered_image() is whatever changes you're making to the image before it's drawn
                image_location = drawn_image.get_rect(center=component.rect.center) #returns the Surface's rect with rect.center set to the center of the object
                component.image, component.rect = (drawn_image, image_location)
            if data[count][12] == -90:
                altered_image =  component.image = pygame.transform.rotate(component.image, -90)
                drawn_image = altered_image # altered_image() is whatever changes you're making to the image before it's drawn
                image_location = drawn_image.get_rect(center=component.rect.center) #returns the Surface's rect with rect.center set to the center of the object
                component.image, component.rect = (drawn_image, image_location)
            if data[count][12] == -180:
                altered_image =  component.image = pygame.transform.rotate(component.image, -180)
                drawn_image = altered_image # altered_image() is whatever changes you're making to the image before it's drawn
                image_location = drawn_image.get_rect(center=component.rect.center) #returns the Surface's rect with rect.center set to the center of the object
                component.image, component.rect = (drawn_image, image_location)
            if data[count][12] == -270:
                altered_image =  component.image = pygame.transform.rotate(component.image, -270)
                drawn_image = altered_image # altered_image() is whatever changes you're making to the image before it's drawn
                image_location = drawn_image.get_rect(center=component.rect.center) #returns the Surface's rect with rect.center set to the center of the object
                component.image, component.rect = (drawn_image, image_location)




def resistancetext():
    count = -1
    # selects all data from tblcomponents and saves it to data
    cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
    data = cursor.fetchall()
    for component in component_list: # initialises a loop of all components
        count += 1
        if data[count][1] == "Resistor": # detects if the selcted component is a resistor
            value = component.resistance # sets the resistance to the value of the component
            # detects the magnitude of the resistance and selects an appropriate unit to display
            unit = "Ω"
            if value < 1:
                value *=1000
                unit = "mΩ"
                if value < 1:
                    value *=1000
                    unit = "µΩ"
                if value < 1:
                    value *= 1000
                    unit = "nΩ"
            if value >= 1000:
                value /= 1000
                unit = "KΩ"
                if value >= 1000:
                    value /= 1000
                    unit = "MΩ"
                    if value >= 1000:
                        value /= 1000
                        unit = "GΩ"
                        value = round(float(value))
                        if value >= 1000:
                            value /= 1000
                            unit = "TΩ"
            # rounds the resistance value to an appropriate amount of decimal places
            text = str(round(float(value))) + unit
            if value <= 9.9:
                value = round(value, 1)
                if (value*10)%10 == 0:
                    value = round(value)
                text = str(value) + unit
            
            
            # displays the resitance text on to the resistor
            text_surface = font.render(text, False, (0, 0, 0))
            if data[count][12] == -90 or data[count][12] == -270:
                text_surface = pygame.transform.rotate(text_surface, 90)
                WIN.blit(text_surface, (component.rect.x-3, component.rect.y+6))
            else:
                WIN.blit(text_surface, (component.rect.x+3, component.rect.y-2))

def voltagetext():
    count = -1
    # selects all data from tblcomponents and saves it to data
    cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
    data = cursor.fetchall()
    for component in component_list: # initialises a loop of all components
        count += 1
        if data[count][1] == "Cell": # detects if the component is a cell
            value = component.voltage # sets voltage to the voltage of the cell
            # detects the magnitude of the voltage and sets an appropriate unit to display
            unit = "V"
            if value < 1:
                value *=1000
                unit = "mV"
                if value < 1:
                    value *=1000
                    unit = "µV"
                    if value < 1:
                        value *= 1000
                        unit = "nV"
            if value >= 1000:
                value /= 1000
                unit = "KV"
                if value >= 1000:
                    value /= 1000
                    unit = "MV"
                    if value >= 1000:
                        value /= 1000
                        unit = "GV"
                        value = round(float(value))
                        if value >= 1000:
                            value /= 1000
                            unit = "TV"
            # rounds the value to an appropriate amount of decimal places
            text = str(round(float(value))) + unit
            if value <= 9.9:
                value = round(value, 1)
                if (value*10)%10 == 0:
                    value = round(value)
                text = str(value) + unit
            
            
            # displays the voltage above the cell
            text_surface = font.render(text, False, (0, 0, 0))
            if data[count][12] == -90 or data[count][12] == -270:
                text_surface = pygame.transform.rotate(text_surface, 90)
                WIN.blit(text_surface, (component.rect.x-22, component.rect.y))
            else:
                WIN.blit(text_surface, (component.rect.x, component.rect.y-19))


def switch():
    count = -1
    # selects all data from tblcomponents and saves it to data
    cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
    data = cursor.fetchall()
    for component in component_list: # initialises a loop of all components
        count += 1
        if data[count][1] == "Switch":
            if component.uniquestate == True:
                component.image = component.closedimage
            if component.uniquestate == False:
                component.image = component.originalimage

    



def ohmslaw():
    try:
        # selects all components from tblcomponents
        cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
        data = cursor.fetchall()
        branchvoltage = 0
        branchresistance = 0
        count = -1
        for item in data:
            count += 1
            if item[13] == True and item[1] != "Fuse": # detects if an item is powered or is a fuse
                 # adds up all the resitances in the branch
                branchresistance += component_list.sprites()[count].resistance
                if item[1] == "Cell": # detects if the component is a cell
                    # adds the voltage of all the cells
                    branchvoltage += component_list.sprites()[count].voltage
        # divides the total voltage of the branch by the total resistance
        currentofbranch = branchvoltage/branchresistance
        return currentofbranch # returns the resistance of the branch
    except:
        1

def voltages():
    # selects all data from tblcomponents
    cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
    data = cursor.fetchall()
    for component in data:
        if component[1] == "Voltmeter": # detects if the component is a voltmeter
            compid = component[0]
            cursor.execute('SELECT * FROM tblpositiveconnections ORDER BY compID')
            connectdata = cursor.fetchall()
            for connection in connectdata:
                if connection[1] == compid:
                    # detects what component the voltmneter is measuring
                    testing = connection[2]
                    for component in data:
                        if component[0] == testing:
                            resistance = int(component[14]) # finds the resistnace of the measured component
                            try:
                                voltage = (ohmslaw()*resistance)# calculates the voltage over the component
                            except:
                                voltage = 0
            try:
                count = -1
                # selects all data from tblcomponents and saves it to data
                cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
                data = cursor.fetchall()
                for component in component_list: # initialises a loop of all components
                    count += 1
                    if data[count][0] == compid: # detects if the selected component is a voltmeter
                        # sets the voltage value with appropriate units
                        value = voltage
                        unit = "V"
                        if value < 1:
                            value *=1000
                            unit = "mV"
                            if value < 1:
                                value *=1000
                                unit = "µV"
                                if value < 1:
                                    value *= 1000
                                    unit = "nV"
                        if value >= 1000:
                            value /= 1000
                            unit = "KV"
                            if value >= 1000:
                                value /= 1000
                                unit = "MV"
                                if value >= 1000:
                                    value /= 1000
                                    unit = "GV"
                                    value = round(float(value))
                                    if value >= 1000:
                                        value /= 1000
                                        unit = "TV"
                        # rounds the voltage to a suitable amount of decimal places
                        text = str(round(float(value))) + unit
                        if value <= 9.9:
                            value = round(value, 1)
                            if (value*10)%10 == 0:
                                value = round(value)
                            text = str(value) + unit
                                        
                                        
                        # displays the text on the voltmeter
                        text_surface = font.render(text, False, (0, 0, 0))
                        if data[count][12] == -90 or data[count][12] == -270:
                            text_surface = pygame.transform.rotate(text_surface, 90)
                            WIN.blit(text_surface, (component.rect.x-22, component.rect.y))
                        else:
                            WIN.blit(text_surface, (component.rect.x, component.rect.y-19))
            except:
                text_surface = font.render("0V", False, (0, 0, 0))
                if data[count][12] == -90 or data[count][12] == -270:
                    text_surface = pygame.transform.rotate(text_surface, 90)
                    WIN.blit(text_surface, (component.rect.x-22, component.rect.y))
                else:
                    WIN.blit(text_surface, (component.rect.x, component.rect.y-19))
                                                    
                                
def ammetertext():
    try:
        count = -1
        # selects all data from tblcomponents and saves it to data
        cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
        data = cursor.fetchall()
        for component in component_list: # initialises a loop of all components
            count += 1
            if data[count][1] == "Ammeter": # detects if the component is an ammeter
                value = ohmslaw() # determines the current using the ohmslaw function
                if value == 0:
                    raise exception
                    
                # selects a suitable unit for the current
                unit = "A"
                if value < 1:
                    value *=1000
                    unit = "mA"
                    if value < 1:
                        value *=1000
                        unit = "µA"
                        if value < 1:
                            value *= 1000
                            unit = "nA"
                if value >= 1000:
                    value /= 1000
                    unit = "KA"
                    if value >= 1000:
                        value /= 1000
                        unit = "MA"
                        if value >= 1000:
                            value /= 1000
                            unit = "GA"
                            value = round(float(value))
                            if value >= 1000:
                                value /= 1000
                                unit = "TA"
                # rounds the current to an appropriate amount of decimal places
                text = str(round(float(value))) + unit
                if value <= 9.9:
                    value = round(value, 1)
                    if (value*10)%10 == 0:
                        value = round(value)
                    text = str(value) + unit
                
                
                # displays the current on the ammmeter
                text_surface = font.render(text, False, (0, 0, 0))
                if data[count][12] == -90 or data[count][12] == -270:
                    text_surface = pygame.transform.rotate(text_surface, 90)
                    WIN.blit(text_surface, (component.rect.x-22, component.rect.y))
                else:
                    WIN.blit(text_surface, (component.rect.x, component.rect.y-19))
    except :
        text_surface = font.render("0A", False, (0, 0, 0))
        if data[count][12] == -90 or data[count][12] == -270:
            text_surface = pygame.transform.rotate(text_surface, 90)
            WIN.blit(text_surface, (component.rect.x-22, component.rect.y))
        else:
            WIN.blit(text_surface, (component.rect.x, component.rect.y-19))

def fusecheck():
    try:
        count = -1
        # selects all data from tblcomponents and saves it to data
        cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
        data = cursor.fetchall()
        for component in component_list: # initialises a loop of all components
            count += 1
            if data[count][1] == "Fuse": # detects if the component is a fuse
                value = data[count][14]
                # selects a suitable unit for the current
                unit = "A"
                if value < 1:
                    value *=1000
                    unit = "mA"
                    if value < 1:
                        value *=1000
                        unit = "µA"
                        if value < 1:
                            value *= 1000
                            unit = "nA"
                if value >= 1000:
                    value /= 1000
                    unit = "KA"
                    if value >= 1000:
                        value /= 1000
                        unit = "MA"
                        if value >= 1000:
                            value /= 1000
                            unit = "GA"
                            value = round(float(value))
                            if value >= 1000:
                                value /= 1000
                                unit = "TA"
                # rounds the current to an appropriate amount of decimal places
                text = str(round(float(value))) + unit
                if value <= 9.9:
                    value = round(value, 1)
                    if (value*10)%10 == 0:
                        value = round(value)
                    text = str(value) + unit
                                
                                
                # displays the current on the fuse
                text_surface = font.render(text, False, (0, 0, 0))
                if data[count][12] == -90 or data[count][12] == -270:
                    text_surface = pygame.transform.rotate(text_surface, 90)
                    WIN.blit(text_surface, (component.rect.x-22, component.rect.y+10))
                else:
                    WIN.blit(text_surface, (component.rect.x+10, component.rect.y-19))
    
                current = ohmslaw() # determines the current using the ohmslaw function
                if current >= data[count][14]: #detects if the value of current is graeter than the maximum specified for the fuse
                             # updates the fuse to its broken state if the current is greater
                             component.uniquestate = True
                             component.image = FUSE_BROKEN
                             cursor.execute("UPDATE tblpositiveconnections SET ignore=? WHERE compID=?", (True, data[count][0]) )
                             conn.commit()
    except:
        pass

    




# definitions for the component class and each individual component as a subclass
class Component(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, group, resistance, voltage, uniquestate):
        super(Component, self).__init__(group)
        self.image = ""
        self.rect = self.image.get_bounding_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.clicked = False
        self.resistance = resistance
        self.voltage = voltage
        self.uniquestate = uniquestate

class Cell(Component):
    def __init__(self, xpos, ypos, group, resistance, voltage, uniquestate):
        super(Component, self).__init__(group)
        self.image = CELL
        self.poweredimage = CELL
        self.originalimage = CELL
        self.rect = self.image.get_rect()
        self.clicked = False
        self.rect.y = ypos
        self.rect.x = xpos
        self.resistance = 0
        self.voltage = voltage
        self.uniquestate = uniquestate

class Bulb(Component):
       def __init__(self, xpos, ypos, group, resistance, voltage, uniquestate):
        super(Component, self).__init__(group)
        self.image = BULB
        self.originalimage = BULB
        self.poweredimage = BULB_POWERED
        self.rect = self.image.get_rect()
        self.clicked = False
        self.rect.y = ypos
        self.rect.x = xpos
        self.resistance = 1400
        self.voltage = voltage
        self.uniquestate = uniquestate

class Resistor(Component):
       def __init__(self, xpos, ypos, group, resistance, voltage, uniquestate):
        super(Component, self).__init__(group)
        self.image = RESISTOR
        self.poweredimage = RESISTOR
        self.originalimage = RESISTOR
        self.rect = self.image.get_bounding_rect()
        self.clicked = False
        self.rect.y = ypos
        self.rect.x = xpos
        self.resistance = resistance
        self.voltage = voltage
        self.uniquestate = uniquestate

class Ammeter(Component):
     def __init__(self, xpos, ypos, group, resistance, voltage, uniquestate):
        super(Component, self).__init__(group)
        self.image = AMMETER
        self.poweredimage = AMMETER
        self.originalimage = AMMETER
        self.rect = self.image.get_rect()
        self.clicked = False
        self.rect.y = ypos
        self.rect.x = xpos
        self.resistance = 0 
        self.voltage = voltage
        self.uniquestate = uniquestate
        self.reading = 0
        
class Diode(Component):
       def __init__(self, xpos, ypos, group, resistance, voltage, uniquestate):
        super(Component, self).__init__(group)
        self.image = DIODE
        self.poweredimage = DIODE
        self.originalimage = DIODE
        self.rect = self.image.get_rect()
        self.clicked = False
        self.rect.y = ypos
        self.rect.x = xpos
        self.resistance = 1100
        self.voltage = voltage
        self.uniquestate = uniquestate
        
class Fuse(Component):
      def __init__(self, xpos, ypos, group, resistance, voltage, uniquestate):
        super(Component, self).__init__(group)
        self.image = FUSE
        self.poweredimage = FUSE
        self.originalimage = FUSE
        self.closedimage = FUSE_BROKEN
        self.rect = self.image.get_rect()
        self.clicked = False
        self.rect.y = ypos
        self.rect.x = xpos
        self.resistance = resistance # fuse will have no resistance but this value will be used for its maximum current
        self.voltage = voltage
        self.uniquestate = uniquestate
        
class Led(Component):
      def __init__(self, xpos, ypos, group, resistance, voltage, uniquestate):
        super(Component, self).__init__(group)
        self.image = LED
        self.poweredimage = LED_POWERED
        self.originalimage = LED
        self.rect = self.image.get_rect()
        self.clicked = False
        self.rect.y = ypos
        self.rect.x = xpos
        self.resistance = 1100
        self.voltage = voltage
        self.uniquestate = uniquestate
        
class Switch(Component):
       def __init__(self, xpos, ypos, group, resistance, voltage, uniquestate):
        super(Component, self).__init__(group)
        self.image = SWITCH_OPEN
        self.poweredimage = self.image
        self.originalimage = SWITCH_OPEN
        self.closedimage = SWITCH_CLOSED
        self.rect = self.image.get_rect()
        self.clicked = False
        self.rect.y = ypos
        self.rect.x = xpos
        self.resistance = 0
        self.voltage = voltage
        self.uniquestate = uniquestate
        
class Voltmeter(Component):
       def __init__(self, xpos, ypos, group, resistance, voltage, uniquestate):
        super(Component, self).__init__(group)
        self.image = VOLTMETER
        self.poweredimage = VOLTMETER
        self.originalimage = VOLTMETER
        self.rect = self.image.get_rect()
        self.clicked = False
        self.rect.y = ypos
        self.rect.x = xpos
        self.resistance = 0.0000000001
        self.voltage = voltage
        self.uniquestate = uniquestate
        self.reading = 0


cursor.execute('SELECT * FROM tblcomponents ORDER BY compID')
data = cursor.fetchall()
for info in data:
    component = info[1]
    compclass = globals()[component]
    xvalue = info[2]
    yvalue = info[3]
    resistance = info[14]
    voltage = info[15]
    uniquestate = info[16]
    component_list.add(compclass(xvalue, yvalue, camera_group, resistance, voltage, uniquestate))
collidecheck = False

# sets id count to number of components in the database
try:
    cursor.execute('SELECT compID FROM tblcomponents ORDER BY compID desc')
    id_count = int(cursor.fetchone()[0])+2
except TypeError:
    id_count = 1
    

wait = False    
showmenu = False
pconnectcheck = False
nconnectcheck = False
wincolour = 241, 241, 250
hover = False
md = False
md2 = False
mu = False
reset()
runstate = False
textbox = False
textbox2 = False
textbox3 = False
cellidlist = []
user_text = ""

###################################################################### WINDOW LOOP ##########################################################################
# All functions from above will be called here as well as event checks such as detecting mouse inputs
run = True
while run:
    
    #----------Window updates----------------
    clock.tick(FPS)# waits a specific amount of time so the program cycles based on what the fps variable is set to
    WIN.fill((wincolour))# colours the main window
    if runstate != True:
       draw_window()
    component_list.draw(WIN)
    pconnections()
    nconnections()
    wirecoords()
    redgreen()
    resistancetext()
    voltagetext()
    power_components()
    switch()
    power_components()
    ohmslaw()
    voltages()
    ammetertext()
    fusecheck()
    power_components()
    mousestate = pygame.mouse.get_pressed(3) #gets the state of all mouse buttons
    leftclick = mousestate[0] #gets the state of the left mouse button
    if (leftclick == True) and (wait == False) and (runstate != True): #this function will run on every pass of the loop but only when the left mose button is pressed down
        cameraoffsetcheck()
    if pconnectcheck == True:
        positiveconnect()
    if nconnectcheck == True:
        negativeconnect()
    if runstate == False:
        if mu == True:
            runstate = playbutton()
        

    if runstate == True:
        fusecheck()
        updatepos()
        power_components()
        if md2 == True:
            runstate = pausebutton()
        WIN.blit(pause, comprect(pause, 1400, -2))
        try:
            #reset()
            power_components()
            check_powered(cellidlist)
            fusecheck()
            power_components()

            
        except IndexError:
            pass
        if runstate == False:
            reset()
    if runstate != True:
        user_text = presentmenu(user_text)
        camera_group.update()


#=========================================Event checks==================================================================================================

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            unrotate()
            updatepos()
            run = False

# this will end the main loop when the window is closed by the user

        if event.type == pygame.MOUSEBUTTONDOWN: # this detects when any mouse button is pressed but only runs the code for the single frame it is pressed, not continuosly
            startpos = (pygame.mouse.get_pos())
            if runstate != True:
                updatepos()
                deletecheck()
                user_text = presentmenu(user_text)
            if runstate == True:
                md2 = True
            if runstate == False:
                mu = True



            mousestate = pygame.mouse.get_pressed(3)
            leftclick = mousestate[0]
            
            pos = pygame.mouse.get_pos()# gets coordinates of current mouse position
            mx = pos[0] # stores the x value of mouse position
            my = pos[1] # stores the y value of mouse position
            
            if wait == False and runstate != True:
                #2
                id_count = drag_and_drop_check(comprect(AMMETER_W, 23,265), Ammeter, "Ammeter", id_count)
                id_count = drag_and_drop_check(comprect(BULB_W, 23,130), Bulb, "Bulb", id_count)
                id_count = drag_and_drop_check(comprect(CELL_W, 25,70), Cell, "Cell", id_count)
                id_count = drag_and_drop_check(comprect(DIODE_W, 28,200), Diode, "Diode", id_count)
                id_count = drag_and_drop_check(comprect(FUSE_W, 60,330), Fuse, "Fuse", id_count)
                id_count = drag_and_drop_check(comprect(LED_W, 130,198), Led, "Led", id_count)
                id_count = drag_and_drop_check(comprect(RESISTOR_W, 110,79), Resistor, "Resistor", id_count)
                id_count = drag_and_drop_check(comprect(SWITCH_W, 125,136), Switch, "Switch", id_count)
                id_count = drag_and_drop_check(comprect(VOLTMETER_W, 130,265), Voltmeter, "Voltmeter", id_count)

            showmenu = False
            dropdown()

            if hover == False:
                md = True
            hover = False
            
            if leftclick == True and runstate != True:
                check_clicked()
                    
        #----------------------component place-----------------------------------------------------------            
        if event.type == pygame.MOUSEBUTTONUP: # detects when any mouse button has been released but only runs for a single frame, the same as MOUSEBUTTONDOWN
            startpos = (pygame.mouse.get_pos())
            if runstate != True:
                updatepos()
                drop_component()
            wait = False
            md = False
            md2 = False
            mu = False

        if event.type == pygame.KEYDOWN:
            if user_text == None:
                user_text = ""
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif len(user_text) >= 12:
                user_text = user_text
            else:
                user_text += event.unicode



            

#====================================================rest of game code====================================================================================
            
   #---------------------component drag-------------------------------------------------
    if runstate != True:
        drag_component()
            

    
    pygame.display.update() # updates the window with everything that has been drawn

pygame.quit() # closes the window when the loop ends



