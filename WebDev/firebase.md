Google Firebase
---
>Google Firebase의 지원범위, 유/무료, 제약조건 등의 전반적인 지식을 전달. 또한 Tutorial 형식으로 핵심 기능을 구현하면서 학습하는 것을 목표로 하는 문서입니다.

### Index : 
1. [개요](#m1)
    +   Firebase 정의
    +   Firebase 기능
    +   Firebase vs Reaml vs AWS
2. [기능별 사용법](#m2)
3. [튜토리얼](#m3)
    +   Android로 시작하기
    +   웹으로 시작하기
    +   iOS로 시작하기
### Reference :
-    [Google Firebase 문서][r1]
-    [Android 튜토리얼][r2]

---
## 1.개요<a name="m1" />
>FireBase 소개

![Alt text][img0]
>출처:http://cdn03.androidauthority.net/wp-content/uploads/2017/04/Firebase-Logo-840x272.png

### Firebase 정의
Firebase는 Andrew Lee와 James Tamplin이 2011년에 만들어 2012년에 공식적으로 발표했습니다. Firebase는 유저들이 클라이언트로부터의 데이터를 저장하고 동기화하는 것을 가능하게 해주는 API를 제공하는 real-time database의 역할을 했습니다. 2년 후 Firebase는 구글에 합병되고, 성공적인 앱 개발을 위한 다양한 서비스들을 갖추게 됩니다.

Google Firebase는 효율적이고 더 좋은 앱을 개발하기 위한 tool과 infrastructure을 제공하는 Baas(Backend-as-a-service)입니다. 앱을 개발하는 과정엔 제공하고자하는 서비스를 기획/설계하고, Back-end, Front-end를 개발하고 테스트 및 유지보수를 하는 등 많은 인력과 시간을 소비합니다. 이에 Google Firebase는 Back-end 프로그램과 그 외 앱을 성장시키기 위한 기능들을 제공합니다. 앱의 개발을 돕는 Realtime Database, Hosting, Authentication 등과 앱의 성장을 돕기 위한 Analytics, Invite, Ads 등의 기능으로 구성됩니다. 이러한 모든 도구들은 iOS와 Android에서 모두 작동되고, 또한 web, C++, Unity 플랫폼에서 사용할 수 있도록 SDK를 제공합니다. 다양한 서비스를 제공합으로써 시간과 에너지를 차별성 있는 앱을 개발하고, 성공적인 앱을 개발하는데 집중할 수 있도록 하는 것이죠.

![Alt text][app_dev]

### Firebase 기능
여기선 Firebase를 구성하는 기능들에 대해 소개할 것입니다. 아래의 그림과 같이 Firebase는 개발을 돕는 기능들과 앱의 성장을 돕는 기능들로 구성됩니다. 먼저 개발을 돕는 기능들을 살펴 보겠습니다.
![Alt text][img1]

- 실시간 데이터베이스 :

Firebase 실시간 데이터베이스는 클라우드 호스팅 데이터베이스입니다. 데이터는 JSON으로 저장되고 연결된 모든 클라이언트에 실시간으로 동기화 됩니다. 또한 오프라인에 최적화 되어있습니다. 사용자의 인터넷 연결이 끊기면 데이터베이스 SDK는 기기의 로컬 캐시를 사용하여 변경사항을 저장하고 온라인 상태가 되면 로컬 데이터가 자동으로 동기화됩니다. 

데이터베이스 보안규칙을 사용해 사용자별, 데이터별 액세스 권한, 데이터베이스 구조를 지정할 수 있습니다. 이를 통해 데이터베이스의 보안이 유지되는 것이죠. 데이터베이스 관리와 보안규칙은 콘솔을 통해 접근할 수 있습니다.

- 인증 : 

Firebase 인증은 안전한 인증 시스템을 손쉽게 구축하도록 지원합니다. 이메일/비밀번호 계정, 전화인증, Google, Twitter, Facebook, GitHub 로그인 등을 지원하는 종합적인 ID 솔루션을 제공합니다.

- 저장소 : 

Firebase 저장소를 이용해 빠르고 쉽고 네트워크 품질에 관계 없이 사진, 동영상 등의 콘텐츠를 저장하고 제공할 수 있습니다. 

- 호스팅 : 

Firebase 호스팅은 웹 앱에 대한 빠른 정적 호스팅을 제공합니다. 개발자를 위한 웹 콘텐츠 호스팅 서비스이고 몇 줄의 코드만으로 웹 앱과 정적 콘텐츠를 글로벌 콘텐츠 전송 네트워크(CDN)에 빠르게 배포할 수 있습니다.

- Test Lab : 

우리는 여러 모바일 앱을 다양한 기기에서 사용합니다. 사용하는 환경도 모두 다르죠. 이러한 모든 다양한 상황을 테스트하기는 부담스러울 것입니다. 이에 Firebase Test Lab은 쉽게 다양한 기기에서 앱의 사용 편의성을 검증해줍니다. 클라우드에 호스팅되는 Test Lab에서 앱 테스트 용으로 준비된 다양한 실제 기기를 제공합니다. Test Lab에서 제공되는 Robo 테스트를 통해서 코드 없이 자동 테스트를 실행할 수 있고, 더 고급 테스팅을 원한다면 앱 상호작용을 스크립트로 작성하고 특정한 사용 사례를 시뮬레이션해 정상 작동 여부를 검증할 수 있습니다. 테스트 결과에는 기기별 상세 보고서가 포함되고 스크린샷과 로그, 테스트 중에 발생한 오류 기록 또한 첨부되어 확인할 수 있습니다.

- 성능 모니터링 : 

이 기능을 통해 사용자들이 앱을 통해 어떤 experience을 하는지에 대한 정보를 얻을 수 있습니다. 앱에 SDK를 통합함으로써 어떠한 코드 없이 Firebase Console의 dashboard가 사용자의 앱 performance를 수집합니다. 이러한 정보를 지역, 기기, 버젼 별로 분리해 모니터링 할 수 있습니다.

- 오류 보고 : 

Firebase 오류 보고는 사용자가 겪는 오류에 대한 정보를 수집하고 정보를 전송해 dashboard로 추적합니다. 개발자는 dashboard를 통해 앱의 전반적인 상태를 모니터링 할 수 있습니다. 또한 dashboard를 통해 주요한 오류가 무엇인지, 사용자가 겪을 수 있는 오류의 심각도에 따른 분류 등 효과적으로 오류를 확인할 수 있는 다양하고 효율적인 UI를 제공합니다.

- Cloud 함수 : 

다음으로 앱의 성장을 위한 기능들 입니다.

- Analytics : 

Firebase Analytics는 모바일 앱 개발자에게 필요한 모든 데이터를 한 곳에서 보기 쉽게 제공합니다. Firebase SDK를 설치하기만 하면 앱 통계 자료를 자동으로 제공합니다. 인구통계 정보, 사용자의 앱 방문 주기, 앱 사용시간, 앱에 지출한 금액 등을 알 수 있습니다. 또한 맞춤 사용자 속성을 설정해 사용자 그룹별 앱 활동 패턴을 분석할 수 있습니다. 그 외에도 잠재고객 분석과 Analytics 이외의 기능들을 통해 앱을 성장시킬 방법을 찾을 수 있습니다.

- 원격 구성(Remote Config) : 

Firebase 원격 구성은 클라우드를 통해 앱이 인식하는 변경사항을 몇 분 안에 배포할 수 있습니다. 기존의 방식으로 앱을 수정하려면 새 빌드를 구성하고 출시 과정을 다시 거쳐야 하지만, Firebase 원격 구성은 앱의 동작과 모양을 Firebase 콘솔의 dashboard를 통해서 변경 할 수 있습니다. 변경 후  앱 사용자가 앱을 실행하면 원격 구성 기능이 최신 값을 가져와서 앱을 변경합니다. 또한 세그먼트 기능으로 사용자 그룹을 분리해 특정 사용자 그룹에만 변경사항을 적용해 천천히 앱을 업데이트 해나갈 수 있습니다.

- 앱 색인 생성(App Indexing) :

App Indexing 은 Google 검색과 통합되어 사용자의 재사용을 유도합니다. 앱에 Index를 생석해주고 사용자가 앱에 포함된 콘텐츠를 검색하면 검색결과에 앱을 표시할 뿐 아니라, 자동완성 등을 통해 앱을 노출 시킵니다.

- 동적 링크(Dynamic Link) : 

모바일 사용이 늘어남에 따라 사람들은 어떤 기기나 상황에서도 링크를 사용해 원하는 웹페이지나 앱의 화면으로 이동하기를 원해 deep link라는 개념이 생겨났습니다. 웹 페이지 뿐만아니라 앱의 특정 페이지에서도 링크를 사용하게 되는 것이죠. 하지만 이러한 다양한 환경에 맞춰 deep link는 제대로 동작하기가 어려웠습니다. Firebase Dynamic Link는 완벽하게 작동하는 deep link입니다. iOS, Android, 데스크톱 브라우저에서 각기 다르게 동작하고 적절한 위치로 알아서 링크를 통해 이동하도록 만들었습니다. 앱의 설치 여부에 따라 다르게 작동하도록 동적 링크를 설정할 수도 있습니다. 

- 초대 : 
- 애드워즈 : 
- 클라우드 메시징 : 
- AdMob : 

### Firebase VS AWS VS Realm DB

이러한 기능들은 대부분 무료로 제공된다. 일부 기능은 사용량에 따라, 규모에 따라 가격이 책정된다. [Firebase 가격책정][1]

## 2.기능별 사용법<a name="m2" />

### Android
우선 Firebase의 기능들을 사용하기 위해서 앱에 Firebase를 연결해야합니다. 그러기 위해 Firebase SDK를 설치, Firebase 계정을 만들고 Firebase console에서 Project를 생성하고 앱을 추가해주면 됩니다. 아래 [튜토리얼](#m3)을 참고하세요

#### Realtime Database
-    Realtime Database 추가
-    Realtime Database 쓰기
-    Realtime Database 읽기
-    Realtime Database Rule 설정
-    데이터 구조화

#### Realtime Database 추가
Firebase 연결이 되었다면 Realtime Database를 앱에 추가해줍니다. app-level의 build.gradle 파일에 다음 dependency를 추가해줍니다.

```
    compile 'com.google.firebase:firebase-database:10.2.6'
```

이것으로 Firebase Database를 사용할 수 있게 되었습니다. 이제 Realtime database에 데이터를 쓰고, 읽는 방법을 알아보겠습니다.

#### Realtime Database 쓰기

Firebase Database를 액세스하기 위해 FirebaseDatabase 클래스의 인스턴스를 생성해줍니다. getInstance() 메소드로 인스턴스를 생성할수 있습니다. 

```
Firebase database = Fireabase.getInstance();
```

데이터베이스의 특정한 지점에서 데이터를 읽고 쓰기위해 DatabaseReference 클래스를 생성해 액세스 지점을 입력해줍니다. FirebaseDatabase에서 생성한 인스턴스로 getReference() 메소드를 이용해 root node, String 형식의 path, String 형식의 url 지점으로 입력해줄 수 있습니다.

```
DatabaseReference myRef = database.getReference("path");
```

이제 DatabaseReference의 메소드 setValue()로 데이터 저장 경로에 데이터를 입력할 수 있습니다.

```
myRef.setValue("Hi Firebase");
```

#### Realtime Database 읽기

데이터를 읽기 위한 인터페이스가 두가지 있습니다
1. ValueEventListener
이 인터페이스를 실행하는 클래스는 한 위치에 데이터 변화에 대한 이벤트를 받습니다. 

```
myRef.addValueEventListener(new ValueEventListener() {
    @Override
    public void onDataChange(DataSnapShot dataSnapshot){
        String value = dataSnapshot.getValue(String.class);
    }
}
```

2. ChildEventListener
이 인터페이스를 실행하는 클래스는 DatabaseReference에 지정한 child location에서 변화에 대한 이벤트들을 받기 위해 사용될 수 있습니다. 리스너에 대한 이벤트를 작성하고 참조 지점에 addChildEventListener(ChildEventListener) 를 통해 리스너를 추가합니다.

#### Realtime Database Rule 설정

#### 데이터 구조화



### Web
 
#### Realtime Database
-    선행 조건
-    데이터 읽기 및 쓰기
-    Realtime Database Rule 설정
-    데이터 구조화

#### 선행 조건
앱에 Firebase JavaScript 클라이언트 SDK를 추가하고 구성해야합니다. 그러기 위해 Firebase 프로젝트와 Firebase SDK 및 프로젝트에 대한 몇 가지 세부정보를 포함하는 짧은 초기화 코드가 필요합니다.
1. Firebase 프로젝트 생성

[Firebase 계정을 만들고 프로젝트를 생성]합니다. 프로젝트가 생성되고 클릭하면 다음 화면이 나옵니다. 여기서 '앱 추가'를 누르고 '웹'아이콘을 클릭해줍니다.

![Alt text][Web_add]

2. 초기화 코드

그러면 '웹 앱에 Firebase 추가'라는 창이 뜹니다. 여기서 코드 '복사'버튼을 누르고 HTML에 붙여 넣습니다.

![Alt text][Web_add_copy]

이 코드는 Firebase 인증, Cloud Storage, 실시간 데이터베이스를 사용하도록 Firebase 자바스크립트 SDK를 초기화 하는 정보를 포함합니다. 사용하고 싶은 기능에 따라 개별적으로 설치가 가능합니다.<참고:https://firebase.google.com/docs/web/setup>

이제 웹에서 Realtime Database를 사용할 준비는 끝났습니다.

#### 웹에서 데이터 읽기 및 쓰기

Firebase 데이터를 검색하려면 firebase.database.Reference 에 비동기 리스너를 연결합니다. 리스너는 데이터의 초기 상태가 확인될 때 한 번 호출된 후 데이터가 변경될 때마다 다시 호출됩니다.

#### code

+ firebae.database

firebase.database()는 특정 앱이나 기본 설정앱의 database에 액세스하기 위해 호출됩니다. 또한 다양한 Database 서비스와 관련있는 메서드들과 global constants를 액세스하는데도 사용됩니다.

```
//기본 설정으로 데이터베이스 서비스를 사용합니다
var defaultDatabase = firebase.database();

//설정한 앱으로 데이터베이스 서비스를 사용합니다
var otherDatabase = firebase.database(app);
```

+ firebase.databae.DataSnapshot

DataSnapshot 은 데이터베이스 location의 데이터를 포함합니다. 

데이터베이스로부터 데이터를 읽을 때, DataSnapshot으로 받습니다. DataSnapshot은 on()이나 once()를 사용한 이벤트 콜백에 전달됩니다. 그리고 val()메서드를 호출함으로써 JavaScript object로 snapshot의 콘텐츠를 추출할 수 있습니다. child snapshot을 반환하기위해서 child()메서드를 호출해 snapshot을 조회할 수 있습니다(여기셔 child는 데이터들의 아래 항목을 뜻하는 것으로 추정됩니다.)

Datasnapshot은 효율적으로 생성되고, 데이터베이스 location에 있는 data의 불변의 copy입니다. Reference의 set() 메서드를 호출함으로써 데이터를 바꿀 수 있습니다.

    +    key

Databse location에 가장 상단에 있는 token을 'key'라고 합니다. 예를 들면 "name"은 /user/name/' node에서 key입니다. 어떤 DataSnapshot에 키를 액세스하면 그 키를 생성한 위치의 키가 반환됩니다. 반면 데이터베이스의 root URL에 키를 액세스하는 것은 null 값을 반환합니다. 이해가 어려울 수 있음으로 Firebase reference에서 가져온 예를 보고 이해하시기 바랍니다.
```
// Assume we have the following data in the Database:
{
  "name": {
    "first": "Ada",
    "last": "Lovelace"
  }
}

var ref = firebase.database().ref("users/ada");
ref.once("value")
  .then(function(snapshot) {
    var key = snapshot.key; // "ada"
    var childKey = snapshot.child("name/last").key; // "last"
  });
var rootRef = firebase.database().ref();
rootRef.once("value")
  .then(function(snapshot) {
    var key = snapshot.key; // null
    var childKey = snapshot.child("users/ada").key; // "ada"
  });
```
    +    ref

DataSnapshot을 생성한 위치에 대한 Reference(참조)입니다.
<...>

+ firebase.database.Reference

Reference는 데이터베이스에서 특정한 location을 나타내고 데이터베이스 location에서 데이터를 읽거나 쓰기 위해 사용된다.

firebase.database().ref() 또는 fireabse.database().ref("child/path")를 호출함으로써 데이터베이스의 root 또는 child location을 reference(참조)할 수 있다.

set() 메소드로 쓰고, on() 메소드로 읽는다.  


## 3.튜토리얼<a name="m3" />
>Android, iOS, 웹에서 실행 가능한 채팅 앱을 만들어보면서 Firebase 사용방법을 익힌다.

### Android에서 시작하기

#### 선행 조건
-    Android 4.0(Ice Cream Sandwich) 이상 및 Google Play 서비스 10.2.6 이상을 실행하는 기기
-    Google 저장소의 Google Play 서비스 SDK (Android SDK Manager에서 다운로드 가능)
-    Android 스튜디오 최신 버전 (버전 1.5 이상)

#### Android Studio에 Firebase를 추가
> Firebase의 기능들을 사용하기 위한 준비를 합니다.

먼저 Firebase의 기능을 적용시킬 프로젝트를 준비합니다. 이 튜토리얼에서는 Google Firebase에서 제공하는 샘플 프로젝트를 사용할 것입니다. 다음 링크를 통해 프로젝트를 받을 수 있습니다.

[Git: https://github.com/udacity/and-nd-firebase][samplelink]

프로젝트가 준비되었으면 Firebase를 추가시킵니다. Firebase를 추가시키는 방법에는 두 가지가 있습니다
1.   Firebase Assistant 사용(Android Studio 버전 2.2이상)
2.   직접 추가
>이 튜토리얼은 직접 추가 방법으로 진행합니다.

1.Firebase Assistant를 사용하는 방법입니다.

Android Studio >상단 메뉴의 Tools > Firebase를 클릭합니다.

![Alt text][Ass_img]

Firebase의 여러 기능들 중 사용할 항목을 선택합니다.(예 : Realtime Database 선택 시 Save and retrieve data링크를 클릭합니다.)

![Alt text][Ass_img2]

Connect to Firebase를 클릭하면 Firebase에 연결하고 앱에 필요한 코드를 추가한다.

![Alt text][Ass_img3]

2.직접 추가

Firebase 사이트에서 '시작하기'나 ' 오른쪽 상단의 'GO TO CONSOLE'을 클릭합니다.

![Alt text][firebase_home]

프로젝트 추가하기를 눌러 프로젝트 이름과 국가/지역을 설정하고 프로젝트를 생성합니다. 안드로이드 프로젝트를 생성 중이기 때문에 가운데 Android버튼을 누르면 'Android 앱에 Firebase 추가'라는 창이 뜹니다. 여기선 Android 패키지 이름과 디버그 서명 인증서 SHA-1을 입력해야 합니다. [<SHA-1 찾기>][SHA-1]

![Alt text][firebase_pro]

마지막으로 안내에 따라 google-services.json 파일을 다운로드해 프로젝트의 모듈 폴더(app/)에 복사합니다.

#### Firebase SDK 추가
>Android Studio->Tools->SDK Manager 를 통해 Google play services 와 Google Repositiory를 업데이트 함으로써 오류를 방지할 수 있습니다.

Firebase 라이브러리를 기능을 사용하기 위해선 Firebase SDK를 추가해야합니다.

루트 수준 build.gradle 파일에 google-services플러그인을 포함시킵니다.

```
    buildscript {

        dependencies {

            classpath 'com.google.gms:google-services:3.1.0'

        }

    }
```

다음으로 모듈의 Gradle 파일 하단에 apply plugin 줄을 추가해 Gradle 플러그인을 사용 설정합니다.

```
    apply plugin: 'com.android.application'

    android {

    }
    dependencies {

      //compile 'com.google.firebase:firebase-core:10.2.6'

    }
    apply plugin: 'com.google.gms.google-services'
```

이제 아래의 라이브러리를 사용해 Firebase를 이용할 수 있습니다. 여러 라이브러리를 사용하게 된다면 동일한 버젼의 라이브러리를 사용해야 버젼 충돌로 일어나는 에러를 막을 수 있습니다. 현재 Firebase 사이트의 '문서'에서 기능마다 각각 다른 라이브러리 버젼을 사용해 가이드하고 있기 때문에 주의해야 합니다. 
![Alt text][gradle_library]

사용하고자 하는 라이브러리를 모듈 dependencies 안에 추가하고 Sync Now를 클릭합니다.

#### Android앱에서 Firebase 라이브러리 사용하기
>Firebase 라이브러리 메소드를 사용해 채팅앱을 완성시켜본다.

현재 아무 기능 구현도 되어있지 않은 채팅 앱의 모습입니다.

![Alt text][Chat_main]

---
[r1]:https://firebase.google.com/docs/
[r2]:https://www.udacity.com/course/firebase-in-a-weekend-by-google-android--ud0352
[1]:https://firebase.google.com/pricing/
[samplelink]:https://github.com/udacity/and-nd-firebase
[SHA-1]:https://developers.google.com/places/android-api/signup?hl=ko

[app_dev]:https://i.imgur.com/iQlOXm6.jpg
[img0]:http://i.imgur.com/Ks8Ugya.jpg
[img1]:http://i.imgur.com/cTsZBZd.jpg
[Ass_img]:http://i.imgur.com/1IHTdtK.jpg
[Ass_img2]:http://i.imgur.com/4CgCvLD.jpg
[Ass_img3]:http://i.imgur.com/Tcsh9lj.jpg
[firebase_home]:https://i.imgur.com/uoN5G4t.jpg
[firebase_pro]:https://i.imgur.com/RASh152.jpg
[gradle_plugin]:http://i.imgur.com/EY9wNoN.jpg
[gradle_app]:http://i.imgur.com/QHFtLVj.jpg
[gradle_library]:http://i.imgur.com/4xcBqg1.jpg
[gradle_addL]:http://i.imgur.com/3MYamKX.jpg
[Chat_main]:http://i.imgur.com/R5m5ZSa.jpg
[Web_add]:https://i.imgur.com/cMnmZkZ.jpg
[Web_add_copy]:https://i.imgur.com/xf2D16E.jpg
