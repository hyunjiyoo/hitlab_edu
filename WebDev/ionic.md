## ionic framework
> Hybrid Application의 개발툴인 **ionic framework**에 대한 전반적인 개념 및 어떻게 사용하는지 배울 수 있는 페이지이다.
--------------------------

### Index : 
1. [ionic framework 란?](#m1)
    +   ionic framework의 정의
    +   Native App vs Web App vs Hybrid App
    +   ionic framework의 특징
    +   Angular.js와 Apache Cordova
    +   MVC / MVVM Pattern
    +   ionic framework vs 그 외 하이브리드앱 개발 프레임워크 비교

2. [ionic framework 설치](#m2)
    +   ionic framework의 본격적인 설치 단계
    +   기본 프로젝트 살펴보기

3. [ionic framework 튜토리얼](#m3)(수정예정)
    +   App 생성
    +   App Build
    +   ionic이 제공하는 UI 컴포넌트
    +   (추후 공부 후 내용 추가 예정)

4. [ionic framework의 미래](#m4)
    +   현재 ionic framework는 어디까지 왔을까?
    +   ionic framework는 앞으로 어디로 갈까?
### Reference 
##### [ionic framework 관련 문서](https://ionicframework.com/docs/)
##### [ionic framework 포럼 바로가기](https://forum.ionicframework.com/c/ionic-v1)
------------------

## ionic framework란?<a name="m1" />
> ionic framework 및 Hybrid App에 대한 개념

![Alt Text][ionic_logo]

### ionic framework의 정의

 **ionic framework**는 **Hybrid Applicaion**을 만들기 위한 HTML5 모바일 어플리케이션 개발 Framework로써 Mobile App에서 사용되는 UI를 **HTML**, **CSS**, **JavaScript**를 이용하여 제작할 수 있게 해주는 **Cordova 기반**으로 구성된 Hybrid App 개발 Framework.

![Alt Text][native_web_hybrid]

### Native App vs Web App vs Hybrid App

**Native App**, **Web App**, **Hybrid App**의 특징

먼저 **Native App**은 일반적으로 순수(pure) Application을 말하는데, 일반적인 어플들을 생각할 수 있다. Native App의 개발툴은 **Android Studio**, **Xcode** 등이 대표적이다.

**Web App**은 Mobile Web과 Native App을 결합한 앱이다. Mobile Web의 특징을 가지면서도 Native App의 장점을 가지고 있다. Web App의 개발툴로는 **JQM(JQuery Mobile)**, **Sencha** 같은 Framework가 있고, **PhoneGap**, **Appspresso**을 통해서 Hybrid App으로 변환이 가능.

마지막으로 **Hybrid App**은 Hybrid라는 단어에 맞게 Native와 Web App의 특징을 섞어서 만든 앱으로 Native Platform으로 틀을 구성하고 그 안에 Web App의 속성이 들어있는 앱이다.

Native App, Web App, Hybrid App의 특징들을 비교해놓은 표

|     | Native App | Web App | Hybrid App |
| --- | ---------- | ------- | ---------- |
| 마켓 | 등록 가능 | 등록 불가능 | 등록 가능 |
| 기기 고유 정보 | 접근 가능 | 접근 불가능 | 접근 가능 |
| 접근 | App | URL | App |
| 재사용 가능성 | 불가능 | 가능 | 가능 |
| 동작(구동) 속도 | 매우 빠름 | 브라우저 성능 의존적 | 빠름 |
| 주요 언어 | Java, Swift, Kotlin, Object-C | HTML, CSS, JS | HTML, CSS, JS |

### ionic framework의 특징
 + **Cordova 기반** -> Cordova와 매우 유사
 + **AngularJS**를 기반으로 만들어짐. **MVC** 혹은 **MVVM** 패턴으로 개발
 + HTML로 UI를 만들지만 Native App에 가까운 UI 컴포넌트를 제공
 + **Cross Platform** 빌드가 가능
 + 활발한 개발자 포럼을 지원 [ionic forum 사이트 바로가기][ionic forum]
 + ionic framework로 개발한 앱의 Architecture
![Alt text][ionic_architecture]

### AngularJS와 Apache Cordova(내용 보강 예정)

#### AnuglarJS
![Alt Text][angular_logo]

AngularJS는 Google에서 만든 Web App을 만들 수 있는 Single Page Application(SPA) Framework 로 Javascript 를 사용하여 간단하게 Web App을 만들 수 있는 framework.
 + SPA란? 하나의 웹 페이지가 실행될 때 페이지 주소의 변동이 없이 View를 로드하여 사용하는 것.

#### AngularJS의 특징
 + 코드의 양이 기존의 제작 방식에 비해서 대폭 줄어듦
 + 양방향 데이터 바인딩(Two-way Binding)이 가능

```
<body ng-app>
 <span>Insert Your Name : </span>
 <input type="text" ng-model="user-name" />
 <h3>Echo: {{ user.name }}</h3>
</body>
```
ng-model 지시어로 양방향 바인딩을 하여 input에 입력한 내용이 바로 출력됨.
 + Directives(지시어)의 사용
```
<body>
 <div id="chart" />
</body>
```
이 코드만 보아서는 어떤 역할을 하는지 모르기 때문에 javascript를 참조해야함.
```
<body>
 <pie-chart width="400" height="400" data="data" />
</body>
```
Directives(지시어)의 사용으로써 훨씬 더 명확하게 파이차트를 추가한다는 사실을 알아보기 쉬움.
 + 개발 영역을 명확히 분리시켜 줌(MV*)
 + HTML을 템플릿으로 사용 및 확장 사용이 가능
 + Dependency Injection(의존성 주입)으로 객체 및 함수를 생성하고 연결이 가능

#### Apache Cordova

![Alt Text][cordova_logo]

Apache Cordova 는 모바일 어플리케이션을 Multi-Platform(Cross Platform) 개발을 위한 Framework.

#### Apache Cordova 특징
 + HTML5, CSS3, JavaScript 등 표준 웹기술 사용
 + Native Device에 접근 할 수 있는 Device API set 제공
 + 다양한 플러그인으로 Native App 기능들 구현


### MVC / MVVM Pattern

#### MVC Pattern

Model-View-Controller 의 Software Architecture.

![Alt Text][mvc_pattern]

 | Model | View | Controller |
 | ----- | ----- | ------    |
 | Data Layer   | UI Layer | Logic Layer
 | 뷰와 컨트롤러 사이에서 전달되는 데이터를 나타냄   | Model로부터 오는 데이터를 보여줌 | Behavior에 알림 받고 필요하면 Model Update

MVC의 장점
 + 사용자 인터페이스로부터 비즈니스 로직을 분리
 + 어플리케이션의 시각적 요소나 비즈니스 로직을 서로 영향없이 수정 가능
 + Testability 를 높여줌

**MVC Pattern 예시**

![Alt Text][mvc_exam]

#### MVVM Pattern

MVC Pattern의 변형으로 Model - View - ViewModel의 Software Architecture. View의 추상화를 만드는 것이 핵심. Model과 View는 MVC Pattern과 동일.

![Alt Text][mvvm_pattern]

View Model : Controller 대신 나온 개념. View가 필요로하는 데이터와 Command를 담당.

MVC Pattern과의 차이점 : ViewModel은 View를 지원하고 View가 필요한 데이터와 Command를 제공.

MVVM의 장점
 + View와의 의존성을 완벽히 분리 가능.
 + Binding을 통해 ViewModel의 속성이 변경되면 View가 변경되게 가능.
 + View와 Binding될 때 가장 강력함.
 + 프로그램(App)의 구조가 단순화 됨.

**MVVM Pattern 예시**

![Alt Text][mvvm_exam]

가운데 코드를 통해서 ViewModel(왼쪽)과 View(오른쪽)를 Binding하여 완전한 독립성을 보여줌. (예시 수정 예정)

### ionic framework vs 그 외 하이브리드 앱 개발 프레임워크 비교

ionic framework, 그리고 타 Hybrid App 개발 Framework

> ionic framework vs Phone Gap vs Framework 7 vs Mobile Angular UI

![Alt Text][hybrid_compare]

| ionic framework | Phone Gap | Framework 7 | Mobile Angular UI |
| --------------- | --------- | ----------- | ----------------- |
| Angular.js, Apache Cordova 위에 구축됨 | Adobe에서 인수 후 Plugin 개발과 Open-Source 정책이 좋아짐 | Mobile OS의 기본 모양, 느낌의 Hybrid App 개발 가능 | Bootstrap3 Angular.js framework를 사용한 Hybrid App 구축 |
| 무료 Open-Source Project | 기기의 가속도, 카메라, 나침반, 파일 시스템 등에 접근 가능 | 무료 Open-Source | Angular.js 지시문만을 사용하여 모바일 사용자 환경 구축 |
| 약 120개의 기본 장치 기능 제공 (ex: Bluetooth, HealthKit...) | Rendering은 HTML5, CSS로, Logic은 JavaScript로 함 | Native Scrolling 및 다중보기 지원 | fastclick.js와 overthrow.js가 함께 제공 |
| CLI(Command Line Interface) | Native Layer와 HTML5 간의 직접 통신 가능 | CSS3를 통한 가속 애니메이션 | UI 컴포넌트 제공(ex: Overlay, sidebars...) |

이 외에도 Xamarin, Intel의 XDK, Appcelerator Titanium 등이 있음.

## ionic framework 설치<a name="m2" />
> ionic framework 를 위해 필요한 AngularJS, Apache Cordova에 대한 간단한 학습 및 ionic framework 설치법

ionic framework를 설치하기 앞서 먼저 필수로 설치해야하는 AngularJS, Apache Cordova 에 대해서 간단한 정리를 하고 설치 단계에 들어가도록하자. (배치 수정 예정)


### ionic framework의 본격적인 설치
#### Node.js 설치
npm을 이용하여 설치를 진행할 것이기 때문에 먼저 Node.js를 설치해줌.

[Node.js 설치 바로가기](https://nodejs.org/en/download/)

Mac으로 Homebrew를 쓸 경우에는 다음과 같은 명령어로 간단하게 설치를 할 수 있음.
```
brew install node
```

#### Apache Cordova 설치
Apache Cordova를 기반으로 만들어진 Framework이기 때문에 Cordova에 대한 설치가 필요.
```
npm install -g cordova
```

Cordova의 설치가 끝나면 다음과 같은 화면이 나온다.
![Alt Text][cordova_install]

#### ionic framework 설치
```
npm install -g ionic
```
ionic framework의 설치가 끝나면 다음과 같은 화면이 나온다.
![Alt Text][ionic_install]

### 기본 프로젝트 살펴보기

#### Project 생성
ionic framework의 설치가 끝났으므로 프로젝트를 생성하여 작업을 할 수 있다.
```
ionic start blank_exam blank
```

blank는 아무런 Template 없이 빈 프레임으로 시작을 한다는 의미이다. 프로젝트를 생성하면 다음과 같은 화면이 나온다.
![Alt Text][ionic_exam]

기본 제공되는 Template으로는 다음과 같음.
 + tabs : 기본 3개의 tab menu로 구성된 template
 + blank : template이 없는 기본 프로젝트
 + sidemenu : content 부분에 navigation bar가 있는 side menu template
 + super : 14개의 준비된 페이지 디자인으로 시작할 수 있는 template
 + tutorial : ionic framework에 대한 튜토리얼이 담긴 template

Project를 생성했으면 실행하기 위해서 생성한 blank_exam 디렉토리로 들어간다.
```
cd blank_exam
ls -l
```
다음과 같이 디렉토리의 구성이 이루어져있다.
![Alt Text][ionic_directory]

중요 디렉토리 및 파일
 + bower.json : bower dependencies
 + config.xml : cordova configuration
 + gulpfile.js : gulp tasks
 + hooks : custom cordova hooks to execute on specific commands
 + ionic.project : ionic configuraion
 + package.json : node dependencies
 + platforms : iOS / Android specific builds will reside here
 + plugins : where your cordova/ionic plugins will be installed
 + scss : scss code, which will output to www/css/
 + www : applicastion - JS code and libs, css, images, etc.

#### Web Page로 확인하기
만든 프로젝트를 수정한 후 실시간으로 확인을 하고 싶으면 다음과 같은 Command를 친다.
```
ionic serve
```
그러면 build를 하면서 다음과 같은 Web Page가 나오는 것을 볼 수 있다.
![Alt Text][ionic_serve]

#### App build
만든 프로젝트를 디바이스에서 확인을 하고싶다면 다음과 같은 명령어를 친다.
```
ionic cordova platform add android(ios)
```
초기 버전에는 명령어가 ionic build ios(android) 였지만 현재 버전(3.x)에서는 위처럼 바뀌었다.
platform을 추가하면 다음과 같은 창이 나온다.

![Alt Text][ionic_addplatform]

만약 실행 결과를 Simulator로 보고싶다면 다음과 같은 명령어를 수행한다.
```
ionic cordova build android(ios)
ionic cordova emulate android(ios)
```
그러면 설치되어있는 에뮬레이터에서 돌아가는 것을 확인할 수 있다.
본인의 Device에서 실행 결과를 보고싶다면 다음과 같은 명령어를 수행한다.
```
ionic cordova run android
```
명령어를 수행하면 마지막에 다음과 같은 메세지가 나오고 Android Device에 다음과 같이 정상적으로 빌드가 된 것을 볼 수 있다.
![Alt Text][ionic_run]

#### 코드 수정
코드 수정은 주로 ./www/index.html 파일에서 이루어진다.
Bracket이나 다른 에디터를 이용하여 수정이 가능하고 css, javascript 코드 삽입이 가능하다.
blank일 때 기본 프레임은 다음과 같다.

![Alt Text][index_code1]

![Alt Text][index_code2]

## ionic framework 튜토리얼<a name="m3" />
> ionic framework를 사용한 Hybrid App 만들기


## ionic framework의 미래<a name="m4" />
> ionic framework는 현재, 그리고 미래

### 현재 ionic framework는 어디까지 왔을까?

#### ionic framework로 만든 Hybrid App
ionic framework 를 이용하여 현재 나온 앱의 예시.

![Alt Text][app_sample1]
![Alt Text][app_sample2]

이 중에서 'MarketWatch' App을 참조해보면,

![Alt Text][sample1]

앱의 상단부를 보면 sidebar 등의 Menu 버튼이 구현이 되어있고, 페이지는 Web App 처럼 구현이 되어있다.
또한 두 번째 사진을 보면 밑에 Tab 버튼 기능이 구현된 것을 볼 수 있다. 위에서 말했듯 ionic framework를 사용하여 native 와 web의 조화로 만들어진 hybrid App을 볼 수 있다.

[ionic_logo]:http://i.imgur.com/YHn0XaK.png
[native_web_hybrid]:http://i.imgur.com/GN15L1V.jpg
[ionic forum]:<https://forum.ionicframework.com/>
[ionic_architecture]:https://imgur.com/CNdSVqK.png
[mvc_pattern]:https://imgur.com/4QdbaTE.png
[mvc_exam]:https://imgur.com/nxUoqfE.png
[mvvm_pattern]:https://imgur.com/jx2vHaw.png
[mvvm_exam]:https://imgur.com/s2ZELu1.png
[angular_logo]:https://imgur.com/FiVhVa0.jpg
[hybrid_compare]:https://imgur.com/8Rou30i.png
[cordova_logo]:https://imgur.com/CK0S6qy.png
[app_sample1]:https://imgur.com/IVqj8pu.jpeg
[app_sample2]:https://imgur.com/qKeo8Lm.jpeg
[sample1]:https://imgur.com/MHRUGF9.jpeg
[cordova_install]:https://imgur.com/Xqz8st8.png
[ionic_install]:https://imgur.com/8uTj3EC.png
[ionic_exam]:https://imgur.com/dbZ7xUo.png
[ionic_directory]:https://imgur.com/YmqQj9y.png
[ionic_serve]:https://imgur.com/U7TDW5f.png
[ionic_addplatform]:https://imgur.com/H04Pnp7.png
[ionic_run]:https://imgur.com/bVsnJfo.png
[index_code1]:https://imgur.com/O3VVSz4.png
[index_code2]:https://imgur.com/YJaVQzl.png
