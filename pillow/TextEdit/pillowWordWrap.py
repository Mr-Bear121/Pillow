import sys
import math
from PIL import ImageFont,ImageDraw
import re
sys.path.append('..')

class WordWrap():

    def __init__(self,image,font,fontColor,fontSize,Spacing=7,imageName='New_Testing_Image'):
        self.font=font
        self.fontSize=fontSize
        self.fontColor=fontColor
        #this is an image give with the Image.open PIL command
        self.image=image
        self.spacing=Spacing
        self.imageName=imageName
        self._lineHeight=0
        self._OriginalColor=fontColor
        #canvas because you can draw on a canvas
        self._canvas=None

    def getImageName(self):
        return self.imageName

    def changeImageName(self,imageName):
        self.imageName

    def changeFont(self,style):
        self.font=style

    def changeFontSize(self,size):
        self.fontSize=size

    def changeColor(self,color):
        self.fontColor=color

    def getImage(self):
        return self.image

    def resetLineHeight(self):
        self._lineHeight=0
  
    def _placeText(self,lines,current_Line,placement):
        return (self.image.size[1] - (lines - current_Line) * self._lineHeight) - placement

    def _createCanvas(self):
        self._canvas=ImageDraw.Draw(self.image)

    def _createfont(self):
        return ImageFont.truetype(self.font,size=self.fontSize)

    def _getWords(self,text):
        return text.split(' ')

    def _countLines(self,total):
        #lines:
        return math.ceil (total / (self.image.size[0] - 300))

    def _writeTextWShadow(self,horizontalText,height,phrase,formatedFont,textColor):
        self._canvas.text((horizontalText+3, height+3), phrase, font=formatedFont, fill=(000,000,000,200))
        self._canvas.text((horizontalText, height), phrase, font=formatedFont, fill=textColor)

    # finds how many lines are needed total
    def _getPhraseSize(self,totalWords,formatedFont,spacing):
        total=0
        phraseSize=[]
        for phrase in totalWords:
            #returns the size of a given string
            p = self._canvas.textsize(phrase, font=formatedFont)
            total += p[0] + spacing
            phraseSize.append(p[0])
            self._lineHeight = max(p[1] + spacing, self._lineHeight)
        return phraseSize,total

    def _seperateJson(self,mList):
        phrase=[]
        for item in mList:
            if re.search(' ',item):
                for word in self._getWords(item):
                    phrase.append(f'{word} ')
            else:
                phrase.append(f'{item} ')
        return phrase

    def _typeOfString(self,text):

        if (type(text) == type(list())):
            return self._seperateJson(text)
        else:
            return self._getWords(text)
        return None
    

    def writeWordWrap(self,text,horizontalText,verticalText=100,spacing=7):
        colorChanged=False
        count=1
        phrase_size=[]
        lineStart=horizontalText
        horizontalMargin=100
        current_line = 0
        totalWords = self._typeOfString(text)
        isTitle=totalWords[0].strip()=='[title]'
        print(totalWords)
        #if this contains a Json title, 'denoted by [title] which has been added to the string' then remove it and recolor the word.
        #need to do this or it will effect, 'phrase_size' which will effect the ending result of the card
        if isTitle:
            del totalWords[0]
            self.changeColor((50, 135, 46))
            colorChanged=True
        formatedFont=self._createfont()
        self._createCanvas()
        phrase_size,total = self._getPhraseSize(totalWords,formatedFont,spacing)
        lines=self._countLines(total)
        #this code naturally word wraps from the bottom.
        #however, I can reset the lines to the top of the image by subtracting the first line`s` value from all other values. 'since 0 represents the top of the page'
        resetToTop=self._placeText(lines,current_line,verticalText)
        for index in range(len(totalWords)):
            word = totalWords[index]
            size = phrase_size[index]
            #determines the height placement of each line
            height = (self.image.size[1] - (lines - current_line) * self._lineHeight)-resetToTop 
            #used for the card logic. if I get the denoted line item number then color the numbers but if it doesnt then return to the default color
            if word.strip()==f'({count})': 
                self.changeColor((50, 135, 46))
                colorChanged=True
                isTitle=False
                count+=1
            elif isTitle:
                pass
            elif colorChanged==(True):
                self.changeColor(self._OriginalColor)
                colorChanged=False
            
            #if you write something that is black then write it without the shadow since you won`t be able to see it    
            if self.fontColor==(000,000,000):
                self._canvas.text((horizontalText, height), word, font=formatedFont, fill=self.fontColor)
            #else write with text shadow    
            else:
                self._writeTextWShadow(horizontalText,height,word,formatedFont,self.fontColor)
            horizontalText += size + spacing
            #\n has lost functionality therefore I must reinstate it:
            #if you find a \n 'newline' then move the current line up 1 and start at the beginning of the line else continue with word wrap
            for letter in word:
                if letter == '\n':
                    #recalculate to nextlines
                    current_line += 1
                    height = (self.image.size[1] - (lines - current_line) * self._lineHeight)-resetToTop
                    horizontalText = lineStart
            # is there enough space on the rest of the line to fit the next word?
            if index +1 < len(totalWords): 
                # (but only check if we're not the last word)
                if horizontalText + phrase_size[index+1] > self.image.size[0] - horizontalMargin: 
                    #restart to beginning of line
                    horizontalText = lineStart
                    current_line += 1
            #if you`ve reached the end of the phrase then make sure to reset line height for re-use    
            #elif index == len(totalWords):
            #    self.resetLineHeight()
                        
                    
        #return self.image
            
