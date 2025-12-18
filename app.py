import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title="SHL Assessment Recommendation System",
    layout="centered"
)
API_URL = "https://shl-assessment-recommendation-system-462r.onrender.com/recommend"

st.title("SHL Assessment Recommendation System")
st.write(
    "Enter a job description or requirement text to get the most relevant "
    "SHL assessment recommendations."
)

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

if st.button("Get Recommendations"):
    if not query.strip():
        st.warning("Please enter a job description.")
    else:
        with st.spinner("Generating recommendations..."):
            try:
                response = requests.post(
                    API_URL,
                    json={
                        "text": query,
                        "max_results": top_k
                    },
                    timeout=30
                )

                if response.status_code != 200:
                    st.error(f"API Error: {response.text}")
                else:
                    results = response.json()

                    if not results:
                        st.info("No recommendations found.")
                    else:
                        df = pd.DataFrame(results)
                        
                        df = df.dropna(axis=1, how="all")
                        required_cols = [
                            "assessment_name",
                            "test_type",
                            "description",
                            "url",
                            "score"
                        ]
                        df = df[[c for c in required_cols if c in df.columns]]

                        df.rename(columns={
                            "assessment_name": "Assessment",
                            "test_type": "Test Type",
                            "description": "Description",
                            "url": "URL",
                            "score": "Relevance Score"
                        }, inplace=True)

                        if "Relevance Score" in df.columns:
                            df = df.sort_values(
                                by="Relevance Score",
                                ascending=False
                            )

                        st.subheader("Recommended SHL Assessments")
                        st.dataframe(df, use_container_width=True)

                        csv = df.to_csv(index=False).encode("utf-8")
                        st.download_button(
                            label="📥 Download as CSV",
                            data=csv,
                            file_name="shl_recommendations.csv",
                            mime="text/csv"
                        )

            except Exception as e:
                st.error(f"Failed to connect to API: {str(e)}")
