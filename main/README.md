#  process of project

## contents

- csv_dataset
- dataset
- experiment
- results
- save_weights

## csv_dataset

- 이번 프로젝트는 주요 정보를 json 파일을 통해서 제공하고 있습니다. 그래서 프로젝트 기간 동안 원활한 작업 진행을 위해서 csv 파일로 추출했습니다.
- json 파일의 구조는 이미지 정보, 주석 정보, 비엔나 코드 정보 세 개로 구분되어 있습니다.
- 1.json_to_csv는 세 개의 정보를 따로 csv 파일로 추출하는 과정입니다.
- 2.csv_edit은 병합하기 위해서 겹치는 컬럼을 만들어 주는 과정입니다.
- 3.csv_merge는 겹치는 칼럼을 토대로 3개의 정보를 하나로 병합하는 과정입니다.
- 3.csv_merge의 마지막에는 각 비엔나 코드의 숫자상 오름차순으로 0~391의 인덱스 칼럼을 추가했습니다.

## dataset

- YOLOv8 학습을 위해서 해당 알고리즘 모델에 맞는 데이터셋이 존재해야 하기 때문에 알맞은 데이터셋을 구성하기 위한 코드입니다.
- 기존에 제공된 정보에는 bbox 정보가 존재하는데 bbox의 형태는 x_min, y_min, width, height 순서로 되어 있습니다.
- 제공된 bbox는 이미지 사이즈의 범위를 벗어나거나 x_min, y_min값이 음의 영역에 존재하고 있는 경우가 있었습니다.
- dataset_v1은 범위를 지정해주고 YOLOv8의 형태인 x_center/image_width, y_center/image_height, bbox_width/image_width, bbox_height/image_width의 정보를 담고 있는 txt 파일을 생성해줍니다.
- 데이터셋을 구성하고 확인해보니 제공된 bbox는 width, height에서도 음수를 가지고 있는 경우가 존재했습니다.
- dataset_v2는 width, height를 직접 사용하지 않고 x_max, y_max 값으로 변환시켜줘서 잘 못된 부분을 바로 잡았습니다.
- dataset_v3는 양의 범위로 완전히 bbox 좌표가 벗어나는 경우를 제거시켜줬습니다.
- dataset_v4는 음의 범위로 완전히 bbox 좌표가 벗어나는 경우를 제거시켜줬습니다.

## experiment

- YOLOv8 모델을 5 epochs만 학습을 시켜서 gpu vram 할당량을 확인하는 실험을 진행했습니다.
- gpu vram 할당량을 확인한 이유는 학습을 돌리는 로컬 환경이 제한되어 있어서 적절한 조건을 찾기 위해서 실험을 했습니다.
- experiment_imgsz는 32, 320, 416(기존 이미지 사이즈), 640, 960, 1280의 원활한 변경해가면서 진행했습니다.
- 32 사이즈는 YOLOv8의 최소 사이즈였는데 너무 작아서 결과가 거의 나오지 않는 수준이었습니다.
- 나머지 사이즈는 gpu vram 할당량의 차이만큼 결과의 차이가 그리 크지 않았습니다.
- experiment_model(n,s,m,l,x)는 이름 그대로 YOLOv8의 모델을 비교해 보는 실험이었습니다.
- 가벼운 모델에서 무거운 모델로 갈수록 gpu vram 할당량이 많아지는 것은 물론이고 속도에서도 확실히 가벼운 모델이 빨랐습니다.
- 다만 epoch가 5밖에 안 되어서 성능을 깊게 확인하지는 못했지만 이미 이 부분에 대해서는 홈페이지의 문서에 자세하게 나와 있습니다.

## results

- 로컬 환경에서 적절한 데이터 범위와 이미지 크기, 배치 사이즈, 모델 종류를 바꿔가면서 학습한 결과입니다. (배치 사이즈는 patience가 5인 early stopper가 설정되어 있어서 학습한 epochs는 다를 수 있습니다.)
- v1은 dataset_v1을 통해서 비엔나 코드가 ＇010102＇인 단일 클래스만 학습한 결과입니다. 모델은 YOLOv8n이고 이미지 사이즈는 320, 배치 사이즈는 2, epochs는 29입니다.
- v2는 dataset_v1을 통해서 비엔나 코드가 ＇010102＇, ＇010103＇, ＇010104＇, ＇010105＇, ＇010109＇인 다중 클래스를 학습한 결과입니다. 모델은 YOLOv8n이고 이미지 사이즈는 320, 배치 사이즈는 2, epochs는 100입니다.
- v3는 dataset_v2를 통해서 비엔나 코드가 ＇010102＇인 단일 클래스만 학습한 결과입니다. 모델은 YOLOv8n이고 이미지 사이즈는 320, 배치 사이즈는 2, epochs는 16입니다.
- v4는 dataset_v3를 통해서 비엔나 코드가 ＇010102＇인 단일 클래스만 학습한 결과입니다. 모델은 YOLOv8n이고 이미지 사이즈는 640, 배치 사이즈는 2, epochs는 44입니다.
- v5는 dataset_v4를 통해서 비엔나 코드가 ＇010102＇인 단일 클래스만 학습한 결과입니다. 모델은 YOLOv8n이고 이미지 사이즈는 640, 배치 사이즈는 2, epochs는 36입니다.
- v6는 dataset_v1을 통해서 비엔나 코드가 ＇010102＇인 단일 클래스만 학습한 결과입니다. 모델은 YOLOv8m이고 이미지 사이즈는 640, 배치 사이즈는 8, epochs는 28 입니다.
- v7은 dataset_v1을 통해서 비엔나 코드가 ＇010102＇, ＇010103＇, ＇010104＇, ＇010105＇, ＇010109＇인 다중 클래스를 학습한 결과입니다. 모델은 YOLOv8m이고 이미지 사이즈는 640, 배치 사이즈는 8, epochs는 71입니다.
- v8은 dataset_v4를 통해서 비엔나 코드가 ＇010102＇ 단일 클래스만 학습한 결과입니다. 모델은 YOLOv8m이고 이미지 사이즈는 640, 배치 사이즈는 4, epochs는 22입니다.
- v9은 dataset_v4를 통해서 비엔나 코드가 ＇010102＇, ＇010103＇, ＇010104＇, ＇010105＇, ＇010109＇,＇010110＇, ＇010112＇, ＇010114＇, ＇010115＇인 다중 클래스를 학습한 결과입니다. 모델은 YOLOv8m이고 m이미지 사이즈는 640, 배치 사이즈는 4, epochs는 62입니다.
- v10은 dataset_v4를 통해서 비엔나 코드가 392개 모두인 다중 클래스를 학습한 결과입니다. 모델은 YOLOv8m이고 이미지 사이즈는 320, 배치 사이즈는 256, epochs는 10입니다. 

## save_weights

- save_weights는 results를 통해서 생성된 weights 파일 따로 분리해서 저장한 공간입니다.
- 이곳의 pt 파일들은 이번 프로젝트의 최종 결과물인 데모 페이지를 만들 때 사용될 것입니다.