# المسار: tools/brute_force.py
"""
Tool: Brute-Force & Theoretical Key Space Analyzer (English Enterprise)
CyberKey Suite Enterprise - Eng. Arafat Al-Kamaly
"""

class BruteForceEstimator:
    KEY_SPACE_DATA = {
        "Caesar": {
            "keyspace": "25 Keys (26 - 1)",
            "time": "< 0.000001 sec",
            "status": "Vulnerable (Instant Brute-Force)"
        },
        "Multiplicative": {
            "keyspace": "12 Co-Prime Keys",
            "time": "< 0.000001 sec",
            "status": "Vulnerable (Instant Exhaustion)"
        },
        "Affine": {
            "keyspace": "312 Keys (12 x 26)",
            "time": "< 0.00001 sec",
            "status": "Vulnerable (Trivial Attack)"
        },
        "RailFence": {
            "keyspace": "N - 1 Permutations",
            "time": "< 0.0001 sec",
            "status": "Weak (Text Length Dependent)"
        },
        "Vigenere": {
            "keyspace": "26^L Possibilities",
            "time": "Seconds (Kasiski/Friedman Test)",
            "status": "Insecure against Frequency Analysis"
        },
        "Hill": {
            "keyspace": "2x2: ~1.5x10^5 | 3x3: ~5.4x10^12",
            "time": "< 0.05 sec (GPU Linear Algebra)",
            "status": "Vulnerable to Known Plaintext Attack (KPA)"
        },
        "DES": {
            "keyspace": "2^56 (~7.2 x 10^16 Keys)",
            "time": "~56 Hours (EFF Deep Crack)",
            "status": "Deprecated for Modern Standards"
        },
        "AES": {
            "keyspace": "2^128 (~3.4 x 10^38 Keys)",
            "time": "Billions of Years (Universal Limit)",
            "status": "Fully Secure & Globally Certified ✓"
        },
        "RSA": {
            "keyspace": "Hard Integer Factorization of Modulus n",
            "time": "Instant demo (14-bit) / Quantum-Safe 2048+",
            "status": "Secure Standard for Key Exchange"
        },
        "Hashes": {
            "keyspace": "Collision Resistance: 2^128 (SHA-256)",
            "time": "One-Way Function (Irreversible)",
            "status": "Data Integrity Compliant ✓"
        }
    }

    @classmethod
    def analyze(cls, algo_name: str) -> dict:
        return cls.KEY_SPACE_DATA.get(
            algo_name, 
            {"keyspace": "N/A", "time": "N/A", "status": "N/A"}
        )
