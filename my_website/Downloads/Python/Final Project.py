import PIL
import numpy as np
import os.path
import random

def createTieDye(runtimes = 10, width = 255, height = 255):
    try:
        #checks if folder named Tie Dye Prints exists where the file is. If not it creates one
        os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Tie Dye Prints'))
    except OSError:
        os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Tie Dye Prints'))
        os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Tie Dye Prints'))
    directory = os.getcwd()
    
    
    
    for f in range(runtimes):       #built in loop in function. allows for running multiple times.
        image = PIL.Image.new ('RGBA', (width, height), 'black')            #initiates PIL image
        tieDye = np.array(image)                                            #converts PIL image to a numpy array for pixel manipulation
        randomVal = random.random()*255                                     #initiates a random value
        randomChoose = random.randint(1,12)                                 #chooses which layout function will yuse
        try:
            if randomChoose == 1:                                           #changes pixel values depending on location
                randomInt = random.randint(1,int((width+height)/127.5))      
                for row in range(height):
                    y = 255*row/height
                    for column in range(width):
                        x=255*column/width
                        tieDye[y][x] = [y,randomInt*y*x,x,255-100*random.random()]
                        
            elif randomChoose == 2:
                randomInt = random.randint(1,int((width+height)/127.5))      
                for row in range(height):
                    y = 255*row/height
                    for column in range(width):
                        x=255*column/width
                        tieDye[y][x] = [(x+y)/2,randomInt*y*x,(x+y)/2,255-100*random.random()]
                        
            elif randomChoose == 3:
                randomInt = random.randint(1,int((width+height)/127.5))
                for row in range(height):
                    y = 255*row/height
                    for column in range(width):
                        x=255*column/width
                        tieDye[y][x] = [x,randomInt*y*x,y,255-100*random.random()]
                        
            elif randomChoose == 4:
                randomInt = random.randint(1,int((width+height)/127.5))
                for row in range(height):
                    y = 255*row/height
                    for column in range(width):
                        x=255*column/width
                        tieDye[y][x] = [randomVal,randomInt*y*x,(x+y)/2,255-50*random.random()]
                        
            elif randomChoose == 5:
                randomInt = random.randint(1,int((width+height)/127.5))
                for row in range(height):
                    y = 255*row/height
                    for column in range(width):
                        x=255*column/width
                        tieDye[y][x] = [randomInt*y*x,y,x,255-100*random.random()]
                        
            elif randomChoose == 6:
                randomInt = random.randint(1,int((width+height)/127.5))
                for row in range(height):
                    y = 255*row/height
                    for column in range(width):
                        x=255*column/width
                        tieDye[y][x] = [randomInt*y*x,(x+y)/2,(x+y)/2,255-100*random.random()]
            
            elif randomChoose == 7:
                randomInt = random.randint(1,int((width+height)/127.5))
                for row in range(height):
                    y = 255*row/height
                    for column in range(width):
                        x=255*column/width
                        tieDye[y][x] = [randomInt*y*x,x,y,255-100*random.random()]
            
            elif randomChoose == 8:
                randomInt = random.randint(1,int((width+height)/127.5))
                for row in range(height):
                    y = 255*row/height
                    for column in range(width):
                        x=255*column/width
                        tieDye[y][x] = [randomInt*y*x,randomVal,(x+y)/2,255-50*random.random()]
            
            elif randomChoose == 9:
                randomInt = random.randint(1,int((width+height)/127.5))
                for row in range(height):
                    y = 255*row/height
                    for column in range(width):
                        x=255*column/width
                        tieDye[y][x] = [y,x,randomInt*y*x,255-100*random.random()]
        
            elif randomChoose == 10:
                randomInt = random.randint(1,int((width+height)/127.5))
                for row in range(height):
                    y = 255*row/height
                    for column in range(width):
                        x=255*column/width
                        tieDye[y][x] = [(x+y)/2,(x+y)/2,randomInt*y*x,255-100*random.random()]
            
            elif randomChoose == 11:
                randomInt = random.randint(1,int((width+height)/127.5))
                for row in range(height):
                    y = 255*row/height
                    for column in range(width):
                        x=255*column/width
                        tieDye[y][x] = [x,y,randomInt*y*x,255-100*random.random()]
            
            elif randomChoose == 12:
                randomInt = random.randint(1,int((width+height)/127.5))
                for row in range(height):
                    y = 255*row/height
                    for column in range(width):
                        x=255*column/width
                        tieDye[y][x] = [randomVal,(x+y)/2,randomInt*y*x,255-50*random.random()]
                        
            tieDyeImg = PIL.Image.fromarray(tieDye, 'RGBA')                     #converts image array to PIL image
            tieDyeImg.save(directory + '\\TieDye' + str(f+1) + '.png')          #saves PIL image to directory with name TieDye(number of print).png
            print "Image Saved"
        except IOError:
            print "Something went wrong. You might have run out of space on your computer."

createTieDye()