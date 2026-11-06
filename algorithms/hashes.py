# المسار: algorithms/hashes.py
"""
Algorithm: Cryptographic Hashing Engine (MD5, SHA-256, SHA-512)
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: محرك استخراج بصمات الهاش المعيارية الثلاث لحفظ النزاهة الرقمية.
"""

import hashlib

class HashEngine:


    @staticmethod
    def md5(text: str) -> str:
        """إرجاع هاش MD5 للنص المحدد كـ hex string."""
        return hashlib.md5(text.encode("utf-8")).hexdigest()

    @staticmethod
    def sha256(text: str) -> str:
        """إرجاع هاش SHA-256 للنص المحدد كـ hex string."""
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    @staticmethod
    def sha512(text: str) -> str:
        """إرجاع هاش SHA-512 للنص المحدد كـ hex string."""
        return hashlib.sha512(text.encode("utf-8")).hexdigest()

    @staticmethod
    def compute_all(text: str) -> dict:
        
        return {
            "MD5": HashEngine.md5(text),
            "SHA-256": HashEngine.sha256(text),
            "SHA-512": HashEngine.sha512(text),
        }
