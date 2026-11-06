# المسار: tools/report_exporter.py
"""
Tool: Cryptographic Audit & Lab Report Exporter
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: توليد وتصدير تقرير التدقيق المخبري المعتمد بصيغة نصية رسمية.
"""

from datetime import datetime

class ReportExporter:
    @staticmethod
    def generate_report(
        algo_name: str,
        operation: str,
        input_text: str,
        output_text: str,
        key_info: str,
        metrics: dict
    ) -> str:
        """توليد نص التقرير المخبري الموثق"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report = f"""================================================================================
           CYBERKEY SUITE ENTERPRISE - LAB AUDIT REPORT
================================================================================
تاريخ ووقت الفحص: {timestamp}
إعداد المهندس     : عرفات عبدالله حسين الكاملي
التخصص الأكاديمي  : الأمن السيبراني وشبكات الحاسوب
المؤسسة التعليمية : كلية المنار الجامعية
--------------------------------------------------------------------------------
1. التوصيف الفني للخوارزمية (Algorithm Specification):
   - الخوارزمية     : {algo_name}
   - نوع العملية    : {operation}
   - إعدادات المفتاح: {key_info}

2. فحص وتدقيق البيانات (Data Payload):
   - النص المدخل:
{input_text}
   - مخرجات المعالجة:
{output_text}

3. التحليلات الأمنية والحسابية (Cryptographic & Security Metrics):
   - زمن المعالجة الفعلي (Execution Time) : {metrics.get('speed', 'N/A')}
   - إنتروبيا شانون (Shannon Entropy)      : {metrics.get('entropy', 'N/A')}
   - فضاء المفاتيح (Key Space Size)       : {metrics.get('keyspace', 'N/A')}
   - زمن الكسر النظري (Est. Brute-Force)  : {metrics.get('cracktime', 'N/A')}
   - معيار الانهيار الجليدي (SAC / Diff)  : {metrics.get('avalanche', 'N/A')}

--------------------------------------------------------------------------------
ملاحظة تقنية: تم إنشاء وتنفيذ هذا الفحص عبر نواة بايثون الصرفة (Pure Python Core)
وفق معايير التشفير والنزاهة الرقمية المعتمدة أكاديمياً.
================================================================================
"""
        return report

    @classmethod
    def save_report_to_file(cls, filename: str, report_content: str) -> str:
        """حفظ التقرير إلى ملف خارجي بترميز UTF-8"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report_content)
        return filename
