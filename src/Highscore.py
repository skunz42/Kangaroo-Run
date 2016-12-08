import json
import pygame

class Highscore:
    def __init__(self):
        self.mylist = [0, 0, 0, 0, 0]
        i = 0
        self.string = str((open("highscore.txt", "r")).read())
        self.dict = json.loads(self.string)
        for j in self.dict:
            self.mylist[i] = int(j)
            i += 1
        self.hslist = sorted(self.mylist)
        print(self.hslist)
        self.lowest = str(self.hslist[0])
        self.newDict = self.dict
    def getNames(self, dict):
        self.name1 = dict.get(str(self.hslist[4]))
        self.name2 = dict.get(str(self.hslist[3]))
        self.name3 = dict.get(str(self.hslist[2]))
        self.name4 = dict.get(str(self.hslist[1]))
        self.name5 = dict.get(str(self.hslist[0]))
        self.names = ([self.name1, self.name2, self.name3, self.name4, self.name5])
        return self.names
    def getScores(self):
        return self.hslist
    def updateList(self, newscore):
        newDict = self.dict
        name = input("Input name: ")
        newDict[str(newscore)] = name
        print(self.lowest)
        print(newDict)
        if(len(newDict) == 6):
            del(newDict[self.lowest])
        print(newDict)
        return (newDict)
    def writeToFile(self, dict):
        finalStr = json.dumps(dict)
        outfile = (open("highscore.txt", "w"))
        outfile.write(finalStr)
        outfile.close()













