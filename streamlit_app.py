import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="מדד החירות בפסח", layout="wide")  

# הגדרות עיצוב כלליות
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
tab1, tab2, tab3, tab4 = st.tabs(["📈 מדד החירות", "🧪 איזה בן דאטה אתה?", "🎲 מצה או דאטה", "👥 על היוצרים"])

# טאב 1 – גרף מדד החירות
with tab1:
    events = [
        "שעבוד במצרים", "הולדת משה", "הסנה הבוער", "תחילת המכות",
        "יציאה ממצרים", "קריעת ים סוף"
    ]
    freedom_level = [1, 2, 3, 1, 6, 10]
    funny_notes = [
   timeline = [
    "מנקים אקסלים ידנית. אין סוף לעבדות.",
    "שומעים על פייתון. יש תקווה.",
    "קוד ראשון רץ בהצלחה. הנס מתגלה.",
    "מריצים סקריפטים. דיבאגים אינסופיים.",
    "AI מנקה הכל. בשניות.",
    "מציגים להנהלה דשבורד מהחלומות."
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

# טאב 2 – שאלון הבן הדאטאיסט
with tab2:
    st.subheader("🔍 איזה בן דאטה אתה?")
    st.markdown("ענה על כמה שאלות קצרות וגלֵה איזה טיפוס אנליטי מסתתר בך.")

    q1 = st.radio("כשאתה מקבל דאטה-סט ענקי אקסל עם Missing Values:", [
        "אני כותב קוד שישלים את כל החוסרים",
        "מה זה קשור אליי? שישלח לאנליסט אחר",
        "למה יש Missing בכלל? זה באג?",
        "משהו לא נראה תקין בדאטה אבל אני לא בטוח מה"])

    q2 = st.radio("בפגישת דאטה, מה התגובה שלך?", [
        "שואל שאלות עומק ומבקש מקור נתונים",
        "מציע להתעלם מהדאטה כי אין כמו אינטואיציה טובה",
        "מופתע שיש פגישה בכלל",
        "מחייך ומתעלם, גם ככה אף אחד לא מבין שום דבר"])

    q3 = st.radio("איך אתה מרגיש לגבי דשבורדים?", [
        "אהבה בלב",
        "נחמד אבל  overrated",
        "עדיין מנסה להבין את הקטע של הסלייסרים",
        "חשבתי שזו בכלל מצגת"])

    if st.button("גלה מי אתה או את"):
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
            st.success("🧠 יצאת החכם – הדאטה אצלך בידיים טובות. אתה יודע לשאול, לבדוק ולבנות דשבורדים בזמן שכולם עוד שואלים מה זה KPI.")
        elif score >= 3:
            st.warning("😈 יצאת הרשע – אתה שואל שאלות, אבל רק אם זה משרת אותך. בוא נגיד שדאטה קיים, אבל אתה מעדיף אינטואיציה.")
        elif score >= 1.5:
            st.info("🤔 יצאת התם – אתה מתעניין, אבל עוד קצת תרגול ותהיה מאסטר של דאטה. תמשיך לשאול!")
        else:
            st.error("😶 יצאת שאינו יודע לשאול – אבל זה בסדר! כל דאטה-אנליסט מתחיל ככה. נתחיל מהבנת סוגי גרפים ונמשיך משם!")

# טאב 3 – משחק אפיקומן או סתם מצה (מוקאפ)
with tab3:
    st.subheader("🎲 אפיקומן או סתם מצה?")
    st.markdown("בחרי בכל שלב איך להמשיך: באמונה או בנתונים. מה יצא לך בסוף?")
    step = st.radio("שלב ראשון: מגיע אלייך דאטה מהפרויקט.", ["בודקת קודם מה יש בפנים (דאטה)", "זורמת עם האינטואיציה שלי (מצה)"])
    if step == "בודקת קודם מה יש בפנים (דאטה)":
        step2 = st.radio("שלב שני: יש מלא עמודות חסרות.", ["מתחילה לנקות ולתעד (דאטה)", "זה בטח סתם – ממשיכה ככה (מצה)"])
        if step2 == "מתחילה לנקות ולתעד (דאטה)":
            st.success("🎉 יצאת דאטה חכמה – אפילו פרעה היה גאה בך")
        else:
            st.warning("🤷‍♀️ יצאת מאמינה – אבל המסר לא עבר... תנסי שוב!")
    else:
        st.info("😇 יצאת עם לב של זהב... אבל בלי תובנות")

# טאב 4 – על היוצרים
with tab4:
    st.subheader("👥 מאחורי הקלעים")
    st.markdown("""
    **היוצרת:** [Dana Arnon Perry](https://www.2dpoint.co.il) –  מלמדת אוריינות דאטה, קוסמת של אינסייטים ומי שאחראית לכך שפסח השנה קיבל גרסת BI 😎

    **המוציא לפועל:** ChatGPT – רובוט צייתן עם חוש הומור בריא ואובססיה לדאטה סטים מוזרים מתקופת המקרא.

    **מאחורי הקלעים של השיחה:**
    > "מחכה במכת חושך" 🌑  
    > "עזוב, אני באנליסיס פרלסיס – קח שליטה במקומי"  
    > "אני חיה את החלום" ☁️✨

    **🎥 לצפייה בסרטון מאחורי הקלעים של הפרומפטים:**  
    [לחצו כאן כדי לצפות ביוטיוב](https://youtu.be/p89aR2z6B40?si=aMuLlleukoBXtyVA)

    זה הדשבורד הראשון שנכתב בצחוק, נבנה באהבה, ומוגש עם כף מרק של דאטה. 
    חג חירות שמח! 🥳
    """)
