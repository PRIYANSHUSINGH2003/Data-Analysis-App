import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from PIL import Image
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import openpyxl

import warnings
import matplotlib.pyplot as plt  # Import matplotlib's pyplot module

# Filter out Matplotlib deprecation warnings
warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

# Set the page title
logo = Image.open("images/Logo.png")
st.set_page_config(page_title='~AnalysisMaster',page_icon=logo,layout="wide")
# Add a title
st.title("My Dashboard")
with open('style.css') as f:
    st.sidebar.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.sidebar.image(logo)
# Add a sidebar with options
option = st.sidebar.selectbox(
    'Which option do you like best?',
    ('Option 1', 'Option 2', 'Option 3')
)

# Add a slider
x = st.slider('Select a value',min_value=6)

# Add a chart
line_chart_data = np.random.randn(10, x)
st.line_chart(line_chart_data)
line_chart_columns = [f'Column {i+1}' for i in range(x)]
df_line_chart = pd.DataFrame(line_chart_data, columns=line_chart_columns)
st.write("Total No. of Participants")

# Add a table
cards1, cards2= st.columns(2)

cards1.write(df_line_chart)
pie_char_columns =[f'Column {i+1}' for i in range(x)]
pie_chart = px.pie(df_line_chart, values=df_line_chart.iloc[0],names=line_chart_columns,width=350, height=350)

cards2.plotly_chart(pie_chart)


x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

st.plotly_chart(fig, use_container_width=True,width=350, height=350)

# add custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

st.header('Data Progress Report')
st.subheader('A data progress report shows that the progress of analyzing and cleaning the data. It is a report in which you are updating information about a project. The typical progress report give some summary of the project goal, states the progress made toward that goal during the reporting period.')
st.markdown('<div class="text-overlay">Data Processing</div>', unsafe_allow_html=True)
st.markdown("### What does a  Data Analyst do?")
st.write("A data analyst is a professional who extracts, interprets, and processes large volumes of data to identify patterns, trends and insights to help organizations make informed decisions. They use statistical and analytical methods to analyze complex data sets and transform information into meaningful reports, graphs and presentations. Data analysts work in a variety of industries to optimize performance, measure effectiveness and identify areas for improvement. They must possess strong communication skills to articulate data insights to business leaders, and technical skills to utilize software and programming languages such as SQL, Python, and R.")

st.header("The Importance of Data Analysis in Business Decision Making ")
st.markdown("Data analysis is giving small businesses the opportunity to be even more competitive through the use of analytics.")
st.markdown("One of the importance is it increased transparency  and accountability of the organization.")

chart1, chart2 = st.columns(2)
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
chart1.bar_chart(chart_data)
chart2.line_chart(chart_data)
st.markdown("They can help companies make informed decision by identifying patterns and trends in data that can help to improve business operations and increase efficiency or reduce costs.")
st.markdown("Data analysis can help companies measure the effectiveness of their marketing campaigns , customer engagement strategies and other business initiatives.")

# image
st.markdown("### Data Analyze")
img1 , img2 = st.columns(2)
image_data1 = Image.open('images/data1.png')
image_data2 = Image.open('images/data2.jpg')
img1.image(image_data1, width=None,caption='Data Analyze')
img2.image(image_data2, width=None,caption='Data Structure')

# st.image(image_url, )
st.markdown("Finally, the data analysis project will culminate in the creation of a report or dashboard that presents the findings of the analysis in an easily understandable format. The report may include visualizations, key insights, and recommendations based on the findings of the analysis.")
st.markdown("Overall, this data analysis project is a critical step in transforming raw data into actionable insights that can help stakeholders make informed decisions and improve outcomes.")

#  video
video_data1 , video_data2 , video_data3 , video_data4 = st.columns(4)
vid = open('video/dashboard-data.mp4','rb').read()
vid1= open('video/network.mp4','rb').read()
vid2= open('video/evaluation.mp4','rb').read()
vid3= open('video/data.mp4','rb').read()

video_data1.video(vid)
video_data2.video(vid1)
video_data3.video(vid2)
video_data4.video(vid3)

