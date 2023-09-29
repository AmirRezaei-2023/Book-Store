import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import random
import plotly.express as px

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='13771377Mnn@',
    database='book_store'
)

cursor = conn.cursor()
#color
color =[
            "#4477dd",
            "#00a67e",
            "#8ffe09",
            "#c90b42",
            "#ffaa0088"
            ]


st.title('BOOK STORE')

tab1, tab2 ,tab3 = st.tabs(["📈 Analytical Chart", "🗃 filter book","📈 Analytical Chart"])

with tab1:
    col1, col2 = st.columns([1, 3])

    with col1:
        type=st.radio(
            "Analytical charts",
            key="Analytical charts",
            options=["count tag", "count publisher", "count year","count writer","count translator"],
        )
    with col2:
        # First part: Analytical charts
        if type == "count tag":
            # plot question 1
            st.header('count tag book')
            number = st.number_input('Choose number', step=1,value=20,min_value=5)
            cursor.execute(f"select name,count(*) as count_book from group_category \
                        inner join category c on group_category.category_id = c.id\
                                group by name order by count_book desc limit {number}")
            result = cursor.fetchall()
            df = pd.DataFrame(
                    result,
                        columns=("name","count_book"))
            ###
            st.title('bar chart')
            chart = alt.Chart(df).mark_bar().encode(
                x=alt.X('name', title="دسته بندی ها"),
                y=alt.Y('count_book', title="تعداد کتاب ها"),
                color=alt.ColorValue(random.choice(color))
            ).properties(
                width=500,
                height=300
            )

            st.altair_chart(chart, use_container_width=True)
            ###
            st.title('Pie chart')
            fig = px.pie(df, values='count_book', names='name')

            st.plotly_chart(fig, use_container_width=True)
        elif type == "count publisher":
            # plot question 2
            st.header('count publisher book')
            cursor.execute(f"select name,count(*) as count_book from book_publisher \
                           inner join publisher p on book_publisher.publisher_id = p.id \
                            group by publisher_id order by count_book desc limit 10")
            result = cursor.fetchall()
            df = pd.DataFrame(
                    result,
                        columns=("name","count_book"))
            ###
            st.title('bar chart')
            chart = alt.Chart(df).mark_bar().encode(
                x=alt.X('name', title=" انتشارات "),
                y=alt.Y('count_book', title="تعداد کتاب ها"),
                color=alt.ColorValue(random.choice(color))
            ).properties(
                width=500,
                height=300
            )

            st.altair_chart(chart, use_container_width=True)
            ###
            st.title('Pie chart')
            fig = px.pie(df, values='count_book', names='name')

            st.plotly_chart(fig, use_container_width=True)    
        elif type == "count year":
            # plot question 3
            st.header('count year book')
            
            release_year = st.selectbox(
                'release year',
                ('miladi', 'shamsi'))

            st.write('You selected:', release_year)
            if release_year=="miladi":
                release_year ="release_year_mi"
                start_year = 1980
                end_year = 2030
                end_count = 300
            else:
                release_year ="release_year_sh"
                start_year = 1370
                end_year = 1405
                end_count = 1000

            number = st.number_input('Choose number', step=1,value=10,min_value=5,max_value =30)
            cursor.execute(f"select {release_year},count(*) as count_book from book group by \
                            {release_year} order by count_book desc limit {number}")
            result = cursor.fetchall()
            df = pd.DataFrame(
                    result,
                        columns=(f"{release_year}","count_book"))
            df.dropna(subset=[f"{release_year}"],inplace=True)
            ###
            st.title('bar chart')
            chart = alt.Chart(df).mark_bar().encode(
                x=alt.X(f'{release_year}', title="سال انتشار",
                        scale=alt.Scale(domain=(start_year, end_year)),
                        axis=alt.Axis(tickCount=4)),
                y=alt.Y('count_book', title="تعداد کتاب ها",
                        scale=alt.Scale(domain=(0, end_count))),
                color=alt.ColorValue(random.choice(color))
            ).properties(
                width=500,
                height=300
            )

            st.altair_chart(chart, use_container_width=True)
            ###
            st.title('Pie chart')
            fig = px.pie(df, values='count_book', names=f'{release_year}')

            st.plotly_chart(fig, use_container_width=True)
        elif type == "count writer":
            # plot question 4
            st.header('count writer book')
            cursor.execute(f"select name , count(*) as book_code from crew \
                           inner join person p on crew.person_counter = p.counter\
                               where role ='writer'group by name \
                               order by book_code desc limit 10")
            result = cursor.fetchall()
            df = pd.DataFrame(
                    result,
                        columns=("name","count_book"))
            ###
            st.title('bar chart')
            chart = alt.Chart(df).mark_bar().encode(
                x=alt.X('name', title=" نویسندگان "),
                y=alt.Y('count_book', title="تعداد کتاب ها"),
                color=alt.ColorValue(random.choice(color))
            ).properties(
                width=500,
                height=300
            )

            st.altair_chart(chart, use_container_width=True)
            ###
            st.title('Pie chart')
            fig = px.pie(df, values='count_book', names='name')

            st.plotly_chart(fig, use_container_width=True) 
        elif type == "count translator":
            # plot question 5
            st.header('count translator book')
            cursor.execute(f"select name , count(*) as book_code from crew \
                           inner join person p on crew.person_counter = p.counter\
                               where role ='translator'group by name \
                               order by book_code desc limit 10")
            result = cursor.fetchall()
            df = pd.DataFrame(
                    result,
                        columns=("name","count_book"))
            ###
            st.title('bar chart')
            chart = alt.Chart(df).mark_bar().encode(
                x=alt.X('name', title=" مترجمان "),
                y=alt.Y('count_book', title="تعداد کتاب ها"),
                color=alt.ColorValue(random.choice(color))
            ).properties(
                width=500,
                height=300
            )

            st.altair_chart(chart, use_container_width=True)
            ###
            st.title('Pie chart')
            fig = px.pie(df, values='count_book', names='name')

            st.plotly_chart(fig, use_container_width=True) 
