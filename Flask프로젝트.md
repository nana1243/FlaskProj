## 1. 기획의도

> 프로젝트 주제는 각 편의점 행사 상품을 하나의 웹상으로 띄우는 것이었습니다.
>
>  이는 1인 가구 및 2030대의 지출 중 편의점 소비가 점점 늘어나는 트렌드에 맞춰 주제가 정해졌고, 저희가 만든 웹을 통해 소비자들이 빠르고, 똑똑하게 소비할 수 있도록 편의를 제공할 수 있다는 판단이 되어 시작하게 되었습니다.



## 2. 화면구성

| app.py                         | URL                                        | TEMPLATES             |
| ------------------------------ | ------------------------------------------ | --------------------- |
| index                          | localhost                                  | index.html            |
| search(메인창에서검색)         | localhost/search_list                      | alllist.html          |
| search(각 편의점항목에서 검색) | localhost/편의점이름_list                  | alllist.html          |
| 편의점이름_행사이름 _list      | localhost/편의점이름__행사이름/<int :page> | 편의점이름_list.html  |
| board_list                     | locahost/borad/<int :page>                 | board.html            |
| add_board_pro                  | localhost/add_board                        | add_board.html        |
| detailed                       | localhost/detail                           | board_content.html    |
| map                            | localhost/map/store명                      | location_service.html |



## 3. DB-erd

![erd](https://user-images.githubusercontent.com/52269210/72675186-f152f180-3ac3-11ea-9dbb-46dbc9bbc107.png)





## 4. 사용된기술

| Front      | Back                     |
| ---------- | ------------------------ |
| JavaScript | Flask Framework          |
| JQuery     | aws Mysql                |
| JINJA2     | PyCharm, Jupyternotebook |

| 배포    | 협업 툴 |
| ------- | ------- |
| AWS EC2 | github  |

## 5. 맡은 역할

1. 상품 뿌리기

![image](https://user-images.githubusercontent.com/52269210/72674567-bea4fb00-3abb-11ea-8b7c-ad008008a1d3.png)

2. 팝업창(모달)

<img src="https://user-images.githubusercontent.com/52269210/72674594-de3c2380-3abb-11ea-96bb-36aaa83f6083.png" alt="image" style="zoom:150%;" />

3.  pagination

   ![image](https://user-images.githubusercontent.com/52269210/72674610-ff9d0f80-3abb-11ea-9eec-993236ed5ebf.png)



