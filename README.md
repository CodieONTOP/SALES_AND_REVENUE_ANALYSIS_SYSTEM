🚀 Sales & Revenue Intelligence Platform

A high-performance, visually stunning business analytics dashboard built using **Streamlit** and **Plotly**. Designed with a custom "Universe/Galaxy" glassmorphism theme and interactive mouse-tracking gradients, this tool transforms raw transactional datasets into dynamic, enterprise-grade revenue insights.

### ✨ Key Features
- **Dynamic Global Slicers:** Filter data seamlessly across product categories, regions, and custom time horizons.
- **Glassmorphism UI & Animations:** Custom CSS glass cards, smooth entrance keyframes, and fluid Plotly chart transitions.
- **High-Visibility KPIs:** Real-time metrics tracking Total Revenue, Units Sold, Average Order Value, and Total Volume.
- **Out-of-the-Box Execution:** Ships with a synthetic data generator script so reviewers can run and test the app immediately.
   
## 📊 Dataset & Ingestion Strategy
This application is designed with robust data ingestion flexibility, allowing it to adapt to various transactional schemas without missing a beat:

- **Out-of-the-Box Execution:** Ships with a built-in synthetic dataset generator (`generate_data.py`) that instantly provisions mock retail records (`sales_data.csv`) so reviewers can test the app immediately without configuration errors.
- **Custom Dataset Support:** Easily scalable to heavy, real-world data sources (such as automotive auction analytics). The app dynamically detects columns, parses complex date strings, and maps out key financial metrics.
- **Graceful Fallbacks:** If no custom file is uploaded via the sidebar ingestion panel, the app automatically defaults to local sample data while maintaining a clean, responsive interface.
