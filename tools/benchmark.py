# المسار: tools/benchmark.py
"""
Tool: Performance Benchmarking & High-Precision Latency Timer
المشروع: CyberKey Suite Enterprise
إعداد المهندس: عرفات عبدالله حسين الكاملي | كلية المنار الجامعية
الوصف: قياس زمن التنفيذ الحسابي بدقة النانو ثانية لإجراء المقارنات الأكاديمية.
"""

import time
from typing import Callable, Any, Tuple

class BenchmarkEngine:
    """محرك القياس الزمني اللحظي للخوارزميات الرياضية بدقة متناهية"""

    @staticmethod
    def measure_execution(func: Callable, *args, **kwargs) -> Tuple[Any, float, str]:
        """
        تشغيل الدالة وقياس زمن التنفيذ الصافي:
        يرجع: (نتيجة_الدالة, الزمن_بالملي_ثانية, نص_منسق_للعرض)
        """
        start_ns = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_ns = time.perf_counter_ns()

        duration_ns = end_ns - start_ns
        duration_ms = duration_ns / 1_000_000.0
        duration_us = duration_ns / 1_000.0

        # التنسيق التلقائي للوحدة بحسب القيمة لسهولة القراءة
        if duration_ms >= 1.0:
            formatted_speed = f"{duration_ms:.3f} ms"
        else:
            formatted_speed = f"{duration_us:.2f} µs"

        return result, duration_ms, formatted_speed
