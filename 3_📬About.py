import streamlit as st

st.header("ABOUT THIS PROJECT")

st.subheader(":violet[1. Data Collection:]")

st.write('''***Gather data from Airbnb's public API or other available sources.
    Collect information on listings, hosts, reviews, pricing, and location data.***''')

st.subheader(":violet[2. Data Cleaning and Preprocessing:]")

st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
    Convert data types, handle duplicates, and standardize formats.***''')

st.subheader(":violet[3. Exploratory Data Analysis (EDA):]")

st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data.
    Explore relationships between variables and identify potential insights.***''')

st.subheader(":violet[4. Visualization:]")

st.write('''***Create visualizations to represent key metrics and trends.
    Use charts, graphs, and maps to convey information effectively.
    Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''')

# Adding contributor's name in the right corner
st.markdown(
    """
    <div style="position: fixed; bottom: 30px; right: 10px; font-size: large;">
        <i>Contributor: Naveen Anandhan</i>
    </div>
    """, unsafe_allow_html=True
)
