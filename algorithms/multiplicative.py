# المسار: algorithms/multiplicative.py
"""
Algorithm: Multiplicative Cipher
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: التشفير بالضرب النمطي مع التحقق من المعكوس الضربي والحفاظ على المسافات.
"""

import math
from algorithms.padding import TextSanitizer

class MultiplicativeCipher:
    @staticmethod
    def mod_inverse(a: int, m: int = 26) -> int:
        """
        حساب المعكوس الضربي تحت مقياس m:
        (a * x) mod m == 1
        """
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return -1

    @classmethod
    def validate_key(cls, key: int) -> int:
        """
        شرح للمناقشة: في التشفير الضربي يجب أن يكون المفتاح أولياً نسبياً مع 26
        لأن المعكوس الضربي موجود فقط عندما gcd(k, 26) = 1.
        السؤال الذي غالبًا يُسأل: لماذا يجب أن يكون gcd(k, 26) == 1؟
        الجواب: لأنه إذا اشترك المفتاح مع 26 في قاسم مشترك (مثل الأعداد الزوجية أو 13)،
        فلن يمتلك معكوساً ضربياً وسيحصل تصادم يمنع استرجاع النص الأصلي.
        """
        k = key % 26
        if math.gcd(k, 26) != 1:
            raise ValueError(
                f"المفتاح {key} غير صالح لأن gcd({k}, 26) = {math.gcd(k, 26)} != 1.\n"
                "القاعدة: يجب أن يكون المفتاح أولياً نسبياً مع 26 لوجود المعكوس الضربي!"
            )
        return k

    @classmethod
    def encrypt(cls, text: str, key: int) -> str:
        # شرح للمناقشة: هنا كل حرف يأخذ قيمة تمثل موضعه في الأبجدية، ثم يضرب في المفتاح ويعالجModulo 26.
        # هذا يوضح فكرة التشفير الرياضي بدلًا من التعويض البسيط في قيصر.
        k = cls.validate_key(key)
        clean_text, non_alpha = TextSanitizer.filter_alpha_only(text)
        res = []
        for ch in clean_text:
            base = ord("A") if ch.isupper() else ord("a")
            res.append(chr(((ord(ch) - base) * k) % 26 + base))
        return TextSanitizer.restore_non_alpha("".join(res), non_alpha)

    @classmethod
    def decrypt(cls, text: str, key: int) -> str:
        # شرح للمناقشة: فك التشفير يحتاج إلى المعكوس الضربي للمفتاح، لأن العملية الأصلية كانت ضربية.
        # بدون المعكوس لا يمكن استعادة النص، وهذا السبب العلمي الرئيسي لهذا النوع من الخوارزميات.
        k = cls.validate_key(key)
        k_inv = cls.mod_inverse(k, 26)
        clean_text, non_alpha = TextSanitizer.filter_alpha_only(text)
        res = []
        for ch in clean_text:
            base = ord("A") if ch.isupper() else ord("a")
            res.append(chr(((ord(ch) - base) * k_inv) % 26 + base))
        return TextSanitizer.restore_non_alpha("".join(res), non_alpha)
