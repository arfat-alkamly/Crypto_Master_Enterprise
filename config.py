# المسار: config.py
"""
System Configuration: Themes & Localization Dictionary
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
"""

THEMES = {
    "dark": {
        "bg_primary": "#1a1a1a",
        "bg_secondary": "#242424",
        "accent": "#1f538d",
        "text": "#ffffff",
        "card_bg": "#2b2b2b"
    },
    "light": {
        "bg_primary": "#f5f5f5",
        "bg_secondary": "#e5e5e5",
        "accent": "#3b8ed0",
        "text": "#000000",
        "card_bg": "#ffffff"
    }
}

LOCALIZATION = {
    "ar": {
        "title": "منظومة CyberKey Suite Enterprise 2026",
        "encrypt": "تشفير (Encrypt)",
        "decrypt": "فك التشفير (Decrypt)",
        "demo": "نموذج سريع (Quick Demo)",
        "export": "تصدير تقرير التدقيق",
        "input_label": "النص الصريح / المراد معالجته:",
        "output_label": "النتيجة بعد المعالجة:",
        "metrics_time": "زمن التنفيذ الفعلي",
        "metrics_entropy": "إنتروبيا شانون",
        "metrics_keyspace": "فضاء المفاتيح النظري",
        "metrics_sac": "معيار الانهيار الجليدي (SAC)"
    },
    "en": {
        "title": "CyberKey Suite Enterprise 2026",
        "encrypt": "Encrypt",
        "decrypt": "Decrypt",
        "demo": "Quick Demo",
        "export": "Export Audit Report",
        "input_label": "Plaintext / Input Data:",
        "output_label": "Processed Output:",
        "metrics_time": "Execution Time",
        "metrics_entropy": "Shannon Entropy",
        "metrics_keyspace": "Theoretical Key Space",
        "metrics_sac": "Avalanche Criterion (SAC)"
    }
}
