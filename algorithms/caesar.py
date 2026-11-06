# المسار: algorithms/caesar.py
"""
Algorithm: Caesar Cipher & Shift Substitution
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: تشفير وفك تشفير قيصر مع الحفاظ الكامل على المسافات والرموز بمواضعها.
"""

from algorithms.padding import TextSanitizer

class CaesarCipher:
    @staticmethod
    def validate_shift(shift: int) -> int:
    
        s = shift % 26
        if s == 0:
            raise ValueError("مفتاح الإزاحة لا يمكن أن يكون صفراً أو مضاعفاً لـ 26 (النص سيبقى دون تغيير)!")
        return s

    @classmethod
    def encrypt(cls, text: str, shift: int) -> str:
        s = cls.validate_shift(shift)
        clean_text, non_alpha = TextSanitizer.filter_alpha_only(text)
        res = []
        for ch in clean_text:
            base = ord("A") if ch.isupper() else ord("a")
            res.append(chr((ord(ch) - base + s) % 26 + base))
        return TextSanitizer.restore_non_alpha("".join(res), non_alpha)

    @classmethod
    def decrypt(cls, text: str, shift: int) -> str:
     
        s = cls.validate_shift(shift)
        return cls.encrypt(text, -s)
