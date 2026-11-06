# المسار: ui_theme.py
"""
Theme, HCI Palette, Accessibility & Bilingual Localization (AR / EN)
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
التخصص: الأمن السيبراني وشبكات الحاسوب
"""

THEME_COLORS = {
    "bg_base": "#070a12",
    "bg_card": "#111726",
    "bg_input": "#0b111e",
    "border": "#1f293d",
    "cyan_accent": "#00e5ff",
    "blue_accent": "#0284c7",
    "text_main": "#f8fafc",
    "text_muted": "#94a3b8",
    "btn_encrypt": "#059669",
    "btn_decrypt": "#4338ca",
    "danger": "#e11d48",
    "success": "#10b981",
    "warning": "#f59e0b",
    "matrix_inv": "#1e1b4b",
}

FONT_TITLE = ("Segoe UI", 13, "bold")
FONT_SUBTITLE = ("Segoe UI", 9, "normal")
FONT_BUTTON = ("Segoe UI", 10, "bold")
FONT_MONO = ("Consolas", 10, "normal")
FONT_BADGE = ("Segoe UI", 9, "bold")
FONT_TOOLTIP = ("Segoe UI", 8, "normal")

LANG_DICT = {
    "ar": {
        "title": "CYBERKEY SUITE | منصة التشفير والتحليل الأكاديمي",
        "subtitle": "نواة بايثون صرفة * خالٍ من المكتبات الخارجية * معايير HCI * حماية من الانهيار",
        "eng_name": "المهندس: عرفات عبدالله حسين الكاملي",
        "college_dept": "الأمن السيبراني والشبكات | كلية المنار الجامعية",
        "algos_header": "الخوارزميات المعتمدة",
        "input_label": "النص المراد معالجته (صريح / مشفر):",
        "keys_label": "الضوابط الرياضية للمفتاح وإعدادات المصفوفة:",
        "encrypt_btn": "🔒 تشفير البيانات (Encrypt)",
        "decrypt_btn": "🔓 فك التشفير (Decrypt)",
        "output_label": "المخرجات ونتائج الفحص والتحليل:",
        "copy_btn": "📋 نسخ",
        "copied": "تم النسخ ✓",
        "export_btn": "📄 تصدير تقرير التدقيق (.txt)",
        "preset_btn": "⚡ تجربة سريعة نموذجية",
        "autogen_key": "🎲 توليد مفتاح صالح تلقائياً",
        "key_valid": "✓ [المفتاح صالح رياضياً]",
        "key_invalid": "✕ [المفتاح غير صالح رياضياً]",
        "dim_mode": "أبعاد هيل:",
        "toggle_lang": "Switch to English",
        "status_ready": "الحالة: جاهز للتشغيل | الحساب النمطي والكتلي مدقق | صمام الأمان نشط",
        "mat_k_title": "مصفوفة المفتاح (K):",
        "mat_inv_title": "مصفوفة المعكوس النمطي (K⁻¹ mod 26):",
        "metric_speed": "زمن التنفيذ:",
        "metric_entropy": "إنتروبيا شانون:",
        "metric_keyspace": "فضاء المفاتيح:",
        "metric_cracktime": "زمن الكسر التقديري:",
    },
    "en": {
        "title": "CYBERKEY SUITE | ACADEMIC CRYPTO PLATFORM",
        "subtitle": "Pure Python Core * Zero External Crypto Libs * HCI Standard * Fail-Safe Engine",
        "eng_name": "Eng. Arafat Abdullah Al-Kamaly",
        "college_dept": "Cybersecurity & Networks | Al-Manar University College",
        "algos_header": "SUPPORTED ALGORITHMS",
        "input_label": "Input Text (Plaintext / Ciphertext):",
        "keys_label": "Dynamic Mathematical Keys & Dimension Selector:",
        "encrypt_btn": "🔒 ENCRYPT DATA",
        "decrypt_btn": "🔓 DECRYPT DATA",
        "output_label": "Cryptographic Output & Analytical Metrics:",
        "copy_btn": "📋 Copy",
        "copied": "Copied ✓",
        "export_btn": "📄 Export Audit (.txt)",
        "preset_btn": "⚡ Quick Demo Preset",
        "autogen_key": "🎲 Auto-Gen Valid Key",
        "key_valid": "✓ [Mathematical Constraints Satisfied]",
        "key_invalid": "✕ [Invalid Key Constraints]",
        "dim_mode": "Hill Dim:",
        "toggle_lang": "تحويل إلى العربية",
        "status_ready": "Status: Operational | Modulo Arithmetic Verified | Fail-Safe Active",
        "mat_k_title": "Key Matrix (K):",
        "mat_inv_title": "Modular Inverse Matrix (K⁻¹ mod 26):",
        "metric_speed": "Latency (Speed):",
        "metric_entropy": "Shannon Entropy:",
        "metric_keyspace": "Key Space Size:",
        "metric_cracktime": "Est. Brute-Force:",
    }
}

TOOLTIPS_INFO = {
    "shannon_entropy": "مقياس عدم اليقين والعشوائية لشانون (0 - 8 بت/بايت). القيم فوق 7.5 تشير لتشتت كامل واستحالة التحليل الترددي.",
    "avalanche_sac": "معيار التشتت الصارم (Strict Avalanche Criterion): تغيير بت واحد بالمدخل يؤدي لتغيير 50% من بتات المخرج.",
    "matrix_det": "محدد مصفوفة المفتاح: يجب ألا يساوي صفراً وأن يكون أولياً نسبياً مع 26 (gcd(det, 26) == 1) لضمان وجود المعكوس الضربي.",
    "pkcs7": "معيار الحشو القياسي للكتل: يكمل الكتلة الناقصة ببايتات تحمل قيمة النقص ذاته لضمان استرجاع النص بدقة 100%.",
    "brute_force_time": "معادلة Stallings لزمن الكسر النظري: T = N / (2 * R) حيث N فضاء المفاتيح و R معدل التخمين."
}
