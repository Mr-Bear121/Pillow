import math
from PIL import Image,ImageFont,ImageDraw

class WordWrap():

    def __init__(self,image,font,fontSize,text,textFill=(0,0,0,200),Spacing=7,textPlacement=100):
        self.text = text
        self.font=font
        self.fontSize=fontSize
        #this is an image give with the Image.open PIL command
        self.image=image
        self.spacing=Spacing
        self.textFill=textFill
        self.textPlacement = textPlacement
        self._lineHeight=0
        self._phrase_size=[]
        #canvas because you can draw on a canvas
        self._canvas=None
        
    def _textPlacement(self,lines,current_Line,placement):
        return (self.image.size[1] - (lines - current_Line) * self._lineHeight) - placement

    def createCanvas(self):
        self._canvas=ImageDraw.Draw(self.image)

    def _createfont(self):
        return ImageFont.truetype(self.font,size=self.fontSize)

    def _breakUpPhrase(self,text):
        return text.split(' ')

    
    # finds how many lines are needed total
    def _countLines(self,totalWords,formatedFont):
        total=0
        for phrase in totalWords:
            #returns the size of a given string
            p = self._canvas.textsize(phrase, font=formatedFont)
            total += p[0] + self.spacing
            self._phrase_size.append(p[0])
            self._lineHeight = max(p[1] + self.spacing, self._lineHeight)
        lines = math.ceil (total / (self.image.size[0] - 300))
        return lines

    def writeWordWrap(self):
        linesWrap=0
        current_line = 0
        startleft = 150
        formatedFont=self._createfont()
        totalWords = self._breakUpPhrase(self.text)
        self.createCanvas()
        lines=self._countLines(totalWords,formatedFont)
        #this code naturally word wraps from the bottom.
        #however, I can reset the lines to the top of the image by subtracting the first line`s` value from all other values. 'since 0 represents the top of the page'
        resetToTop=self._textPlacement(lines,current_line,self.textPlacement)
        for index in range(len(totalWords)):
            phrase = totalWords[index]
            size = self._phrase_size[index]
            #determines the height placement of each line
            height = (self.image.size[1] - (lines - current_line) * self._lineHeight)-resetToTop
            #writes the actual words
            self._canvas.text((startleft+3, height+3), phrase, font=formatedFont, fill=(0,0,0,200))
            self._canvas.text((startleft, height), phrase, font=formatedFont, fill=(255,255,255,255))
            startleft += size + self.spacing
            # is there enough space on the rest of the line to fit the next word?
            if index +1 < len(totalWords): 
                # (but only check if we're not the last word)
                if startleft + self._phrase_size[index+1] > self.image.size[0] - 150:
                    startleft = 150
                    current_line += 1
        return self.image
            
