import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from streamlit_option_menu import option_menu
from PIL import Image
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import pickle5 as pickle
import plotly.graph_objects as go

def main_menu():
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Stock Analysis", "Cancer Predict","Protein Structure", "Cryptocurrency Price","Chatbot" ,"Contact"],
    )
    return selected

def home_page():
    st.title("My Dashboard")
    st.sidebar.image(logo, width=None)


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
    image_data1 = open('images/data.gif','rb').read()
    image_data2 = open('images/internet.gif','rb').read()
    responsive_image_css = """
    .responsive-image {
        max-width: 100%;
        height: auto;
    }
    """
    st.markdown(f'<style>{responsive_image_css}</style>', unsafe_allow_html=True)
    img1.image(image_data1,caption='Data Analyze')
    img2.image(image_data2,caption='Data Structure')


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

def Stock_Performance():
    import pandas as pd
    import base64
    import yfinance as yf
    import matplotlib.pyplot as plt
    
    st.sidebar.header('User Input Features')
    # Function to load S&P 500 data
    @st.cache_data
    def load_data():
        url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
        html = pd.read_html(url, header=0)
        df = html[0]
        return df
    
    # Load S&P 500 data
    df = load_data()
    sector = df.groupby('GICS Sector')
    
    # Sidebar - Sector selection
    sorted_sector_unique = sorted(df['GICS Sector'].unique())
    selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)
    
    # Filtering data
    df_selected_sector = df[df['GICS Sector'].isin(selected_sector)]
    
    # Display selected companies
    st.header('Display Companies in Selected Sector')
    st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
    st.dataframe(df_selected_sector)
    
    # Download S&P 500 data as CSV
    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
        href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
        return href
    
    st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)
    
    # Download historical stock data for selected companies
    num_company = st.sidebar.slider('Number of Companies', 1, 5)
    
    if st.button('Show Plots'):
        st.header('Stock Closing Price')
        data = yf.download(
            tickers=list(df_selected_sector['Symbol'][:num_company]),
            period="ytd",
            interval="1d",
            group_by='ticker',
            auto_adjust=True,
            prepost=True,
            threads=True,
            proxy=None
        )

        # Create an empty DataFrame for the portfolio performance
        portfolio_performance = pd.DataFrame(index=data.index)

        # Plot Closing Price of Selected Companies
        def price_plot(data, symbol):
            df = pd.DataFrame(data[symbol]['Close'])
            df['Date'] = df.index
            plt.fill_between(df['Date'], df['Close'], color='skyblue', alpha=0.3)
            plt.plot(df['Date'], df['Close'], color='skyblue', alpha=0.8)
            plt.xticks(rotation=90)
            plt.title(symbol, fontweight='bold')
            plt.xlabel('Date', fontweight='bold')
            plt.ylabel('Closing Price', fontweight='bold')
            return plt

        for i in range(num_company):
            symbol = df_selected_sector.iloc[i]['Symbol']
            st.write(f"### {symbol}")

            try:
                fig = price_plot(data, symbol)
                st.pyplot(fig)

                # Add the closing price data to the portfolio performance DataFrame
                portfolio_performance[symbol] = data[symbol]['Close']

            except KeyError:
                st.warning(f"Stock data for '{symbol}' not found.")
        # Plot Portfolio Performance
        st.subheader("Portfolio Performance")
        st.line_chart(portfolio_performance)

