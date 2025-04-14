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
    
    /* עיצוב לכרטיסיית הפתיח */
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
    
    .logo-right {
        margin-right: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .logo-container {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    
    .feature-card {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
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
        }
        
        .xtick text {
            text-overflow: ellipsis !important;
            max-width: 80px !important;
        }
        
        .welcome-header {
            flex-direction: column;
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
tab0, tab1, tab2, tab3, tab4 = st.tabs([" ברוכים הבאים", "📈 מדד החירות", " איזה בן דאטה אתה?", " אפיקומן או סתם מצה", "👥 על היוצרים"])

# טאב 0 - פתיח וברכה
with tab0:
    st.markdown("""
    <div class="welcome-header">
        <div class="welcome-title-container">
            <h1 class="welcome-title">ברוכים הבאים לדשבורד מדד החירות !</h1>
            <p>לחצו על הלשוניות למעלה כדי לנווט בין חלקי הדשבורד השונים.</p>
            <div class="github-info">
                <h4 style="margin-top: 20px; color: #8000FF;">יוצרי הדשבורד</h4>
                <p><b>על הרעיון:</b> Dana Arnon Perry – מלמדת אוריינות נתונים, חוקרת קוגניטיבית ומי שאחראית לכך שפסח השנה קיבל גרסת BI עם AI 😎</p>
                <p><b>המוציא לפועל:</b> ChatGPT – רובוט צייתן עם חוש הומור בריא ואובססיה לדאטה סטים מוזרים מתקופת המקרא.</p>
                <p><b>דאטה סטוריטלר:</b> Claude – אחראי על שדרוג הקוד והמראה של הדשבורד ותכל'ס הייתי צריך לעשות את רוב העבודה בסוף (רק אומר).</p>
                <p><b>לפרטים נוספים וקישור להורדת הקוד, גללו ללשונית "👥 על היוצרים"</b></p>
            </div> 
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
            <h3>חג חירות שמח! 🎉</h3>
            <p>הדשבורד הזה נוצר בהשראת חג הפסח, לחגוג את הדרך מעבדות הנתונים אל חירות הדאטה והתובנות.</p>
            <p>כמו בסיפור יציאת מצרים, גם בעולם הנתונים אנחנו עוברים מסע - מעבודה ידנית מייגעת ועד לאוטומציה ותובנות שמשנות את הארגון.</p>
            <p><i>מאחלים לכם פסח כשר ושמח, ועבודת דאטה נקייה מחמץ! 🌟</i></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
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

       
# טאב 1 – גרף מדד החירות בסגנון פשוט
with tab1:
    # הסבר קצר לפני הגרף
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-family: 'Rubik', sans-serif;">
    <h3 style="margin-top: 0; font-family: 'Rubik', sans-serif;">מדד החירות הדיגיטלית: המסע מעבדות לחירות</h3>
    <p style="font-family: 'Rubik', sans-serif;">הגרף הבא מציג את רמת החירות הדיגיטלית בכל שלב של עבודה עם נתונים, בהשוואה לשלבי יציאת מצרים.
    לחצו על הנקודות בגרף כדי לגלות פרטים נוספים על כל שלב במסע!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # נתונים למדד החירות - מסתכל יותר כמו בתמונה שהצגת
    events = [
        "שעבוד במצרים",
        "הולדת משה", 
        "הסנה הבוער", 
        "תחילת המכות",
        "יציאה ממצרים", 
        "קריעת ים סוף",
        "הארץ המובטחת"
    ]
    
    freedom_level = [1, 2, 3, 1, 5, 8, 10]
    
    funny_notes = [
        "מנקים אקסלים ידנית ומעתיקים נתונים בלי סוף",
        "שומעים על פייתון ולומדים שיש חיים אחרי אקסל",
        "קוד ראשון רץ בהצלחה! תחושת חירות ראשונית",
        "מריצים סקריפטים אבל נתקעים בים של דיבאגים",
        "בינה מלאכותית מנקה ומעבדת את הכל אוטומטית",
        "יוצרים דשבורדים ותובנות מתקדמות מהנתונים",
        "מציגים להנהלה את הדשבורד המובטח מהחלומות"
    ]
    
    tech_notes = [
        "Excel + העתק הדבק",
        "Jupyter Notebook",
        "Python scripts",
        "Data pipeline ראשוני",
        "AI-assisted Analytics",
        "Streamlit + BI חלקי",
        "Streamlit + BI Dashboards מלא"
    ]
    
    # קיצורים למובייל
    short_names = ["שעבוד", "משה", "הסנה", "המכות", "יציאה", "קריעה", "הארץ"]
    
    # אייקונים טקסטואליים בטוחים שלא יגרמו לבעיות תאימות
    safe_icons = ["🧱", "👶", "🔥", "🐸", "👣", "💧", "🏞️"]
    
    # צבעים לכל נקודה בגרף - לפי מה שנראה בתמונה
    colors = ["#8B0000", "#FF4500", "#FF8C00", "#8B0000", "#1E90FF", "#00BFFF", "#4169E1"]
    
    # יצירת DataFrame
    chart_data = pd.DataFrame({
        "אירוע": events,
        "מדד_חירות": freedom_level,
        "הערה": funny_notes,
        "טכנולוגיה": tech_notes,
        "צבע": colors,
        "אייקון": safe_icons,
        "שם_קצר": short_names
    })
    
    # יצירת אינדיקציה למובייל
    is_mobile = """
    <script>
    if (window.innerWidth < 768) {
        document.documentElement.style.setProperty('--is-mobile', 'true');
    } else {
        document.documentElement.style.setProperty('--is-mobile', 'false');
    }
    </script>
    """
    st.markdown(is_mobile, unsafe_allow_html=True)
    
    # יצירת כרטיסיה למידע שנבחר
    info_container = st.empty()
    
    # יצירת גרף פשוט יותר
    fig = go.Figure()
    
    # הוספת קו החירות
    fig.add_trace(go.Scatter(
        x=events,
        y=freedom_level,
        mode='lines',
        line=dict(
            width=4, 
            color='#8000FF', 
            shape='spline',
            smoothing=1.3
        ),
        showlegend=False,
        hoverinfo='none'
    ))
    
    # הוספת נקודות על הקו לכל שלב
    for i, row in chart_data.iterrows():
        # הוספת נקודה בלבד על הגרף (ללא טקסט)
        fig.add_trace(go.Scatter(
            x=[row["אירוע"]],
            y=[row["מדד_חירות"]],
            mode='markers',
            marker=dict(
                size=25, 
                color=row["צבע"],
                symbol='circle',
                line=dict(width=2, color='white')
            ),
            name=row["אירוע"],
            customdata=[[
                row["אירוע"], 
                row["הערה"],
                row["טכנולוגיה"],
                row["מדד_חירות"],
                row["אייקון"]
            ]],
            hovertemplate="<b>%{customdata[0]}</b><br>" + 
                          "מדד החירות: %{customdata[3]}<br>" +
                          "טכנולוגיה: %{customdata[2]}<br>" +
                          "<i>%{customdata[1]}</i><extra></extra>"
        ))
    
    # הוספת אייקונים בתחתית הגרף
    for i, row in chart_data.iterrows():
        fig.add_annotation(
            x=row["אירוע"],
            y=0,
            text=row["אייקון"],
            showarrow=False,
            font=dict(size=20),
            yshift=-30
        )
    
    # עיצוב פשוט יותר לגרף
    fig.update_layout(
        template="plotly_white",
        font=dict(family="Rubik, sans-serif", size=14),
        plot_bgcolor='#F8F9FA',
        xaxis=dict(
            title="",
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False
        ),
        yaxis=dict(
            title="רמת החירות הדיגיטלית",
            range=[0, 11],
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)',
            zeroline=False,
            tickvals=[1, 3, 5, 8, 10],
            ticktext=["1", "3", "5", "8", "10"],
            tickfont=dict(size=12, family="Rubik, sans-serif")
        ),
        margin=dict(l=20, r=20, t=30, b=50),
        showlegend=False,
        height=400,
        hoverlabel=dict(
            bgcolor="white",
            font_size=14,
            font_family="Rubik, sans-serif"
        ),
        hovermode="closest",
    )
    
    # הגדרת כפתורים שיוצגו בגרף
    config = {
        'displayModeBar': True,
        'modeBarButtonsToRemove': [
            'zoom', 'pan', 'select', 'zoomIn', 'zoomOut', 
            'autoScale', 'resetScale', 'lasso2d'
        ],
        'displaylogo': False,
        'responsive': True
    }
    
    # הצגת הגרף בלי חלוקה לעמודות (יותר פשוט)
    st.plotly_chart(
        fig, 
        config=config,
        use_container_width=True
    )
    
    # הוספת אזור להצגת אינפורמציה כאשר הגרף נלחץ
    st.markdown("""
    <div style="text-align:center; margin-top:-10px; margin-bottom:20px;">
        <div style="display:inline-block; background-color:#f8f9fa; padding:10px 20px; border-radius:50px;">
            <span style="font-size:24px;">👆</span>
            <span style="font-family: Rubik, sans-serif; font-size:16px; margin-right:5px;">לחצו על נקודה בגרף לפרטים</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # מקרא פשוט יותר ברוח התמונה שהצגת - בצד ימין
    st.markdown("""
    <div style="text-align:right; margin-top:10px; font-family: Rubik, sans-serif;">
        <h4 style="color:#8000FF; font-size:16px; margin-bottom:5px;">
            <span style="margin-left:10px;">🔑</span> מקרא רמות החירות:
        </h4>
        <div style="display:flex; flex-direction:column; gap:8px; max-width:300px; margin-right:auto;">
            <div style="display:flex; align-items:center; justify-content:flex-end;">
                <span style="font-size:14px;">עבדות דיגיטלית</span>
                <div style="width:14px; height:14px; background-color:#8B0000; border-radius:50%; margin-right:8px;"></div>
                <span style="margin-right:5px; font-weight:bold;">1-2:</span>
            </div>
            <div style="display:flex; align-items:center; justify-content:flex-end;">
                <span style="font-size:14px;">חירות מוגבלת</span>
                <div style="width:14px; height:14px; background-color:#1E90FF; border-radius:50%; margin-right:8px;"></div>
                <span style="margin-right:5px; font-weight:bold;">3-5:</span>
            </div>
            <div style="display:flex; align-items:center; justify-content:flex-end;">
                <span style="font-size:14px;">חירות דיגיטלית מלאה</span>
                <div style="width:14px; height:14px; background-color:#8A2BE2; border-radius:50%; margin-right:8px;"></div>
                <span style="margin-right:5px; font-weight:bold;">6-10:</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # הסבר נוסף אחרי הגרף
    st.markdown("""
    <div style="background-color:rgba(128,0,255,0.05); padding:15px; border-radius:8px; border-right:4px solid #8000FF; margin-top:20px; font-family:Rubik, sans-serif;">
        <h4 style="color:#8000FF; margin-top:0; font-family:Rubik, sans-serif; display:flex; align-items:center;">
            <span style="margin-left:10px;">⭐</span> המסע מעבדות לחירות בעולם הדאטה
        </h4>
        <p>בעולם הדאטה, אנחנו עוברים מסע דומה ליציאת מצרים:</p>
        <ul style="padding-right:20px;">
            <li><b>שלב העבדות:</b> עבודה ידנית עם אקסלים ללא סוף וללא אוטומציה</li>
            <li><b>שלבי המעבר:</b> דרך נפתול הדיבאגים והלמידה של כלים חדשים</li>
            <li><b>גאולת הדאטה:</b> כשמגיעים לאוטומציה מלאה, דשבורדים חכמים ותובנות עמוקות</li>
        </ul>
        <p>בכל שלב במסע, אנו משתחררים יותר מעבודה ידנית ומתקרבים לחירות דיגיטלית אמיתית!</p>
    </div>
    """, unsafe_allow_html=True)
# טאב 2 – שאלון הבן הדאטאיסט
with tab2:
    st.markdown("<h3 style='font-family: Rubik, sans-serif;'>🔍 איזה בן דאטה אתה?</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-family: Rubik, sans-serif;'>ענה על כמה שאלות קצרות וגלֵה איזה טיפוס אנליטי מסתתר בך.</p>", unsafe_allow_html=True)

    q1 = st.radio("בפגישת דאטה, מה התגובה שלך?", [
        "שואל שאלות עומק ומבקש מקור נתונים",
        "מציע להתעלם מהדאטה כי אין כמו אינטואיציה טובה",
        "מופתע שיש פגישה בכלל",
        "מחייך ומתעלם, גם ככה אף אחד לא מבין שום דבר"], index=None)

    q2 = st.radio("איך אתה מרגיש לגבי דשבורדים?", [
        "אהבה בלב",
        "נחמד אבל overrated",
        "עדיין מנסה להבין את הקטע של הסלייסרים",
        "חשבתי שזו בכלל מצגת"], index=None)

    if st.button("גלה מי אתה או את"):
        score = 0
        answers = [q1, q2]
        for ans in answers:
            if "עומק" in ans or "אהבה" in ans:
                score += 3
            elif "להתעלם" in ans or "נחמד" in ans:
                score += 1.5
            elif "מופתע" in ans or "להבין" in ans:
                score += 1
            else:
                score += 0.5

        if score >= 5:
            st.markdown("<div style='font-family: Rubik, sans-serif; background-color: #d4edda; color: #155724; padding: 10px; border-radius: 5px;'>🧠 יצאת החכם – הדאטה אצלך בידיים טובות. אתה יודע לשאול, לבדוק ולבנות דשבורדים בזמן שכולם עוד שואלים מה זה KPI.</div>", unsafe_allow_html=True)
        elif score >= 3:
            st.markdown("<div style='font-family: Rubik, sans-serif; background-color: #fff3cd; color: #856404; padding: 10px; border-radius: 5px;'>😈 יצאת הרשע – אתה שואל שאלות, אבל רק אם זה משרת אותך. בוא נגיד שדאטה קיים, אבל אתה מעדיף אינטואיציה.</div>", unsafe_allow_html=True)
        elif score >= 1.5:
            st.markdown("<div style='font-family: Rubik, sans-serif; background-color: #d1ecf1; color: #0c5460; padding: 10px; border-radius: 5px;'>🤔 יצאת התם – אתה מתעניין, אבל עוד קצת תרגול ותהיה מאסטר של דאטה. תמשיך לשאול!</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='font-family: Rubik, sans-serif; background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px;'>😶 יצאת שאינו יודע לשאול – אבל זה בסדר! כל דאטה-אנליסט מתחיל ככה. נתחיל מהבנת סוגי גרפים ונמשיך משם!</div>", unsafe_allow_html=True)

# טאב 3 – משחק אפיקומן או סתם מצה
with tab3:
    st.markdown("<h3 style='font-family: Rubik, sans-serif;'> אפיקומן או סתם מצה?</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-family: Rubik, sans-serif;'>בחרי בכל שלב : אפיקומן או סתם מצה. האם תמצאי את האפיקומן?</p>", unsafe_allow_html=True)
    
    step = st.radio("שלב ראשון: מגיע אלייך דאטה מהפרויקט.", ["בודקת קודם מה יש בפנים (אפיקומן)", "הולכת ישר לאנליזה (סתם מצה)"], index=None)
    if step == "בודקת קודם מה יש בפנים (אפיקומן)":
        step2 = st.radio("שלב שני: יש מלא עמודות חסרות.", ["מתחילה לנקות ולתעד (אפיקומן)", "זה בטח סתם – ממשיכה ככה (סתם דאטה)"], index=None)
        if step2 == "מתחילה לנקות ולתעד (אפיקומן)":
            st.markdown("<div style='font-family: Rubik, sans-serif; background-color: #d4edda; color: #155724; padding: 10px; border-radius: 5px;'>🎉 יצאת דאטה חכמה – אפילו פרעה היה גאה בך</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='font-family: Rubik, sans-serif; background-color: #fff3cd; color: #856404; padding: 10px; border-radius: 5px;'>עוד מאמץ קטן ואת בדרך למצוא אפיקומן</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='font-family: Rubik, sans-serif; background-color: #d1ecf1; color: #0c5460; padding: 10px; border-radius: 5px;'>🤷‍♀️ יצאת מאמינה – אבל בלי דאטה ... תנסי שוב!</div>", unsafe_allow_html=True)

# טאב 4 – על היוצרים
with tab4:
    st.markdown("<h3 style='font-family: Rubik, sans-serif;'>👥 מאחורי הקלעים</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-family: Rubik, sans-serif;'>
    <p><strong>היוצרת:</strong> <a href="https://www.2dpoint.co.il">Dana Arnon Perry</a> –  מלמדת אוריינות נתונים, קוסמת של אינסייטים ומי שאחראית לכך שפסח השנה קיבל גרסת BI 😎</p>

    <p><strong>המוציא לפועל:</strong> ChatGPT – רובוט צייתן עם חוש הומור בריא ואובססיה לדאטה סטים מוזרים מתקופת המקרא.</p>

    <p><strong>דאטה סטוריטלר:</strong> Claude – אחראי על שדרוג הקוד והמראה של הדשבורד ותכל'ס הייתי צריך לעשות את רוב העבודה בסוף (רק אומר).</p>

    <p><strong>קוד המקור:</strong> <a href="https://github.com/DanaArnonPerry/passover_dashboard" target="_blank">צפייה והורדה מ-GitHub</a> 💻</p>

    <p><strong>מאחורי הקלעים של השיחה:</strong></p>
    <blockquote>
    "אם כל שאר הקבצים תקינים (והם כן), הדשבורד שלך יעלה חלק כמו מצה עם שוקולד"<br> 
    "אנחנו במכת "כמעט עובד" – וזה הכי כואב" 😅<br>
    "אוקיי בואי ננשום עמוק ונעוף על זה יחד" 💨🛠️<br>
    "ברור שיש תיקונים – את הרי לא תתני לדשבורד לצאת בלי שהוא פסח פרפקט"💅📊<br>

    </blockquote>

    <p><strong>🎥 לצפייה בסרטון מאחורי הקלעים של הפרומפטים:</strong><br>  
    <a href="https://youtu.be/yVnQN7UOu3A?si=2ibL5eztYYdzSTis">לחצו כאן כדי לצפות ביוטיוב</a></p>

    <p>זה הדשבורד הראשון שנכתב בצחוק, נבנה באהבה, ומוגש עם כף מרק של דאטה.<br> 
    חג חירות שמח! 🥳</p>
    </div>
    """, unsafe_allow_html=True)
