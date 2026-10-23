import streamlit as st
import pandas as pd

st.set_page_config(page_title="Carpentry Workshop Log", page_icon="🪚", layout="wide")

st.title("🪚 Carpentry Workshop Daily Production Log")
st.write("Record daily production and automatically calculate workshop totals and averages.")

if "records" not in st.session_state:
    st.session_state.records = [
        {"Day": "Monday", "Chairs": 8, "Timber (m)": 24.0, "Nails (kg)": 3.0, "Paint (L)": 2.0},
        {"Day": "Tuesday", "Chairs": 6, "Timber (m)": 18.0, "Nails (kg)": 2.5, "Paint (L)": 1.3},
        {"Day": "Wednesday", "Chairs": 10, "Timber (m)": 18.0, "Nails (kg)": 3.0, "Paint (L)": 2.2},
        {"Day": "Thursday", "Chairs": 7, "Timber (m)": 21.0, "Nails (kg)": 2.0, "Paint (L)": 2.5},
        {"Day": "Friday", "Chairs": 9, "Timber (m)": 27.0, "Nails (kg)": 3.1, "Paint (L)": 3.0},
        {"Day": "Saturday", "Chairs": 6, "Timber (m)": 19.0, "Nails (kg)": 4.0, "Paint (L)": 2.7},
    ]

st.subheader("➕ Add a new production record")

with st.form("production_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        day = st.selectbox("Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        chairs = st.number_input("Chairs made", min_value=0, step=1)
    with col2:
        timber = st.number_input("Timber used (m)", min_value=0.0, step=0.1, format="%.1f")
        nails = st.number_input("Nails used (kg)", min_value=0.0, step=0.1, format="%.1f")
    with col3:
        paint = st.number_input("Paint used (L)", min_value=0.0, step=0.1, format="%.1f")
        submitted = st.form_submit_button("Add Record", use_container_width=True)

    if submitted:
        st.session_state.records.append({
            "Day": day,
            "Chairs": int(chairs),
            "Timber (m)": float(timber),
            "Nails (kg)": float(nails),
            "Paint (L)": float(paint)
        })
        st.success(f"{day} record added successfully.")

df = pd.DataFrame(st.session_state.records)

st.subheader("📋 Daily production")
st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("📊 Workshop Summary")

total_chairs = int(df["Chairs"].sum())
total_timber = df["Timber (m)"].sum()
total_nails = df["Nails (kg)"].sum()
total_paint = df["Paint (L)"].sum()
days = len(df)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Chairs", total_chairs)
m2.metric("Timber Used", f"{total_timber:.1f} m")
m3.metric("Nails Used", f"{total_nails:.1f} kg")
m4.metric("Paint Used", f"{total_paint:.1f} L")

m5, m6 = st.columns(2)
m5.metric("Average Chairs / Day", f"{total_chairs / days:.1f}" if days else "0.0")
m6.metric("Average Nails / Day", f"{total_nails / days:.1f} kg" if days else "0.0")

st.subheader("📈 Production Chart")
chart_df = df.set_index("Day")[["Chairs"]]
st.bar_chart(chart_df)

csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    "⬇️ Download Production Records (CSV)",
    data=csv,
    file_name="carpentry_workshop_log.csv",
    mime="text/csv"
)

if st.button("🗑️ Reset to Original Sample Data"):
    st.session_state.records = [
        {"Day": "Monday", "Chairs": 8, "Timber (m)": 24.0, "Nails (kg)": 3.0, "Paint (L)": 2.0},
        {"Day": "Tuesday", "Chairs": 6, "Timber (m)": 18.0, "Nails (kg)": 2.5, "Paint (L)": 1.3},
        {"Day": "Wednesday", "Chairs": 10, "Timber (m)": 18.0, "Nails (kg)": 3.0, "Paint (L)": 2.2},
        {"Day": "Thursday", "Chairs": 7, "Timber (m)": 21.0, "Nails (kg)": 2.0, "Paint (L)": 2.5},
        {"Day": "Friday", "Chairs": 9, "Timber (m)": 27.0, "Nails (kg)": 3.1, "Paint (L)": 3.0},
        {"Day": "Saturday", "Chairs": 6, "Timber (m)": 19.0, "Nails (kg)": 4.0, "Paint (L)": 2.7},
    ]
    st.rerun()