def Cancer_Predict():
    with open("assets/style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
        input_data = add_sidebar()
    with st.container():
        st.title("Breast Cancer Predictor")
        st.write("Please connect this app to your cytology lab to help diagnose breast cancer form your tissue sample. This app predicts using a machine learning model whether a breast mass is benign or malignant based on the measurements it receives from your cytosis lab. You can also update the measurements by hand using the sliders in the sidebar. ")
    col1, col2 = st.columns([4,1])
    with col1:
        radar_chart = get_radar_chart(input_data)
        st.plotly_chart(radar_chart)
    with col2:
        add_predictions(input_data)

def get_clean_data():
    data = pd.read_csv("data/data.csv")
    
    data = data.drop(['Unnamed: 32', 'id'], axis=1)
    
    data['diagnosis'] = data['diagnosis'].map({ 'M': 1, 'B': 0 })
    
    return data


def add_sidebar():
    st.sidebar.header("Cell Nuclei Measurements")

    data = get_clean_data()  
    slider_labels = [
        ("Radius (mean)", "radius_mean"),
        ("Texture (mean)", "texture_mean"),
        ("Perimeter (mean)", "perimeter_mean"),
        ("Area (mean)", "area_mean"),
        ("Smoothness (mean)", "smoothness_mean"),
        ("Compactness (mean)", "compactness_mean"),
        ("Concavity (mean)", "concavity_mean"),
        ("Concave points (mean)", "concave points_mean"),
        ("Symmetry (mean)", "symmetry_mean"),
        ("Fractal dimension (mean)", "fractal_dimension_mean"),
        ("Radius (se)", "radius_se"),
        ("Texture (se)", "texture_se"),
        ("Perimeter (se)", "perimeter_se"),
        ("Area (se)", "area_se"),
        ("Smoothness (se)", "smoothness_se"),
        ("Compactness (se)", "compactness_se"),
        ("Concavity (se)", "concavity_se"),
        ("Concave points (se)", "concave points_se"),
        ("Symmetry (se)", "symmetry_se"),
        ("Fractal dimension (se)", "fractal_dimension_se"),
        ("Radius (worst)", "radius_worst"),
        ("Texture (worst)", "texture_worst"),
        ("Perimeter (worst)", "perimeter_worst"),
        ("Area (worst)", "area_worst"),
        ("Smoothness (worst)", "smoothness_worst"),
        ("Compactness (worst)", "compactness_worst"),
        ("Concavity (worst)", "concavity_worst"),
        ("Concave points (worst)", "concave points_worst"),
        ("Symmetry (worst)", "symmetry_worst"),
        ("Fractal dimension (worst)", "fractal_dimension_worst"),
    ]

    input_dict = {}

    for label, key in slider_labels:
        input_dict[key] = st.sidebar.slider(
            label,
            min_value=float(0),
            max_value=float(data[key].max()),
            value=float(data[key].mean())
        )
    
    return input_dict


def get_scaled_values(input_dict):
    data = get_clean_data()
    
    X = data.drop(['diagnosis'], axis=1)
    
    scaled_dict = {}
    
    for key, value in input_dict.items():
        max_val = X[key].max()
        min_val = X[key].min()
        scaled_value = (value - min_val) / (max_val - min_val)
        scaled_dict[key] = scaled_value
    
    return scaled_dict
    

def get_radar_chart(input_data):
    input_data = get_scaled_values(input_data)
    
    categories = ['Radius', 'Texture', 'Perimeter', 'Area', 
                'Smoothness', 'Compactness', 
                'Concavity', 'Concave Points',
                'Symmetry', 'Fractal Dimension']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_mean'], input_data['texture_mean'], input_data['perimeter_mean'],
            input_data['area_mean'], input_data['smoothness_mean'], input_data['compactness_mean'],
            input_data['concavity_mean'], input_data['concave points_mean'], input_data['symmetry_mean'],
            input_data['fractal_dimension_mean']
        ],
        theta=categories,
        fill='toself',
        name='Mean Value'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_se'], input_data['texture_se'], input_data['perimeter_se'], input_data['area_se'],
            input_data['smoothness_se'], input_data['compactness_se'], input_data['concavity_se'],
            input_data['concave points_se'], input_data['symmetry_se'],input_data['fractal_dimension_se']
        ],
        theta=categories,
        fill='toself',
        name='Standard Error'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_worst'], input_data['texture_worst'], input_data['perimeter_worst'],
            input_data['area_worst'], input_data['smoothness_worst'], input_data['compactness_worst'],
            input_data['concavity_worst'], input_data['concave points_worst'], input_data['symmetry_worst'],
            input_data['fractal_dimension_worst']
        ],
        theta=categories,
        fill='toself',
        name='Worst Value'
))

    fig.update_layout(
        polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 1]
        )),
        showlegend=True
    )

    return fig


