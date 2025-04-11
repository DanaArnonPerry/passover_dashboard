import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64
from PIL import Image
import io

st.set_page_config(page_title="מדד החירות בפסח", layout="wide")  

# פונקציה להמרת תמונה לbase64 לשימוש ב-HTML
def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# הגדרות עיצוב כלליות וטיפול ב-undefined
st.markdown("""
    <style>
    /* טעינת הגופן רוביק */
    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;500;700&display=swap');
    
    body, .stApp {
        direction: rtl;
        text-align: right;
        font-family: 'Rubik', sans-serif;
    }
    .main .block-container {
        padding-top: 1rem;
    }
    h1, h2, h3 {
        color: #8000FF;
        font-family: 'Rubik', sans-serif;
    }
    
    /* עיצוב כותרת וסידור עם לוגו בצד */
    .welcome-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-right: 5px solid #8000FF;
        margin-bottom: 20px;
    }

    .welcome-title-container {
        flex: 1;
    }

    .logo-right {
        margin-right: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .welcome-title {
        color: #8000FF;
        font-size: 24px;
        margin-bottom: 10px;
        font-family: 'Rubik', sans-serif;
    }
    
    .welcome-subtitle {
        color: #555;
        font-size: 16px;
        margin-bottom: 15px;
        font-family: 'Rubik', sans-serif;
    }
    
    /* עיצוב לשוניות (tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: #f6f6f6;
        border-radius: 10px;
        padding: 10px 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .stTabs [data-baseweb="tab"] {
        height: auto;
        white-space: pre-wrap;
        background-color: #f1f1f1;
        border-radius: 8px;
        padding: 10px 16px;
        font-family: 'Rubik', sans-serif;
        font-size: 16px;  /* גודל גופן גדול יותר */
        font-weight: 500;
        color: #333;
    }

    .stTabs [aria-selected="true"] {
        background-color: #8000FF !important;
        color: white !important;
    }
    
    .feature-card {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 15px;
        font-family: 'Rubik', sans-serif;
    }
    
    /* גישה אגרסיבית להסתרת undefined */
    .js-plotly-plot .plotly .g-gtitle,
    .js-plotly-plot text[data-unformatted="undefined"],
    text[data-unformatted="undefined"],
    div:empty,
    div:only-child:contains('undefined') {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        color: rgba(0,0,0,0) !important;
        fill: rgba(0,0,0,0) !important;
    }
    
    .gtitle, .fig-content text {
        visibility: hidden !important;
    }
    
    /* התאמות למסכים קטנים */
    @media (max-width: 768px) {
        .block-container {
            padding: 1rem 0.5rem !important;
            max-width: 100% !important;
        }
        
        .js-plotly-plot, .plotly, .plot-container {
            width: 100% !important;
            min-width: 100% !important;
            height: auto !important;
        }
        
        .js-plotly-plot .plotly text {
            font-size: 10px !important;
            font-family: 'Rubik', sans-serif !important;
        }
        
        .xtick text {
            text-overflow: ellipsis !important;
            max-width: 80px !important;
            font-family: 'Rubik', sans-serif !important;
        }
        
        .welcome-header {
            flex-direction: column-reverse;
        }
        
        .logo-right {
            margin-top: 20px;
            margin-right: 0;
        }
    }
    </style>
""", unsafe_allow_html=True)

# תכלית הקוד - להסתיר undefined בגרף 
st.markdown("""
    <script>
    const hideUndefined = function() {
        const allElements = document.querySelectorAll('*');
        allElements.forEach(function(element) {
            if (element.textContent === 'undefined') {
                element.style.display = 'none';
                element.style.visibility = 'hidden';
            }
            
            if (element.tagName === 'text' && element.textContent === 'undefined') {
                element.style.display = 'none';
                element.setAttribute('visibility', 'hidden');
            }
        });
    };
    
    setTimeout(hideUndefined, 500);
    setTimeout(hideUndefined, 1000);
    setTimeout(hideUndefined, 2000);
    </script>
    """, unsafe_allow_html=True)

# טאבים לדשבורד
tab0, tab1, tab2, tab3, tab4 = st.tabs(["🏠 ברוכים הבאים", "📈 מדד החירות", "🧪 איזה בן דאטה אתה?", "🎲 אפיקומן או סתם מצה", "👥 על היוצרים"])

