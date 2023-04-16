import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from PIL import Image
import numpy as np
import plotly.figure_factory as ff



# Set the page title

st.set_page_config(page_title="My Data Progress Report")
# Add a title
st.title("My Dashboard")

# Add a sidebar with options
option = st.sidebar.selectbox(
    'Which option do you like best?',
    ('Option 1', 'Option 2', 'Option 3')
)

# Add a slider
x = st.slider('Select a value')

# Add a chart
st.line_chart(np.random.randn(10, x))

# Add a table
cards1, cards2= st.columns(2)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)



x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)


# /////////////////////////////



with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

st.header('Data Progress Report')
st.subheader('This report shows the progress of data cleaning and analysis.')
st.markdown('<div class="text-overlay">Data Processing</div>', unsafe_allow_html=True)

st.header("The Importance of Data Analysis in Business Decision Making ")
st.markdown("This data analysis project involves transforming progress reports in CSV or Excel sheet format into a more easily understandable and visual format. The project likely involves using specialized software or programming tools to convert the data into graphical or tabular form.")
st.markdown("The first step in this project is likely to import the raw data from the progress reports into the data analysis tool. Once the data is loaded, the next step is to clean and manipulate the data to ensure that it is consistent and accurate.")

chart1, chart2 = st.columns(2)
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
chart1.bar_chart(chart_data)
chart2.line_chart(chart_data)
st.markdown("Next, the data will be transformed into a more visual format, such as graphs or tables. The goal is to make it easier for stakeholders to understand the information and see patterns and trends in the data.")
st.markdown("Once the data is transformed, the analyst will likely carry out exploratory data analysis to identify any outliers, trends, or patterns in the data. This will help to identify any areas of concern or opportunity that need to be addressed.")

# image
st.markdown("### Data Analyze")
img1 , img2 = st.columns(2)
image_data1 = Image.open('data1.png')
image_data2 = Image.open('data2.jpg')
img1.image(image_data1, width=None,caption='Data Analyze')
img2.image(image_data2, width=None,caption='Data Structure')

# st.image(image_url, )
st.markdown("Finally, the data analysis project will culminate in the creation of a report or dashboard that presents the findings of the analysis in an easily understandable format. The report may include visualizations, key insights, and recommendations based on the findings of the analysis.")
st.markdown("Overall, this data analysis project is a critical step in transforming raw data into actionable insights that can help stakeholders make informed decisions and improve outcomes.")

#  video
video_data1 , video_data2 , video_data3 , video_data4 = st.columns(4)
vid = open('dashboard-data.mp4','rb').read()
vid1= open('network.mp4','rb').read()
vid2= open('evaluation.mp4','rb').read()
vid3= open('data.mp4','rb').read()

video_data1.video(vid)
video_data2.video(vid1)
video_data3.video(vid2)
video_data4.video(vid3)

with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

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
    st.header("Pandas Profiling Report....!")
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example dara
        @st.cache
        def load_Csv():
            a = pd.DataFrame(
                np.random.randn(100,8),
                columns=['a','b','c','d','e','f','g','h']
            )
            return a
        df = load_Csv()
        pr = ProfileReport(df, explorative=True)
        st.header("Input DataFrame.....!")
        st.code("loading.....!")
        st.write(df)
        st.write('-----')
        st.header("Normal Data.....!")
        st_profile_report(pr)

programmer_name = "Priyanshu Singh"

# Add the programmer name with animation to the sidebar
st.sidebar.markdown(f"""
    <div class="animated fadeInDown" style="animation-delay: 0.5s;">
        <h3>Programmed by:</h3>
        <p style="font-size: 24px; font-weight: bold; color: #f3725b;">{programmer_name}</p>
    </div>
""", unsafe_allow_html=True)


st.markdown('<div class="footer">This is a Streamlit app for uploading and displaying CSV data.</div>', unsafe_allow_html=True)
# # print(df)

# # Generatew a report
# profile = ProfileReport(df)
# profile.to_file(output_file = "students - Sheet1.html")
