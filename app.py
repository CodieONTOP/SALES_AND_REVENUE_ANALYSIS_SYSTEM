import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

# Page Setup
st.set_page_config(page_title="Sales & Revenue Intelligence", layout="wide", page_icon="⚡")

# 1. Inject JavaScript to track mouse coordinates across the parent document
components.html(
    """
    <script>
    const doc = window.parent.document;
    doc.addEventListener('mousemove', function(e) {
        doc.documentElement.style.setProperty('--mouse-x', e.clientX + 'px');
        doc.documentElement.style.setProperty('--mouse-y', e.clientY + 'px');
    });
    </script>
    """,
    height=0,
    width=0,
)

# 2. Universe/Galaxy Theme CSS + Mouse Follower Gradient + Glassmorphism + Text Animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
    /* Safely apply fonts without breaking Streamlit's native Material Icons */
    html, body, .stApp, h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, div[data-testid="stMetricValue"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Restore native icon fonts for Streamlit UI elements */
    .material-symbols-rounded, .material-icons, [class^="stIcon"] {
        font-family: 'Material Symbols Rounded', 'Material Icons' !important;
    }

    /* Interactive Mouse Tracking Background over a Galaxy Image */
    .stApp {
        background-color: #050810 !important;
        background-image: 
            radial-gradient(circle 600px at var(--mouse-x, 50vw) var(--mouse-y, 50vh), rgba(167, 139, 250, 0.15), transparent 45%),
            linear-gradient(rgba(5, 8, 16, 0.7), rgba(5, 8, 16, 0.85)),
            url('https://images.unsplash.com/photo-1506703719100-a0f3a48c0f41?auto=format&fit=crop&w=2560&q=80') !important;
        background-size: cover !important;
        background-attachment: fixed !important;
        background-position: center !important;
        color: #ffffff;
    }

    /* Sidebar Glassmorphism Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.6) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3, 
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p {
        color: #f8fafc !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
    }

    /* File Uploader Container - Exclude internal buttons from global button CSS */
    section[data-testid="stSidebar"] div[data-testid="stFileUploader"] {
        background-color: rgba(30, 41, 59, 0.5) !important;
        border: 2px dashed #a78bfa !important;
        border-radius: 12px !important;
        padding: 10px !important;
    }
    
    /* Target only the primary visible button in the uploader to prevent double-text */
    section[data-testid="stSidebar"] div[data-testid="stFileUploader"] button[kind="primary"] {
        background: transparent !important;
        border: 1px solid #60a5fa !important;
    }

    /* Select Inputs & Multiselect Boxes */
    div[data-baseweb="select"] > div, 
    div[data-baseweb="input"] > div {
        background-color: rgba(15, 23, 42, 0.7) !important;
        border: 1px solid #60a5fa !important;
        border-radius: 10px !important;
        color: #ffffff !important;
    }

    span[data-baseweb="tag"] {
        background: #3b82f6 !important;
        border-radius: 6px !important;
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* Keyframe Animations for Smooth Entrances */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Main Dashboard Header */
    .dashboard-title {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #60a5fa, #a78bfa, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        animation: fadeInUp 0.8s ease-out forwards;
    }
    
    .dashboard-sub {
        color: #cbd5e1 !important;
        font-size: 1.05rem;
        font-weight: 500;
        margin-bottom: 1.8rem;
        animation: fadeInUp 1s ease-out forwards;
    }

    /* Glassmorphism KPI Cards */
    div[data-testid="stMetric"] {
        background-color: rgba(30, 41, 59, 0.55) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        padding: 22px 26px;
        border-radius: 16px;
        border: 1.5px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        transition: transform 0.3s ease, border-color 0.3s ease;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-4px);
        border-color: #a78bfa !important;
        box-shadow: 0 12px 40px rgba(167, 139, 250, 0.3);
    }

    div[data-testid="stMetricLabel"] * {
        font-size: 0.95rem !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    div[data-testid="stMetricValue"] * {
        font-size: 2.1rem !important;
        font-weight: 800 !important;
        color: #ffffff !important;
    }

    /* Glassmorphism Chart Enclosures */
    div[data-testid="stPlotlyChart"] {
        background-color: rgba(15, 23, 42, 0.55) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border-radius: 16px;
        padding: 16px;
        border: 1.5px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        transition: transform 0.3s ease;
    }

    div[data-testid="stPlotlyChart"]:hover {
        transform: translateY(-3px);
        border-color: #60a5fa !important;
    }

    .section-header {
        font-size: 1.15rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Main Dashboard Title
st.markdown('<div class="dashboard-title">Sales & Revenue Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="dashboard-sub">Interactive Data Analytics & Business Insights Platform</div>', unsafe_allow_html=True)

# Sidebar Ingestion Panel
st.sidebar.markdown("### 📁 Ingestion Panel")
uploaded_file = st.sidebar.file_uploader("Upload Dataset (CSV/XLSX)", type=["csv", "xlsx"])

@st.cache_data
def load_data(file):
    if file is not None:
        return pd.read_csv(file) if file.name.endswith(".csv") else pd.read_excel(file)
    try:
        return pd.read_csv("sales_data.csv")
    except Exception:
        st.error("Upload a valid CSV or Excel file to begin.")
        st.stop()

df = load_data(uploaded_file)
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])

# Sidebar Filters
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔍 Global Slicers")

all_categories = df["Category"].unique().tolist() if "Category" in df.columns else []
selected_categories = st.sidebar.multiselect("Category Filter:", options=all_categories, default=all_categories)

all_regions = df["Region"].unique().tolist() if "Region" in df.columns else []
selected_regions = st.sidebar.multiselect("Region Filter:", options=all_regions, default=all_regions)

if "Date" in df.columns:
    min_date, max_date = df["Date"].min().date(), df["Date"].max().date()
    selected_dates = st.sidebar.date_input("Time Horizon:", value=[min_date, max_date], min_value=min_date, max_value=max_date)
else:
    selected_dates = []

# Filtering Data
filtered_df = df.copy()
if selected_categories:
    filtered_df = filtered_df[filtered_df["Category"].isin(selected_categories)]
if selected_regions:
    filtered_df = filtered_df[filtered_df["Region"].isin(selected_regions)]
if len(selected_dates) == 2 and "Date" in filtered_df.columns:
    start_d, end_d = selected_dates
    filtered_df = filtered_df[(filtered_df["Date"].dt.date >= start_d) & (filtered_df["Date"].dt.date <= end_d)]

# High Visibility KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,.2f}" if "Revenue" in filtered_df else "$0.00")
col2.metric("Total Units Sold", f"{filtered_df['UnitsSold'].sum():,}" if "UnitsSold" in filtered_df else "0")
col3.metric("Avg Order Value", f"${filtered_df['Revenue'].mean():,.2f}" if "Revenue" in filtered_df else "$0.00")
col4.metric("Total Volume", f"{len(filtered_df):,} Orders")

st.markdown("<br>", unsafe_allow_html=True)

# Chart Config (Responsive plot background with smooth transitions)
def apply_chart_style(fig):
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e2e8f0', family='Plus Jakarta Sans', size=12),
        margin=dict(l=20, r=20, t=30, b=20),
        colorway=['#38bdf8', '#a78bfa', '#f472b6', '#34d399', '#fbbf24'],
        transition=dict(duration=500, easing='cubic-in-out')
    )
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255,255,255,0.05)', tickfont=dict(color='#cbd5e1'))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255,255,255,0.05)', tickfont=dict(color='#cbd5e1'))
    return fig

