# Restful Web Service 개발
> ## 기본 개발 버전
> - Java JDK 1.8.x(매우 중요함, 1.9는 activation framework 문제가 있음),  Tomcat9
> - Servlet 3.0, Apache Jersey2 

#### 프로젝트 생성시 기본 정보
```
package: com.dinfree.demo.ws
class: DemoService, DemoData
groupid: com.dinfree
artifact: demo
project name: wsdemo
```

## IntelliJ를 사용하는 경우
> Project Location: Project -> WSIntelliJ -> wsdemo
> 개발PC를 변경할 경우 Tomcat 디렉토리가 다를수 있으므로 위치변경/동일체계 유지 필요.

### Maven Project 로 진행
1. New -> Maven Project -> maven-archetype-webapp 선택 -> 기본정보입력 -> 프로젝트 생성.
2. pom.xml 에 다음 추가
```xml
<dependencies>
		<dependency>
			<groupId>javax.servlet</groupId>
			<artifactId>javax.servlet-api</artifactId>
			<version>3.1.0</version>
		</dependency>			
		<dependency>
			<groupId>org.glassfish.jersey.containers</groupId>
			<artifactId>jersey-container-servlet-core</artifactId>
			<version>2.25.1</version>
		</dependency>
		<dependency>
			<groupId>org.glassfish.jersey.containers</groupId>
			<artifactId>jersey-container-servlet</artifactId>
			<version>2.25.1</version>
		</dependency>
		<dependency>
			<groupId>org.glassfish.jersey.media</groupId>
			<artifactId>jersey-media-json-jackson</artifactId>
			<version>2.25.1</version>
		</dependency>
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-api</artifactId>
			<version>1.7.25</version>
		</dependency>
	</dependencies>
```

3. src -> main ->  java 폴더를 추가하고 오른쪽 마우스 -> Mark Directory as -> Source root 폴더로 지정함. 이후 패키지와 클래스 생성
4. web.xml 추가는 필요없고 다음과 같이 ResourceConfig 설정 클래스 생성
```java
package com.dinfree.demo.ws.ResourceConfig;
import org.glassfish.jersey.server.ResourceConfig;
import javax.ws.rs.ApplicationPath;

@ApplicationPath("/rest")
public class ApplicationConfig extends ResourceConfig {
	public ApplicationConfig() {
		packages("com.dinfree.demo.ws");
	}
}
```
5. DemoService.java
```java
package com.dinfree.demo.ws;

import javax.ws.rs.GET;
import javax.ws.rs.Produces;
import javax.ws.rs.Path;
import javax.ws.rs.core.MediaType;
import java.util.ArrayList;

@Path("/member")
public class DemoService {
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String getHello() {
        return "Welcome to Member WebService";
    }

    @GET
    @Produces({MediaType.APPLICATION_JSON , MediaType.APPLICATION_XML})
    public Member getMember() {
        Member m = new Member();
        m.setName("홍길동");
        m.setAge(50);
        m.setTel("010-123-1234");
        return m;
    }

    @GET
    @Path("memberlist")  // /rest/member/memberlist
    @Produces({MediaType.APPLICATION_JSON , MediaType.APPLICATION_XML})
    public ArrayList<Member> getMemberList() {
        ArrayList<Member> list = new ArrayList<Member>();

        Member m = new Member();
        m.setName("홍길동");
        m.setAge(50);
        m.setTel("010-123-1234");
        list.add(m);

        m = new Member();
        m.setName("김사랑");
        m.setAge(30);
        m.setTel("010-123-1234");
        list.add(m);

        m = new Member();
        m.setName("아무개");
        m.setAge(35);
        m.setTel("010-123-1234");
        list.add(m);
        return list;
    }
}
```
6. Member.java
```java
package com.dinfree.demo.ws;

import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
public class Member {
    private String name;
    private String tel;
    private int age;
    ... gettter/setter...
}
```
7. 실행
	* Edit Configuration 에서 웹 실행 설정 해주어야 함. Name -> wsdemo run
	* `+ -> Tomcat Server -> Local`
	* Application server 디렉토리 설정
	* `Deployment -> + -> Artifact -> wsdemo:war exploded`
