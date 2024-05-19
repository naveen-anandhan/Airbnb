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
st.title("AIRBNB DATA ANALYSIS")
st.write("")


image1 = Image.open("C:\\Users\\mrnav\\OneDrive\\Desktop\\Python\\Airbnb\\airbnb.jpg")



st.image(image1)

st.header("About Airbnb")
st.write("")
st.write('''***Airbnb is an online marketplace that connects people who want to rent out
            their property with people who are looking for accommodations,
            typically for short stays. Airbnb offers hosts a relatively easy way to
            earn some income from their property.Guests often find that Airbnb rentals
            are cheaper and homier than hotels.***''')
st.write("")
st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                The company provides a mobile application (app) that enables users to list,
                discover, and book unique accommodations across the world.
                The app allows hosts to list their properties for lease,
                and enables guests to rent or lease on a short-term basis,
                which includes vacation rentals, apartment rentals, homestays, castles,
                tree houses and hotel rooms. The company has presence in China, India, Japan,
                Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                Airbnb is headquartered in San Francisco, California, the US.***''')

st.header("Background of Airbnb")
st.write("")
st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
            San Francisco home, and has since grown to over 4 million Hosts who have
            welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')
