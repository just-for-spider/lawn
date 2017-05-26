#! c:\python27\python

import sys
import os
import math
import random

FileName = sys.argv[1]
TrainingDataFile = FileName + ".train"
TestDataFile = FileName + ".test"
WordDic = {}
DocList = []
LabelList = []
TestDocList = []
TestLabelList = []
MinFeatureValues = {}
MaxFeatureValues = {}
StepSize = 1
N = 0
W = 0
T = 10

def LoadData():
	global N
	global W
	i = 0
	positiveNum = 0
	negativeNum = 0
	maxWid = 0
	infile = file(TrainingDataFile, 'r')
	sline = infile.readline().strip()
	while len(sline) > 0:
		pos = sline.find("#")
		if pos > 0:
			sline = sline[:pos].strip()
		words = sline.split(' ')
		if len(words) < 1:
			print "Format error!"
			break
		#classid must belong to {+1,-1}
		classid = int(words[0])
		if classid == 1:
			positiveNum += 1
		elif classid == -1:
			negativeNum += 1
		else:
			print "Too many classes!",sline
		LabelList.append(classid)
		words = words[1:]
		tempDic = {}
		for word in words:
			wid = int(word)
			if wid > maxWid:
				maxWid = wid
			if wid not in tempDic:
				tempDic[wid] = 1.0
			else:
				tempDic[wid] += 1.0
			if wid not in WordDic:
				WordDic[wid] = True
		DocList.append(tempDic)
		sline = infile.readline().strip()
		i += 1
	infile.close()
	N = len(DocList)
	W = len(WordDic)
	print i, "files loaded!"
	print len(WordDic), "words!","Max word id is:",maxWid
	print positiveNum,"positive instances!"
	print negativeNum,"negative instances!"

def LoadTestData():
	i = 0
	positiveNum = 0
	negativeNum = 0
	infile = file(TestDataFile, 'r')
	sline = infile.readline().strip()
	while len(sline) > 0:
		pos = sline.find("#")
		if pos > 0:
			sline = sline[:pos].strip()
		words = sline.split(' ')
		if len(words) < 1:
			print "Format error!"
			break
		#classid must belong to {+1,-1}
		classid = int(words[0])
		if classid == 1:
			positiveNum += 1
		elif classid == -1:
			negativeNum += 1
		else:
			print "Too many classes!",sline
		TestLabelList.append(classid)
		words = words[1:]
		tempDic = {}
		for word in words:
			wid = int(word)
			if wid not in tempDic:
				tempDic[wid] = 1.0
			else:
				tempDic[wid] += 1.0
		TestDocList.append(tempDic)
		sline = infile.readline().strip()
		i += 1
	infile.close()
	print i, "test files loaded!"
	print positiveNum,"positive instances in test data!"
	print negativeNum,"negative instances in test data!"

def GetFeatureValueRange():
	global MinFeatureValues
	global MaxFeatureValues
	for doc in DocList:
		for word,freq in doc.items():
			if word not in MinFeatureValues:
				MinFeatureValues[word] = 0.0
			elif MinFeatureValues[word] >= freq:
				MinFeatureValues[word] = freq
			if word not in MaxFeatureValues:
				MaxFeatureValues[word] = freq
			elif MaxFeatureValues[word] <= freq:
				MaxFeatureValues[word] = freq

#stump: (featureID, threshold, label)
#where label means the class label when the feature value is equal to or greater than the threshold
def StumpClassify(stump, x):
	fvalue = 0.0
	if stump[0] in x:
		fvalue = x[stump[0]]
	if fvalue >= stump[1]:
		return stump[2]
	else:
		return -1*stump[2]

def CalculateErr(fid, threshold, wlist):
	tmpErr = 0.0
	predResult = []
	for i in range(len(DocList)):
		doc = DocList[i]
		fvalue = 0.0
		predresult = 1
		if fid in doc:
			fvalue = doc[fid]
		if fvalue < threshold:
			predresult = -1
		if predresult != LabelList[i]:
			tmpErr += wlist[i]
		predResult.append(predresult)
	return tmpErr,predResult

def ReverseValue(alist):
	for i in range(len(alist)):
		alist[i] = -1*alist[i]
	return alist

def BuildBestStump(wlist):
	bestStump = (0,0,1)
	err = 0.0
	predResult = []
	minErr = 1.0
	bestPredResult = []
	for fid in WordDic.keys():
		threshold = MinFeatureValues[fid]
		while threshold <= MaxFeatureValues[fid]:
			err,predResult = CalculateErr(fid, threshold, wlist)
			label = 1
			if err <= 0.0 or err >= 1.0:
				print err,fid
			if err > 0.5:
				label = -1
				err = 1 - err
				predResult = ReverseValue(predResult)
			if err < minErr:
				minErr = err
				bestStump = (fid, threshold, label)
				bestPredResult = predResult
				print minErr,fid,threshold,label
			threshold += StepSize
	return bestStump, minErr, bestPredResult

def AdaBoostTrain():
	w = float(1.0/N)
	wList = [w]*N
	model = []
	totalScore = [0.0]*N
	for it in range(T):
		totalError = 0.0
		print it,"th iteration:"
		bestStump, err, predResultList = BuildBestStump(wList)
		tempf = (1-err)/err
		if tempf < 0.0 or err >= 0.5:
			print tempf,err,bestStump
			raw_input("?s")
		alpha = math.log((1-err)/err)
		if alpha <= 0.0:
			print tempf,err,bestStump
			raw_input("?s")
		print err,alpha
		model.append((bestStump, alpha))
		sum = 0.0
		for i in range(N):
			totalScore[i] += alpha * predResultList[i]
			if totalScore[i] >= 0.0 and LabelList[i] != 1:
				totalError += 1.0
			elif totalScore[i] < 0 and LabelList[i] != -1:
				totalError += 1.0
			if predResultList[i] != LabelList[i]:
				wList[i] = wList[i]*math.exp(alpha)
			sum += wList[i]
		for i in range(N):
			wList[i] = wList[i]/sum
		totalError /= N
		print "Total error rate is:",totalError
		if totalError <= 0.0:
			break
	return model

def AdaBoostPredict(model, x):
	sum = 0.0
	for (stump, alpha) in model:
		sum += StumpClassify(stump, x)*alpha
	if sum >= 0.0:
		return 1
	else:
		return -1

def Evaluate(TrueList, PredList):
	accuracy = 0
	i = 0
	while i < len(TrueList):
		if TrueList[i] == PredList[i]:
			accuracy += 1
		i += 1
	accuracy = (float)(accuracy)/(float)(len(TrueList))
	print "Accuracy:",accuracy

def CalPreRec(TrueList,PredList,classid):
	correctNum = 0
	allNum = 0
	predNum = 0
	i = 0
	while i < len(TrueList):
		if TrueList[i] == classid:
			allNum += 1
			if PredList[i] == TrueList[i]:
				correctNum += 1
		if PredList[i] == classid:
			predNum += 1
		i += 1
	return (float)(correctNum)/(float)(predNum),(float)(correctNum)/(float)(allNum)

#main framework
LoadData()
GetFeatureValueRange()
ABModel = AdaBoostTrain()

LoadTestData()
TestPredList = []
for doc in TestDocList:
	c = AdaBoostPredict(ABModel, doc)
	TestPredList.append(c)

Evaluate(TestLabelList,TestPredList)
pre,rec = CalPreRec(TestLabelList, TestPredList,1)
print "Precision and recall for Class 1:",pre,rec
pre,rec = CalPreRec(TestLabelList, TestPredList,-1)
print "Precision and recall for Class -1:",pre,rec