def add_predictions(input_data):
    model = pickle.load(open("model/model.pkl", "rb"))
    scaler = pickle.load(open("model/scaler.pkl", "rb"))
    
    input_array = np.array(list(input_data.values())).reshape(1, -1)
    
    input_array_scaled = scaler.transform(input_array)
    
    prediction = model.predict(input_array_scaled)
    
    st.subheader("Cell cluster prediction")
    st.write("The cell cluster is:")
    
    if prediction[0] == 0:
        st.write("<span class='diagnosis benign'>Benign</span>", unsafe_allow_html=True)
    else:
        st.write("<span class='diagnosis malicious'>Malicious</span>", unsafe_allow_html=True)
    
    
    st.write("Probability of being benign: ", model.predict_proba(input_array_scaled)[0][0])
    st.write("Probability of being malicious: ", model.predict_proba(input_array_scaled)[0][1])
    
    st.write("This app can assist medical professionals in making a diagnosis, but should not be used as a substitute for a professional diagnosis.");



def protein_structure_prediction():
    import streamlit as st
    from st_speckmol import speck_plot
    import glob

    st.markdown('''# st-speckmol :package:
    _A Streamlit **Component** for creating Speck molecular structures within Streamlit Web app._
    ''')

    x_files = glob.glob("DNA_Structure/*.xyz")
    with st.sidebar:
        ex_xyz = st.selectbox('Select a molecule', x_files)
        f = open(ex_xyz, "r")
        ex_xyz = f.read()
        
    res = speck_plot(ex_xyz, wbox_height="500px", wbox_width="800px", scroll=True)

    with st.sidebar.expander("Parameters", expanded=True):
        outl = st.checkbox('Outline', value=True)
        bond = st.checkbox('Bond', value=True)
        bond_scale = st.slider('BondScale', min_value=0.0, max_value=1.0, value=0.8)
        brightness = st.slider('Brightness', min_value=0.0, max_value=1.0, value=0.4)
        relativeAtomScale = st.slider('RelativeAtomScale', min_value=0.0, max_value=1.0, value=0.64)
        bondShade = st.slider('BondShade', min_value=0.0, max_value=1.0, value=0.5)

    _PARAMETERS = {
        'outline': outl, 'bondScale': bond_scale,
        'bonds': bond, 'bondShade': bondShade,
        'brightness': brightness, 'relativeAtomScale': relativeAtomScale,
    }
    res = speck_plot(ex_xyz, wbox_height="500px", wbox_width="800px", scroll=True, _PARAMETER=_PARAMETERS)

    st.markdown('''# st-speckmol :package:
    _A Streamlit **Component** for creating Speck molecular structures within Streamlit Web app._
    ''')

    st.sidebar.header("Add your own xyz coordinates below. :art:")
    example_xyz = '''5
    methane molecule (in ångströms)
    C        0.000000        0.000000        0.000000
    H        0.000000        0.000000        1.089000
    H        1.026719        0.000000       -0.363000
    H       -0.513360       -0.889165       -0.363000
    H       -0.513360        0.889165       -0.363000
    '''
    _xyz = st.sidebar.text_area(
        label="Paste your coordinates ⬇️",
        value=example_xyz,
        height=200
    )

    st.code(_xyz.splitlines()[1])
    res = speck_plot(_xyz)

