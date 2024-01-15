#  👑 Vienna Code Project 👑

## 주제
![마크클라우드](./imgs/corp_logo.png)<br>
**[CV] 마크클라우드 도형코드 인식 서비스**




## 문제정의
Object Detection

## 사용환경
<!-- <img src=https://img.shields.io/badge/{배지이름}-{css컬러}?style={스타일}&logo={로고}&logoColor={로고컬러}> -->
<img src="https://img.shields.io/badge/windows-0078D4?style=for-the-badge&logo=windows&logoColor=white">
<img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=white">
<br>
<img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white">
<img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=Jupyter&logoColor=white">

## 사용기술
<img src="https://img.shields.io/badge/Python-3776AB?style=plastic&logo=Python&logoColor=white">
<img src="https://img.shields.io/badge/Numpy-013243?style=plastic&logo=Numpy&logoColor=white">
<img src="https://img.shields.io/badge/Pandas-150458?style=plastic&logo=Pandas&logoColor=white">
<img src=https://img.shields.io/badge/scikit_learn-F7931E?style=plastic&logo=scikitlearn&logoColor={로고컬러}>
<img src=https://img.shields.io/badge/pytorch-122323?style=plastic&logo=pytorch&logoColor={로고컬러}>


## 📅 기간
2023.12.26 ~ 2024.01.09


##  ✍ 평가지표
(임시) mAP IoU Threshold(=0.5) 

목표

![평가](./imgs/evaluation.png)

- mAP 값 0.8 달성을 목표로 함 (기존의 프로덕트는 0.7으로 해당 값을 기준값으로 정함)

- mAP의 측정 방식
    - 분류된 도형코드 모두가 정답 도형코드에 포함되어야 통과
        
        i.e.
        
        분류된 도형코드: **050711, 050103, 020117**, 010201, 140102
        
        정답 도형코드: **050711, 050103, 020117**
        
        → 정답 050711, 050103, 020117 모두가 분류 코드 내에 포함됨으로 통과


##  🔔 컨벤션 규칙

### 주로 사용하는 태그

- **Feat** : 새로운 기능을 추가하는 경우
- **Fix** : 버그를 고친경우
- **Docs** : 문서를 수정한 경우
- **Style** : 코드 포맷 변경, 세미콜론 누락, 코드 수정이 없는경우
- **Refactor** : 코드 리펙토링
- **Test** : 테스트 코드. 리펙토링 테스트 코드를 추가했을 때
- **Chore** : 빌드 업무 수정, 패키지 매니저 수정
- **Design** : CSS 등 사용자가 UI 디자인을 변경했을 때
- **Rename** : 파일명(or 폴더명) 을 수정한 경우
- **Remove** : 코드(파일) 의 삭제가 있을 때. "Clean", "Eliminate" 를 사용하기도 함

### 기타 태그 타입들(참고)

- **Add** : 코드나 테스트, 예제, 문서등의 추가 생성이 있는경우 
- **Improve** : 향상이 있는 경우. 호환성, 검증 기능, 접근성 등이 될수 있습니다.
- **Implement** : 코드가 추가된 정도보다 더 주목할만한 구현체를 완성시켰을 때
- **Move** : 코드의 이동이 있는경우
- **Updated** : 계정이나 버전 업데이트가 있을 때 사용. 주로 코드보다는 문서나, 리소스, 라이브러리등에 사용합니다.
- **Comment** : 필요한 주석 추가 및 변경



## 팀원
| 이름        | Connect To                           |
|--------------|------------------------------------------|
| 이현희      | [ardor924@gmail.com](mailto:ardor924@gmail.com)  |
| 강재성      | [@username2](mailto:email1@example.com) |
| 이도형      | [@username4](mailto:email1@example.com) |
| 정재훈      | [@username5](mailto:email1@example.com) |


## References
[(예시) YOLOv8 깃허브 주소](https://github.com/ultralytics/ultralytics)