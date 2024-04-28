from PIL import Image, ImageDraw, ImageFont
from TextEdit.pillowWordWrap import WordWrap
#format: x, ex, y, ey
#seems x and ex controls the circle and y and ey is supposed to be window size making me think its more like: (x,y,ex,ey).
#^EDIT: seems to be more like start at x end at y, start at ex end at ey
#  note can move image off of window

text = "Evan Nagy; this doesnt have enough letters so I need to add more to pass the time. tha sdsd thtsada thasa wasdthads thasgfdas thagdfsath aadfgthasd"
circle = (0,0,1152, 648)
imageName='test'
imageLocation = 'images/'
desiredImage = f'{imageName}.jpg'
fontSelection = './fonts/Courier_Prime/CourierPrime-Regular.ttf'
fontSize = 50
#font = ImageFont.truetype(fontSelection,size=fontSize)


def saveImage(image):
    newImageName = 'images/New_Testing_Image.jpg'
    image.save(newImageName)
    
def previewImage(image):
    image.show()

#color should be a hex value
def drawCircle(canvas,color='#4ea8d9',outline=None):
    if outline !=None:
        canvas.ellipse(circle,fill=color, outline=outline)
        return canvas
    else:
        canvas.ellipse(circle,fill=color)
        return canvas

if __name__ == '__main__':
    textHeight = 435
    textLength = 300
    newImage =None
    with Image.open(f'{imageLocation}{desiredImage}').convert('RGBA') as baseImage:
        newImage=Image.new('RGB',size=baseImage.size)
        canvas = ImageDraw.Draw(newImage)
        canvas = drawCircle(canvas)
        
        writeWithWrap = WordWrap(image=newImage,font=fontSelection,fontSize=fontSize,text=text)
        #wordWrapped image
        newImage = writeWithWrap.writeWordWrap()
        previewImage(newImage)
        #saveImage(newImage)



        #mode, size, color
        # or mode, sizes
        #newImage = Image.new('RGB',size=baseImage.size)
        #drawingCanvas = ImageDraw.Draw(newImage)
        #drawingCanvas.text((textHeight,textLength),text,font=font, fill=(0,0,0,200))
        #drawingCanvas.text((textHeight - 3,textLength - 3),text,font=font)
        #previewImage(newImage)
        #saveImage(newImage)
