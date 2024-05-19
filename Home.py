import streamlit as st
import pandas as pd
pd.set_option("display.max_columns",None)
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
from PIL import Image
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(layout= "wide")


# Load the image
image1 = Image.open("C:\\Users\\mrnav\\OneDrive\\Desktop\\Python\\Airbnb\\airbnb.jpg")
image2 = Image.open("C:\\Users\\mrnav\\OneDrive\\Desktop\\Python\\Airbnb\\airbnb2.jpg")

# Create columns
col1, col2 = st.columns([1, 1])
col3, col4 = st.columns([1, 1])

# Add image1 to col1
with col1:
    st.image(image1, use_column_width=True)

# Add text to col2
with col2:
    st.markdown(
        """
        <div class="text-container">
            <h2>About Airbnb</h2>
            <p><strong>Airbnb</strong> is an online marketplace that connects people who want to rent out their property with people who are looking for accommodations, typically for short stays. Airbnb offers hosts a relatively easy way to earn some income from their property. Guests often find that Airbnb rentals are cheaper and homier than hotels.</p>
            <p><strong>Airbnb Inc (Airbnb)</strong> operates an online platform for hospitality services. The company provides a mobile application (app) that enables users to list, discover, and book unique accommodations across the world. The app allows hosts to list their properties for lease, and enables guests to rent or lease on a short-term basis, which includes vacation rentals, apartment rentals, homestays, castles, tree houses, and hotel rooms. The company has a presence in China, India, Japan, Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy, Norway, Portugal, Russia, Spain, Sweden, the UK, and others. Airbnb is headquartered in San Francisco, California, the US.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Add the Background of Airbnb section to col3
with col3:
    st.header("Background of Airbnb")
    st.write(
        """
        **Airbnb** was born in 2007 when two Hosts welcomed three guests to their San Francisco home, and has since grown to over 4 million Hosts who have welcomed over 1.5 billion guest arrivals in almost every country across the globe.
        """
    )

# Add image2 to col4
with col4:
    st.image(image2, caption='', use_column_width=False, width=600)  # Adjust width as needed


