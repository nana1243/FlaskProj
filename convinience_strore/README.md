1. app.py

   ```python
   @app.route('/cu_oneplusone/<int:page>', methods=['GET'])
   def cu_oneplusone_list(page):
       if db.get_oneplusone_list_totCnt == 0:
           message = "해당 상품이 없습니다."
       else:
           message = "총 " + str(db.get_oneplusone_list_totCnt('df_cu_oneplusone')) + "개 입니다."
         
       data = "cu_oneplusone"
       oneplusone_list= db.get_oneplusone_list('df_cu_oneplusone', page)
       num = db.get_oneplusone_list_totCnt('df_cu_oneplusone')
       pagenum= (num//20)+2
       return render_template('cu_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data , message=message, active = 'cu_oneplusone')
   
   
   ```

   



2. db.py

   ```python
   #### get_oneplusone_list는 이름만 oneplusone이고 행사명_list를 모두 뽑아낼 수 있는 역할의 함수입니다
   def get_oneplusone_list(df_name_oneplusone, page):
      
       conn = get_connection()
       
       cursor = conn.cursor()
       page=(int(page)-1)*20
       page = str(page)
       sql = 'SELECT * from ' + df_name_oneplusone + ' LIMIT '+ page + ',20';
       cursor.execute(sql)
       oneplusone_list= cursor.fetchall()
       
       conn.close()
       return oneplusone_list
    
    #### pagenum을 계산하기 필요한 함수
   def get_oneplusone_list_totCnt(df_name_oneplusone):
   
       conn = get_connection()
   
       cursor = conn.cursor()
       sql = 'SELECT count(*) FROM ' + df_name_oneplusone ;
       cursor.execute(sql)
       totCnt= cursor.fetchone()
       conn.close()
   
       return int(totCnt[0])
   ```

   

3. html 

   3-1. pagination

   ```jinja2
   <div class="text-center">
       <ul class="pagination">
           <li><a href="/{{data}}/{{curpage-1}}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>
        {% if curpage % 5 ==0 %}
        {%     set nstart= (curpage//5-1)*5+1 %}
        {%     set nend=(curpage//5-1)*5+6 %}
        {% else %}
        {%     set nstart = (curpage//5)*5+1 %}
        {%     set nend =  (curpage//5)*5+6 %}
        {% endif %}
   
   
       {% for i in range(nstart,nend) %}
   
                   {% if i == curpage %}
           <li class="page-item active"><a href="/{{data}}/{{i}}"><em>{{i}}</em></a></li>
                   {% else %}
           <li class="page-item"><a href="/{{data}}/{{i}}"><em>{{i}}</em></a></li>
                   {% endif %}
   
           {% endfor %}
           <li><a href="/{{data}}/{{curpage+1}}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>
       </ul>
   </div>
   
   ```

   

3-2 modal

```javascript
<script>
        function modal_view(data,img,title,price){
            var imgSrc = img;
            $("#myModal").on("show.bs.modal",function(event) {
                $(".modal-body #prodImg").attr("src", imgSrc)
                $(".modal-body #title").text(title);
                $(".modal-body #price").text(price);
            })
        }
    </script>
```

```jinja2
   {% if oneplusone_list[0][6] == None %}
        {% for item in oneplusone_list %}
        <div class="col-xs-6 col-sm-3">
            <br>
            <br>
            <a href="#" data-toggle="modal" data-target="#myModal">
                <img src="{{item[3]}}"  width="150px" height="150px"
                     onclick="modal_view('{{data}}','{{item[3]}}','{{ item[1] }}','{{ item[2] }}');">
            </a>
            <div><text align="center"><button type="button" class="btn">{{ item[4] }}</button></text></div>
            <div><p>{{ item[1] }}</p></div>
            <div><p>{{ item[2] }}</p></div>
        </div>
        {% endfor %}
    {% else %}
     {% for item in oneplusone_list %}
        <div class="col-xs-6 col-sm-3 col-lg-4">
            <div style= "width:150px; height:300px;  float:left; margin-right:30px;">
                <a href="#" data-toggle="modal" data-target="#myModal">
                    <img src="{{item[3]}}"  width="100px" height="100px"
                         onclick="modal_view('{{data}}','{{item[3]}}','{{ item[1] }}','{{ item[2] }}');">
                </a>
                <text align="center"><button type="button" class="btn">{{ item[4] }}</button></text>
                <p>{{ item[1] }}</p>
                <p>{{ item[2] }}</p>
            </div>

            <div style = "width:150px; height:300px; float:left;">

                <p><img src="{{item[6]}}" width="80px" height="80px"></p>
                <p>{{ item[5] }}</p>
            </div>
        </div>
        {% endfor %}
    {% endif %}
</div>
```



