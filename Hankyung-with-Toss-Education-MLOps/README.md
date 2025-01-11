# Hankyung-with-Toss-Education-MLOps

#### 한국경제신문 with Toss Bank MLOps 교육 과정에서 배운 내용에 대한 TIL입니다.

---

1. Python Programming Basics: **week1**

2. Python Data Analysis: **week2**

---

3. Database: **week3**

---

4. ML [Machine Learning]: **week4 ~ week8**


  - Mathematics for ML

https://www.notion.so/Mathematics-for-ML-177b89b9b67880f8a4a4ca50e12d0035?pvs=4

    : 효율적인 학습을 위해 수학적 깊이를 당장 다지는 것보다, 프로그래밍을 통해 개념을 적용하고 결과를 얻는 것이 더 빠르고 효율적인 학습 방법이라고 판단. 
    : 다만, 수식을 깊이 이해하지 않으면, 모델이 잘못 작동하거나 성능이 떨어질 때 근본 원인을 파악하기 어렵고, 새로운 알고리즘이나 비표준적인 문제를 다룰 때나 알고리즘 설계 및 최적화 시 한계에 부딪힐 수 있기에 장기적으로 더 깊은 성과를 위해 모든 것을 동시에 하기 보단 프로그래밍과 개념 적용(수식의 계산과 최적화는 이미 라이브러리가 처리해 주기에, 모델 선택, 하이퍼파라미터 튜닝, 데이터 전처리에 집중)에 집중하되, 개념 적용 시 필요한 수식을 점진적으로 이해하는 방향으로 학습.

    - 수열과 집합의 합과 곱
    - 데이터와 행렬
    - 벡터와 행렬의 연산
    - 행렬의 성질
    - 선형 연립방정식과 역행렬 
    - 선형대수와 해석기하의 기초
    - 좌표와 변환
    - 고윳값 분해
    - 특잇값 분해
    - 미적분
    - 함수
    - 함수 미분

  - ML Theory

https://www.notion.so/ML-Theory-177b89b9b67880f08f75d9729c18d9fb?pvs=4

    - 머신러닝 개념
    - 분류 모델 평가 방법
    - Classification
    - Regression
    - 차원 축소(Dimension Reduction)
    - 군집
    - 추천 시스템
    - Text Preprocessing
    - Text Vectorization
    - Topic Modeling

  - ML Programming

---

- 실무 프로젝트 (중간 프로젝트: MLOps 반): **week9 ~ week11**

https://github.com/HKToss-JSIJ/HKToss-Project.git

    : 대상 수상

---

5. DL [Deep Learning]: **week11 ~ week17**
  
  - DL Theory

https://www.notion.so/DL-Theory-177b89b9b67880b89028ec803764748d?pvs=4
    
    -  기초

        - ML | DL 각각의 주 사용처
        - 퍼셉트론
        - 활성화 함수
        - 신경망 설계
        - 손실 함수
        - 신경망 학습의 이해
        - 오차역전파
    
    - 심화

      - 최적화
      - 정규화
      - 학습 스케쥴링
      - 초기화
      - 표준화 

    - CV: Computer Vision
    
      - CNN
      - Advanced CNN
        - VGG Net
        - Inception Net
          - v1, v2, v3
        - Residual Network
          - Loss Landscape
          - Skip Connection
          - Residual Learning

    - NLP: Natural Language Processing

      - 딥러닝 기반 자연어 처리란?
      - Word Embedding
        - Word Sense, WordNet, Word2Vec, GloVe, FastText, Embedding Layer
      - RNN 기반 자연어 처리
         - RNN, BPTT, LSTM
      - Language Model
        - LM과 LM의 수식, LM 평가 척도(Perplexity)
      - Seq2Seq
        - Encoder, Decoder, Generator
      - Attention  
        - Query, Key, Value, Attention 예시, Linear Transform, Batch Matrix Multiplication, Attention 수식, Seq2Seq 기반 Attention 전체 구조, Masking, Input Feeding, Teacher Forcing
      - Transformer(Attention is All You Need 2017.06)
        - Transformer 모델 개요 (Self-Attention 기법의 핵심 원리, Transformer의 주요 구성 요소)
        - 트랜스포머 구조 (인코더(Encoder)와 디코더(Decoder) 구조)
        - 어텐션 메커니즘 (Scaled Dot-Product Attention, Multi-Head Attention)
        - 인코더(Encoder) 디테일 (Input Embedding과 Positional Encoding, Feed-Forward 네트워크, Add & Norm 및 Skip Connections)
        - 디코더(Decoder) 디테일 (Masked Multi-Head Attention, 인코더-디코더 어텐션 Teacher Forcing과 Masking)
        - Evaluation(BLEU Score)      
      - Transformer Based Model

  - DL Programming

---
6. MLOps: **week18 ~ week20**

https://www.notion.so/Hankyung-with-Toss-Education-MLOps-MLOps-127b89b9b6788091b77dc54f78a810be?pvs=4

    - Linux 기반 환경 세팅
    - Data & Model Management
      - DVC
      - MLFlow
      - Feature Store
    - Model Serving
      - Flask
    - Monitoring
      - Prometheus
      - Grafana
      - Node 모니터링
    - Container
      - Docker
      - Docker Image & Container
      - 이미지와 컨테이너 관리
      - Data Management, Volume
      - 컨테이너 네트워크 통신
      - 다중 컨테이너 실습
      - Docker Compose
    - CI/CD Pipeline
      - ML Workflow: Github Actions, Jenkins
      - Model Tracking & Experiment: CML, DVC-CML
    - Project 연습: Docker 기반 MLOps CI/CD Pipeline
      - FastAPI Serving API
      - FastAPI - Prometheus Metric 수집
      - Prometheus - Grafana 연동
      - Locust Simulation
      - Jenkins ML Model Changing
      - Jenkins Monitoring

---

- 협업 프로젝트 (최종 프로젝트: MLOps반 + FullStack반): **Week20 ~ Week26**

https://github.com/meowmung

    : 대상 수상

---