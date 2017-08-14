

########  Microsoft Computer Vision 을 이용한 사진 내용 분석  ########

import requests

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

