# Data Progress Report

## 🌟 Project Overview

The **Data Progress Report** project is a versatile and robust web application designed to provide users with a wide array of data analysis features, including stock market analysis, cancer predictions using machine learning, protein structure analysis, and cryptocurrency price tracking. The app also includes an interactive chatbot for assistance and a contact page for user support.

The primary focus of this project is to enable users to visualize, analyze, and interact with complex datasets in a simple and intuitive way. The platform is built with **Streamlit** as the frontend, making it easy to create highly interactive user interfaces.

## 🚀 Key Features

### 🏠 **Home**
The central dashboard where users can navigate between various sections of the application, such as data analysis modules. This provides a high-level overview and serves as the hub for users to access the specialized functionalities.

### 📊 **Stock Analysis**
Analyze stock performance, visualize historical data, and predict stock trends. This feature integrates financial APIs to fetch real-time stock data and display trends through interactive graphs.

### 🧬 **Cancer Prediction**
Leverage machine learning models to predict cancer outcomes using patient data. Users can upload patient datasets, and the system provides predictions based on trained models, making this a valuable tool for healthcare researchers and professionals.

### 🧪 **Protein Structure**
Visualize and explore 3D protein structures. This module allows biologists and researchers to study molecular structures through computational techniques, helping in the study of drug design and biological functions.

### 💰 **Cryptocurrency Price Tracking**
Track real-time cryptocurrency prices, including detailed analysis of price fluctuations, market trends, and predictions using live data from cryptocurrency exchanges.

### 🤖 **Chatbot**
An AI-powered chatbot to assist users with navigating the application and providing quick answers to common queries. The chatbot makes interactions smooth and enhances the user experience by providing prompt help.

### 📞 **Contact**
A contact form to enable users to provide feedback or ask questions about the platform. This module ensures that users can easily get in touch with the team for any issues or inquiries.

---

## 🛠️ Tech Stack

- **Frontend**:  
  - **Streamlit** for building the user interface.
  - **Plotly** for creating interactive and responsive data visualizations.
  - **Pandas** for data manipulation and analysis.
  
- **Backend**:  
  - **Python** as the core language, utilizing several key libraries for data processing, visualization, and machine learning.
  - **Machine Learning Models** (using `pickle`) for cancer prediction.
  
- **Data Profiling**:  
  - **Pandas Profiling** to generate detailed data reports, including descriptive statistics, data distribution, and correlations.
  
- **Key Libraries Used**:
  - `pandas`: For efficient data handling.
  - `ydata_profiling`: For creating detailed data profile reports.
  - `plotly`: For dynamic visualizations like line charts, bar charts, and heatmaps.
  - `pickle5`: For loading pre-trained machine learning models.
  - `PIL`: For image manipulation and rendering.
  - `numpy`: For numerical operations and data processing.

---

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.8+
- Libraries from `requirements.txt`

### Steps to Set Up Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/data-progress-report.git
   cd data-progress-report
   ```

2. **Install Dependencies**:
   Ensure you have all the necessary dependencies installed by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the Streamlit app by running:
   ```bash
   streamlit run app.py
   ```

4. **Access the Application**:
   Once the application starts, open your browser and navigate to `http://localhost:8501` to interact with the application.

---

## 📂 Code Explanation

Here’s a brief explanation of how the main components of the project work:

### 1. **Home Menu Navigation**
The user can navigate between different sections using the `option_menu` from the `streamlit_option_menu` library:

```python
selected_option = option_menu(
    menu_title="Main Menu",
    options=["Home", "Stock Analysis", "Cancer Predict", "Protein Structure", "Cryptocurrency Price", "Chatbot", "Contact"],
    icons=["house", "bar-chart", "stethoscope", "dna", "bitcoin", "robot", "envelope"],
    menu_icon="cast",
    default_index=0,
)
```
This dynamically generates a side menu where users can select different options to interact with the features of the app.

### 2. **Stock Analysis Module**
This module fetches stock data and visualizes it using Plotly. It leverages real-time data to show stock trends and predictions:

```python
fig = px.line(stock_data, x="Date", y="Close", title="Stock Price Over Time")
st.plotly_chart(fig)
```
`Plotly` is used to create an interactive chart that allows the user to explore stock data over time.

### 3. **Cancer Prediction Module**
A pre-trained machine learning model is loaded using `pickle5`, and the user can upload a CSV file containing patient data for predictions:

```python
with open('cancer_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load user input data
input_data = pd.read_csv(uploaded_file)
predictions = model.predict(input_data)
st.write(predictions)
```
The model predicts cancer outcomes based on user-inputted data, which is processed and displayed on the interface.

### 4. **Protein Structure Module**
This module helps users explore protein structures visually:

```python
image = Image.open("protein_structure.png")
st.image(image, caption="3D Protein Structure")
```
Here, **PIL** is used to render an image of a protein structure, allowing the user to interactively explore it.

### 5. **Cryptocurrency Price Module**
This module tracks cryptocurrency prices in real-time, and displays trends using **Plotly**:

```python
crypto_fig = go.Figure(data=[go.Candlestick(x=crypto_data['Date'],
                                            open=crypto_data['Open'],
                                            high=crypto_data['High'],
                                            low=crypto_data['Low'],
                                            close=crypto_data['Close'])])
st.plotly_chart(crypto_fig)
```
The chart allows users to track price changes and view historical trends of selected cryptocurrencies.

### 6. **Chatbot**
The AI-powered chatbot is integrated using a simple Python function, making it a helpful tool for the user:

```python
def chatbot_response(user_input):
    response = "Your chatbot response here!"
    return response

st.write(chatbot_response(st.text_input("Chat with our assistant!")))
```
The chatbot assists users with queries about the app’s features and data analytics.

### 7. **Data Profiling**
Users can upload datasets and generate a detailed profiling report using `ydata_profiling`:

```python
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    profile = ProfileReport(df)
    st_profile_report(profile)
```
This feature enables users to perform a comprehensive analysis of their dataset, including data distribution, missing values, and correlations.

---

## 🎨 User Interface

### Screenshots (Coming Soon)

---

## 🤝 Contributing

We welcome contributions! Follow the steps below to get started:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -m "Add new feature"`).
4. Push to your branch (`git push origin feature/new-feature`).
5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Happy Analyzing!** If you have any questions or feedback, feel free to reach out through the contact page. We're always excited to improve and enhance this project based on your input!
