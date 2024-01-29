#=======================================
# 모듈불러오기
#=======================================
import streamlit as st
from PIL import Image
import torch
from torchvision import transforms
import timm

#=======================================
# 모델로드 및 전처리
#=======================================
# EfficientNet 모델 생성
model = timm.create_model('efficientnet_b0', pretrained=False, num_classes=2)

# state_dict 로드
state_dict = torch.load('./[Category_Classification]EPC50_BAT32_efficientnet_b0_v0.0.2.pt', map_location=torch.device('cpu'))
model.load_state_dict(state_dict)

# 모델을 GPU로 옮김
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 모델을 evaluation 모드로 설정
model.eval()


#=======================================
# 함수정의
#=======================================

# 이미지 전처리 함수
def preprocess_image(image_path):
    image = Image.open(image_path)
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = transform(image)
    input_batch = input_tensor.unsqueeze(0)

    # 입력 데이터도 모델이 현재 사용하는 디바이스로 옮김
    input_batch = input_batch.to(device)

    return input_batch

# 예측 함수
def predict_image(image):
    with torch.no_grad():
        output = model(image)
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    return probabilities


#=======================================
# Streamlit 앱
#=======================================
st.title("개/고양이 이미지 분류기")

uploaded_file = st.file_uploader("이미지를 업로드하세요.", type=["jpg", "jpeg", "png"])

# 이미지처리
if uploaded_file is not None:
    st.image(uploaded_file, caption="업로드한 이미지", use_column_width=True)
    st.write("")
    st.write("예측 결과:")

    # 업로드한 이미지 전처리 및 예측
    input_image = preprocess_image(uploaded_file)
    predictions = predict_image(input_image)

    # 소프트맥스 함수를 사용하여 확률 값을 정규화
    normalized_probabilities = predictions * 100

    # 예측 결과 표시
    probability_cat = normalized_probabilities[0].item()
    probability_dog = normalized_probabilities[1].item()

    if probability_dog > probability_cat:
        st.write(f"개에 가까울 확률: {probability_dog:.2f}%")
    else:
        st.write(f"고양이에 가까울 확률: {probability_cat:.2f}%")