8. 테스트
	* Tools -> Test RESTful Web Service, 테스트 툴에서 한글결과 깨짐
	* http://localhost:8080/rest/member, http://localhost:8080/rest/member/list
		* `Accept */* -> Welcome to Member WebService`
		* `Accept application/json ->` 
		* `Accept application/xml ->`

### Spring-boot 로 진행 절차
> - 최신 버전과 버전 종속 관계를 유지하는 것이 중요함.
> - gradle  사용을 위해서는 IntelliJ 기본 설정에서 자체 gradle plug-in support 추가를 해주어야 한다.

1. 프로젝트 생성시 Spring Initializer 로 필요항목 설정
2. Gradle Project로 설정
3. Spring Boot 2.0 기준 Web, Jersey(JAX-RS)설정
4. WsdemoApplication.java 선택후 오른쪽 마우스  run WsdemoApplication  해서 실행하고 나면 상단에 실행설정 생김.
5. Restful WebService 클래스 등록을 위해 다음과 같이 설정 클래스 추가
```java
public class JerseyConfig extends ResourceConfig {
    public JerseyConfig() {
    	// Eclipse 에서만 필요한 상황임.
    	register(JacksonXMLProvider.class);
        //register(DemoService.class);
        packages("com.dinfree.demo.ws");
    }
}
```	

	7. `Tools->Test Restful Web Service` 로 테스트 (한글 출력에 문제가 있음)
	8. 독립실행을 위한 Export
		* jar export 설정
```
메뉴 > File > Project Structure > Artifacts 
click the plus icon 
and create new artifact choose --> jar --> From modules with dependencies.
메뉴 > Build > Build artifacts --> choose your artifact.
Artifacts에서 지정했던 위치에 가보면 jar파일이 우리를 기다리고 있음.

실행은 해당 디렉토리에서 java -jar ***.jar
``` 


## 참고: Eclipse Oxygen을 사용하는 경우
> 여러 문제가 많음. Gradle 은 잘 안되고 maven 은 되기는 하는데 동작에 일관성이 없음.
> java9 에서 activation framework 이 deprecated 되어 일부 라이브러리들이 문제가 됨.
> 문제가 있을 경우  `—add-modules java.activation` 을 VM argument로 실행환경에 추가.

### Maven 프로젝트로 진행 -> IntelliJ 와 동일함

### Spring-boot 로 진행
1. 프로젝트 생성시 https://start.spring.io 에서 maven project 로 기본 프로젝트.zip 생성
2. `zip 압축해제 -> import from existing maven project` 로 임포트
3. jaxb-api dependency 를 pom.xml  에 반드시 추가
```
<dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.2.12</version>
</dependency>
```
4. xml 데이터 처리를 위해 pom.xml 에 다음과 같이 xml provider 등록 -> 
```
<dependency>
    <groupId>com.fasterxml.jackson.jaxrs</groupId>
    <artifactId>jackson-jaxrs-xml-provider</artifactId>
</dependency>
```
### 현재까지 문제점: 2017.11.18
* `application/xml` 요청시 데이터가 나오지 않음.

### XML 데이터 produce 문제
* Data 클래스에서 @XmlRootElement(javax.xml.bind.annotation.XmlRootElement) 를 명시하지 않아도 json request 는 모두 잘 처리가 됨.
* IntelliJ 는 @XmlRootElement 를  기본 spring-boot나 maven 라이브러리 추가로 별도 설정없이 사용할 수 있음.
* Eclipse 에서는 jaxb-api 추가로 사용할 수 있는데 이 경우 xml 데이터 produce 가 안됨.
* @XmlRootElement 를 지우고 jackson-jaxrs-xml-provider를 추가한뒤 JerseyConfig.java 에 아래와 같이 등록해서 사용이 가능함.
```
@Component
public class JerseyConfig extends ResourceConfig {
    public JerseyConfig() {
    	// Eclipse 에서만 필요한 상황임.
    	register(JacksonXMLProvider.class);
      //register(DemoService.class);
      packages("com.dinfree.demo.ws");
    }
}
```

* 결론
	* 결론적으로 XML 처리만 아니면 @XmlRootElement 는 필요 없고 JacksonXMLProvider 도 필요 없음.
	* @XmlRootElement 있는 코드를 사용하고 IntelliJ 는 json/xml 다 되고 eclipse 는 json 만 되는 상태로 사용하면서 추후 버전 변환에 따른 모니터링 필요.
---


#dev
