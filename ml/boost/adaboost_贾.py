import os
import math
import random


wordDict = {}
filespath = "E:\\Machine Learning\Data\\data-classify\\"

def initData():
    trainFile = "E:\\Machine Learning\Data\\train.txt"
    predictionFile = "E:\\Machine Learning\Data\\prediction.txt"
    wordDictFile = "E:\\Machine Learning\Data\\dict.txt"

    t = open(trainFile,"w")
    p = open(predictionFile,"w")
    d = open(wordDictFile,"w")
    
    type = 0
    files = os.listdir(filespath)
    for file in files:
        if file.find("sports")>-1:
            type = 1
        else:
            type = -1

        words = set()
        r = open(filespath + file,"r")
        line = r.readline().strip()
        
        while len(line)>0:
            linewords = line.split(" ")
            for word in linewords:
                #print word.decode("utf-8")
                if not wordDict.has_key(word):
                    wordDict[word] = len(wordDict)
                words.add(wordDict[word])
            line = r.readline().strip()
        r.close()
            
        r = random.random()
        if r<0.8:
            t.write(str(type) + " ")
            for word in words:
                t.write(str(word) + " ")
            t.write("\n")
        else:
            p.write(file + " "+str(type)+ " ")
            for word in words:
                p.write(str(word) + " ")
            p.write("\n")

    for key in wordDict.keys():
        d.write(key +" "+ str(wordDict[key])+ " ")

wordDict2 = {}
trainList = []
weightList = []

def loadData():
    trainfile = "E:\\Machine Learning\\Data\\train.txt"
    r = open(trainfile,"r")
    line = r.readline().strip()
    while len(line)>0:
        words = line.split(" ")
        for i in range(1,len(words)):
            if not wordDict2.has_key(words[i]):
                wordDict2[words[i]] = set()
        line = r.readline().strip()
    r.close()
    
    r2 = open(trainfile,"r")
    line = r2.readline().strip()
    idx = 0
    while len(line)>0:
        words = line.split(" ")
        classtype = int(words[0])
        wordset = set()
        for i in range(1,len(words)):
            wordset.add(words[i])
        if classtype == 1:
            for key in wordDict2.keys():
                if not (key in wordset):
                    wordDict2[key].add(idx)
        else:
            for key in wordDict2.keys():
                if key in wordset:
                    wordDict2[key].add(idx)
        idx +=1
        line = r2.readline().strip()
    r2.close()

    for i in range(idx):
        weightList.append(1.0/(idx+1))

M = 5
def adaboost():
    currentkey = 0
    currenterr = 1.0
    aList = []
    times = 0
    print "ok"
    while currenterr>0 and times<M:
        currenterr = 1.0
        for key in wordDict2.keys():
            err = 0.0
            errset = wordDict2[key]
            for x in errset:
                err += weightList[x]
            if err<currenterr:
                currentkey = key
                currenterr = err
                #print currentkey
        c = math.log((1-currenterr)/currenterr)
        aList.append([c,currentkey])
        for x in wordDict2[currentkey]:
            weightList[x] = weightList[x]*math.exp(c)
        sumw = 0.0
        for i in range(len(weightList)):
            sumw += weightList[i]
        for i in range(len(weightList)):
            weightList[i] = weightList[i]/sumw
        print currentkey
        times +=1
        pList = aList
    return aList


def predict(pList):
    predictionFile = "E:\\Machine Learning\Data\\prediction.txt"
    rowcnt = 0
    correctcnt = 0

    r = open(predictionFile,"r")
    line = r.readline().strip()
    while len(line)>0:
        rowcnt+=1
        words = line.split(" ")
        wordset = set()
        value = 0.0
        for i in range(2,len(words)):
            wordset.add(words[i])
        for x in pList:
            if x[1] in wordset:
                value += x[0]
            else:
                value -= x[0]
        if value * int(words[1])>0:
            correctcnt+=1
        print words[0] + " " + words[1] + " " + str(value)
        line = r.readline().strip()
    print str(rowcnt) + " -- " +  str(correctcnt)
    r.close()

if __name__ == "__main__":

    #initData()
    loadData()
    clist = adaboost()
    for x in clist:
       print x
    predict(clist)
