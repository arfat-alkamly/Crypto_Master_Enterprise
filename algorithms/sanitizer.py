# المسار: algorithms/sanitizer.py
"""
Text Sanitizer & Symbol/Whitespace Preservation Engine
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: عزل الحروف الصالحة للتشفير وتوثيق مواضع المسافات والرموز لإعادتها بعد المعالجة بدقة 100%.
"""

class TextSanitizer:
    @staticmethod
    def clean_and_extract(text: str) -> tuple[str, list[tuple[int, str]]]:
        """
        استخراج الأحرف الإنجليزية الكبيرة فقط، وحفظ مواضع الرموز والمسافات وحالة الأحرف
        """
        letters = []
        positions = []
        
        for idx, ch in enumerate(text):
            if ch.isalpha() and ch.isascii():
                # حفظ حالة الحرف (كبير أو صغير)
                letters.append(ch.upper())
                positions.append((idx, "UPPER" if ch.isupper() else "LOWER"))
            else:
                # حفظ الرمز أو المسافة كما هي
                positions.append((idx, ch))
                
        return "".join(letters), positions

    @staticmethod
    def restore_structure(processed_letters: str, positions: list[tuple[int, str]]) -> str:
        """
        إعادة دمج الأحرف المعالجة في أماكنها الأصلية مع الحفاظ على الرموز وحالة الأحرف
        """
        result = []
        letter_idx = 0
        total_letters = len(processed_letters)

        for _, item in positions:
            if item in ("UPPER", "LOWER"):
                if letter_idx < total_letters:
                    ch = processed_letters[letter_idx]
                    result.append(ch.upper() if item == "UPPER" else ch.lower())
                    letter_idx += 1
            else:
                result.append(item)

        # إضافة أي حروف إضافية ناتجة عن الحشو في نهاية النص
        if letter_idx < total_letters:
            result.append(processed_letters[letter_idx:])

        return "".join(result)
