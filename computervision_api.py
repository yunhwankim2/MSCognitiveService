

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


#########################

cv_subscription_key = ""

for user_id in user_ids:

    result_name = results_path + "/" + user_id

    photo_path = ids_path + user_id
    photo_names = os.listdir(photo_path)
    photo_names = [photo_name for photo_name in photo_names if not photo_name.startswith('.')]
    
    with open(result_name + "_cv.jsonl", 'a') as f:
        for photo_name in photo_names:
            image_name = photo_path + '/' + photo_name
            results = anl.computer_vision_api(image_name, cv_subscription_key)
            photo_dict = {}
            photo_dict[photo_name] = results
            f.write(json.dumps(photo_dict) + '\n')
            
            time.sleep(5)