# טאב 0 - פתיח וברכה
with tab0:
    # כותרת עם לוגו בצד שמאל
    st.markdown("""
    <div class="welcome-header">
        <div class="welcome-title-container">
            <h1 class="welcome-title">ברוכים הבאים לדשבורד מדד החירות !</h1>
            <p class="welcome-subtitle">מעבדות הנתונים לחירות הדאטה - חוגגים את יציאת מצרים בגרסת הדאטה סיינס</p>
        </div>
        <div class="logo-right">
            <img src="https://raw.githubusercontent.com/DanaArnonPerry/passover_dashboard/main/Logo.png" alt="לוגו" style="max-width:150px;">
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # הסבר על הדשבורד
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>מה יש בדשבורד?</h3>
            <ul>
                <li><b>מדד החירות</b> - עקבו אחר התפתחות החירות הדיגיטלית לאורך תהליך עבודה עם נתונים</li>
                <li><b>איזה בן דאטה אתה?</b> - גלו איזה טיפוס אנליטי אתם בעזרת שאלון קצר</li>
                <li><b>אפיקומן או סתם מצה?</b> - משחק קצר שיסייע לכם לגלות את האפיקומן בדאטה</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>חג חירות שמח! 🎉</h3>
            <p>הדשבורד הזה נוצר בהשראת חג הפסח, לחגוג את הדרך מעבדות הנתונים אל חירות הדאטה והתובנות.</p>
            <p>כמו בסיפור יציאת מצרים, גם בעולם הנתונים אנחנו עוברים מסע - מעבודה ידנית מייגעת ועד לאוטומציה ותובנות שמשנות את הארגון.</p>
            <p><i>מאחלים לכם פסח כשר ושמח, ועבודת דאטה נקייה מחמץ! 🌟</i></p>
        </div>
        """, unsafe_allow_html=True)
    
    # טיפים לשימוש - ללא הצגת הטאבים
    st.markdown("""
    <div class="feature-card">
        <h3>טיפים לשימוש בדשבורד</h3>
        <p>לחצו על הלשוניות למעלה כדי לנווט בין חלקי הדשבורד השונים.</p>
        <p>בגרף מדד החירות תוכלו לראות את שלבי המעבר מעבדות לחירות דיגיטלית, כשכל שלב מייצג נקודת מפנה בעבודה עם נתונים.</p>
    </div>
    """, unsafe_allow_html=True)

