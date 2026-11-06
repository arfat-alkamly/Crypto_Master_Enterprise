# المسار: algorithms/rsa_core.py
"""
Algorithm: RSA Asymmetric Cryptosystem (Pure Python Zero-Freezing)
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: محرك RSA الصافي (إقليدس الممتد، توليد مفاتيح سريع بدون تجمد، والأس النمطي).
"""

import random

class RSACore:
    @staticmethod
    def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
        """خوارزمية إقليدس الممتدة لحساب gcd والمعاملين x و y"""
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = RSACore.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    @classmethod
    def mod_inverse(cls, e: int, phi: int) -> int:
        """
        حساب المفتاح الخاص d كمعكوس ضربي لـ e تحت مقياس phi(n):
        (e * d) mod phi == 1
        """
        gcd, x, _ = cls.extended_gcd(e, phi)
        if gcd != 1:
            raise ValueError("لا يوجد معكوس ضربي لمفتاح التشفير e مع دالة أويلر phi(n)!")
        return (x % phi + phi) % phi

    @staticmethod
    def is_prime(n: int) -> bool:
        """اختبار الأولية الاحتمالي ميلر-رابين السريع"""
        if n < 2:
            return False
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
            if n == p:
                return True
            if n % p == 0:
                return False
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 3, 5, 7):
            if pow(a, d, n) == 1:
                continue
            for r in range(s):
                if pow(a, d * (2 ** r), n) == n - 1:
                    break
            else:
                return False
        return True

    @classmethod
    def generate_keys(cls, bits: int = 14) -> dict:
        """
        شرح للمناقشة: هنا يتم توليد مفتاح عام ومفتاح خاص باستخدام أعداد أولية،
        ثم حساب قيمة n و phi(n) والمفاتيح d و e. هذا هو جوهر نظام RSA غير المتماثل.
        السؤال الذي غالبًا يُسأل: ما هو حجم المفاتيح ولماذا تم اختياره؟
        الجواب: تم اعتماد 14-16 بت ليعطي استجابة فورية بالملي ثانية أثناء التقييم الأكاديمي،
        دون الدخول في عمليات حسابية معقدة تؤدي لتجميد واجهة المستخدم (UI Freeze).
        """
        primes = []
        low = 1 << (bits - 1)
        high = (1 << bits) - 1
        
        while len(primes) < 2:
            candidate = random.randint(low, high) | 1  # ضمان أن يكون فردياً
            if cls.is_prime(candidate):
                if not primes or candidate != primes[0]:
                    primes.append(candidate)
                    
        p, q = primes[0], primes[1]
        n = p * q
        phi = (p - 1) * (q - 1)
        
        # اختيار مفتاح التشفير العام e الشائع (Fermat number F4)
        e = 65537
        gcd, _, _ = cls.extended_gcd(e, phi)
        if gcd != 1 or e >= phi:
            e = 3
            while True:
                gcd, _, _ = cls.extended_gcd(e, phi)
                if gcd == 1:
                    break
                e += 2
                
        d = cls.mod_inverse(e, phi)
        
        return {
            "p": p, "q": q, "n": n, "phi": phi,
            "public_key": (e, n),
            "private_key": (d, n)
        }

    @staticmethod
    def encrypt(text: str, e: int, n: int) -> str:
        """شرح للمناقشة: تشفير RSA يعتمد على الأسومية (الرفع إلى قوة) modulo n،
        وهذا يجعل النص غير قابل للقراءة دون المفتاح الخاص."""
        blocks = []
        for char in text:
            m = ord(char)
            if m >= n:
                raise ValueError(f"قيمة المحرف '{char}' ({m}) أكبر من المقياس n ({n})! قم بتوليد مفتاح بمقياس أكبر.")
            c = pow(m, e, n)
            blocks.append(str(c))
        return " ".join(blocks)

    @staticmethod
    def decrypt(cipher_str: str, d: int, n: int) -> str:
        """شرح للمناقشة: فك RSA يتم باستخدام المفتاح الخاص d، وهو العملية العكسية للرفع إلى أس e modulo n."""
        blocks = cipher_str.strip().split()
        decrypted_chars = []
        for b in blocks:
            if not b.isdigit():
                raise ValueError(f"كتلة RSA '{b}' غير صالحة؛ يجب أن تكون أرقاماً صحيحة فقط!")
            c = int(b)
            m = pow(c, d, n)
            decrypted_chars.append(chr(m))
        return "".join(decrypted_chars)