with tab2:
    text_search = st.text_input('text to search')
    fields_book = st.multiselect(
    'search fields',
    ['عنوان فارسی', 'عنوان انگلیسی','سال انتشار میلادی','سال انتشار شمسی', 'نویسنده', 'مترجم','ناشر','نوع جلد','قطع'],
    ['عنوان فارسی'])
    change_persion_to_English ={'title_persian':'عنوان فارسی','title_english': 'عنوان انگلیسی',
                                'release_year_mi':'سال انتشار میلادی','release_year_sh':'سال انتشار شمسی',
                                'person_writer':'نویسنده','person_translator': 'مترجم',
                                'p.name':'ناشر','cover':'نوع جلد',
                                'ghate':'قطع'}
    if fields_book ==[]:
        list_search ={'title_persian':'عنوان فارسی','title_english': 'عنوان انگلیسی',
                            'release_year_mi':'سال انتشار میلادی','release_year_sh':'سال انتشار شمسی',
                            'person_writer':'نویسنده','person_translator': 'مترجم',
                            'p.name':'ناشر','cover':'نوع جلد',
                            'ghate':'قطع'}
    else:
        list_search ={}
        for field in fields_book:
            for k, v in change_persion_to_English.items():
                if field == v:
                    list_search[k] = field
    # search all
    base_query ="SELECT code,title_persian,title_english,release_year_sh,release_year_mi,\
            cover,ghate,p.name as publisher,p2.name as person,role\
            FROM book inner join book_publisher bp on book.code = bp.book_code\
            inner join publisher p on bp.publisher_id = p.id\
            inner join  crew c on book.code = c.book_code\
            inner join  person p2 on c.person_counter = p2.counter WHERE "
    i = 0
    where_query = " "
    for k, v in list_search.items():
        i= i + 1
        if k == "person_translator":
            where_query = " " + where_query +f" p2.name LIKE '%{text_search}%' "+" "+ "and"+" "                
            where_query = " " + where_query +f"role = 'translator'" +" "               
        elif k == "person_writer":
            where_query = " " + where_query +f" p2.name LIKE '%{text_search}%' "+" "+ "and"+" "                
            where_query = " " + where_query +f"role = 'writer'" +" "
        else:
            where_query = " " + where_query +f" {k} LIKE '%{text_search}%' "                
        if len(list_search) != i: 
            where_query = where_query +" "+ "or"+" "
    query = base_query +where_query
    st.header('filter book')
    cursor.execute(query)
    result = cursor.fetchall()
    df = pd.DataFrame(
            result,
                columns=("code","title_persian","title_english",
                        "release_year_sh","release_year_mi",
                        "cover","ghate","publisher",
                        "person","role"))
    st.table(df)
            

