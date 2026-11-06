# المسار: algorithms/padding.py
"""
Helper Module: PKCS#7 Padding & Text Preservation Engine
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: محرك حشو الكتل وفق معيار PKCS#7، والتعامل الذكي مع المسافات والرموز.
"""

class PKCS7:
    """معيار حشو الكتل PKCS#7 الصافي بلغة بايثون دون مكاتب خارجية.
    هذا العنصر مهم في المناقشة لأنه يوضح كيفية التعامل مع النصوص غير المتساوية في الطول عند استخدام DES و AES."""
    
    @staticmethod
    def pad(data: bytes, block_size: int = 16) -> bytes:
        """
        شرح للمناقشة: إذا كان النص أقل من مضاعف الكتلة، نضيف بايتات متطابقة بقيمة عدد البايتات الناقصة.
        هذا ضروري حتى تكون العملية القابلة للعكس في DES و AES.
        السؤال الذي غالبًا يُسأل: ماذا يحدث إذا كان النص مضاعفاً تاماً لحجم الكتلة؟
        الجواب: يُضاف كتلة حشو كاملة بقيمة block_size لضمان عدم الخلط بين البيانات والحشو عند فك التشفير.
        """
        pad_len = block_size - (len(data) % block_size)
        return data + bytes([pad_len] * pad_len)

    @staticmethod
    def unpad(data: bytes, block_size: int = 16) -> bytes:
        """إزالة حشو PKCS#7 والتحقق الصارم من نزاهته"""
        if not data or len(data) % block_size != 0:
            raise ValueError("طول البيانات لا يطابق مضاعفات حجم الكتلة المعياري!")
        pad_len = data[-1]
        if pad_len == 0 or pad_len > block_size:
            raise ValueError("حشو PKCS#7 غير صالح أو تالف!")
        # التأكد أن جميع بايتات الحشو متطابقة
        if data[-pad_len:] != bytes([pad_len] * pad_len):
            raise ValueError("تطابق بايتات الحشو غير سليم (Padding Integrity Failure)!")
        return data[:-pad_len]


class TextSanitizer:
    """معالجة المسافات والرموز مع الاحتفاظ بها في مواضعها للخوارزميات الكلاسيكية"""
    
    @staticmethod
    def filter_alpha_only(text: str) -> tuple[str, list[tuple[int, str]]]:
        """
        استخراج الأحرف فقط مع تخزين مواضع الرموز والمسافات لاستعادتها بدقة
        """
        clean_chars = []
        non_alpha_map = []  # قائمة (index, char)
        for idx, ch in enumerate(text):
            if ch.isalpha():
                clean_chars.append(ch)
            else:
                non_alpha_map.append((idx, ch))
        return "".join(clean_chars), non_alpha_map

    @staticmethod
    def restore_non_alpha(cipher_chars: str, non_alpha_map: list[tuple[int, str]]) -> str:
        """شرح للمناقشة: هذه الدالة تحافظ على المسافات والرموز في أماكنها الأصلية أثناء التشفير/الفك.
        وهي تجعل الخوارزميات الكلاسيكية أكثر واقعية عند التعامل مع النصوص الحقيقية في التطبيقات اليومية."""
        result = list(cipher_chars)
        for idx, ch in non_alpha_map:
            result.insert(idx, ch)
        return "".join(result)