# טאב 1 – גרף מדד החירות
with tab1:
    # הסבר קצר לפני הגרף
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-family: 'Rubik', sans-serif;">
    <h3 style="margin-top: 0; font-family: 'Rubik', sans-serif;">מדד החירות לאורך יציאת מצרים - המסע מעבדות לחירות דיגיטלית</h3>
    <p style="font-family: 'Rubik', sans-serif;">הגרף הבא מציג את רמת החירות הדיגיטלית בכל שלב של עבודה עם נתונים, בהשוואה לשלבי יציאת מצרים המסורתית. 
    ככל שעולים בסולם, כך גדלה החירות מעבודה ידנית מייגעת לעבר אוטומציה משחררת.</p>
    </div>
    """, unsafe_allow_html=True)
    
    events = [
        "שעבוד במצרים", "הולדת משה", "הסנה הבוער", "תחילת המכות",
        "יציאה ממצרים", "קריעת ים סוף"
    ]
    
    freedom_level = [1, 2, 3, 1, 5, 8]
    
    funny_notes = [
        "מנקים אקסלים ידנית",
        "שומעים על פייתון",
        "קוד ראשון רץ בהצלחה",
        "מריצים סקריפטים עם ים דיבאגים",
        "בינה מלאכותית מנקה הכל",
        "מציגים להנהלה דשבורד מהחלומות"
    ]
    
    # שימוש בשמות מקוצרים לתוויות X במובייל
    shortened_events = {
        "שעבוד במצרים": "שעבוד",
        "הולדת משה": "משה", 
        "הסנה הבוער": "הסנה",
        "תחילת המכות": "המכות", 
        "יציאה ממצרים": "יציאה",
        "קריעת ים סוף": "קריעה"
    }
    
    # יצירת DataFrame
    chart_data = pd.DataFrame({"אירוע": events, "מדד חירות": freedom_level, "הערה": funny_notes})
    
    # יצירת עותק עם שמות מקוצרים למובייל
    mobile_chart_data = chart_data.copy()
    mobile_chart_data["אירוע"] = mobile_chart_data["אירוע"].map(lambda x: shortened_events.get(x, x))
    
    # יצירת גרף קבוע (לא רספונסיבי) לטלפון נייד
    fig = go.Figure()
    
    # הוספת הקו והנקודות
    fig.add_trace(go.Scatter(
        x=events,
        y=freedom_level,
        mode='lines+markers',
        line=dict(width=4, color='#000000', dash='solid', shape='spline', smoothing=1.3),
        marker=dict(size=12, symbol='circle', line=dict(width=2, color='#000000'))
    ))
    
    # הוספת אזורים מוצללים לרמות חירות
    fig.add_hrect(
        y0=0, y1=3, 
        fillcolor="rgba(255,0,0,0.07)", 
        layer="below", 
        line_width=0,
        annotation_text="אזור שעבוד",
        annotation_position="bottom right",
        annotation_font=dict(size=12, color="darkred", family="Rubik, sans-serif")
    )
    
    fig.add_hrect(
        y0=3, y1=7, 
        fillcolor="rgba(255,165,0,0.07)", 
        layer="below", 
        line_width=0,
        annotation_text="אזור מעבר",
        annotation_position="bottom right",
        annotation_font=dict(size=12, color="darkorange", family="Rubik, sans-serif")
    )
    
    fig.add_hrect(
        y0=7, y1=11, 
        fillcolor="rgba(0,128,0,0.07)", 
        layer="below", 
        line_width=0,
        annotation_text="אזור חירות",
        annotation_position="bottom right",
        annotation_font=dict(size=12, color="darkgreen", family="Rubik, sans-serif")
    )
    
    # הוספת annotations מותאמות אישית לכל נקודה
    for i, row in chart_data.iterrows():
        # ביצוע טקסט קצר יותר למובייל
        short_text = row["הערה"].split('.')[0] + '.' if '.' in row["הערה"] else row["הערה"]
        
        fig.add_annotation(
            x=row["אירוע"],
            y=row["מדד חירות"],
            text=short_text,
            showarrow=False,
            yshift=50,
            font=dict(
                family="Rubik, sans-serif",  # שינוי לגופן רוביק
                size=13, 
                color="#333333",
                weight="bold"
            ),           
            borderpad=4,
            align="center"
        )
    
    # עיצוב כללי של הגרף
    fig.update_layout(
        title=None,
        showlegend=False,
        plot_bgcolor='rgba(240,248,255,0.3)',
        paper_bgcolor='white',
        font=dict(family="Rubik, sans-serif", size=14, color="#505050"),  # הגדרת גופן כללית
        xaxis=dict(
            title="שלבי יציאת מצרים",  # הוספת כותרת לציר X
            title_font=dict(size=16, color="#8000FF", family="Rubik, sans-serif"),
            tickfont=dict(size=14, color="#333333", family="Rubik, sans-serif"),
            gridcolor='rgba(200,200,200,0.2)',
            zeroline=False,
            tickangle=-45,
        ),
        yaxis=dict(
            title="מדד החירות הדיגיטלי",
            title_font=dict(size=16, color="#8000FF", family="Rubik, sans-serif"),
            tickfont=dict(size=14, color="#333333", family="Rubik, sans-serif"),
            gridcolor='rgba(200,200,200,0.5)',
            zeroline=False,
            range=[0, 11]
        ),
        margin=dict(l=10, r=10, t=30, b=50),
        height=550,  # גובה קבוע במקום רספונסיבי
        width=800,   # רוחב קבוע במקום רספונסיבי
        autosize=False,  # ביטול הגודל האוטומטי
    )
    
    # הצגת הגרף עם הגדרות לא רספונסיביות
    st.plotly_chart(fig, config={
        'displayModeBar': False,
        'responsive': False,  # ביטול רספונסיביות
        'staticPlot': True   # הפיכה לתמונה סטטית לחלוטין
    })
    
    # הסבר נוסף אחרי הגרף
    st.markdown("""
    <div style="background-color: rgba(240,248,255,0.5); padding: 15px; border-radius: 5px; border-right: 4px solid #8000FF; margin-top: 20px; font-family: 'Rubik', sans-serif;">
    <h4 style="color: #8000FF; margin-top: 0; font-family: 'Rubik', sans-serif;">המסע מעבדות לחירות בעולם הדאטה</h4>
    <p style="font-family: 'Rubik', sans-serif;">כפי שניתן לראות בגרף, האנליסט מתחיל את דרכו בעבודה ידנית מפרכת עם אקסלים, ממש כמו עבודת פרך במצרים.
    דרך תהליך אוטומציה הדרגתי, הוא עובר את ים הדיבאגים, עד שמגיע לחירות מלאה עם דשבורדים אוטומטיים ותובנות שמשנות את הארגון.</p>
    </div>
    """, unsafe_allow_html=True)

# טאב 2 – שאלון הבן הדאטאיסט
with tab2:
    st.markdown("<h3 style='font-family: Rubik, sans-serif;'>🔍 איזה בן דאטה אתה?</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-family: Rubik, sans-serif;'>ענה על כמה שאלות קצרות וגלֵה איזה טיפוס אנליטי מסתתר בך.</p>", unsafe_allow_html=True)

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
        "נחמד אבל overrated",
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
            st.markdown("<div style='font-family:
