import streamlit as st
from recommender import SHLRecommender

st.set_page_config(
    page_title="SHL Assessment Recommendation System",
    layout="centered"
)

st.title("SHL Assessment Recommendation System")
st.write(
    "Enter a job description or hiring requirement to receive "
    "recommended SHL assessments."
)


@st.cache_resource
def load_recommender():
    return SHLRecommender("shl_catalog.csv")

recommender = load_recommender()


query = st.text_area(
    "Job Description / Requirement",
    height=150,
    placeholder="Example: Looking for a Java backend developer with strong OOP and problem-solving skills"
)

top_k = st.number_input(
    "Number of recommendations (min 5, max 10)",
    min_value=5,
    max_value=10,
    value=10,
    step=1
)


if st.button("Get Recommendations"):
    if query.strip() == "":
        st.warning("Please enter a job description.")
    else:
        results = recommender.recommend(query, top_k)

        st.success(f"Top {top_k} Recommended Assessments")

        # Display results (without score)
        st.dataframe(
            results.drop(columns=["score"]),
            use_container_width=True
        )


        csv_data = results.drop(columns=["score"]).to_csv(index=False)

        st.download_button(
            label="⬇ Download Predictions CSV",
            data=csv_data,
            file_name="predictions.csv",
            mime="text/csv"
        )
