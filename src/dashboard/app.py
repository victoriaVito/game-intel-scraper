"""
EoC Streamlit dashboard entry point.
All visualized data is English-only & store-validated.
"""
import streamlit as st
from src.dashboard.charts import (
    top_games_chart, competitor_ranking_chart, update_frequency_chart, levels_per_patch_chart,
    verification_pie_chart, store_comparison_diff_chart, trendline_chart
)

st.title("EoC Game Intelligence Dashboard")

st.markdown("View top games, verified updates, and competitor trends—all based on validated, official data.")

tab1, tab2, tab3, tab4 = st.tabs(["Top Games", "Competitors", "Update Frequency", "Trends"])
with tab1:
    st.plotly_chart(top_games_chart())
with tab2:
    st.plotly_chart(competitor_ranking_chart())
with tab3:
    st.plotly_chart(update_frequency_chart())
    st.plotly_chart(levels_per_patch_chart())
with tab4:
    st.plotly_chart(verification_pie_chart())
    st.plotly_chart(store_comparison_diff_chart())
    st.plotly_chart(trendline_chart())