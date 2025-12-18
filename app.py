import streamlit as st
import pandas as pd
import requests

API_URL = "https://shl-assessment-recommendation-system-462r.onrender.com/recommend"

st.set_page_config(
    page_title="SHL Assessment Recommendation System",
    layout="centered"
)

st.title("SHL Assessment Recommendation System")

st.write(
    "Enter a job description or requirement text to receive the most relevant "
    "SHL assessment recommendations."
)

query = st.text_area(
    "Job Description / Requirement Text",
    height=150,
    placeholder="e.g. Looking for a Python developer with strong problem solving skills..."
)

top_k = st.number_input(
    "Number of Recommendations",
    min_value=5,
    max_value=10,
    value=5,
    step=1
)

if st.button(" Get Recommendations"):
    if not query.strip():
        st.warning("Please enter a job description.")
    else:
        with st.spinner("Fetching recommendations..."):
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

                        st.subheader("Recommended SHL Assessments")
                        st.dataframe(df, use_container_width=True)

                        csv = df.to_csv(index=False).encode("utf-8")
                        st.download_button(
                            label=" Download as CSV",
                            data=csv,
                            file_name="shl_recommendations.csv",
                            mime="text/csv"
                        )

            except Exception as e:
                st.error(f"Failed to connect to API: {str(e)}")


st.markdown("---")
st.caption("Powered by Semantic Similarity & SHL Assessment Catalog")
