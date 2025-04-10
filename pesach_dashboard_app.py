import streamlit as st
import pandas as pd
import plotly.express as px

# הגדרות עיצוב כלליות
st.set_page_config(page_title="מדד החירות בפסח", layout="wide")
st.markdown("""
    <style>
    body, .stApp {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# טאבים לדשבורד
tab1, tab2, tab3, tab4 = st.tabs(["📈 מדד החירות", "🧪 איזה בן דאטה אתה?", "🔥 מפת חום", "👥 על היוצרים"])

# טאב 1 – גרף מדד החירות
with tab1:
    events = [
        "שעבוד במצרים", "הולדת משה", "הסנה הבוער", "תחילת המכות",
        "מכת חושך", "מכת בכורות", "יציאה ממצרים", "קריעת ים סוף"
    ]
    freedom_level = [1, 2, 4, 5, 3, 6, 8, 10]
    funny_notes = [
        "עובדים בפרך + בלי וויפי",
        "נולד מושיע, אבל תינוק",
        "התחיל לקבל הוראות מהשיחים",
        "עשר מכות - מצב משתפר",
        "חושך? דאטה לא זורם",
        "פרעה נשבר - כמעט",
        "התחלנו ללכת... סוף סוף",
        "מים נבקעו – דאטה בשיא"
    ]
    chart_data = pd.DataFrame({"אירוע": events, "מדד חירות": freedom_level, "הערה": funny_notes})
    st.subheader("מדד החירות לאורך יציאת מצרים")
    fig = px.line(chart_data, x="אירוע", y="מדד חירות", text="הערה", markers=True)
    fig.update_traces(textposition="top center")
    fig.update_layout(
        yaxis_range=[0, 11],
        font=dict(family="Arial", size=14),
    )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander("📜 טיימליין - סיפור החירות בהומור"):
        for i in range(len(events)):
            st.markdown(f"**{events[i]}** – {funny_notes[i]}")

# טאב 2 – שאלון הבן הדאטאיסט
with tab2:
    st.subheader("🔍 איזה בן דאטה אתה?")
    st.markdown("ענה על כמה שאלות קצרות וגלֵה איזה טיפוס אנליטי מסתתר בך.")

    q1 = st.radio("כשאתה מקבל קובץ אקסל עם חוסרים בכל שורה:", [
        "אני כותב קוד שמנקה וממלא לפי מודל",
        "מה זה קשור אליי? שישלחו למישהו אחר",
        "למה יש Missing בכלל? זה באג?",
        "אני לא מצליח לפתוח את הקובץ בכלל"])

    q2 = st.radio("בפגישת דאטה, מה התגובה שלך?", [
        "שואל שאלות עומק ומבקש מקור נתונים",
        "מציע לזרוק הכל ולהתחיל מההרגשה שלי",
        "מופתע שיש פגישה בכלל",
        "מחייך ומחפש את הלינק לזום"])

    q3 = st.radio("איך אתה מרגיש לגבי דשבורדים?", [
        "כלי הכרחי – כמו ארבע כוסות",
        "מיותר. אני סומך על תחושות בטן",
        "עדיין לא מבין איך לוחצים שם על כפתורים",
        "חשבתי שזה מצגת"])

    if st.button("גלה מי אתה"):
        score = 0
        answers = [q1, q2, q3]
        for ans in answers:
            if "קוד" in ans or "שואל" in ans or "הכרחי" in ans:
                score += 2
            elif "מה זה קשור" in ans or "להתחיל מההרגשה" in ans or "מיותר" in ans:
                score += 0
            elif "למה יש" in ans or "מופתע" in ans or "עדיין לא מבין" in ans:
                score += 1
            else:
                score += 0.5

        if score >= 5:
            st.success("🧠 יצאת החכם – הדאטה אצלך בידיים טובות.")
        elif score >= 3:
            st.warning("😈 יצאת הרשע – אתה שואל שאלות, אבל רק אם זה משרת אותך.")
        elif score >= 1.5:
            st.info("🤔 יצאת התם – אתה מתעניין, אבל עוד קצת תרגול ותהיה מאסטר.")
        else:
            st.error("😶 יצאת שאינו יודע לשאול – אבל זה בסדר! נתחיל יחד מהבסיס.")

# טאב 3 – מפת חום של עשר המכות
with tab3:
    st.subheader("🔥 מפת חום: עשר המכות על דאטה, מצרים ו-BI")
    heat_data = pd.DataFrame({
        'מכה': ['דם', 'צפרדע', 'כינים', 'ערוב', 'דבר', 'שחין', 'ברד', 'ארבה', 'חושך', 'מכת בכורות'],
        'השפעה על המצרים': [9, 8, 6, 7, 9, 6, 10, 8, 4, 10],
        'השפעה על הדאטה': [2, 3, 1, 4, 2, 3, 8, 6, 10, 1],
        'כאב ל-BI': [3, 5, 1, 4, 5, 3, 9, 6, 10, 7]
    })
    selected_metric = st.selectbox("בחר מדד להצגה", ['השפעה על המצרים', 'השפעה על הדאטה', 'כאב ל-BI'])
    fig2 = px.imshow(
        heat_data[[selected_metric]].T,
        labels=dict(x="מכה", y="מדד", color="דרוג"),
        x=heat_data['מכה'],
        color_continuous_scale='Reds'
    )
    fig2.update_layout(title=f"מפת חום – {selected_metric}", font=dict(family="Arial", size=14))
    st.plotly_chart(fig2, use_container_width=True)

# טאב 4 – על היוצרים
with tab4:
    st.subheader("👥 מאחורי הקלעים")
    st.markdown("""
    **היוצרת:** Dana – מאמנת אוריינות דאטה, קוסמת של אינסייטים ומי שאחראית לכך שפסח השנה קיבל גרסת BI 😎

    **המוציא לפועל:** ChatGPT – רובוט צייתן עם חוש הומור בריא ואובססיה לדאטה סטים מוזרים מתקופת המקרא.

    **מאחורי הקלעים של השיחה:**
    > “מחכה במכת חושך” 🌑  
    > “עזוב, אני באנליסיס פרלסיס – קח שליטה במקומי”  
    > “אני חיה את החלום” ☁️✨

    זה הדשבורד הראשון שנכתב בצחוק, נבנה באהבה, ומוגש עם כף מרק של דאטה.  
    חג חירות שמח! 🥳
    """)