def Cryptocurrency_Price():
    st.markdown('''# **Binance Price App**
    A simple cryptocurrency price app pulling price data from *Binance API*.
    ''')

    st.header('**Selected Price**')
    # Load market data from Binance API
    try:
        df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')
    except Exception as e:
        st.error(f"An error occurred while fetching data: {e}")
        return

    # Custom function for rounding values
    def round_value(input_value):
        if input_value.values > 1:
            a = float(round(input_value, 2))
        else:
            a = float(round(input_value, 8))
        return a

    crpytoList = {
        'Price 1': 'BTCBUSD',
        'Price 2': 'ETHBUSD',
        'Price 3': 'BNBBUSD',
        'Price 4': 'XRPBUSD',
        'Price 5': 'ADABUSD',
        'Price 6': 'DOGEBUSD',
        'Price 7': 'SHIBBUSD',
        'Price 8': 'DOTBUSD',
        'Price 9': 'MATICBUSD'
    }
    crypto_names = {
        'BTCBUSD': 'Bitcoin to Binance USD',
        'ETHBUSD': 'Ethereum to Binance USD',
        'BNBBUSD': 'Binance Coin to Binance USD',
        'XRPBUSD': 'Ripple to Binance USD',
        'ADABUSD': 'Cardano to Binance USD',
        'DOGEBUSD': 'Dogecoin to Binance USD',
        'SHIBBUSD': 'Shiba Inu to Binance USD',
        'DOTBUSD': 'Polkadot to Binance USD',
        'MATICBUSD': 'Polygon (MATIC) to Binance USD'
    }

    col1, col2, col3 = st.columns(3)

    for i in range(len(crpytoList.keys())):
        selected_crypto_label = list(crpytoList.keys())[i]
        selected_crypto_index = list(df.symbol).index(crpytoList[selected_crypto_label])
        selected_crypto = st.sidebar.selectbox(selected_crypto_label, df.symbol, selected_crypto_index, key = str(i))
        col_df = df[df.symbol == selected_crypto]
        col_price = round_value(col_df.weightedAvgPrice)
        col_percent = f'{float(col_df.priceChangePercent)}%'
        full_name = crypto_names[crpytoList[selected_crypto_label]]
        border_style = "1px solid #ddd; padding: 10px; border-radius: 10px;"
        if i < 3:
            with col1:
                st.info(full_name,icon="💰")
                st.metric(selected_crypto, col_price, col_percent)
        if 2 < i < 6:
            with col2:
                st.info(full_name,icon="💰")
                st.metric(selected_crypto, col_price, col_percent)
        if i > 5:
            with col3:
                st.info(full_name,icon="💰")
                st.metric(selected_crypto, col_price, col_percent)

    st.header('All Price')
    st.markdown("### ₿ Explore the cryptocurrency prices and trends.")
    with st.container():
        st.subheader("🪙 Cryptocurrency Prices")
        st.dataframe(df)
        st.subheader("🪙 Price Trend")
        st.markdown("## See the trend of cryptocurrency prices over time.")
        st.line_chart(df.set_index('symbol')['weightedAvgPrice'])


def chatbot_page():
    import streamlit as st
    import random
    import time

    st.title("Chatbot")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    prompt = st.chat_input("What is up?")

    # Display user message in chat message container
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Response logic based on input prompt
        if prompt and "hello" in prompt.lower():
            assistant_response = random.choice(["Hi there!", "Hello!", "Hey!"])
        elif prompt and "how are you" in prompt.lower():
            assistant_response = random.choice(["I'm good, thanks!", "Doing well, how about you?", "Not bad!"])
        elif prompt and "bye" in prompt.lower():
            assistant_response = random.choice(["Goodbye!", "See you later!", "Bye!"])
        else:
            assistant_response = random.choice(["I'm not sure how to respond to that.", "Could you please provide more details?", "I don't understand."])

        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})



def contact_select():
    st.title("Contact Information")
    st.write("You can contact us via the following methods:")
    st.write("1. Emali: priyanshusingh00004@gmail.com.")
    st.write("2. Phone: 9971196062")
    st.write("3. Portfolio Website: [Portfolio Website](https://my-portfolio-website-0.netlify.app/)")
    st.write("4. Github: [Github](https://github.com/PRIYANSHUSINGH2003)")


def main():
    global logo
    logo = Image.open("images/Logo.png")
    st.set_page_config(page_title='~AnalysisMaster', page_icon=logo, layout="wide")
    st.snow()
    selected = main_menu()

    if selected == "Home":
        home_page()
    elif selected == "Stock Analysis":
        Stock_Performance();
    elif selected == "Cancer Predict":
        Cancer_Predict();
    elif selected == "Protein Structure":
        protein_structure_prediction();
    elif selected == "Cryptocurrency Price":
        Cryptocurrency_Price();
    elif selected == "Chatbot":
        chatbot_page();
    elif selected == "Contact":
        contact_select();

if __name__ == '__main__':
    main()
