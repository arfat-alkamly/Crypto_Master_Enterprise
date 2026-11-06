# المسار: algorithms/vigenere.py
"""
Algorithm: Vigenere Cipher (Polyalphabetic Substitution)
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: تطبيق استبدال فيجنير مع مؤشر مفتاح ديناميكي يحافظ على المسافات والرموز.
"""

class VigenereCipher:
    @staticmethod
    def validate_key(key: str) -> str:

        clean_k = "".join([c.upper() for c in key if c.isalpha()])
        if not clean_k:
            raise ValueError("مفتاح فيجنير يجب أن يحتوي على حروف أبجدية صالحة!")
        return clean_k

    @classmethod
    def encrypt(cls, text: str, key: str) -> str:
   
        
        k = cls.validate_key(key)
        res = []
        k_idx = 0
        for ch in text:
            if ch.isalpha():
                base = ord("A") if ch.isupper() else ord("a")
                shift = ord(k[k_idx % len(k)]) - ord("A")
                res.append(chr((ord(ch) - base + shift) % 26 + base))
                k_idx += 1  # استهلاك حرف المفتاح فقط عند تشفير حرف أبجدي
            else:
                res.append(ch)  # الحفاظ على الرموز والأرقام والمسافات دون استهلاك المفتاح
        return "".join(res)

    @classmethod
    def decrypt(cls, text: str, key: str) -> str:
        
        
        k = cls.validate_key(key)
        res = []
        k_idx = 0
        for ch in text:
            if ch.isalpha():
                base = ord("A") if ch.isupper() else ord("a")
                shift = ord(k[k_idx % len(k)]) - ord("A")
                res.append(chr((ord(ch) - base - shift) % 26 + base))
                k_idx += 1
            else:
                res.append(ch)
        return "".join(res)
