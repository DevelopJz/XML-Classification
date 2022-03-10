# Python3 연습 과제
## 2-Python3 XML Classification

### 사용 언어
**Python 3.7.6**  
**Anaconda 4.8.2**

### 사용 환경
**Windows**

### 라이브러리
os  
sys  
subprocess  
time  
datetime  
lxml  
shutill  
xml  

### 라이브러리 설치
```python

python -m pip install 라이브러리명

```

### 코드 설명
**xml_search.py**  

XML 파일에 접근하는 XML 라이브러리 사용, 상위 태그부터 각 태그별 저장된 값들을 분류하여 리스트로 저장  
태그 내 값들을 리스트로 출력 후 값 선택하여 검색  

**xml_mode.py**  

XML 파일에 접근, 파일에 데이터 모드 별로 추가 / 수정 / 삭제 기능 구현  
실행 후 파일명 다르게 저장 (ex) xmlfile_Add.xml / xmlfile_Fix.xml / xmlfile_Delete.xml  

**xml_database.py**  

XML 파일에 접근, 파일 읽고 나라->회사->가수->연도 순으로 폴더를 만들어 데이터 분류 저장
