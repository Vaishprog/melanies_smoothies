# Import python packages
import streamlit as st
import requests

#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
# Write directly to the app
st.title("Customize Your Smoothie!:cup_with_straw:")
st.write(
    """
    Choose the fruits you want in your custom smoothie.
    """
)

title=st.text_input('Name on Smothie')
st.write('the current movie title is',title)

#session = get_active_session()
cnx=st.connection("snowflake")
session=cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('fruit_name'),col('SEARCH_ON'))
st.dataframe(data=my_dataframe, use_container_width=True)
pd_df=my_dataframe.to_pandas()
ingredients_list=st.multiselect('Choose up to 5 ingredients:',my_dataframe, max_selections=5 )

if ingredients_list:
    st.write(ingredients_list)
    st.text(ingredients_list)
    ingredients_string=''
    for  fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
        search_on=pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
        st.write('The search value for ', fruit_chosen ,' is ', search_on, '.')
        st.subheader(fruit_chosen+ 'Nutrition information')
        fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+ fruit_chosen)

    
    st.write(ingredients_string)
    my_insert_stmt = """ insert into smoothies.public.orders(name_on_order,ingredients)
            values ('"""+title+"""','"""+ingredients_string+"""')"""
    st.write(my_insert_stmt)
    time_to_insert=st.button('Submit Order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")

        '''

 streamlit as st
import requests
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
# Write directly to the app
st.title("Customize Your Smoothie!:cup_with_straw:")
st.write(
    """
    Choose the fruits you want in your custom smoothie.
    """
)

title=st.text_input('Name on Smothie')
st.write('the current movie title is',title)
#st.text(fruityvice_response.json())
cnx=st.connection("snowflake")
session=cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'),col('SEARCH_ON'))
st.dataframe(data=my_dataframe, use_container_width=True)
pd_df=my_dataframe.to_pandas()
#st.dataframe(pd_df)
#st.stop()
     
ingredients_list=st.multiselect('Choose up to 5 ingredients:',my_dataframe, max_selections=5)
if ingredients_list:
    ingredients_string=''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
        search_on=pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
        st.write('The search value for ', fruit_chosen,' is ', search_on, '.')
        st.subheader(fruit_chosen + 'Nutrition Information')
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_chosen)
        fv_df=st.dataframe(data=fruityvice_response.json(),use_container_width=True)
        my_insert_stmt = """ insert into smoothies.public.orders(name_on_order,ingredients)
            values ('"""+title+"""','"""+ingredients_string+"""')"""
        st.write(my_insert_stmt)
        time_to_insert=st.button('Submit Order')
        if time_to_insert:
            session.sql(my_insert_stmt).collect()
            st.success('Your Smoothie is ordered!', icon="✅")

title=st.text_input('Name on Smothie')
st.write('the current movie title is',title)

#session = get_active_session()
cnx=st.connection("snowflake")
session=cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('fruit_name'))
st.dataframe(data=my_dataframe, use_container_width=True)

pd_df=my_dataframe.to_pandas()
#st.dataframe(pd_df)
#st.stop()
ingredients_list=st.multiselect('Choose up to 5 ingredients:',my_dataframe, max_selections=5 )

if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)
    ingredients_string=''
    for  x in ingredients_list:
        ingredients_string += x + ' '
        search_on=pd_df.loc[pd_df['FRUIT_NAME'] == x, 'SEARCH_ON'].iloc[0]
        st.write('The search value for ', x,' is ', search_on, '.')
        st.subheader(x+ 'Nutrition information')
        fruityvice_response=request.get("https://fruityvice.com/api/fruit/"+ x)
        my_insert_stmt = """ insert into smoothies.public.orders(name_on_order,ingredients) values ('"""+title+"""','"""+ingredients_string+"""')"""
        st.write(my_insert_stmt)
        time_to_insert=st.button('Submit Order')
        if time_to_insert:
            session.sql(my_insert_stmt).collect()
            st.success('Your Smoothie is ordered!', icon="✅")'''

