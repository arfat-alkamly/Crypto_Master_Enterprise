# المسار: algorithms/affine.py
"""
Algorithm: Affine Cipher (C = (a * P + b) mod 26)
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: تطبيق شفرة التآلف الرياضية مع فحص المعكوس الضربي وحفظ المسافات.
"""

import math
from algorithms.padding import TextSanitizer

class AffineCipher:
    @staticmethod
    def mod_inverse(a: int, m: int = 26) -> int:
        """حساب المعكوس الضربي النمطي a^-1 mod m"""
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return -1

    @classmethod
    def validate_keys(cls, a: int, b: int) -> tuple[int, int]:
        
        a_mod = a % 26
        if math.gcd(a_mod, 26) != 1:
            raise ValueError(
                f"معامل الضرب a = {a} غير صالح لأن gcd({a_mod}, 26) != 1.\n"
                "القاعدة: يجب أن يكون المعامل a أولياً نسبياً مع 26 لوجود المعكوس الضربي!"
            )
        return a_mod, b % 26

    @classmethod
    def encrypt(cls, text: str, a: int, b: int) -> str:
  
        a_val, b_val = cls.validate_keys(a, b)
        clean_text, non_alpha = TextSanitizer.filter_alpha_only(text)
        res = []
        for ch in clean_text:
            base = ord("A") if ch.isupper() else ord("a")
            p = ord(ch) - base
            c = (a_val * p + b_val) % 26
            res.append(chr(c + base))
        return TextSanitizer.restore_non_alpha("".join(res), non_alpha)

    @classmethod
    def decrypt(cls, text: str, a: int, b: int) -> str:
        a_val, b_val = cls.validate_keys(a, b)
        a_inv = cls.mod_inverse(a_val, 26)
        clean_text, non_alpha = TextSanitizer.filter_alpha_only(text)
        res = []
        for ch in clean_text:
            base = ord("A") if ch.isupper() else ord("a")
            c = ord(ch) - base
            p = (a_inv * (c - b_val)) % 26
            res.append(chr(p + base))
        return TextSanitizer.restore_non_alpha("".join(res), non_alpha)
