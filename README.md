# MSCognitiveService

Microsoft Cognitive Service (<https://azure.microsoft.com/ko-kr/services/cognitive-services/>) 를 이용하여 사진을 분석하는 파이썬 코드입니다. 예전에는 Project Oxford 라는 이름으로 베타 서비스가 되다가 몇 달 전에 정식으로 오픈한 것 같습니다. 이름도 Microsoft Azure Cognitive Service 로 바뀐 것 같습니다.

다른 분석도 요긴하게 사용할 수 있지만, 사회과학도의 입장에서는 

- 주어진 사진의 내용이 무엇인지에 대한 분석
- 주어진 사진에 등장하는 사람의 얼굴 탐지 및 탐지된 얼굴에 표현된 감정 추출

이상의 두 가지 작업이 가장 유용할 듯 싶습니다. 따라서 위 뒤 작업을 수행할 수 있는 코드를 첨부합니다.

두 작업 모두 일단 subscription key 가 필요합니다. Microsoft Azure Cognitive Service (<https://azure.microsoft.com/ko-kr/services/cognitive-services/>) 에 접속해서 subscription key 를 발급합니다. '무료 평가판'을 클릭하고 해당되는 API 메뉴에서 'API 키 가져오기'를 클릭해서 무료 key 를 발급받을 수 있습니다. 또는 Azure 계정을 만들어서 유료 key 를 발급받을 수도 있습니다. 당연히 유료 key 가 무료 key 보다 단위 시간당 많은 수의 사진을 분석할 수 있습니다.

