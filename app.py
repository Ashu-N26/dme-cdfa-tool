import streamlit as st

st.set_page_config(page_title="DME-CDFA Tool", layout="wide")

st.title("🧮 DME-CDFA Calculator")

st.markdown("""
This tool helps calculate **CDFA** and **DME** values.
""")

st.header("🔢 Input Parameters")

col1, col2 = st.columns(2)

with col1:
    a = st.number_input("Enter value for a", value=0.0)
    b = st.number_input("Enter value for b", value=0.0)

with col2:
    c = st.number_input("Enter value for c", value=0.0)
    d = st.number_input("Enter value for d", value=0.0)

if st.button("Calculate"):
    try:
        dme = (a + b) / 2
        cdfa = (c + d) / (a + 1)  # Adding 1 to avoid division by zero
        st.success(f"✅ DME = {dme:.2f}")
        st.success(f"✅ CDFA = {cdfa:.2f}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
