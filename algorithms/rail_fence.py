# المسار: algorithms/rail_fence.py
"""
Algorithm: Rail Fence Cipher (Zig-Zag Transposition)
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: تشفير وفك تشفير التبديل المتعرج مع محاكاة هندسية للمسار.
"""

class RailFenceCipher:
    @staticmethod
    def validate_rails(rails: int, text_len: int) -> int:
        """
        التحقق من صحة عمق الزجزاج.
        شرح للمناقشة: لماذا يجب أن يكون rails >= 2 وأقل من طول النص؟
        الجواب: العمق 1 يعني صفا واحدا فلا يتغير ترتيب النص إطلاقا،
        وعمق أكبر من أو يساوي طول النص يجعل كل حرف في صف منفصل دون أي تداخل تبديلي.
        """
        if rails < 2:
            raise ValueError("عمق الزجزاج (Rails) يجب أن يكون 2 على الأقل لإحداث تبديل في المواضع!")
        if rails >= text_len and text_len > 1:
            raise ValueError(f"عمق الزجزاج ({rails}) يجب أن يكون أقل من طول النص ({text_len})!")
        return rails

    @classmethod
    def encrypt(cls, text: str, rails: int) -> str:
        # شرح للمناقشة: نكتب النص على هيئة مسار متعرج، ثم نقرأ الصفوف بشكل أفقي.
        # هذا يجعل ترتيب الحروف مختلفًا، ويُعد مثالًا جيدًا على التشفير القائم على التبديل لا على الإزاحة.
        if not text:
            return ""
        r = cls.validate_rails(rails, len(text))
        
        # إنشاء مصفوفة المسارات
        fence = [[] for _ in range(r)]
        row, direction = 0, 1
        
        for ch in text:
            fence[row].append(ch)
            row += direction
            # تغيير اتجاه الحركة عند القمة أو القاع
            if row == r - 1:
                direction = -1
            elif row == 0:
                direction = 1
                
        return "".join(["".join(rail) for rail in fence])

    @classmethod
    def decrypt(cls, text: str, rails: int) -> str:
        # شرح للمناقشة: فك التشفير يعكس المسار، ويعيد ترتيب الحروف إلى مواضعها الأصلية.
        # هذه الوظيفة توضح أن التشفير والتبديل يمكن عكسهما إذا كانت خريطة المسار محفوظة أو معرفة.
        if not text:
            return ""
        r = cls.validate_rails(rails, len(text))
        
        # 1. رسم خريطة المسار لمعرفة أماكن الأحرف
        pattern = [[False] * len(text) for _ in range(r)]
        row, direction = 0, 1
        for i in range(len(text)):
            pattern[row][i] = True
            row += direction
            if row == r - 1:
                direction = -1
            elif row == 0:
                direction = 1
                
        # 2. ملء مصفوفة المسارات بالأحرف المشفرة حسب خريطة النمط
        idx = 0
        fence = [[""] * len(text) for _ in range(r)]
        for i in range(r):
            for j in range(len(text)):
                if pattern[i][j] and idx < len(text):
                    fence[i][j] = text[idx]
                    idx += 1
                    
        # 3. قراءة النص في مسار الزجزاج الأصلي
        res = []
        row, direction = 0, 1
        for i in range(len(text)):
            res.append(fence[row][i])
            row += direction
            if row == r - 1:
                direction = -1
            elif row == 0:
                direction = 1
                
        return "".join(res)
