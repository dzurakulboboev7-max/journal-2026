import streamlit as st
import pandas as pd

st.set_page_config(page_title="Журнали Рақамӣ", layout="wide")
st.title("📊 Журнал: Чорякҳо, Нимсола ва Солона")

columns = [
    "№", "Ному Насаб", 
    "1.Ҷорӣ (Ч1)", "1.Санҷиш (Ч1)", "Баҳои Ч1",
    "2.Ҷорӣ (Ч2)", "2.Санҷиш (Ч2)", "Баҳои Ч2",
    "🔵 Нимсолаи 1",
    "3.Ҷорӣ (Ч3)", "3.Санҷиш (Ч3)", "Баҳои Ч3",
    "4.Ҷорӣ (Ч4)", "4.Санҷиш (Ч4)", "Баҳои Ч4",
    "🔵 Нимсолаи 2",
    "🔴 БАҲОИ СОЛОНА"
]

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame([
        {col: "" if col == "Ному Насаб" or "Ҷорӣ" in col else 0 for col in columns} 
        for i in range(1, 41)
    ])
    for i in range(40):
        st.session_state.df.at[i, "№"] = i + 1

edited_df = st.data_editor(st.session_state.df, use_container_width=True, height=600)

def calc_q(current, exam):
    try:
        marks = [float(m) for m in str(current).replace(" ", "").split(",") if m.strip()]
        if not marks: return 0
        avg = sum(marks) / len(marks)
        return int((avg + float(exam)) / 2 + 0.5)
    except: return 0

if st.button("🚀 ҲИСОБ КАРДАНИ ҲАМАИ НАТИҶАҲО"):
    for i, row in edited_df.iterrows():
        q1 = calc_q(row["1.Ҷорӣ (Ч1)"], row["1.Санҷиш (Ч1)"])
        q2 = calc_q(row["2.Ҷорӣ (Ч2)"], row["2.Санҷиш (Ч2)"])
        q3 = calc_q(row["3.Ҷорӣ (Ч3)"], row["3.Санҷиш (Ч3)"])
        q4 = calc_q(row["4.Ҷорӣ (Ч4)"], row["4.Санҷиш (Ч4)"])
        
        edited_df.at[i, "Баҳои Ч1"] = q1
        edited_df.at[i, "Баҳои Ч2"] = q2
        edited_df.at[i, "Баҳои Ч3"] = q3
        edited_df.at[i, "Баҳои Ч4"] = q4
        
        h1 = int((q1 + q2) / 2 + 0.5) if (q1 + q2) > 0 else 0
        h2 = int((q3 + q4) / 2 + 0.5) if (q3 + q4) > 0 else 0
        
        edited_df.at[i, "🔵 Нимсолаи 1"] = h1
        edited_df.at[i, "🔵 Нимсолаи 2"] = h2
        edited_df.at[i, "🔴 БАҲОИ СОЛОНА"] = int((h1 + h2) / 2 + 0.5) if (h1 + h2) > 0 else 0

    st.session_state.df = edited_df
    st.rerun()
