# Microsoft Cognitive Service 를 이용한 
# 사진의 내용 분석
# 2017/8/14 현재 Microsoft Azure Cognitive Service 로 이름이 바뀜.

import requests
import os

# subscription key 를 확보하여 아래에 복사해 넣어주어야 함.
# Microsoft Azure Cognitive Service 
# (https://azure.microsoft.com/ko-kr/services/cognitive-services/)
# 로 접속하여 무료 평가판 메뉴를 통해 무료 key 를 발급받거나,
# Azure 계정을 통해 유료 key 를 발급.

subscription_key = ""

ids_path = "./images/"      # images 폴더 내에 계정 id 별로 별도의 폴더가 만들어져 있고, 그 폴더 안에 사진이 들어 있다고 가정
user_ids = os.listdir(ids_path)
user_ids = [user_id for user_id in user_ids if not user_id.startswith('.')]

results_path = "./results/"     # 분석 결과를 담은 .json 파일이 저장될 경로

# 개별 사진을 서버로 보내 분석을 실시할 함수
def computer_vision_api(filename, subscription_key):
    
    headers = {             # Request headers 
        'Content-Type': 'application/octet-stream',     # 'application/json' if image on the web
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    
    params = {
        'visualFeatures': 'Categories,Tags,Description,Color'
    }
        
    with open(filename, "rb") as f:
        body = f.read()
    
    url = "https://westus.api.cognitive.microsoft.com/vision/v1.0/analyze"
    
    try:
        response = requests.post(url, headers=headers, params=params, data=body)
        results = response.json()
    except Exception as e:
        print(e)
        results = None
    
    return results


#########################

# 모든 폴더의 모든 사진을 루프를 돌면서 분석 실시
for user_id in user_ids:
    result_name = results_path + "/" + user_id

    photo_path = ids_path + user_id
    photo_names = os.listdir(photo_path)
    photo_names = [photo_name for photo_name in photo_names if not photo_name.startswith('.')]
    
    with open(result_name + "_cv.jsonl", 'a') as f:
        for photo_name in photo_names:
            image_name = photo_path + '/' + photo_name
            results = computer_vision_api(image_name, subscription_key)
            photo_dict = {}
            photo_dict[photo_name] = results
            f.write(json.dumps(photo_dict) + '\n')
            
            time.sleep(5)

