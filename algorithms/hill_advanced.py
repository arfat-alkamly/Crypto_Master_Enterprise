# المسار: algorithms/hill_advanced.py
"""
Algorithm: Advanced Hill Cipher (Strict 2x2 & 3x3 Modular Matrix Engine)
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: محرك هيل الجبري الصافي الدقيق 100% مع حساب المعكوس النمطي وحفظ الرموز والمسافات.
"""

import math
from .sanitizer import TextSanitizer

class AdvancedHillCipher:
    @staticmethod
    def mod_inverse(a: int, m: int = 26) -> int:
        """حساب المعكوس الضربي القياسي gcd(a, 26) = 1"""
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        raise ValueError(f"المحدد {a} ليس له معكوس ضربي مع {m} (ليس أولياً نسبياً)!")

    @classmethod
    def get_matrix_inverse(cls, matrix: list[list[int]]) -> list[list[int]]:
        """شرح للمناقشة: هذا هو الجزء الأهم في هيل؛ حساب المعكوس النمطي للمصفوفة لتتمكن من فك التشفير."""
        n = len(matrix)
        if n == 2:
            a, b = matrix[0][0], matrix[0][1]
            c, d = matrix[1][0], matrix[1][1]
            det = (a * d - b * c) % 26
            inv_det = cls.mod_inverse(det, 26)
            # 2 2x2
            inv_matrix = [
                [( d * inv_det) % 26, (-b * inv_det) % 26],
                [(-c * inv_det) % 26, ( a * inv_det) % 26]
            ]
            return inv_matrix

        elif n == 3:
            m = matrix
            #  3
            det = (
                m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
                m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
                m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
            ) % 26
            
            inv_det = cls.mod_inverse(det, 26)

            # مصفوفة العوامل المرافقة الكلاسيكية المنقولة (Adjugate Matrix)
            adj = [[0]*3 for _ in range(3)]
            adj[0][0] = (m[1][1]*m[2][2] - m[1][2]*m[2][1])
            adj[0][1] = -(m[0][1]*m[2][2] - m[0][2]*m[2][1])
            adj[0][2] = (m[0][1]*m[1][2] - m[0][2]*m[1][1])

            adj[1][0] = -(m[1][0]*m[2][2] - m[1][2]*m[2][0])
            adj[1][1] = (m[0][0]*m[2][2] - m[0][2]*m[2][0])
            adj[1][2] = -(m[0][0]*m[1][2] - m[0][2]*m[1][0])

            adj[2][0] = (m[1][0]*m[2][1] - m[1][1]*m[2][0])
            adj[2][1] = -(m[0][0]*m[2][1] - m[0][1]*m[2][0])
            adj[2][2] = (m[0][0]*m[1][1] - m[0][1]*m[1][0])

            inv_matrix = [[(adj[r][c] * inv_det) % 26 for c in range(3)] for r in range(3)]
            return inv_matrix
        else:
            raise ValueError("الأبعاد المدعومة لمصفوفة هيل هي 2x2 أو 3x3 فقط!")

    @classmethod
    def process(cls, text: str, matrix: list[list[int]], mode: str = "encrypt") -> tuple[str, str, list[list[int]]]:
        """ش: هنا يتم تقسيم النص إلى كتل، وضرب كل كتلة في المصفوفة modulo 26، وهي طريقة جبرية متقدمة."""
        dim = len(matrix)
        inv_matrix = cls.get_matrix_inverse(matrix)
        op_matrix = matrix if mode == "encrypt" else inv_matrix

        # استخراج الأحرف الإنجليزية فقط مع حفظ مواقع الرموز
        letters_only, positions = TextSanitizer.clean_and_extract(text)
        if not letters_only:
            return "", "لا توجد أحرف صالحة للمعالجة", inv_matrix

        # التعامل مع الحشو الأكاديمي (Padding with X)
        pad_len = (dim - (len(letters_only) % dim)) % dim
        padded_letters = letters_only + ("X" * pad_len)
        
        academic_note = f"Padding: Added {pad_len} 'X' chars" if pad_len > 0 else "Padding: None (Aligned)"

        # معالجة الكتل بالضرب المصفوفي
        result_chars = []
        for i in range(0, len(padded_letters), dim):
            block = [ord(c) - 65 for c in padded_letters[i:i+dim]]
            for r in range(dim):
                val = sum(op_matrix[r][c] * block[c] for c in range(dim)) % 26
                result_chars.append(chr(val + 65))

        final_pure = "".join(result_chars)

        # في حالة التشفير نرجع النص المشفر كاملاً
        # وفي حالة فك التشفير نزيل حروف الحشو X الزائدة في النهاية إذا كان لها موضع
        if mode == "decrypt" and pad_len > 0:
            final_pure = final_pure[:-pad_len]

        restored_text = TextSanitizer.restore_structure(final_pure, positions)
        return restored_text, academic_note, inv_matrix
