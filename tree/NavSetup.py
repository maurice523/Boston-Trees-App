import streamlit as st

# --- PAGE SETUP ---

overview_page = st.Page(
    page="views/overview.py",
    title="Overview of the Trees",
    icon="📊",
    default=True
)

q1_page = st.Page(
    page="views/q1_growth_over_time.py",
    title="Growth Over Time",
    icon="⏳"
)

q2_page = st.Page(
    page="views/q2_species_neighborhood.py",
    title="Species in a Neighborhood",
    icon="🌿"
)

q3_page = st.Page(
    page="views/q3_average_size.py",
    title="Average Tree Size by Neighborhood",
    icon="📏"
)

q4_page = st.Page(
    page="views/q4_rare_species.py",
    title="Rare Species",
    icon="🧬"
)

# --- NAVIGATION ---
pg = st.navigation(
    {
        "Boston Trees Project": [
            overview_page,
            q1_page,
            q2_page,
            q3_page,
            q4_page,
        ]
    }
)

# --- RUN NAV ---
pg.run()