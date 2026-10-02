


import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(r'Student.csv')


cols = df.select_dtypes('str').columns.to_list()
cat_col_df = {}
for col in cols:
    cat_col_df[f'{col}'] = df.groupby(col)['exam_score'].median()

num_cols = df.select_dtypes('number').columns.to_list()

for x in ['online_learning_hours', 'daily_screen_time', 'physical_activity_hours', 'online_course_hours', 'questions_attempted',  'questions_correct', 'age', 'previous_exam_score']:

    num_cols.remove(x)

df_corr = df[num_cols].corr(numeric_only = True).round(2)
df_corr_exam = df_corr.loc['exam_score',:]








st.title('Student Exam Performance Analysis')


st.dataframe(df)

st.write('')

st.write('## The following charts show the effect of columns on the final exam score')


st.write('')


st.subheader('1. Catgorical Columns: Comparing Between each unique value in the Column and its average of final exam score.')

st.plotly_chart(px.bar(data_frame= cat_col_df['school_type']))

st.write('#### Private Schools has the highest average final exam score.')

st.plotly_chart(px.bar(data_frame= cat_col_df['family_income']))

st.write('#### There is a direct relationship between family income and average final exam score.')

st.plotly_chart(px.bar(data_frame= cat_col_df['break_frequency']))

st.write('#### Taking breaks Occasionally is the best choice for higher final exam score.')


st.plotly_chart(px.bar(data_frame= cat_col_df['internet_access']))

st.write('#### Students who have internet access have higher scores.')


st.write('')

st.write('')



st.subheader('2. Numerical Columns: Showing Correlation between Numerical Columns and final exam score.')


st.write('')
st.write('')




st.plotly_chart(px.bar(data_frame= df_corr_exam))


st.write('#### The highest 5 Correlations with exam score:')

st.write('##### 1. Study Hours Per Day')

st.write('##### 2. Self Study Hours')

st.write('##### 3. Practice Test Completed')

st.write('##### 4. Exam Preparation Days')

st.write('##### 5. Sleep hours')

st.write('')
st.write('')
st.write('')

st.write('#### The 2 Negative Correlations With Exam Score:')


st.write('##### 1. Stress Level')

st.write('##### 2. Anxiety Exam Level')
