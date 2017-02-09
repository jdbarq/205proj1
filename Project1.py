from PIL import Image

def medianOdd(myList):
    #store list length in variable listLength
    listLength = len(myList)
    #sort the List
    sortedValues = sorted(myList)
    #location of middle index. Subtract 1 because of zero index
    middleIndex= ((listLength + 1)/2) - 1
    #return object located at the index
    return sortedValues[middleIndex]

imgList = [] #declare my image array


 #try this 
for x in range(9): #loop range from 1-9

    imgList.append(Image.open(str(x + 1)+".png")) #populates a list of image objects
            
            
    print " ",imgList[x].format, imgList[x].size, imgList[x].mode #print out my image values
            
            
            
width,height = imgList[0].size

myRed = [] #red values
myGreen = [] #green values
myBlue = [] #blue values

        

            

            

          
newImage = Image.new('RGB', (width, height)) #declare a new image RGB 

for x in range(0,width):
    #loop for x with a range between 0 and the width
    for y in range(0,height):
        
        for i in range(0,len(imgList)):
                    
            
            
            r,g,b = imgList[i].getpixel((x,y))
                    
            myRed.append(r)
            myGreen.append(g)
            myBlue.append(b)
                    
        medianF = (int(medianOdd(myRed)), int(medianOdd(myGreen)),int(medianOdd(myBlue)))   
                    
                  
                      
                    
                    #Empty Buffers
        myRed[:] = []
        myGreen[:] = []
        myBlue[:] = []

                    
                    
        newImage.putpixel((x,y), medianF)
            
            
            
            
            
            
newImage.save("newPic.png")
#newImage.load()
  
    #print " " newImage.format
            

