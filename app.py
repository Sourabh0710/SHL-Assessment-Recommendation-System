import streamlit as st
import pandas as pd
from recommender import SHLRecommender

st.set_page_config(
    page_title="SHL Assessment Recommendation System",
    layout="centered"
)

st.title("SHL Assessment Recommendation System")
st.write(
    "Enter a job description or requirement text to get the most relevant "
    "SHL assessment recommendations using Generative AI."
)

@st.cache_resource
def load_recommender():
    return SHLRecommender("shl_catalog.csv")

recommender = load_recommender()

query = st.text_area(
    "Job Description / Requirement Text",
    height=150,
    placeholder="e.g. Looking for a Python developer with strong problem solving skills..."
)

top_k = st.number_input(
    "Number of Recommendations (Min 5, Max 10)",
    min_value=5,
    max_value=10,
    value=5,
    step=1
)

if st.button(" Get Recommendations"):
    if not query.strip():
        st.warning("Please enter a job description.")
    else:
        with st.spinner("Generating recommendations..."):
            results = recommender.recommend(query, top_k)
            if results is None or (hasattr(results, "empty") and results.empty):
                st.info("No recommendations found.")
            else:
                df = pd.DataFrame(results)


            st.subheader("Recommended SHL Assessments")
            st.dataframe(df, use_container_width=True)

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download as CSV",
                data=csv,
                file_name="shl_recommendations.csv",
                mime="text/csv"
            )

st.markdown("---")
st.caption("Built using Generative AI (Transformer-based semantic similarity)")
