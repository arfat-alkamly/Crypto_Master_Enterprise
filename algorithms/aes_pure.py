# المسار: algorithms/aes_pure.py
"""
Algorithm: Advanced Encryption Standard (AES-128 & AES-256 Pure Python)
FIPS-197 Standard Compliant Implementation
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
"""

from .padding import PKCS7

class AESCipher:
    """محرك AES الصافي بنظامي 128-بت (10 دورات) و 256-بت (14 دورة) بدون مكاتب خارجية"""

    S_BOX = [
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
        0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
        0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
        0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
        0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5E, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
        0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
        0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
    ]

    INV_S_BOX = [0] * 256
    for i, val in enumerate(S_BOX):
        INV_S_BOX[val] = i

    R_CON = [
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A
    ]

    @classmethod
    def _sub_word(cls, word: list[int]) -> list[int]:
        return [cls.S_BOX[b] for b in word]

    @classmethod
    def _rot_word(cls, word: list[int]) -> list[int]:
        return word[1:] + word[:1]

    @classmethod
    def _key_expansion(cls, key_bytes: bytes) -> list[list[int]]:
        # شرح للمناقشة: AES يبني مفاتيح كل دورة (Round Keys) من المفتاح الأساسي عبر عمليات Rotate و Substitution و XOR.
        # هذا هو السبب الرئيسي في قوة AES مقارنة بالشفرات الكلاسيكية القديمة.
        key_len = len(key_bytes)
        if key_len == 16:
            Nk, Nr = 4, 10
        elif key_len == 32:
            Nk, Nr = 8, 14
        else:
            raise ValueError(f"طول مفتاح AES يجب أن يكون 16 بايت (AES-128) أو 32 بايت (AES-256)! تم إدخال {key_len} بايت.")

        w = []
        for i in range(Nk):
            w.append([key_bytes[4*i], key_bytes[4*i+1], key_bytes[4*i+2], key_bytes[4*i+3]])

        for i in range(Nk, 4 * (Nr + 1)):
            temp = w[i - 1].copy()
            if i % Nk == 0:
                temp = cls._sub_word(cls._rot_word(temp))
                temp[0] ^= cls.R_CON[i // Nk]
            elif Nk > 6 and (i % Nk == 4):
                temp = cls._sub_word(temp)
            w.append([w[i - Nk][j] ^ temp[j] for j in range(4)])

        round_keys = []
        for r in range(Nr + 1):
            rk = []
            for c in range(4):
                rk.extend(w[r * 4 + c])
            round_keys.append(rk)
        return round_keys

    @classmethod
    def _add_round_key(cls, state: list[list[int]], round_key: list[int]):
        for c in range(4):
            for r in range(4):
                state[r][c] ^= round_key[c * 4 + r]

    @classmethod
    def _sub_bytes(cls, state: list[list[int]]):
        for r in range(4):
            for c in range(4):
                state[r][c] = cls.S_BOX[state[r][c]]

    @classmethod
    def _inv_sub_bytes(cls, state: list[list[int]]):
        for r in range(4):
            for c in range(4):
                state[r][c] = cls.INV_S_BOX[state[r][c]]

    @classmethod
    def _shift_rows(cls, state: list[list[int]]):
        state[1] = state[1][1:] + state[1][:1]
        state[2] = state[2][2:] + state[2][:2]
        state[3] = state[3][3:] + state[3][:3]

    @classmethod
    def _inv_shift_rows(cls, state: list[list[int]]):
        state[1] = state[1][-1:] + state[1][:-1]
        state[2] = state[2][-2:] + state[2][:-2]
        state[3] = state[3][-3:] + state[3][:-3]

    @staticmethod
    def _xtime(a: int) -> int:
        return ((a << 1) ^ 0x1B) & 0xFF if (a & 0x80) else (a << 1) & 0xFF

    @classmethod
    def _mul(cls, a: int, b: int) -> int:
        res = 0
        for _ in range(8):
            if b & 1:
                res ^= a
            a = cls._xtime(a)
            b >>= 1
        return res

    @classmethod
    def _mix_columns(cls, state: list[list[int]]):
        for c in range(4):
            s0, s1, s2, s3 = state[0][c], state[1][c], state[2][c], state[3][c]
            state[0][c] = cls._xtime(s0) ^ (cls._xtime(s1) ^ s1) ^ s2 ^ s3
            state[1][c] = s0 ^ cls._xtime(s1) ^ (cls._xtime(s2) ^ s2) ^ s3
            state[2][c] = s0 ^ s1 ^ cls._xtime(s2) ^ (cls._xtime(s3) ^ s3)
            state[3][c] = (cls._xtime(s0) ^ s0) ^ s1 ^ s2 ^ cls._xtime(s3)

    @classmethod
    def _inv_mix_columns(cls, state: list[list[int]]):
        for c in range(4):
            s0, s1, s2, s3 = state[0][c], state[1][c], state[2][c], state[3][c]
            state[0][c] = cls._mul(s0, 0x0E) ^ cls._mul(s1, 0x0B) ^ cls._mul(s2, 0x0D) ^ cls._mul(s3, 0x09)
            state[1][c] = cls._mul(s0, 0x09) ^ cls._mul(s1, 0x0E) ^ cls._mul(s2, 0x0B) ^ cls._mul(s3, 0x0D)
            state[2][c] = cls._mul(s0, 0x0D) ^ cls._mul(s1, 0x09) ^ cls._mul(s2, 0x0E) ^ cls._mul(s3, 0x0B)
            state[3][c] = cls._mul(s0, 0x0B) ^ cls._mul(s1, 0x0D) ^ cls._mul(s2, 0x09) ^ cls._mul(s3, 0x0E)

    @classmethod
    def _encrypt_block(cls, block: bytes, round_keys: list[list[int]]) -> bytes:
        Nr = len(round_keys) - 1
        state = [[block[c * 4 + r] for c in range(4)] for r in range(4)]
        cls._add_round_key(state, round_keys[0])

        for r in range(1, Nr):
            cls._sub_bytes(state)
            cls._shift_rows(state)
            cls._mix_columns(state)
            cls._add_round_key(state, round_keys[r])

        cls._sub_bytes(state)
        cls._shift_rows(state)
        cls._add_round_key(state, round_keys[Nr])

        out = bytearray(16)
        for c in range(4):
            for r in range(4):
                out[c * 4 + r] = state[r][c]
        return bytes(out)

    @classmethod
    def _decrypt_block(cls, block: bytes, round_keys: list[list[int]]) -> bytes:
        Nr = len(round_keys) - 1
        state = [[block[c * 4 + r] for c in range(4)] for r in range(4)]
        cls._add_round_key(state, round_keys[Nr])

        for r in range(Nr - 1, 0, -1):
            cls._inv_shift_rows(state)
            cls._inv_sub_bytes(state)
            cls._add_round_key(state, round_keys[r])
            cls._inv_mix_columns(state)

        cls._inv_shift_rows(state)
        cls._inv_sub_bytes(state)
        cls._add_round_key(state, round_keys[0])

        out = bytearray(16)
        for c in range(4):
            for r in range(4):
                out[c * 4 + r] = state[r][c]
        return bytes(out)

    @classmethod
    def encrypt(cls, plaintext: str, key_str: str) -> str:
        # شرح للمناقشة: AES يقطع النص إلى كتل 128-bit ويطبق عمليات SubBytes و ShiftRows و MixColumns.
        # هذه هي الصور الأساسية للتشفير الحديث الذي يستخدم في التطبيقات الأمنية الحالية.
        key_bytes = key_str.encode("utf-8")
        round_keys = cls._key_expansion(key_bytes)
        padded_data = PKCS7.pad(plaintext.encode("utf-8"), block_size=16)

        ciphertext = bytearray()
        for i in range(0, len(padded_data), 16):
            block = padded_data[i:i+16]
            ciphertext.extend(cls._encrypt_block(block, round_keys))
        return ciphertext.hex().upper()

    @classmethod
    def decrypt(cls, cipher_hex: str, key_str: str) -> str:
        key_bytes = key_str.encode("utf-8")
        round_keys = cls._key_expansion(key_bytes)
        clean_hex = "".join(cipher_hex.split())
        ciphertext_bytes = bytes.fromhex(clean_hex)

        if len(ciphertext_bytes) % 16 != 0:
            raise ValueError("طول النص المشفر يجب أن يكون من مضاعفات 16 بايت!")

        decrypted_bytes = bytearray()
        for i in range(0, len(ciphertext_bytes), 16):
            block = ciphertext_bytes[i:i+16]
            decrypted_bytes.extend(cls._decrypt_block(block, round_keys))

        unpadded_data = PKCS7.unpad(decrypted_bytes, block_size=16)
        return unpadded_data.decode("utf-8", errors="replace")

# للتوافقية
AES128Cipher = AESCipher
