######## 얼굴 개수 카운트 및 드러난 감정 계산 ########

import requests
import pprint
import os

subscription_key = ""

ids_path = "./images/"
user_ids = os.listdir(ids_path)
user_ids = [user_id for user_id in user_ids if not user_id.startswith('.')]

results_path = "./results/"

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

