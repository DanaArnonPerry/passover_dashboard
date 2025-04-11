import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="מדד החירות בפסח", layout="wide")  

# הגדרות עיצוב כלליות וטיפול ב-undefined
st.markdown("""
    <style>
    body, .stApp {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif;
    }
    .main .block-container {
        padding-top: 2rem;
    }
    h1, h2, h3 {
        color: #1E4B7A;
    }
    /* הסתרת אלמנטים שמכילים רק את הטקסט 'undefined' */
    *:empty, *:only-child:contains('undefined') {
        display: none !important;
    }
    /* צביעת הטקסט 'undefined' בלבן כדי להסתירו */
    *:contains('undefined') {
        color: white !important;
    }
    </style>
    
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        // פונקציה להסרת אלמנטים עם הטקסט 'undefined'
        const removeUndefined = () => {
            const walker = document.createTreeWalker(
                document.body, 
                NodeFilter.SHOW_TEXT, 
                null, 
                false
            );
            let node;
            while (node = walker.nextNode()) {
                if (node.nodeValue.trim() === 'undefined') {
                    if (node.parentNode) {
                        node.parentNode.style.color = 'white';  // צביעה בלבן
                    }
                }
            }
        }
        // הפעלה מיידית ושוב אחרי רגע להתמודד עם תוכן דינמי
        setTimeout(removeUndefined, 100);
        setTimeout(removeUndefined, 1000);
    });
    </script>
""", unsafe_allow_html=True)

# טאבים לדשבורד
tab1, tab2, tab3, tab4 = st.tabs(["📈 מדד החירות", "🧪 איזה בן דאטה אתה?", "🎲 אפיקומן או סתם מצה", "👥 על היוצרים"])

# טאב 1 – גרף מדד החירות
with tab1:
    events = [
        "שעבוד במצרים", "הולדת משה", "הסנה הבוער", "תחילת המכות",
        "יציאה ממצרים", "קריעת ים סוף"
    ]
    freedom_level = [1, 2, 3, 1, 6, 10]
    funny_notes = [
        "מנקים אקסלים ידנית. אין סוף לעבדות.",
        "שומעים על פייתון. יש תקווה.",
        "קוד ראשון רץ בהצלחה. הנס מתגלה.",
        "מריצים סקריפטים. דיבאגים אינסופיים.",
        "בינה מלאכותית מנקה הכל. בשניות.",  # שינוי מ-AI לבינה מלאכותית
        "מציגים להנהלה דשבורד מהחלומות."
    ]

    chart_data = pd.DataFrame({"אירוע": events, "מדד חירות": freedom_level, "הערה": funny_notes})
    st.subheader("מדד החירות לאורך יציאת מצרים")
    
    # יצירת גרף בסיסי - בלי טקסט על הקו עצמו
    fig = px.line(chart_data, x="אירוע", y="מדד חירות", markers=True)
    
    # עיצוב קו הגרף והסמנים
    fig.update_traces(
        line=dict(width=4, color='#1f77b4', dash='solid'),
        marker=dict(size=12, symbol='circle', line=dict(width=2, color='darkblue')),
        text=None  # מוודאים שאין טקסט על הקו
    )
    
    # הוספת annotations מותאמות אישית לכל נקודה
    for i, row in chart_data.iterrows():
        fig.add_annotation(
            x=row["אירוע"],
            y=row["מדד חירות"],
            text=row["הערה"],
            showarrow=False,
            yshift=15,  # התאמת המיקום מעל הנקודה
            font=dict(family="Arial", size=13, color="#333333"),
            bgcolor="rgba(255, 255, 255, 0.8)",
            bordercolor="#DDDDDD",
            borderwidth=1,
            borderpad=4,
            align="center"
        )
    
    # עיצוב כללי של הגרף
    fig.update_layout(
        yaxis_range=[0, 11],
        font=dict(family="Arial", size=14, color="#505050"),
        title=None,  # מסירים כותרת
        showlegend=False,  # ביטול הצגת מקרא (legend)
        title_font=dict(size=24, family="Arial", color="darkblue"),
        plot_bgcolor='rgba(240,248,255,0.3)',  # רקע תכלת בהיר מאוד
        paper_bgcolor='white',
        xaxis=dict(
            title="שלבי יציאת מצרים",
            title_font=dict(size=16, color="#1E4B7A"),
            tickfont=dict(size=14, color="#333333", family="Arial"),
            gridcolor='rgba(200,200,200,0.2)',
            zeroline=False
        ),
        yaxis=dict(
            title="מדד החירות הדיגיטלי",
            title_font=dict(size=16, color="#1E4B7A"),
            tickfont=dict(size=14, color="#333333", family="Arial"),
            gridcolor='rgba(200,200,200,0.5)',
            zeroline=False
        ),
        margin=dict(l=20, r=20, t=40, b=80),
        hovermode="x unified",
        legend_title_font_color="#1E4B7A"
    )
    
    # הוספת אזורים מוצללים לפי רמות החירות
    fig.add_hrect(
        y0=0, y1=3, 
        fillcolor="rgba(255,0,0,0.07)", 
        layer="below", 
        line_width=0,
        annotation_text="אזור שעבוד",
        annotation_position="bottom right",
        annotation_font=dict(size=12, color="darkred")
    )
    
    fig.add_hrect(
        y0=3, y1=7, 
        fillcolor="rgba(255,165,0,0.07)", 
        layer="below", 
        line_width=0,
        annotation_text="אזור מעבר",
        annotation_position="bottom right",
        annotation_font=dict(size=12, color="darkorange")
    )
    
    fig.add_hrect(
        y0=7, y1=11, 
        fillcolor="rgba(0,128,0,0.07)", 
        layer="below", 
        line_width=0,
        annotation_text="אזור חירות",
        annotation_position="bottom right",
        annotation_font=dict(size=12, color="darkgreen")
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div style="background-color: rgba(240,248,255,0.5); padding: 10px; border-radius: 5px; border-left: 4px solid #1E4B7A; margin-top: 20px;">
    <h4 style="color: #1E4B7A;">מסע הדאטה לחירות</h4>
    <p>הגרף מציג את התפתחות רמת החירות הדיגיטלית בתהליך עבודה עם דאטה, מקביל לשלבי יציאת מצרים.</p>
    </div>
    """, unsafe_allow_html=True)

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
    st.markdown("בחרי בכל שלב : אפיקומן או סתם מצה. האם תמצאי את האפיקומן?")
    step = st.radio("שלב ראשון: מגיע אלייך דאטה מהפרויקט.", ["בודקת קודם מה יש בפנים (אפיקומן)", "הולכת ישר לאנליזה (סתם מצה)"])
    if step == "בודקת קודם מה יש בפנים (אפיקומן)":
        step2 = st.radio("שלב שני: יש מלא עמודות חסרות.", ["מתחילה לנקות ולתעד (אפיקומן)", "זה בטח סתם – ממשיכה ככה (סתם דאטה)"])
        if step2 == "מתחילה לנקות ולתעד (אפיקומן)":
            st.success("🎉 יצאת דאטה חכמה – אפילו פרעה היה גאה בך")
        else:
            st.warning("עוד מאמץ קטן ואת בדרך למצוא אפיקומן")
    else:
        st.info("🤷‍♀️ יצאת מאמינה – אבל בלי דאטה ... תנסי שוב!")

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
