# CyberKey Suite Enterprise

منصة متكاملة لتشفير وفك تشفير البيانات، مع أدوات تحليل الأمان، تقييم المفاتيح، اختبار SAC (Avalanche), وتحليل إنتروبيا البيانات. المشروع مصمم كواجهة رسومية Python باستخدام tkinter/customtkinter ويوفر مجموعة من الخوارزميات الكلاسيكية والحديثة.

## وصف المشروع

يحتوي المشروع على:

- خوارزميات كلاسيكية: Caesar, Affine, Multiplicative, Rail Fence, Vigenère, Hill
- خوارزميات حديثة: DES, AES, RSA
- وظائف هاش: SHA, MD5, etc. حسب التنفيذ داخل المشروع
- أدوات تحليل: entropy, brute force, benchmark, quick presets, report export
- واجهة مستخدم عربية/إنجليزية مع دعم ألوان ووضع داكن

## البنية الداخلية

```text
Crypto_Master_Enterprise/
├── algorithms/
│   ├── __init__.py
│   ├── aes_pure.py
│   ├── affine.py
│   ├── caesar.py
│   ├── des_pure.py
│   ├── hashes.py
│   ├── hill_advanced.py
│   ├── multiplicative.py
│   ├── padding.py
│   ├── rail_fence.py
│   ├── rsa_core.py
│   ├── sanitizer.py
│   └── vigenere.py
├── tools/
│   ├── avalanche_visualizer.py
│   ├── benchmark.py
│   ├── brute_force.py
│   ├── entropy_calculator.py
│   ├── report_exporter.py
│   └── smart_generator.py
├── config.py
├── main_gui.py
├── ui_theme.py
├── README.md
└── requirements.txt (إن وجد أو يمكن إنشاؤه يدويًا)
```

## المتطلبات

تأكد من تثبيت Python 3.9+ ثم قم بتثبيت الحزم التالية:

```bash
pip install customtkinter
pip install arabic-reshaper python-bidi
```

إذا كان المشروع يتطلب مكتبات إضافية، يمكنك تثبيتها عبر:

```bash
pip install -r requirements.txt
```

## التشغيل

1. افتح الطرفية داخل مجلد المشروع.
2. شغّل التطبيق الرئيسي:

```bash
python main_gui.py
```

3. ستفتح لك واجهة المشروع الرئيسية حيث يمكنك:
   - اختيار الخوارزمية
   - إدخال النص أو البيانات
   - تشفير أو فك تشفير البيانات
   - استخدام أدوات التحليل السريع
   - تصدير تقارير التدقيق

## الاستخدام السريع

- اختر الخوارزمية من القائمة الجانبية.
- أدخل النص في حقل الإدخال.
- اضغط على زر التشفير أو فك التشفير.
- استخدم زرين التحليل المتقدم مثل:
  - Avalanche (SAC)
  - Entropy
  - Benchmark
  - Smart Key Generator

## ملاحظات مهمة

- المشروع موجه لأغراض التعليم، البحث، والتدقيق الأمني.
- لا يُستخدم كبديل للمعايير التجارية الاحترافية في البيئة الإنتاجية.
- تم تصميم الواجهة بدعم عربي/إنجليزي مع تجربة مستخدم أنيقة.

## المطور

- Engineer: Arafat Al-Kamaly
- Institution: Al-Manar University College
- Year: 2026

## الترخيص

هذا المشروع مخصص للاستخدام التعليمي والبحثي. يرجى احترام حقوق النشر والتطوير عند إعادة الاستخدام.