3-3 product 뿌리기

```jinja2
  {% if oneplusone_list[0][6] == None %}
        {% for item in oneplusone_list %}
        <div class="col-xs-6 col-sm-3">
            <br>
            <br>
            <a href="#" data-toggle="modal" data-target="#myModal">
                <img src="{{item[3]}}"  width="150px" height="150px"
                     onclick="modal_view('{{data}}','{{item[3]}}','{{ item[1] }}','{{ item[2] }}');">
            </a>
            <div><text align="center"><button type="button" class="btn">{{ item[4] }}</button></text></div>
            <div><p>{{ item[1] }}</p></div>
            <div><p>{{ item[2] }}</p></div>
        </div>
        {% endfor %}
    {% else %}
     {% for item in oneplusone_list %}
        <div class="col-xs-6 col-sm-3 col-lg-4">
            <div style= "width:150px; height:300px;  float:left; margin-right:30px;">
                <a href="#" data-toggle="modal" data-target="#myModal">
                    <img src="{{item[3]}}"  width="100px" height="100px"
                         onclick="modal_view('{{data}}','{{item[3]}}','{{ item[1] }}','{{ item[2] }}');">
                </a>
                <text align="center"><button type="button" class="btn">{{ item[4] }}</button></text>
                <p>{{ item[1] }}</p>
                <p>{{ item[2] }}</p>
            </div>

            <div style = "width:150px; height:300px; float:left;">

                <p><img src="{{item[6]}}" width="80px" height="80px"></p>
                <p>{{ item[5] }}</p>
            </div>
        </div>
        {% endfor %}
    {% endif %}
</div>
```



4. 웹크롤링 

   4-1 크롤링

   ````python
   n=0
   for i in range(0,6):
       WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.inner.wrap.service1 > div.event_plus_list > div > a.pr_more'))).click()
       time.sleep(5)
       n+=1
   
   
   soup = BeautifulSoup(browser.page_source, "html.parser")
   pro_list = soup.select('div.inner.wrap.service1 > div.event_plus_list > ul>li ')
   
   prod_list=[]
   price_list=[]
   
   for v in pro_list:
       prodname=v.select('a>img')[0]["alt"]
       prod_list.append(prodname)
       price=v.select('p>strong')[0].text.strip()
       price_list.append(price)
       
   ````

   4-2 mysql연결

   ```python
   # conda install pymysql -c conda-forge
   
   from sqlalchemy import create_engine
   import pymysql
   
   # mysql 연결정보 => host 127.0.0.1 / 사용자 root  / 암호 1234  / 데이터베이스명 flask_db
   engine = create_engine('mysql+pymysql://root:1243@127.0.0.1/conv_db?charset=utf8', convert_unicode=True, echo=True)
   conn = engine.connect()
   
   df_ministop_oneplusone.to_sql(name='df_ministop_oneplusone', con=engine, if_exists='replace', index=True)
   ```

   4-3 이미지저장

   ```python
   list_raw=[]
   for v in pro_list:
       list_raw.append(v.select('a> img')[0]["src"])
   
   list_raw
   
   for i in range(0,len(list1)) :
       fullFileName = os.path.join(savePath, savePath + str(i) + '.jpg')
       req.urlretrieve('https://www.ministop.co.kr/MiniStopHomePage/page'+ list1[i], fullFileName)
   ```

   