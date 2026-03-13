import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Журнали Муаллим", layout="wide")
st.title("📊 Журнал: Чорякҳо ва Солона")

columns = [
    "№", "Ному Насаб", 
    "1.Ҷорӣ", "1.Санҷиш", "Баҳои Ч1",
    "2.Ҷорӣ", "2.Санҷиш", "Баҳои Ч2",
    "🔵 Нимсолаи 1",
    "3.Ҷорӣ", "3.Санҷиш", "Баҳои Ч3",
    "4.Ҷорӣ", "4.Санҷиш", "Баҳои Ч4",
    "🔵 Нимсолаи 2",
    "🔴 БАҲОИ СОЛОНА"
]

if 'df' not in st.session_state:
    data = [["" for _ in columns] for _ in range(40)]
    for i in range(40):
        data[i][0] = str(i + 1)
    st.session_state.df = pd.DataFrame(data, columns=columns)

edited_df = st.data_editor(st.session_state.df, num_rows="dynamic", height=600)

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.close()
    return output.getvalue()

st.markdown("---")
excel_data = to_excel(edited_df)
st.download_button(
    label="📥 Боргирии ҷадвал (Excel)",
    data=excel_data,
    file_name="journal_maktab11.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

