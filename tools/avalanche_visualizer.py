# المسار: tools/avalanche_visualizer.py
"""
Tool: Bitwise Strict Avalanche Criterion (SAC) Analyzer
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: قياس تشتت البتات عبر Bitwise XOR واختبار معيار الانهيار الجليدي الصارم.
"""

class AvalancheAnalyzer:
    @staticmethod
    def calculate_bit_difference(c1_bytes: bytes, c2_bytes: bytes) -> tuple[int, int, float, str]:
        """
        مقارنة بايتات نصين مشفرين على مستوى البتات وحساب نسبة التغير:
        يرجع: (عدد_البتات_المتغيرة, إجمالي_البتات, النسبة_المئوية, التقييم_الأكاديمي)
        """
        # مساواة الطول بالمحاذاة الصفرية في حال اختلف الحجم
        max_len = max(len(c1_bytes), len(c2_bytes))
        b1 = c1_bytes.ljust(max_len, b"\x00")
        b2 = c2_bytes.ljust(max_len, b"\x00")

        total_bits = max_len * 8
        changed_bits = 0

        for byte1, byte2 in zip(b1, b2):
            xor_diff = byte1 ^ byte2
            # عد البتات المختلفة (Hamming Weight للناتج)
            changed_bits += bin(xor_diff).count("1")

        percentage = (changed_bits / total_bits) * 100.0 if total_bits > 0 else 0.0

        # التقييم الأكاديمي للانهيار الجليدي (SAC Standard ~ 50%)
        if percentage >= 45.0 and percentage <= 55.0:
            evaluation = "مثالي جداً (SAC Compliant ~50%) - تشتت وارتباك كامل"
        elif percentage >= 35.0 and percentage < 65.0:
            evaluation = "جيد جداً - استجابة انهيارية قوية للبتات"
        else:
            evaluation = "ضعيف - ارتباط خطي واضح بين المدخل والمخرج"

        return changed_bits, total_bits, percentage, evaluation
