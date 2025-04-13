import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const FreedomIndexChart = () => {
  // נתוני הגרף
  const data = [
    { id: 0, name: "שעבוד במצרים", value: 1, icon: "🧱", color: "#8B4513", note: "מנקים אקסלים ידנית ומעתיקים נתונים בלי סוף", tech: "Excel + העתק הדבק" },
    { id: 1, name: "הולדת משה", value: 2, icon: "👶", color: "#FFD700", note: "שומעים על פייתון ולומדים שיש חיים אחרי אקסל", tech: "Jupyter Notebook" },
    { id: 2, name: "הסנה הבוער", value: 3, icon: "🔥", color: "#FF4500", note: "קוד ראשון רץ בהצלחה! תחושת חירות ראשונית", tech: "Python scripts" },
    { id: 3, name: "תחילת המכות", value: 1, icon: "🐸", color: "#800000", note: "מריצים סקריפטים אבל נתקעים בים של דיבאגים", tech: "Data pipeline ראשוני" },
    { id: 4, name: "יציאה ממצרים", value: 5, icon: "🚶‍♂️", color: "#1E90FF", note: "בינה מלאכותית מנקה ומעבדת את הכל אוטומטית", tech: "AI-assisted Analytics" },
    { id: 5, name: "קריעת ים סוף", value: 8, icon: "🌊", color: "#00BFFF", note: "מציגים להנהלה דשבורד אינטראקטיבי מהחלומות", tech: "Streamlit + BI Dashboards" }
  ];

  // מצב נוכחי של שלב נבחר (הוק סטייט)
  const [selectedPoint, setSelectedPoint] = useState(null);
  const [isMobile, setIsMobile] = useState(false);
  const [isAnimating, setIsAnimating] = useState(false);

  // בדיקה אם המכשיר הוא מובייל
  useEffect(() => {
    const checkIfMobile = () => {
      setIsMobile(window.innerWidth <= 768);
    };
    
    checkIfMobile();
    window.addEventListener('resize', checkIfMobile);
    
    return () => {
      window.removeEventListener('resize', checkIfMobile);
    };
  }, []);

  // אנימציה של הגרף בטעינה הראשונית
  useEffect(() => {
    setIsAnimating(true);
    const timer = setTimeout(() => {
      setIsAnimating(false);
    }, 1500);
    
    return () => clearTimeout(timer);
  }, []);

  // טיפול בלחיצה על נקודה בגרף
  const handlePointClick = (point) => {
    setSelectedPoint(point);
  };

  // רנדור הגרף
  return (
    <div className="bg-white rounded-lg shadow-md p-4 font-sans" dir="rtl">
      {/* כותרת הגרף */}
      <div className="mb-4 bg-purple-50 p-4 rounded-lg border-r-4 border-purple-700">
        <h3 className="text-lg font-bold text-purple-800 flex items-center mb-2">
          <span className="ml-2">📊</span> מדד החירות הדיגיטלית: המסע מעבדות לחירות
        </h3>
        <p className="text-sm text-gray-700">
          לחצו על הנקודות בגרף כדי לגלות כיצד מתקדמים משעבוד הדאטה אל החירות הדיגיטלית!
        </p>
      </div>

      {/* רשימת אייקונים למובייל עם שמות המקרא */}
      {isMobile && (
        <div className="mb-4 bg-white rounded-lg overflow-x-auto">
          <div className="flex justify-between px-2 py-3 min-w-full">
            {data.map((point, index) => (
              <div 
                key={index} 
                className="flex flex-col items-center px-2 cursor-pointer"
                onClick={() => handlePointClick(point)}
              >
                <div 
                  className="flex items-center justify-center text-lg w-10 h-10 rounded-full mb-1"
                  style={{ backgroundColor: point.color }}
                >
                  {point.icon}
                </div>
                <div className="text-xs text-center font-bold whitespace-nowrap">
                  {point.name.split(" ")[0]}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      <div className={`flex ${isMobile ? 'flex-col' : 'flex-row'} gap-4`}>
        {/* הגרף */}
        <div className={`${isMobile ? 'w-full' : 'w-3/4'} h-64 bg-gray-50 rounded-lg`}>
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={data} margin={{ top: 20, right: 20, left: 20, bottom: 20 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
              <XAxis 
                dataKey={isMobile ? "icon" : "name"}
                tick={{ 
                  fontSize: isMobile ? 16 : 12,
                  fill: '#333'
                }}
                height={50}
                interval={0}
                angle={0}
                textAnchor="middle"
                tickMargin={8}
              />
              <YAxis 
                domain={[0, 10]} 
                tick={{ fontSize: 12 }}
                tickCount={6}
                label={{ 
                  value: 'רמת החירות', 
                  angle: -90, 
                  position: 'left',
                  style: { textAnchor: 'middle', fontSize: '14px', fill: '#555' }
                }}
              />
              <Tooltip 
                content={({ active, payload }) => {
                  if (active && payload && payload.length) {
                    const data = payload[0].payload;
                    return (
                      <div className="bg-white p-2 border border-gray-200 rounded shadow-md text-right">
                        <div className="font-bold text-purple-800">{data.icon} {data.name}</div>
                        <div className="text-sm mt-1">מדד החירות: {data.value}/10</div>
                        <div className="text-sm text-gray-600">{data.tech}</div>
                      </div>
                    );
                  }
                  return null;
                }}
              />
              <Line 
                type="monotone" 
                dataKey="value" 
                stroke="#8000FF" 
                strokeWidth={3} 
                dot={false}
                activeDot={false}
                isAnimationActive={isAnimating}
                animationDuration={1500}
                animationEasing="ease-in-out"
              />
              
              {/* נקודות אינטראקטיביות עם אייקונים */}
              {data.map((point) => (
                <Line
                  key={point.id}
                  type="monotone"
                  dataKey={() => point.value}
                  stroke="transparent"
                  dot={{
                    r: 14,
                    stroke: 'white',
                    strokeWidth: 2,
                    fill: point.color,
                    cursor: 'pointer'
                  }}
                  activeDot={false}
                  isAnimationActive={isAnimating}
                  animationDuration={1500 + point.id * 200}
                  animationEasing="ease-out"
                  data={[point]}
                  onClick={() => handlePointClick(point)}
                  label={{
                    position: 'center',
                    value: point.icon,
                    style: {
                      fontSize: '14px', 
                      fontWeight: 'bold',
                      fill: 'white'
                    }
                  }}
                />
              ))}
            </LineChart>
          </ResponsiveContainer>
        </div>

        {/* כרטיסיית מידע */}
        <div className={`${isMobile ? 'w-full' : 'w-1/4'} bg-gray-50 rounded-lg p-4`}>
          {selectedPoint ? (
            <div 
              className="rounded-lg p-4 h-full flex flex-col"
              style={{ backgroundColor: `${selectedPoint.color}20`, borderRight: `4px solid ${selectedPoint.color}` }}
            >
              <div className="text-xl font-bold mb-2 flex items-center">
                <span className="ml-2">{selectedPoint.icon}</span>
                {selectedPoint.name}
              </div>
              
              <div className="text-sm mb-3">
                <span className="font-bold">מדד החירות: </span>
                <span>{selectedPoint.value}/10</span>
              </div>
              
              <div className="text-sm mb-3">
                <span className="font-bold">טכנולוגיה: </span>
                <span>{selectedPoint.tech}</span>
              </div>
              
              <div className="text-sm italic flex-grow">{selectedPoint.note}</div>
              
              {/* מד התקדמות ויזואלי */}
              <div className="mt-4 w-full bg-gray-200 rounded-full h-4 overflow-hidden">
                <div
                  className="h-full text-xs flex items-center justify-center text-white transition-all duration-500 ease-out"
                  style={{ 
                    width: `${selectedPoint.value * 10}%`, 
                    backgroundColor: selectedPoint.color 
                  }}
                >
                  {selectedPoint.value}/10
                </div>
              </div>
            </div>
          ) : (
            <div className="text-center h-full flex flex-col items-center justify-center text-gray-500">
              <div className="text-4xl mb-2">👆</div>
              <div>לחצו על נקודה בגרף לפרטים</div>
            </div>
          )}
        </div>
      </div>

      {/* מקרא למדדי החירות */}
      <div className="mt-6 bg-gray-50 p-4 rounded-lg">
        <h4 className="font-bold text-purple-800 mb-2">🔑 מקרא רמות החירות:</h4>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-2">
          <div className="flex items-center">
            <div className="w-4 h-4 bg-gray-400 rounded-full mr-2"></div>
            <span className="text-sm">1-2: עבדות דיגיטלית</span>
          </div>
          <div className="flex items-center">
            <div className="w-4 h-4 bg-blue-400 rounded-full mr-2"></div>
            <span className="text-sm">3-5: חירות מוגבלת</span>
          </div>
          <div className="flex items-center">
            <div className="w-4 h-4 bg-purple-600 rounded-full mr-2"></div>
            <span className="text-sm">6-10: חירות דיגיטלית מלאה</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FreedomIndexChart;
