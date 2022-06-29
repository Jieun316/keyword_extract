import sys
import fitz
from pdfminer.high_level import extract_text
import argparse

# 인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description='Argparse Tutorial')

# 입력받을 인자값 설정 (default 값 설정가능)
parser.add_argument('--url', type=str, default="C:/Users/hnb/Desktop/윤지은/특허문헌_sample3.pdf")

# args 에 위의 내용 저장
args = parser.parse_args()

sys.stdout = open('result_text.txt', 'w')


#url = "C:/Users/hnb/Desktop/윤지은/특허문헌_sample3.pdf"

PDF_text = extract_text(args.url)

###청구항 1

for i in range(len(PDF_text)):
    if PDF_text[i:i+5]=='청구항 1' and PDF_text[i+6]=='\n':
        #print(i)
        tmp=i

for j in range(len(PDF_text)):
    if PDF_text[j:j+5]=='청구항 2'and PDF_text[j+6]=='\n':
        #print(j)
        tmp2=j
        
cg = PDF_text[tmp+6:tmp2]

###배경기술

if '발명이 속하는 기술 및 그 분야의 종래기술' in PDF_text:
    for k in range(len(PDF_text)):
        if PDF_text[k:k+23]=='발명이 속하는 기술 및 그 분야의 종래기술' and PDF_text[k+24]=='\n':
        #print(k)
            tmp3=k
    for m in range(len(PDF_text)):
        if PDF_text[m:m+18]=='발명이 이루고자 하는 기술적 과제'and PDF_text[m+19]=='\n':
            #print(m)
            tmp4=m
    tech = PDF_text[tmp3+24:tmp4]

elif '배 경 기 술' in PDF_text:
    for k in range(len(PDF_text)):
        if PDF_text[k:k+7]=='배 경 기 술' and PDF_text[k+8]=='\n':
        #print(k)
            tmp5=k
    for m in range(len(PDF_text)):
        if PDF_text[m:m+6]=='발명의 내용'and PDF_text[m+7]=='\n':
        #print(m)
            tmp6=m
    tech = PDF_text[tmp5+8:tmp6]

    
result = cg+tech
print(result.replace('\n',' '))

sys.stdout.close()