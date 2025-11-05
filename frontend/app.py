"""Streamlit UI scaffold for PhishGuard phishing detection demo."""

import streamlit as st

st.set_page_config(page_title="PhishGuard - AI Phishing URL Detector", page_icon="🛡️")

st.title("PhishGuard - AI Phishing URL Detector")

st.write(
    "Use this interface to explore phishing detection results. "
    "Backend integration is pending; all outputs are placeholders."
)

url_input = st.text_input("Enter URL to scan", placeholder="https://example.com")

if st.button("Scan URL"):
    # TODO: Send request to FastAPI backend once API is available.
    st.info("Scanning in progress... (placeholder)")
    # TODO: Render prediction label and confidence score from backend response.
    st.warning("Prediction results will appear here once connected to the model.")

# TODO: Add explanation/feature importance visualization for transparency.
st.markdown(
    "---\n"
    "### Next Steps\n"
    "- Integrate with FastAPI predict endpoint.\n"
    "- Surface model confidence, risk score bar, and decision rationale.\n"
)
