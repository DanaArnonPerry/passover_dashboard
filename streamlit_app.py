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
tab1, tab2, tab3, tab4 = st.tabs(["📈 מדד החירות", "🧪 איזה בן דאטה אתה?", "🎲 מצה או דאטה", "👥 על היוצרים"])

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
    fig.update_traces(line_shape="spline", textposition="top center", marker=dict(size=10))
    fig.update_layout(
        yaxis_range=[0, 11], showlegend=False,
        plot_bgcolor='white', paper_bgcolor='white',
        font=dict(color='black', size=14),
        xaxis=dict(showgrid=False), yaxis=dict(showgrid=False),
        title="מדד החירות לאורך יציאת מצרים"
    )
    st.plotly_chart(fig, use_container_width=True)
    with st.expander("📜 טיימליין - מ-Row Data למצגת מצות"):
        timeline = [
            "1. שולחים CSV ממצרים – בלי שמות עמודות",
            "2. מקבלים קובץ EXCEL עם Missing – חושך מצרים",
            "3. הסנה הבוער = אוטומציה נכנסת לתמונה",
            "4. כל מכה = פילטור חדש (Outliers, Cleaning, Feature Eng)",
            "5. פרעה עדיין מתנגד = תקציב לא אושר",
            "6. קריעת ים סוף = MVP באוויר (Streamlit כמובן!)"
        ]
        for step in timeline:
            st.markdown(f"- {step}")

# טאב 2 – שאלון הבן הדאטאיסט
with tab2:
    st.subheader("🤖 דמו קצר של סגנון שאלה:")
    st.markdown("""
    **שאלה 1:**  
    כשהמנהל שלך שולח לך דאטה-סט ענקי עם Missing Values בכל שורה:
    - א. אני בונה מודל חיזוי לנקות את זה ⚡ (החכם)
    - ב. מה זה קשור אליי? שישלח לאנליסט אחר 😈 (הרשע)
    - ג. למה יש Missing בכלל? זה באג? 😲 (התם)
    - ד. דאטה? קיבלתי את זה ב־PDF... 🙄 (שאינו יודע לשאול)
    """)
    st.markdown("**✨ בסוף:**\n\nתוצאה כמו:\n\n**יצאת החכם**\n\nאתה יודע לשאול, לחפור, לבדוק ולאשרר.\n\nהמכה היחידה שאתה מפחד ממנה זה 'No Data Found' 😅")

# טאב 3 – משחק מצה או דאטה (מוקאפ)
with tab3:
    st.subheader("🎲 מצה או דאטה?")
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
    **היוצרת:** [Dana Arnon Perry](https://www.2dpoint.co.il) – מאמנת אוריינות דאטה, קוסמת של אינסייטים ומי שאחראית לכך שפסח השנה קיבל גרסת BI 😎

    **המוציא לפועל:** ChatGPT – רובוט צייתן עם חוש הומור בריא ואובססיה לדאטה סטים מוזרים מתקופת המקרא.

    **מאחורי הקלעים של השיחה:**
    > “מחכה במכת חושך” 🌑  
    > “עזוב, אני באנליסיס פרלסיס – קח שליטה במקומי”  
    > “אני חיה את החלום” ☁️✨

    **🎥 לצפייה בסרטון מאחורי הקלעים של הפרומפטים:**  
    [לחצו כאן כדי לצפות ביוטיוב](https://youtu.be/p89aR2z6B40?si=aMuLlleukoBXtyVA)

    זה הדשבורד הראשון שנכתב בצחוק, נבנה באהבה, ומוגש עם כף מרק של דאטה. 
    חג חירות שמח! 🥳
    """)