# Row 1 Charts
c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="section-header">📈 Revenue Growth Trajectory</div>', unsafe_allow_html=True)
    if "Date" in filtered_df.columns and "Revenue" in filtered_df.columns:
        rev_trend = filtered_df.groupby("Date")["Revenue"].sum().reset_index()
        fig_line = px.area(rev_trend, x="Date", y="Revenue")
        fig_line.update_traces(line_color="#38bdf8", fillcolor="rgba(56, 189, 248, 0.2)")
        st.plotly_chart(apply_chart_style(fig_line), use_container_width=True)

with c2:
    st.markdown('<div class="section-header">🏆 Top Generating Products</div>', unsafe_allow_html=True)
    if "Product" in filtered_df.columns and "Revenue" in filtered_df.columns:
        prod_perf = filtered_df.groupby("Product")["Revenue"].sum().reset_index().sort_values(by="Revenue", ascending=True)
        fig_bar = px.bar(prod_perf, x="Revenue", y="Product", orientation="h", color="Revenue", color_continuous_scale="Viridis")
        st.plotly_chart(apply_chart_style(fig_bar), use_container_width=True)

# Row 2 Charts
c3, c4 = st.columns(2)

with c3:
    st.markdown('<div class="section-header">🍕 Revenue Distribution by Category</div>', unsafe_allow_html=True)
    if "Category" in filtered_df.columns and "Revenue" in filtered_df.columns:
        fig_pie = px.pie(filtered_df, names="Category", values="Revenue", hole=0.5)
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(apply_chart_style(fig_pie), use_container_width=True)

with c4:
    st.markdown('<div class="section-header">🌍 Regional Sales Concentration</div>', unsafe_allow_html=True)
    if "Region" in filtered_df.columns and "Revenue" in filtered_df.columns:
        region_perf = filtered_df.groupby("Region")["Revenue"].sum().reset_index()
        fig_region = px.bar(region_perf, x="Region", y="Revenue", color="Region")
        st.plotly_chart(apply_chart_style(fig_region), use_container_width=True)

# Data Table Expander
with st.expander("🔍 Inspect Processed Data Set"):
    st.dataframe(filtered_df)