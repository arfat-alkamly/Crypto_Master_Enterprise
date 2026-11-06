# المسار: tools/entropy_calculator.py
"""
Tool: Shannon Entropy & Statistical Randomness Calculator
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: قياس الإنتروبيا والعشوائية الإحصائية (0.0 إلى 8.0 بت/بايت) لتقييم مقاومة التحليل الترددي.
"""

import math
from collections import Counter

class EntropyAnalyzer:
    @staticmethod
    def calculate_entropy(data: str | bytes) -> tuple[float, str]:
        """
        حساب إنتروبيا شانون على مستوى البايتات:
        يرجع: (قيمة_الإنتروبيا_الرقمية, التقييم_الأكاديمي)
        """
        if not data:
            return 0.0, "لا توجد بيانات لحساب الإنتروبيا (0.00)"

        # تحويل السلسلة إلى بايتات في حال كانت نصاً
        byte_data = data.encode("utf-8") if isinstance(data, str) else data
        total_len = len(byte_data)
        
        # حساب تكرار كل بايت
        counts = Counter(byte_data)
        
        # تطبيق معادلة شانون
        entropy = 0.0
        for count in counts.values():
            p_x = count / total_len
            if p_x > 0:
                entropy -= p_x * math.log2(p_x)

        # التقييم الأكاديمي وفق المعيار السيبراني (الحد الأقصى النظري للبايت هو 8.0 بت)
        if entropy >= 7.5:
            assessment = "عشوائية تامة (عالية جداً) - يستحيل كسرها بالتحليل الترددي"
        elif entropy >= 5.0:
            assessment = "عشوائية متوسطة - تشتت جزئي للبيانات"
        elif entropy >= 3.0:
            assessment = "عشوائية منخفضة - تماثل ملحوظ للأنماط والترددات"
        else:
            assessment = "عشوائية ضعيفة جداً - النص صريح أو مكرر ومكشوف تماماً"

        return round(entropy, 4), assessment
