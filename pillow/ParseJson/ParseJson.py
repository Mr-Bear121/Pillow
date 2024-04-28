import re
class pJson:
    def __init__(self):
        #self.json=json
        pass

    @staticmethod
    def parseBody(json):
        jsonString=''
        for value in json.values():
            jsonString+=f'{value},'
        return jsonString
    @staticmethod

    def getQuestion(json):
        jsonString=''
        key='question'
        jsonString=json[key]
        return jsonString

    @staticmethod
    def getTitle(json):
        jsonString=''
        keys=['GID','difficulty']
        for key in keys:
            jsonString+=f'{json[key]}\n'
        return jsonString

    @staticmethod
    def breakJsonString(text):
        return text.split(',')

    #there are 2 ways i can deal with the question numbers'(1)' either i can split/regex on: '(count)' and assign my own number at the beginning.
    # or I can regex and return that number then do my transformation on it.    
    @staticmethod
    def seperateQuestionNumber(jsonQuestion):
        count=1
        returnList=['[title]']
        for item in jsonQuestion:
            reResult=re.search(f'({count})',item)
            if reResult:
                splitItem=item.split(f'({count})')
                returnList.append(f'({count})')
                returnList.append(splitItem[1])
                count+=1
            else:
                returnList.append(item)
        return returnList

    @staticmethod
    def isJsonString(text):
        try:
            if text.split(',') == type(list()):
                return True
        except(Exception):
            return False

        '''@staticmethod
    def getQuestion(json):
        jsonString=''
        keys=['question','KID','answer','association','difficulty','question']
        count = 0
        while count <=json.length():
            with keys[count] as key:
                if json[count.keys[count]] == key:
                    jsonString+=f'{json[key]},'
            count+=1
        return jsonString
    '''