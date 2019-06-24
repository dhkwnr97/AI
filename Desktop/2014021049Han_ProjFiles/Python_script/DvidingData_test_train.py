'''
Using : python ~./DvidingData_test_train.py[:sp:]DataSetFolder Path
'''

#Load packages
import math, random
import sys, os, shutil

#Improting argument
path=sys.argv[1]

#Define Making Directory function
def Makedir(paths, dirName):
    try:
        if not(os.path.isdir(paths+"/"+dirName)):
            os.makedirs(os.path.join(paths+"/"+dirName))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory! Same directory exist")
            raise
#Define Move File into Next Directory function
def NextMovefile(originPath, dirName, MoveFileName):
    src=originPath
    dir=originPath+'/'+dirName
    shutil.move(src+'/'+MoveFileName, dir+'/'+MoveFileName)

#Dividing Data to Refference and Annotation
Makedir(path, "Picture")
Makedir(path, "Annotation")
WholeFiles=os.listdir(path)
for fName in WholeFiles:
    if "_Annotation" in fName:
        NextMovefile(path, "Annotation", fName)
    else:
        NextMovefile(path, "Picture", fName)

#Data infomation
PictureNameList=os.listdir(path+"/Picture")
AnnotationNameList=os.listdir(path+"/Annotation")
total_N_Pic=int(len(PictureNameList))
total_N_Anno=int(len(AnnotationNameList))

#Dividing Test and Train deta
#  Train data : Test Data = 8 : 2
test_Index=set(random.sample(range(0, total_N_Pic), int(total_N_Pic*2/10)))#   Random file choose
train_Index=set(range(0, total_N_Pic))-test_Index
print("총 사진 데이터 개수 :", total_N_Pic, '개')#Printing Code Blow
print("총 사진 분석결과 이미지 개수 :", total_N_Anno, '개')
print("테스트용 데이터 개수 :", len(test_Index), '개')
print("훈련용 데이터 개수 :", len(train_Index), '개')
print("-----     -----     -----     -----     -----     -----")

#Dividing Picture Files each train and test of X
X_NameList_test=[]# Make File name list below
X_NameList_train=[]
for index in test_Index:
    X_NameList_test.append(PictureNameList[index])
for index in train_Index:
    X_NameList_train.append(PictureNameList[index])
print("test_set 과 training_set 이름 집합 완성")#  Printing Code
print("-----     -----     -----     -----     -----     -----")

Makedir(path, "Picture/test_set")
Makedir(path, "Picture/training_set")
for fName in X_NameList_test:
    NextMovefile(path+"/Picture", "test_set", fName)
print("test_set 폴더로 파일 이동 완료")#  Printing Code
for fName in X_NameList_train:
    NextMovefile(path+"/Picture", "training_set", fName)
print("training_set 폴더로 파일 이동 완료")#  Printing Code
print("-----     -----     -----     -----     -----     -----")