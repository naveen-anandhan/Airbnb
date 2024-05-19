import streamlit as st
import pandas as pd
pd.set_option("display.max_columns",None)
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


st.title("AIRBNB DATA ANALYSIS")

# Define page navigation
pages = {
    "Price Analysis": "Price Analysis",
    "Review Analysis": "Review Analysis"
}


# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

def load_data():
    df = pd.read_csv("C:\\Users\\mrnav\\OneDrive\\Desktop\\Python\\Airbnb\\Usefulldata.csv")
    return df

df = load_data()

if selection == "Price Analysis":
    st.title("Price Analysis")
    country = st.selectbox("Select the Country", df["country"].unique())
    
    df1 = df[df["country"] == country]
    df1.reset_index(drop=True, inplace=True)

    room_type = st.selectbox("Select the Room Type", df1["room_type"].unique())
    
    df2 = df1[df1["room_type"] == room_type]
    df2.reset_index(drop=True, inplace=True)

    # Use st.columns for side-by-side layout
    col1, col2 = st.columns(2)

    with col1:
        df_bar = pd.DataFrame(df2.groupby("property_type")[["price","review_scores_value","number_of_reviews"]].sum())
        df_bar.reset_index(inplace=True)
        
        average_price = df2["price"].mean()

        fig_bar = px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY_TYPES",
                         hover_data=["number_of_reviews","review_scores_value"],
                         color_discrete_sequence=px.colors.sequential.Redor_r,
                         width=600, height=500)
        
        fig_bar.add_annotation(
        text=f"Average Price: ${average_price:.2f}",
        xref="paper", yref="paper",
        x=0.5, y=1.1, showarrow=False,
        font=dict(size=14, color="white")
)
        
        st.plotly_chart(fig_bar)

    with col2:
            
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
    
        proper_ty= st.selectbox("Select the Property_type",df2["property_type"].unique())

        df4= df2[df2["property_type"] == proper_ty]
        df4.reset_index(drop= True, inplace= True)

        df_pie= pd.DataFrame(df4.groupby("host_response_time")[["price","bedrooms"]].sum())
        df_pie.reset_index(inplace= True)

        fig_pi= px.pie(df_pie, values="price", names= "host_response_time",
                        hover_data=["bedrooms"],
                        color_discrete_sequence=px.colors.sequential.BuPu_r,
                        title="PROPERTY TYPE BASED ON HOST RESPONSE TIME",
                        width= 600, height= 500)
        st.plotly_chart(fig_pi)

    col1,col2= st.columns(2)
    
    with col1:

        
        hostresponsetime= st.selectbox("Select the host_response_time",df4["host_response_time"].unique())

        df5= df4[df4["host_response_time"] == hostresponsetime]
        
        min_nights = int(df5["minimum_nights"].mean())
        max_nights = int(df5["maximum_nights"].mean())
        

        df_do_bar= pd.DataFrame(df5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
        df_do_bar.reset_index(inplace= True)

        fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
        title='MINIMUM NIGHTS AND MAXIMUM NIGHTS',hover_data="price",
        barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow, width=600, height=500)
        
        
        fig_do_bar.add_annotation(
        text=f"Avg Min Nights: {min_nights}",
        xref="paper", yref="paper",
        x=0.5, y=1.1, showarrow=False,
        font=dict(size=14, color="white")
    )

        fig_do_bar.add_annotation(
        text=f"Avg Max Nights: {max_nights}",
        xref="paper", yref="paper",
        x=0.5, y=1.05, showarrow=False,
        font=dict(size=14, color="white")
    )

        st.plotly_chart(fig_do_bar)

    with col2:
        # Calculate summary statistics for the card display
        summary_stats = df5.groupby("bed_type")[["bedrooms", "beds"]].sum().reset_index()
        

        for index, row in summary_stats.iterrows():
            st.write(f"### {row['bed_type']}")
            col3, col4 = st.columns(2)
            with col3:
                st.metric(label="Max Bedrooms", value=row["bedrooms"])
            with col4:
                st.metric(label="Max Beds", value=row["beds"])
                


    df2["availability_type"] = "availability_30"
    df2["availability_type"].iloc[df2.shape[0]:2*df2.shape[0]] = "availability_60"
    df2["availability_type"].iloc[2*df2.shape[0]:] = "availability_90"

    # Combine the three availability columns into a single column
    df2_long = pd.melt(df2, id_vars=["room_type", "bed_type", "availability_type"], 
                    value_vars=["availability_30", "availability_60", "availability_90"], 
                    var_name="availability", value_name="availability_value")

    # Display sunburst chart for all availability values
    fig_sunburst = px.sunburst(df2_long, path=["room_type", "bed_type", "availability_type", "availability"], 
                                values="availability_value", 
                                title="Availability", 
                                color="availability_type",
                                color_discrete_map={"availability_30": px.colors.sequential.Peach_r,
                                                    "availability_60": px.colors.sequential.Blues_r,
                                                    "availability_90": px.colors.sequential.Aggrnyl_r},
                                width=900, height=600)
    st.plotly_chart(fig_sunburst)
  
elif selection == "Review Analysis":
    st.title("Review Analysis")

    def load_data():
            
            df_review = pd.read_csv("C:\\Users\\mrnav\\OneDrive\\Desktop\\Python\\Airbnb\\Airbnb_customer_review.csv")
            
            return df_review
        
    df = load_data()
    
    # 1. Review Count Over Time
    st.header("Review Count Over Time")
    review_count_over_time = df.groupby('date').size()
    st.line_chart(review_count_over_time)
 
    # 2. Number of Reviews by Reviewer
    st.header("Number of Reviews by Reviewer")
    reviews_by_reviewer = df['reviewer_name'].value_counts()
    st.bar_chart(reviews_by_reviewer)

    # 3. Distribution of Reviews by Listing
    st.header("Distribution of Reviews by Listing")
    reviews_by_listing = df['listing_id'].value_counts()
    st.bar_chart(reviews_by_listing)

    # 4. Top Reviewers by Number of Reviews
    st.header("Top Reviewers by Number of Reviews")
    top_reviewers = df['reviewer_name'].value_counts().head(10)
    st.bar_chart(top_reviewers)

    # 5. Word Cloud of Most Common Words in Reviews
    st.header("Most Common Words in Reviews")
    all_comments = ' '.join(df['comments'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_comments)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)