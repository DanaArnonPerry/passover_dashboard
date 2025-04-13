# טאב 1 – גרף מדד החירות המשודרג
with tab1:
    # הסבר קצר לפני הגרף
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-family: 'Rubik', sans-serif;">
    <h3 style="margin-top: 0; font-family: 'Rubik', sans-serif;">מדד החירות הדיגיטלית: המסע מעבדות לחירות 🚀</h3>
    <p style="font-family: 'Rubik', sans-serif;">הגרף הבא מציג את רמת החירות הדיגיטלית בכל שלב של עבודה עם נתונים, בהשוואה לשלבי יציאת מצרים.
    לחצו על הנקודות בגרף כדי לגלות פרטים נוספים על כל שלב במסע!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # נתונים למדד החירות
    events = [
        "שעבוד במצרים",
        "הולדת משה", 
        "הסנה הבוער", 
        "תחילת המכות",
        "יציאה ממצרים", 
        "קריעת ים סוף"
    ]
    
    freedom_level = [1, 2, 3, 1, 5, 8]
    
    funny_notes = [
        "מנקים אקסלים ידנית ומעתיקים נתונים בלי סוף",
        "שומעים על פייתון ולומדים שיש חיים אחרי אקסל",
        "קוד ראשון רץ בהצלחה! תחושת חירות ראשונית",
        "מריצים סקריפטים אבל נתקעים בים של דיבאגים",
        "בינה מלאכותית מנקה ומעבדת את הכל אוטומטית",
        "מציגים להנהלה דשבורד אינטראקטיבי מהחלומות"
    ]
    
    tech_notes = [
        "Excel + העתק הדבק",
        "Jupyter Notebook",
        "Python scripts",
        "Data pipeline ראשוני",
        "AI-assisted Analytics",
        "Streamlit + BI Dashboards"
    ]
    
    # צבעים ואייקונים לכל שלב
    stage_colors = [
        "#8B4513",  # חום כהה לשעבוד
        "#FFD700",  # זהב להולדת משה
        "#FF4500",  # כתום-אדום לסנה הבוער
        "#800000",  # אדום כהה למכות
        "#1E90FF",  # כחול ליציאה ממצרים
        "#00BFFF"   # כחול בהיר לקריעת ים סוף
    ]
    
    stage_icons = ["🧱", "👶", "🔥", "🐸", "🚶‍♂️", "🌊"]
    
    # קיצורים למובייל
    short_names = ["שעבוד", "משה", "הסנה", "המכות", "יציאה", "קריעה"]
    
    # בניית DataFrame עם כל המידע
    chart_data = pd.DataFrame({
        "אירוע": events,
        "מדד_חירות": freedom_level,
        "הערה": funny_notes,
        "טכנולוגיה": tech_notes,
        "צבע": stage_colors,
        "אייקון": stage_icons,
        "שם_קצר": short_names
    })
    
    # יצירת פתרון למובייל - תצוגת אייקונים ושמות למעלה
    # בדיקה אם אנחנו במובייל באמצעות CSS
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .mobile-labels {
            display: flex;
            overflow-x: auto;
            padding: 10px 5px;
            background-color: white;
            border-radius: 10px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            direction: rtl;
        }
        
        .mobile-label-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            min-width: 60px;
            margin: 0 5px;
            cursor: pointer;
        }
        
        .mobile-icon-circle {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            margin-bottom: 5px;
            color: white;
        }
        
        .mobile-label-text {
            font-size: 12px;
            font-weight: bold;
            text-align: center;
            white-space: nowrap;
        }
    }
    
    @media (min-width: 769px) {
        .mobile-labels {
            display: none;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # יצירת שורת אייקונים למובייל
    mobile_labels_html = """
    <div class="mobile-labels">
    """
    
    for i, row in chart_data.iter
    
    # הוספת תוויות לציר Y שמציינות רמות חירות
    freedom_labels = [
        "עבדות<br>דיגיטלית",
        "",
        "חירות<br>מוגבלת",
        "",
        "חירות<br>בינונית",
        "",
        "חירות<br>משמעותית",
        "",
        "חירות<br>מלאה"
    ]
    
    # עיצוב לגרף הראשי (desktop)
    fig.update_layout(
        template="plotly_white",
        font=dict(family="Rubik, sans-serif", size=14),
        plot_bgcolor='rgba(248,249,250,0.8)',
        xaxis=dict(
            title="",
            showgrid=False,
            zeroline=False,
            showline=True,
            linecolor='rgba(0,0,0,0.2)',
            tickfont=dict(size=14, family="Rubik, sans-serif")
        ),
        yaxis=dict(
            title="",
            range=[0, 10],
            showgrid=True,
            gridcolor='rgba(0,0,0,0.07)',
            zeroline=False,
            tickvals=list(range(1, 10, 2)),
            ticktext=[freedom_labels[i] for i in range(0, 9, 2)],
            tickfont=dict(size=12, family="Rubik, sans-serif")
        ),
        margin=dict(l=10, r=10, t=10, b=10),
        showlegend=False,
        height=500,
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
    
    # בדיקה האם המשתמש גולש ממובייל דרך CSS Media Query
    st.markdown("""
    <style>
    .mobile-view, .desktop-view {
        display: none;
    }
    
    /* מסכים בגודל מובייל */
    @media (max-width: 768px) {
        .mobile-view {
            display: block;
        }
    }
    
    /* מסכים גדולים יותר */
    @media (min-width: 769px) {
        .desktop-view {
            display: block;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # התאמות למובייל - אפשרויות בתצוגות שונות
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # הצגת הגרף עם הגדרות משודרגות
        chart_container = st.plotly_chart(
            fig, 
            config=config,
            use_container_width=True
        )
    
    with col2:
        # הצגת כרטיסיות מידע למובייל
        st.markdown("""
        <div class="mobile-view">
            <div style="font-size:14px; font-family: Rubik, sans-serif; margin-bottom:10px;">
                <b>בחרו שלב לפרטים:</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # רשימה ללחיצה מותאמת למסכים קטנים
        selected_event = st.selectbox(
            label="בחרו שלב",
            options=range(len(events)),
            format_func=lambda x: f"{stage_icons[x]} {short_names[x]}",
            label_visibility="collapsed"
        )
        
        if selected_event is not None:
            # כרטיסיית מידע למובייל
            st.markdown(f"""
            <div class="mobile-view">
                <div style="background-color:{stage_colors[selected_event]}; padding:15px; border-radius:10px; color:white; font-family:Rubik, sans-serif;">
                    <h4 style="margin-top:0;">{stage_icons[selected_event]} {events[selected_event]}</h4>
                    <p style="font-size:14px; margin-bottom:5px;"><b>מדד החירות:</b> {freedom_level[selected_event]}/10</p>
                    <p style="font-size:14px; margin-bottom:5px;"><b>טכנולוגיה:</b> {tech_notes[selected_event]}</p>
                    <p style="font-size:14px; font-style:italic;">{funny_notes[selected_event]}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # הצגת מד התקדמות ויזואלי למדד החירות
            st.markdown(f"""
            <div class="mobile-view" style="margin-top:15px;">
                <div style="width:100%; background-color:#e0e0e0; height:20px; border-radius:10px; overflow:hidden;">
                    <div style="width:{freedom_level[selected_event]*10}%; height:100%; background-color:{stage_colors[selected_event]}; text-align:center; color:white; font-size:12px; line-height:20px;">
                        {freedom_level[selected_event]}/10
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # הסבר נוסף אחרי הגרף
    st.markdown("""
    <div style="background-color:rgba(128,0,255,0.05); padding:15px; border-radius:8px; border-right:4px solid #8000FF; margin-top:30px; font-family:Rubik, sans-serif;">
        <h4 style="color:#8000FF; margin-top:0; font-family:Rubik, sans-serif; display:flex; align-items:center;">
            <span style="margin-left:10px;">📊</span> המסע מעבדות לחירות בעולם הדאטה
        </h4>
        <p>בעולם הדאטה, אנחנו עוברים מסע דומה ליציאת מצרים:</p>
        <ul style="padding-right:20px;">
            <li><b>שלב העבדות:</b> עבודה ידנית עם אקסלים ללא סוף וללא אוטומציה</li>
            <li><b>שלבי המעבר:</b> דרך נפתול הדיבאגים והלמידה של כלים חדשים</li>
            <li><b>גאולת הדאטה:</b> כשמגיעים לאוטומציה מלאה, דשבורדים חכמים ותובנות עמוקות</li>
        </ul>
        <p>בכל שלב במסע, אנו משתחררים יותר מעבודה ידנית ומתקרבים לחירות דיגיטלית אמיתית! 🎉</p>
    </div>
    """, unsafe_allow_html=True)
