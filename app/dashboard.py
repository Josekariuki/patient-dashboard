import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Patient Health Dashboard",
                   page_icon="🏥", layout="wide")

@st.cache_data
def load_data():
    # Path relative to project root, works wherever you run from
    path = Path(__file__).parent.parent / "data" / "diabetes_clean.csv"
    return pd.read_csv(path)

df = load_data()

st.title("Patient Health Dashboard")
st.markdown("Exploratory analysis of the Pima Diabetes dataset")

# --- Sidebar filters ---
st.sidebar.header("Filters")
age_filter = st.sidebar.multiselect("Age group",
    options=df['AgeGroup'].dropna().unique(),
    default=df['AgeGroup'].dropna().unique())
outcome_filter = st.sidebar.radio("Diabetes status",
    options=['All', 'Positive', 'Negative'])

# Apply filters
filtered = df[df['AgeGroup'].isin(age_filter)]
if outcome_filter == 'Positive':
    filtered = filtered[filtered['Outcome'] == 1]
elif outcome_filter == 'Negative':
    filtered = filtered[filtered['Outcome'] == 0]

# --- KPI row ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total patients", len(filtered))
col2.metric("Diabetes rate", f"{filtered['Outcome'].mean()*100:.1f}%")
col3.metric("Avg glucose", f"{filtered['Glucose'].mean():.0f} mg/dL")
col4.metric("Avg BMI", f"{filtered['BMI'].mean():.1f}")

st.divider()

# --- Charts row ---
c1, c2 = st.columns(2)

with c1:
    st.subheader("Glucose distribution")
    fig = px.histogram(filtered, x='Glucose', color='Outcome',
        barmode='overlay', nbins=30,
        color_discrete_map={0: '#1D9E75', 1: '#D85A30'})
    fig.update_layout(height=300, margin=dict(t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("BMI by age group")
    fig2 = px.box(filtered, x='AgeGroup', y='BMI', color='Outcome',
        color_discrete_map={0: '#1D9E75', 1: '#D85A30'})
    fig2.update_layout(height=300, margin=dict(t=10, b=10))
    st.plotly_chart(fig2, use_container_width=True)

# --- Correlation heatmap ---
st.subheader("Correlation heatmap")
numeric = filtered.select_dtypes(include='number').corr().round(2)
fig3 = px.imshow(numeric, text_auto=True, color_continuous_scale='RdYlGn',
                 zmin=-1, zmax=1, aspect='auto')
fig3.update_layout(height=400, margin=dict(t=10, b=10))
st.plotly_chart(fig3, use_container_width=True)

# --- Raw data toggle ---
if st.checkbox("Show raw data"):
    st.dataframe(filtered.head(50), use_container_width=True)