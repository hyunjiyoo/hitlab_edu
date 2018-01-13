## Machine Learning 개념 다지기
> Machine Learning에 대한 개념과 학습 방법 등을 나타내는 페이지입니다.

> Machine Learning의 기초 개념을 배우고 Machine Learning Library인 Tensorflow에 대한 기초적인 학습을 진행합니다.

__Machine Learning__(머신 러닝)은 인공지능(AI) 중 한 분야로, 기계가 _자체적으로 학습_ 할 수 있도록 하는 알고리즘을 말한다. 머신 러닝을 통해서 기계는 코드로 작성하지 않아도 학습 데이터 셋으로부터 훈련을 하고, 이를 통해서 새로운 데이터를 처리할 수 있게 된다. Machine Learning의 학습 방법에는 __Supervised Learning__(지도 학습)과 __Unsupervised Learning__(비지도 학습)으로 나뉜다.

### _지도학습_ & _비지도학습_
__지도 학습__ 은 데이터에 대해서 _Label(정답)이 주어진 상태_ 에서 기계를 학습시키는 방법이다.(데이터, 레이블 형태) 예를 들어, 필기체 인식을 하는 알고리즘을 구성한다고 하면, '이 글자는 어떤 글자(숫자)다.' 라고 미리 정답(기준)을 알려준 상태에서 학습을 하는 것이라고 보면 된다. 정답을 기준 삼아서 기계는 학습을 하게 되고, 끝나고 난 후, 임의의 데이터를 통해서 얼마나 정확히 예측하는지 비교를 할 수 있다. 지도 학습에는 학습을 통해 _연속적인 값을 예측_ 하는 __Regression__(회귀 분석), _어떤 종류의 값인지를 표시_ 하는 __Classification__(분류) 등이 있다.

반대로, __비지도 학습__ 은 데이터에 대해서 _Label(정답)이 주어지지 않은 상태_ 로 기계를 학습시키는 방법이다.(데이터 형태) 예를 들어, 필기체 인식을 하는 알고리즘을 구성할 때, 데이터만 주고 이것들을 비슷한 형태로 분류를 하고 나서 집단화를 하는 것이다. 올바르게 학습을 했을 때, 기계는 필기체 데이터를 각 각의 숫자 및 글자에 맞는 그룹을 형성하게 된다. 비지도 학습에는 _비슷한 군집을 추정_ 하는 __Clustering__(군집화)과 _데이터를 새롭게 표현하여 원래 데이터보다 쉽게 해석_ 할 수 있도록 하는 __Unsupervised Transformation__(비지도 변환)등이 있다.

### _Tensorflow_ - Machine Learning Library

![Alt Text][Tensorflow_logo]

앞으로 Machine Learning 학습에 대한 진행을 Tensorflow를 통해 진행할 예정이다. Tensorflow는 Google의 기계 학습 연구 팀 소속의 Google Brain 팀이 개발한 Machine Learning과 Deep Neural Network를 위한 Open-Source Software Library이다.

[Tensorflow 설치 사이트 바로가기](https://www.tensorflow.org/install/)

Tensorflow는 __Data Flow Graph__(데이터 플로우 그래프) 방식을 사용하였다. 데이터 플로우 그래프란 수학 계산과 데이터의 흐름을 __Node__(노드)와 __Edge__(엣지)를 사용한 __Directed Graph__ 로 표현한 것이다. 여기서 Node는 _수학적 계산, 데이터의 입출력, 데이터의 읽기 및 저장_ 기능을 수행한다. 그리고 Edge는 _Node 간의 데이터 입출력 관계_ 를 나타낸다. Edge는 동적 사이즈의 _다차원 데이터 배열(=Tensor)_ 을 실어 나르는데, Tensorflow의 어원은 여기서 나왔다.

- _Tensorflow의 특징_
    1. __Data Flow Graph__ 를 통한 풍부한 표현력
    2. 코드의 수정 없이 __CPU / GPU__ 모드 동작
    3. _Idea Test_ 단계에서 _Service_ 단계까지 이용 가능
    4. __계산 구조__ 와 __목표 함수__ 만 정의해서 _자동으로 미분 계산 처리_ 가능
    5. __Python / C++__ 지원, __SWIG__ 을 통한 다양한 언어 지원 가능

### Tensorflow 기초 개념



[Tensorflow_logo]:https://imgur.com/IB5SYiQ.jpg
