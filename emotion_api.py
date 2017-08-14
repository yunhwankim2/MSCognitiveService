# Microsoft Cognitive Service 를 이용한 
# 사진당 표현된 얼굴 개수 카운트 및 
# 얼굴당 표현된 감정 추출
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
def face_num_emotion(filename, subscription_key):
    # The supported input image formats includes JPEG, PNG, GIF(the first frame), BMP. 
    # Image file size should be no larger than 4MB.
    
    headers = {             # Request headers 
        'Content-Type': 'application/octet-stream',     # 'application/json' if image on the web
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    
    with open(filename, "rb") as f:
        body = f.read()

    url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"
    
    try:
        response = requests.post(url, headers=headers, data=body)
        results = response.json()
    except Exception as e:
        print(e)
        results = None
    
    # If no face is detected, an empty array will be returned. 
    
    """ sample error
        {'error': {'code': 'InvalidImageSize',
          'message': 'Image size is too small or too big.'}}
    """
    return results
    
######################################################################

# 모든 폴더의 모든 사진을 루프를 돌면서 분석 실시
for user_id in user_ids:
    result_name = results_path + "/" + user_id

    photo_path = ids_path + user_id
    photo_names = os.listdir(photo_path)
    photo_names = [photo_name for photo_name in photo_names if not photo_name.startswith('.')]
    
    with open(result_name + "_emotion.jsonl", 'a') as f:
        for photo_name in photo_names:
            image_name = photo_path + '/' + photo_name
            results = face_num_emotion(image_name, subscription_key)
            photo_dict = {}
            photo_dict[photo_name] = results
            f.write(json.dumps(photo_dict) + '\n')
            
            time.sleep(5)

