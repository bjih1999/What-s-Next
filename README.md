# What-s-Next
![issue badge](https://img.shields.io/badge/django-3.2-green)
![issue badge](https://img.shields.io/badge/jquery-3.5.0-blueviolet)
![issue badge](https://img.shields.io/badge/AWS-personalize-orange)
![issue badge](https://img.shields.io/badge/SQLite-3.8.10-blue)
## About Project
<img src="https://user-images.githubusercontent.com/42201356/103290644-62698b80-4a2d-11eb-8dae-e61b1938a5e7.png" alt="로고" width="50%" height="50%">  

&nbsp; What-s-Next는 AWS Personalize를 이용해 사용자 개인의 선호도를 분석하고 OTT 서비스(Netflix, Watcha, Tving, Wavve)에서 제공하는 프로그램들에 적용하여 좋아할만한 프로그램들을 추천하는 WEB 어플리케이션입니다.

---

### 개요

&nbsp; OTT 서비스란 OTT(Over The Top Service)는 인터넷을 통해 방송 프로그램, 영화, 교육 등 각종 미디어 콘텐츠를 제공하는 서비스를 말한다. 대표적인 서비스로는 Youtube, Neflix, Wavve등이 있다. 국내 외 다양한 OTT 서비스가 제공되고, TV방송 콘텐츠 뿐만 아니라 자체 동영상 콘텐츠가 풍성해지고 스마트폰, 스마트패드 등 개인용 미디어가 보편화되면서 OTT 시장이 활성화되고 있다. 온라인 동영상 제공 서비스(OTT) 이용자는 2018년 기준 42.7%로, 2017년에 비해 6.6%p가 증가하면서 온라인 동영상 전성시대로 진입했다고 볼 수 있다. (2016년 35%, 2017년 36.1%)  

&nbsp; 그러나 많은 유료 OTT 플랫폼의 시장이 넓어지면서, 이용자들은 OTT 플랫폼의 콘텐츠 선택 문제에 직면했다. 여러 방송사의 콘텐츠를 보려면, 다양한 OTT 서비스에 접속해야 하는 불편함이 있다. 또한, 장르 구분이 쉬운 영화에 대한 추천 서비스는 흔하지만, 장르 구분이 비교적 어려운 드라마와 예능은 인기순으로 추천해줄 뿐, 개개인에 맞춰 추천해주는 서비스는 드물다. 	이에 Neflix, Tving, Wavve, Watcha 네 플랫폼의 예능과 드라마 콘텐츠들을 통합하고, 개인의 취향에 맞는 콘텐츠를 추천하는데 연구 목적이 있다.  
&nbsp; 이 연구는 Amazon Personalize를 이용해 개인화를 적용하고 있으며, Python의 Django를 통해 웹 사이트에 이 결과를 반환한다.  

---

### 프로젝트 구조

#### 프로젝트 구조도  

<img src="https://user-images.githubusercontent.com/42201356/103270860-47325800-49fc-11eb-96dc-1e45e14c6b80.png" weight="110%" height="110%">  

#### 구조도 주요 모듈 세부 설명  
* S3  
  - 기초 DB 저장 및 관리  
  
* Personallize  
  - 스키마 구조를 지정받아 S3로부터 data import를 진행  
  - 지정한 recipe로 위 ata를 학습하여 campaign 생성  
  
* Web
  - 회원가입 기능 구현
  - 로그인한 사용자로 프로그램 검색 시 리뷰작성 가능
  - 로그인한 사용자의 취향에 맞는 추천 목록 출력
  
  
---  
  
### 화면 예시
  #### 리뷰 작성
  <img src="https://user-images.githubusercontent.com/42201356/103273216-148b5e00-4a02-11eb-9083-a28b40133f0c.png" alt="리뷰 작성 예시">  
  
  #### 특정 유저의 추천 목록 출력 결과
  <img src="https://user-images.githubusercontent.com/42201356/103273297-4d2b3780-4a02-11eb-9787-3947fb232dff.png" alt="추천 목록 출력 결과">  
  
  
---
  
### 참고 영상
  #### 발표 영상  
  
  ⬇이미지 클릭  
  
  <a href="https://youtu.be/KJYTfj8WEnw"><img src="https://user-images.githubusercontent.com/42201356/103292501-3f40db00-4a31-11eb-9177-683fcc0e2990.png" width="50%" height="50%" alt="발표 영상"></a>  
  
  #### 회원가입 시연 영상  
  
  ⬇이미지 클릭  
  
  <a href="https://youtu.be/msYq_ASdbFE"><img src="https://user-images.githubusercontent.com/42201356/103294207-baf05700-4a34-11eb-9291-a3f63c816ee1.png" width="50%" height="50%" alt="발표 영상"></a>  
  
  #### 로그인 및 리뷰 작성 시연 영상  
  
  ⬇이미지 클릭  
  
  <a href="https://youtu.be/1QRALJX8lxY"><img src="https://user-images.githubusercontent.com/42201356/103294207-baf05700-4a34-11eb-9291-a3f63c816ee1.png" width="50%" height="50%" alt="발표 영상"></a>  
  
  #### 컨텐츠 추천 기능 시연 영상  
  
  ⬇이미지 클릭  
  
  <a href="https://youtu.be/KzJmcMfcFRk"><img src="https://user-images.githubusercontent.com/42201356/103294207-baf05700-4a34-11eb-9291-a3f63c816ee1.png" width="50%" height="50%" alt="발표 영상"></a>  
  
  ---
  
  ## Made By
  * [숭실대학교 소프트웨어학부 17 김은혜]
  * [숭실대학교 소프트웨어학부 18 노진주]
  * [숭실대학교 소프트웨어학부 18 변지현]
  * [숭실대학교 소프트웨어학부 18 이수민]