st.subheader("How this website works?")
st.markdown("On of the most important thing about this website is it significantly reduce the time and effort required to analyze the dataset. This is huge time saver and allows me to focus on other aspects of my work.")
st.markdown("This data analysis project involves transforming your Excel sheet and CSV file format into simple and understanding form and also gives a perfect format. The main aim of this project is to convert the data into graphical, tabular form or pie chart form.")
steps = [
    "Step 1:- It Import the CSV data from the progress report into the data analysis tool.",
    "Step 2:- Once the data is loaded, than other step is to clean and manipulate the data is to ensure that the data is accurate and consistent or not.",
    "Step 3:- Next, the data will be transformed into a more visual format, such as graphs or tabular form. The goal is to make it easier for stakeholders to understand the information and see patterns and trends in the data.",
    "Step 4:- Once the data is transformed, the analyst will likely carry out exploratory data analysis to identify any outliers, trends, or patterns in the data. This will help to identify any areas of concern or opportunity that need to be addressed. The report may include visualizations, key insights, and recommendations based on the findings of the analysis." ,
    "Step 5:- Data visualization helps to tell stories by curating data into format that’s easier to understand. Effective data visualization is a delicate balancing act between form and function."
]
st.markdown("<ul>" + "".join([f"<li class='li-steps'>{step}</li>" for step in steps]) + "</ul>", unsafe_allow_html=True)
st.markdown("""
    #### Conclusion:- This data analysis project is a critical step in transforming raw data into actionable insights that can help stakeholders make informed decisions and improve outcomes.
            """)

with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

with st.sidebar.header('2. Upload your Excel file data'):
    uploaded_file1 = st.sidebar.file_uploader('Choose a XLSX file', type='xlsx')

#pandas profiling report data
if uploaded_file is not None:
    progress_bar = st.markdown('<div class="progress-bar"><div class="progress-bar-inner"></div></div>', unsafe_allow_html=True)
    @st.cache
    def load_csv_data():
        csv_data = pd.read_csv(uploaded_file)
        return csv_data
    df = load_csv_data()
    progress_bar.empty()
    pr = ProfileReport(df, explorative = True)
    st.header("View Your Data.....")
    st.code("loading.....!")
    st.write(df)
    st.write('---')
    st.header("Progress Report Showing Now....!")
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        st.markdown(f"""
        <h4>This data is collected by <span style='color:red; font-weight:600;'>Raunak Saluja</span></h3>""",unsafe_allow_html=True)
        # Example data
        @st.cache
        def load_Csv():
            a = pd.read_csv("Analyzing.csv")
            return a
        df = load_Csv()
        pr = ProfileReport(df, explorative=True)
        st.header("Input DataFrame.....!")
        st.code("loading.....!")
        st.write(df)
        st.write('-----')
        st.header("Normal Data.....!")
        st_profile_report(pr)

if uploaded_file1:
    st.markdown('----')
    progress_bar1 = st.markdown('<div class="progress-bar"><div class="progress-bar-inner"></div></div>', unsafe_allow_html=True)
    @st.cache
    def load_xlsx_data():
        xlsx_data = pd.read_excel(uploaded_file1, engine='openpyxl')
        return xlsx_data
    df1 = load_xlsx_data()
    progress_bar1.empty()
    pr1 = ProfileReport(df1, explorative = True)
    st.header("View Your Data.....")
    st.code("loading.....!")
    st.write(df1)
    st.write('---')
    st.header("Progress Report Showing Now....!")
    st_profile_report(pr1)

programmer_name = "Priyanshu Singh"

# Add the programmer name with animation to the sidebar
st.sidebar.markdown(f"""
    <div class="animated fadeInDown" style="animation-delay: 0.5s;">
        <h3>Programmed by:</h3>
        <p style="font-size: 24px; font-weight: bold; color: #f3725b;">{programmer_name}</p>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""<h2> This app is created by <span style="font-weigth:900; color:rgb(243, 114, 91); font-size: 34px; ">Priyanshu Singh.</span></h2>""", unsafe_allow_html=True)
st.markdown(f"""<div class="footer">This is a Streamlit app for uploading and displaying CSV data.</div>""", unsafe_allow_html=True)

hide_st_style = """
    <style>
        #MainMenu {visiblity: hidden;}
        footer {visiblity: hidden;}
        header {visiblity: hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)
