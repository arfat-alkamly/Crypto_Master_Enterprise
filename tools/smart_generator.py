# المسار: tools/smart_generator.py
"""
Tool: Smart Key Generator & Quick Demo Presets
المشروع: CyberKey Suite Enterprise
"""

import math
import random
import string

class SmartKeyGenerator:
    @staticmethod
    def generate_caesar() -> int:
        return random.randint(1, 25)

    @staticmethod
    def generate_multiplicative() -> int:
        valid_keys = [k for k in range(3, 26) if math.gcd(k, 26) == 1]
        return random.choice(valid_keys)

    @staticmethod
    def generate_affine() -> tuple[int, int]:
        valid_a = [k for k in range(3, 26) if math.gcd(k, 26) == 1]
        a = random.choice(valid_a)
        b = random.randint(1, 25)
        return a, b

    @staticmethod
    def generate_rail_fence(text_len: int = 15) -> int:
        max_r = min(5, max(2, text_len - 1))
        return random.randint(2, max_r)

    @staticmethod
    def generate_vigenere(length: int = 6) -> str:
        return "".join(random.choices(string.ascii_uppercase, k=length))

    @staticmethod
    def generate_hill_2x2() -> list[list[int]]:
        while True:
            m = [[random.randint(1, 15) for _ in range(2)] for _ in range(2)]
            det = (m[0][0] * m[1][1] - m[0][1] * m[1][0]) % 26
            if det != 0 and math.gcd(det, 26) == 1:
                return m

    @staticmethod
    def generate_hill_3x3() -> list[list[int]]:
        while True:
            m = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
            det = (
                m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
                m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
                m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
            ) % 26
            if det != 0 and math.gcd(det, 26) == 1:
                return m

    @staticmethod
    def generate_des_key() -> str:
        return "".join(random.choices(string.ascii_letters + string.digits, k=8))

    @staticmethod
    def generate_aes_key(bits: int = 128) -> str:
        length = 16 if bits == 128 else 32
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))


class QuickDemoPresets:
    PRESETS = {
        "Caesar": {"text": "CyberKey Suite: Al-Manar University 2026!", "key": 3},
        "Multiplicative": {"text": "Academic Cryptography Pure Python Engine", "key": 7},
        "Affine": {"text": "Network Security & Cryptographic Lab", "key_a": 5, "key_b": 8},
        "RailFence": {"text": "TOP SECRET MILITARY DATA TRANSMISSION", "rails": 3},
        "Vigenere": {"text": "CONFIDENTIAL PROJECT DEFENSE BRIEFING", "key": "MANAR"},
        "Hill": {"text": "SECURITYEXPERT", "matrix": [[3, 2], [5, 7]]},
        "DES": {"text": "CyberKey Suite Enterprise Core System 2026", "key": "Arafat26"},
        "AES": {"text": "Military Grade Classified Payload AES-256 / AES-128", "key": "ArafatAlKamaly26CyberSecurity2026"},
        "RSA": {"text": "Al-Manar Academic OS RSA Demo", "bits": 14},
        "Hashes": {"text": "Verify Cryptographic Integrity and Immutability"}
    }

    @classmethod
    def get_preset(cls, algo_name: str) -> dict:
        return cls.PRESETS.get(algo_name, {})
