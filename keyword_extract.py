from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import argparse

# 인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description='Argparse Tutorial')

# 입력받을 인자값 설정 (default 값 설정가능)
parser.add_argument('--url', type=str, default="C:/Users/hnb/Desktop/윤지은/result_text.txt")

# args 에 위의 내용 저장
args = parser.parse_args()

credential = AzureKeyCredential("2a51cafc969d4628bed62dac2f468b93")
endpoint="https://hnb.cognitiveservices.azure.com/"

text_analytics_client = TextAnalyticsClient(endpoint, credential)

a = open(args.url, 'r').readlines()
string=''
for i in a:
    #e="".join(map(str, i))
    string+=i
    
documents=[string]

response = text_analytics_client.extract_key_phrases(documents, language="ko")
result = [doc for doc in response if not doc.is_error]

for doc in result:
    keywords = doc.key_phrases
print(keywords)