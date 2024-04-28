from PIL import Image, ImageDraw, ImageFont
from TextEdit.pillowWordWrap import WordWrap
from ParseJson.ParseJson import pJson
#format: x, ex, y, ey
#seems x and ex controls the circle and y and ey is supposed to be window size making me think its more like: (x,y,ex,ey).
#^EDIT: seems to be more like start at x end at y, start at ex end at ey
#  note can move image off of window

#text = "Evan Nagy; this doesnt have enough letters so I need to add more to pass the time. tha sdsd thtsada thasa wasdthads thasgfdas thagdfsath aadfgthasd"
circle = (0,0,1152, 648)
imageName='FbGroup1500x1420_NewCard'
imageLocation = 'images/'
desiredImage = f'{imageName}.png'
#fontSize = 50
""" inputOptions='''
-Write text
-Preview
-Save
-Change font color
-Change font size
-Reference image name
:''' """
""" selection = input(f'please type which operation you`d like to be performed on your image:{inputOptions}') """
#font = ImageFont.truetype(fontSelection,size=fontSize)

def CreateWordWrapper(image,fontSelection,fontColor=(255,255,255,255),fontSize=50):
    return WordWrap(image=image,font=fontSelection,fontColor=fontColor,fontSize=fontSize)

'''requires a set or list for xy values for position'''
def printText(wordWrapper,text,position,spacing=7):
    wordWrapper.writeWordWrap(text=text,horizontalText=int(position[0]),verticalText=int(position[1]),spacing=spacing)
    return wordWrapper

def saveImage(image,imageName='New_Testing_Image_3',imageType='.png'):
    newImageName = f'images/{imageName}{imageType}'
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
    json={'GID': 'tbd',
            'ID': 576,
            'KID': 'KV1001',
            'answer': 'The best answer is 4.',
            'association': 'zassociation',
            'difficulty': 'zdifficulty',
            'question': ['What is a newline?\n',
            '\n',
            '(1) Separates programming statements.\n',
            '(2) Defined by the string.\n',
            '(3) A way to format code.\n',
            '(4) All of the above.\n',
            '(5) None of the above.\n'],
            'status': 'zstat'
            }

    jsonBody = pJson.getQuestion(json)
    jsonTitle=pJson.getTitle(json)
    jsonBody=pJson.seperateQuestionNumber(jsonBody)
    fontSelection = './fonts/Courier_Prime/CourierPrime-Regular.ttf'
    titlePosition=(520,50)
    bodyPosition=(150,420)
    color=(3,232,252)
    white=(255,255,255)
    black=(000,000,000,200)
    newImage =None
    with Image.open(f'{imageLocation}{desiredImage}').convert('RGBA') as baseImage:
        newImage=baseImage.copy()
        wordWrapper=CreateWordWrapper(newImage,fontSelection,white,fontSize=60)
        wordWrapper = printText(wordWrapper=wordWrapper,text=jsonBody,position=bodyPosition)
        wordWrapper.changeFontSize(size=100)
        wordWrapper.changeColor(color=color)
        wordWrapper = printText(wordWrapper=wordWrapper,text=jsonTitle,position=titlePosition)
        #previewImage(wordWrapper.getImage())
        saveImage(newImage)











        '''while str(selection).lower() != 'exit':
            match str(selection).lower():
                case 'write text':
                    text=input('please insert text:')
                    x=input('please input X length for text placement:')
                    y=input('please input y height for text placement:')
                    wordWrapper = printText(wordWrapper=wordWrapper,text=text,position=(x,y))
                case 'change font color':
                    wordWrapper.changeColor(color=color)
                case 'preview':
                    previewImage(wordWrapper.getImage())
                case 'reference image name':
                    pass
                case 'save':
                    saveImage(wordWrapper.getImage,wordWrapper.getImageName)
                case 'change font size':
                    wordWrapper.changeFontSize(size=100)
                case 'json':
                    pass
                case 'testing':
                    wordWrapper = printText(wordWrapper=wordWrapper,text=jsonBody,position=bodyPosition)
                    wordWrapper.changeFontSize(size=100)
                    wordWrapper.changeColor(color=color)
                    wordWrapper = printText(wordWrapper=wordWrapper,text=jsonTitle,position=titlePosition)
                    previewImage(wordWrapper.getImage())
                    #reset word wrap
                    wordWrapper=CreateWordWrapper(newImage,fontSelection,black,fontSize=60)
                
            selection=input(f'\nWhat would you like to do next?{inputOptions}')
            '''
    print('Have a nice day!')



        #mode, size, color
        # or mode, sizes
        #newImage = Image.new('RGB',size=baseImage.size)
        #drawingCanvas = ImageDraw.Draw(newImage)
        #drawingCanvas.text((textHeight,textLength),text,font=font, fill=(0,0,0,200))
        #drawingCanvas.text((textHeight - 3,textLength - 3),text,font=font)
        #previewImage(newImage)
        #saveImage(newImage)
