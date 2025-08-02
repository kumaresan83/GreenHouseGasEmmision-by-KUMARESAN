import streamlit as st

st.set_page_config(
    page_title="Greenhouse Gas Emission Predictor",
    layout="centered",
)

st.markdown("""
<style>
    body {
        font-family: 'Inter', sans-serif;
        background-color: #e6f7e6; /* Light green background */
    }
    .st-emotion-cache-1j0bbx9 p {
        font-size: 1rem;
        color: #6b7280; /* Gray color for description */
    }
    .st-emotion-cache-1k46q40 {
        font-weight: bold;
    }
    .stButton>button {
        background-color: #669933;
        color: white;
        font-weight: bold;
        border-radius: 9999px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: background-color 200ms;
        padding: 0.75rem 2rem;
    }
    .stButton>button:hover {
        background-color: #55802b;
    }
    .stButton>button:focus {
        border-color: #669933;
        outline: none;
    }
    .stSlider [data-baseweb="slider"] {
        background-color: #e2e8f0;
    }
    .stSlider [data-baseweb="slider"] .st-bd {
        background-color: #d1fae5;
    }
    .stSlider [data-baseweb="slider"] .st-be {
        background-color: #669933;
    }
</style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown(
        """
        <div style="padding: 2rem; background-color: white; border: 2px solid #669933; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);">
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 1rem;">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16" style="height:4rem; width:4rem; color:#294c77;" viewBox="0 0 20 20" fill="currentColor">
                <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z" />
            </svg>
            <div>
                <h1 style="color:#294c77; font-size: 1.875rem; font-weight: 700;">Greenhouse Gas Emission Predictor</h1>
                <p style="color:#6b7280; font-size: 1rem;">Estimate total emissions based on supply chain factors and data quality metrics.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.header("Input Parameters")
    col1, col2 = st.columns(2)

    with col1:
        gas_type = st.selectbox(
            "Type of Gas:",
            ("carbon dioxide", "methane", "nitrous oxide", "other GHGs"),
            key="gas_type"
        )
        est_emissions = st.number_input("Est. Emissions:", value=0.0, step=0.1, key="est_emissions")

    with col2:
        unit = st.selectbox(
            "Measurement Unit:",
            ("kg/2018 USD, purchaser price", "kg CO2e/2018 USD, purchaser price"),
            key="unit"
        )
        margin_of_error = st.number_input("Margin of Error:", value=0.0, step=0.1, key="margin_of_error")

    
    st.header("Data Quality")
    st.markdown("Please rate the quality of your data on a scale from 0.0 (low quality) to 1.0 (high quality).")

    dq_reliability = st.slider("Reliability of Data", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    dq_temporal = st.slider("Timeliness of Data", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    dq_geo = st.slider("Geographic Relevance", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    dq_tech = st.slider("Technological Relevance", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    dq_data = st.slider("Data Collection Quality", min_value=0.0, max_value=1.0, value=0.0, step=0.01)

    
    if st.button("Predict Emission Factor"):
        average_dq = (dq_reliability + dq_temporal + dq_geo + dq_tech + dq_data) / 5
        prediction = est_emissions + (margin_of_error * average_dq)
        
        st.markdown(
            f"""
            <div style="background-color: #f0fdf4; border: 2px solid #d1fae5; border-radius: 8px; padding: 1rem; margin-top: 1rem; text-align: center;">
                <span style="font-size: 1.25rem; font-weight: bold; color: #294c77;">Predicted Factor = {prediction:.4f}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("</div>", unsafe_allow_html=True)