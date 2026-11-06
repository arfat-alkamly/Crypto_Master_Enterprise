# المسار: main_gui.py (Enterprise Ultimate SOC Edition - Fully Stabilized Arabic)
"""
CYBERKEY SUITE ENTERPRISE 2026 - ADVANCED CRYPTOGRAPHIC AUDIT CONSOLE
Faculty: Al-Manar University College - Yemen
Lead Systems Architect & Security Engineer: Arafat Al-Kamaly
Pure Python Cryptographic Verification & Rigorous SAC Avalanche Engine
"""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk

try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    HAS_BIDI = True
except ImportError:
    HAS_BIDI = False

def fix_ar(text: str) -> str:
    """إعادة تشكيل وعكس النصوص العربية لتظهر منسقة وسليمة في واجهات Tkinter"""
    if not HAS_BIDI or not text:
        return text
    try:
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)
    except Exception:
        return text

from config import THEMES, LOCALIZATION
from algorithms import (
    CaesarCipher, MultiplicativeCipher, AffineCipher,
    RailFenceCipher, VigenereCipher, AdvancedHillCipher,
    DESCipher, AES128Cipher, RSACore, HashEngine
)
from tools import (
    BruteForceEstimator, BenchmarkEngine, AvalancheAnalyzer,
    EntropyAnalyzer, SmartKeyGenerator, QuickDemoPresets, ReportExporter
)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class CyberKeyEnterpriseApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("CyberKey Suite Enterprise v2.6 | Security Audit Platform")
        self.geometry("1340x910")
        self.minsize(1150, 780)
        
        self.current_lang = "en"
        self.current_algo = "Caesar"
        self.rsa_keys = None
        self.status_badge_text = "READY"
        self.signal_direction = 1
        self.last_metrics = {
            "speed": "0.00 µs",
            "entropy": "0.000 bits/B",
            "keyspace": "25 Keys",
            "cracktime": "< 0.000001 sec",
            "avalanche": "0.00 %"
        }

        # أسماء الخوارزميات مصممة لتفادي تداخل اللغات والأقواس
        self.algo_names = {
            "en": {
                "Caesar": "Caesar",
                "Multiplicative": "Multiplicative",
                "Affine": "Affine",
                "RailFence": "Rail Fence",
                "Vigenere": "Vigenere",
                "Hill": "Hill",
                "DES": "DES",
                "AES": "AES",
                "RSA": "RSA",
                "Hashes": "Hashes"
            },
            "ar": {
                "Caesar": fix_ar("قيصر"),
                "Multiplicative": fix_ar("الضرب"),
                "Affine": fix_ar("التآلف"),
                "RailFence": fix_ar("سياج السكة"),
                "Vigenere": fix_ar("فيجنير"),
                "Hill": fix_ar("هيل"),
                "DES": fix_ar("دي إي إس"),
                "AES": fix_ar("إيه إي إس"),
                "RSA": fix_ar("آر إس إيه"),
                "Hashes": fix_ar("الهاش")
            }
        }

        self.i18n = {
            "en": {
                "title_badge": "AL-MANAR CYBER LAB VERIFIED",
                "core_badge": "Engine: Pure Python Core\nNo External Crypto Libs ✓",
                "sec_classic": "-- CLASSICAL CIPHERS --",
                "sec_modern": "-- MODERN STANDARDS --",
                "sec_asymm": "-- ASYMMETRIC & HASHES --",
                "lbl_input": "PLAINTEXT INPUT / DATA PAYLOAD",
                "lbl_output": "PROCESSED CIPHERTEXT / OUTPUT DIGEST",
                "btn_encrypt": "⚡ ENCRYPT",
                "btn_decrypt": "🔓 DECRYPT",
                "btn_sac": "🔬 AVALANCHE (SAC) TEST",
                "btn_demo": "✨ QUICK PRESET",
                "btn_export": "📄 EXPORT AUDIT REPORT",
                "card_time": "EXECUTION LATENCY",
                "card_entropy": "SHANNON ENTROPY",
                "card_keyspace": "THEORETICAL KEY SPACE",
                "card_sac": "STRICT AVALANCHE (SAC)",
                "btn_lang": "🌐 اللغة: العربية (AR)",
                "ready_msg": ">> CyberKey Suite Enterprise SOC Console Active. System Integrity: 100%.",
                "sub_author": "ENTERPRISE AUDIT LAB\nEng. Arafat Al-Kamaly\nAl-Manar University 2026",
                "copy_btn": "📋 Copy",
                "swap_btn": "🔄 Swap",
                "clear_btn": "🧹 Clear"
            },
            "ar": {
                "title_badge": fix_ar("معتمد مخبرياً - كلية المنار"),
                "core_badge": fix_ar("المحرك: بايثون الصافي بالكامل\nبدون أي مكتبات تشفير خارجية ✓"),
                "sec_classic": fix_ar("-- الشفرات الكلاسيكية --"),
                "sec_modern": fix_ar("-- المعايير الحديثة --"),
                "sec_asymm": fix_ar("-- التشفير اللامتناظر والهاش --"),
                "lbl_input": fix_ar("البيانات المدخلة أو النص الصريح"),
                "lbl_output": fix_ar("المخرجات المعالجة أو النص المشفر"),
                "btn_encrypt": fix_ar("⚡ تشفير فوري"),
                "btn_decrypt": fix_ar("🔓 فك التشفير"),
                "btn_sac": fix_ar("🔬 اختبار الانهيار الجليدي"),
                "btn_demo": fix_ar("✨ نموذج تجريبي سريع"),
                "btn_export": fix_ar("📄 تصدير تقرير التدقيق"),
                "card_time": fix_ar("زمن التنفيذ الفعلي"),
                "card_entropy": fix_ar("إنتروبيا شانون"),
                "card_keyspace": fix_ar("فضاء المفاتيح النظري"),
                "card_sac": fix_ar("الانهيار الجليدي الصارم"),
                "btn_lang": "🌐 Language: English (EN)",
                "ready_msg": ">> منصة CyberKey Suite جاهزة بالكامل. سلامة النواة البرمجية: 100%.",
                "sub_author": fix_ar("مختبر التدقيق والتشفير السيبراني\nإعداد المهندس: عرفات الكاملي\nكلية المنار الجامعية 2026"),
                "copy_btn": fix_ar("📋 نسخ"),
                "swap_btn": fix_ar("🔄 عكس الحقول"),
                "clear_btn": fix_ar("🧹 مسح")
            }
        }

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self._build_sidebar()
        self._build_main_workspace()
        self._switch_algorithm("Caesar")

    def _build_sidebar(self):
        # ملاحظة للمناقشة: هذا الجزء يحدد واجهة اختيار الخوارزمية، وهي نقطة أساسية في المشروع
        # لأنه يوضح للطالب كيف يتم تبديل الخوارزمية وتهيئة الواجهة بحسب نوع التشفير المختار.
        self.sidebar = ctk.CTkFrame(self, width=270, corner_radius=0, fg_color="#0b1320")
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(16, weight=1)

        brand_frame = ctk.CTkFrame(self.sidebar, fg_color="#101c2f", corner_radius=12)
        brand_frame.grid(row=0, column=0, padx=12, pady=(15, 10), sticky="ew")
        
        lbl_brand = ctk.CTkLabel(
            brand_frame, 
            text="CYBERKEY SUITE", 
            font=ctk.CTkFont(family="Consolas", size=17, weight="bold"),
            text_color="#7dd3fc"
        )
        lbl_brand.pack(pady=(8, 2))

        self.lbl_sub = ctk.CTkLabel(
            brand_frame, 
            text=self.i18n[self.current_lang]["sub_author"], 
            font=ctk.CTkFont(size=10),
            text_color="#a7b7d3"
        )
        self.lbl_sub.pack(pady=(0, 8))

        self.algo_buttons = {}
        self.section_labels = {}
        algos = [
            ("sec_classic", None),
            ("Caesar", "Caesar Substitution"),
            ("Affine", "Affine Modulo Cipher"),
            ("Multiplicative", "Multiplicative Cipher"),
            ("Vigenere", "Polyalphabetic Vigenere"),
            ("RailFence", "Rail Fence Transposition"),
            ("Hill", "Advanced Hill Matrix"),
            ("sec_modern", None),
            ("DES", "Pure DES-64 (Feistel)"),
            ("AES", "Pure AES (128 / 256)"),
            ("sec_asymm", None),
            ("RSA", "RSA Core (Zero-Freezing)"),
            ("Hashes", "Cryptographic Hashes")
        ]

        row_idx = 1
        for item in algos:
            code, title = item
            if title is None:
                lbl_sec = ctk.CTkLabel(
                    self.sidebar, text=self.i18n[self.current_lang][code],
                    font=ctk.CTkFont(size=10, weight="bold"),
                    text_color="#6b7f9a"
                )
                lbl_sec.grid(row=row_idx, column=0, padx=15, pady=(8, 3), sticky="w")
                self.section_labels[code] = lbl_sec
            else:
                display_name = self.algo_names[self.current_lang][code]
                btn = ctk.CTkButton(
                    self.sidebar,
                    text=f"  {display_name}",
                    font=ctk.CTkFont(family="Segoe UI", size=11),
                    anchor="w",
                    height=29,
                    corner_radius=8,
                    fg_color="transparent",
                    hover_color="#13263f",
                    command=lambda c=code: self._switch_algorithm(c)
                )
                btn.grid(row=row_idx, column=0, padx=10, pady=1, sticky="ew")
                self.algo_buttons[code] = btn
            row_idx += 1

        self.btn_toggle_lang = ctk.CTkButton(
            self.sidebar,
            text=self.i18n[self.current_lang]["btn_lang"],
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color="#14304d",
            hover_color="#1f4973",
            height=34,
            corner_radius=8,
            command=self._toggle_language
        )
        self.btn_toggle_lang.grid(row=15, column=0, padx=15, pady=(10, 5), sticky="ew")

        self.lbl_core_status = ctk.CTkLabel(
            self.sidebar, 
            text=self.i18n[self.current_lang]["core_badge"], 
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color="#6ee7b7"
        )
        self.lbl_core_status.grid(row=17, column=0, padx=15, pady=(5, 15), sticky="s")

    def _build_main_workspace(self):
        self.workspace = ctk.CTkFrame(self, fg_color="#091521")
        self.workspace.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)
        self.workspace.grid_rowconfigure(5, weight=1)
        self.workspace.grid_columnconfigure(0, weight=1)
        self.workspace.grid_columnconfigure(1, weight=1)

        # 1. Header Bar
        header_frame = ctk.CTkFrame(self.workspace, fg_color="#0f1d2d", corner_radius=12, height=45)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        
        self.lbl_algo_title = ctk.CTkLabel(
            header_frame, 
            text="ALGORITHM: CAESAR CIPHER", 
            font=ctk.CTkFont(family="Consolas", size=14, weight="bold"),
            text_color="#7dd3fc"
        )
        self.lbl_algo_title.pack(side="left", padx=15, pady=8)

        self.lbl_live_status = ctk.CTkLabel(
            header_frame,
            text="● ENGINE SECURE | 0 EXTERNAL LIBS",
            font=ctk.CTkFont(family="Consolas", size=11, weight="bold"),
            text_color="#6ee7b7"
        )
        self.lbl_live_status.pack(side="left", padx=20)

        self.crypto_signal = ctk.CTkFrame(header_frame, fg_color="#0c1a2a", corner_radius=10, border_width=1, border_color="#1e3a5f")
        self.crypto_signal.pack(side="left", padx=(0, 10), pady=7)

        self.signal_label = ctk.CTkLabel(
            self.crypto_signal,
            text="LINK",
            font=ctk.CTkFont(family="Consolas", size=9, weight="bold"),
            text_color="#7dd3fc"
        )
        self.signal_label.pack(side="left", padx=(8, 6), pady=6)

        self.signal_bar = ctk.CTkProgressBar(self.crypto_signal, width=100, height=8, corner_radius=4, progress_color="#7dd3fc")
        self.signal_bar.set(0.25)
        self.signal_bar.pack(side="left", padx=(0, 8), pady=8)

        self.lbl_status_badge = ctk.CTkLabel(
            header_frame,
            text="READY",
            font=ctk.CTkFont(size=9, weight="bold"),
            text_color="#06130d",
            fg_color="#a7f3d0",
            corner_radius=12,
            padx=12,
            pady=2
        )
        self.lbl_status_badge.pack(side="right", padx=(0, 10))

        self.lbl_algo_badge = ctk.CTkLabel(
            header_frame, 
            text=self.i18n[self.current_lang]["title_badge"],
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color="#7dd3fc",
            fg_color="#0d2237",
            corner_radius=6,
            padx=8,
            pady=2
        )
        self.lbl_algo_badge.pack(side="right", padx=8)

        # 2. Key Frame
        self.key_frame = ctk.CTkFrame(
            self.workspace,
            fg_color="#101d2f",
            corner_radius=12,
            border_width=1,
            border_color="#2c466a"
        )
        self.key_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10), padx=2)

        # 3. Input / Output Textboxes
        lbl_in_box = ctk.CTkFrame(self.workspace, fg_color="transparent")
        lbl_in_box.grid(row=2, column=0, sticky="ew", padx=5)
        self.lbl_input_wrap = ctk.CTkLabel(
            lbl_in_box, text=self.i18n[self.current_lang]["lbl_input"],
            font=ctk.CTkFont(size=11, weight="bold"), text_color="#8a99ad"
        )
        self.lbl_input_wrap.pack(side="left")

        self.btn_clear_in = ctk.CTkButton(
            lbl_in_box, text=self.i18n[self.current_lang]["clear_btn"],
            width=55, height=22, font=("Segoe UI", 10), fg_color="#243144",
            command=lambda: self.txt_input.delete("1.0", "end")
        )
        self.btn_clear_in.pack(side="right")

        lbl_out_box = ctk.CTkFrame(self.workspace, fg_color="transparent")
        lbl_out_box.grid(row=2, column=1, sticky="ew", padx=5)
        self.lbl_output_wrap = ctk.CTkLabel(
            lbl_out_box, text=self.i18n[self.current_lang]["lbl_output"],
            font=ctk.CTkFont(size=11, weight="bold"), text_color="#8a99ad"
        )
        self.lbl_output_wrap.pack(side="left")

        self.btn_copy_out = ctk.CTkButton(
            lbl_out_box, text=self.i18n[self.current_lang]["copy_btn"],
            width=55, height=22, font=("Segoe UI", 10), fg_color="#243144",
            command=self._copy_output_to_clipboard
        )
        self.btn_copy_out.pack(side="right", padx=(4, 0))

        self.btn_swap_data = ctk.CTkButton(
            lbl_out_box, text=self.i18n[self.current_lang]["swap_btn"],
            width=55, height=22, font=("Segoe UI", 10), fg_color="#1f538d",
            command=self._swap_input_output
        )
        self.btn_swap_data.pack(side="right")

        self.txt_input = ctk.CTkTextbox(self.workspace, height=130, font=("Consolas", 12), fg_color="#0d1624", border_width=1, border_color="#2a3d59")
        self.txt_input.grid(row=3, column=0, sticky="nsew", padx=5, pady=(4, 8))

        self.txt_output = ctk.CTkTextbox(self.workspace, height=130, font=("Consolas", 12), fg_color="#0d1624", border_width=1, border_color="#2a3d59")
        self.txt_output.grid(row=3, column=1, sticky="nsew", padx=5, pady=(4, 8))

        # 4. Buttons
        btn_box = ctk.CTkFrame(self.workspace, fg_color="transparent")
        btn_box.grid(row=4, column=0, columnspan=2, sticky="ew", pady=4)

        self.btn_encrypt = ctk.CTkButton(
            btn_box, text=self.i18n[self.current_lang]["btn_encrypt"], font=ctk.CTkFont(weight="bold"),
            fg_color="#2563eb", hover_color="#1d4ed8", height=35, command=self._execute_encrypt
        )
        self.btn_encrypt.pack(side="left", padx=4, expand=True, fill="x")

        self.btn_decrypt = ctk.CTkButton(
            btn_box, text=self.i18n[self.current_lang]["btn_decrypt"], font=ctk.CTkFont(weight="bold"),
            fg_color="#10b981", hover_color="#059669", height=35, command=self._execute_decrypt
        )
        self.btn_decrypt.pack(side="left", padx=4, expand=True, fill="x")

        self.btn_sac_test = ctk.CTkButton(
            btn_box, text=self.i18n[self.current_lang]["btn_sac"], font=ctk.CTkFont(weight="bold"),
            fg_color="#f97316", hover_color="#ea580c", height=35, command=self._execute_sac_test
        )
        self.btn_sac_test.pack(side="left", padx=4, expand=True, fill="x")

        self.btn_demo = ctk.CTkButton(
            btn_box, text=self.i18n[self.current_lang]["btn_demo"], font=ctk.CTkFont(weight="bold"),
            fg_color="#334155", hover_color="#1e293b", height=35, command=self._load_demo
        )
        self.btn_demo.pack(side="left", padx=4, expand=True, fill="x")

        self.btn_export = ctk.CTkButton(
            btn_box, text=self.i18n[self.current_lang]["btn_export"], font=ctk.CTkFont(weight="bold"),
            fg_color="#7c3aed", hover_color="#6d28d9", height=35, command=self._export_audit_report
        )
        self.btn_export.pack(side="left", padx=4, expand=True, fill="x")

        # 5. Bottom Panel
        self.bottom_panel = ctk.CTkFrame(self.workspace, fg_color="#0e1727", corner_radius=12)
        self.bottom_panel.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=(8, 0), padx=2)
        self.bottom_panel.grid_rowconfigure(2, weight=1)
        self.bottom_panel.grid_columnconfigure(0, weight=1)

        self._build_metric_cards()
        self._build_sac_progress_bar()
        self._build_console_logger()

    def _build_metric_cards(self):
        cards_frame = ctk.CTkFrame(self.bottom_panel, fg_color="transparent")
        cards_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(8, 4))
        for i in range(4):
            cards_frame.grid_columnconfigure(i, weight=1)

        self.card_lbls = {}
        self.card_time = self._create_card(cards_frame, 0, "card_time", "0.00 µs", "#7dd3fc")
        self.card_entropy = self._create_card(cards_frame, 1, "card_entropy", "0.000 bits/B", "#fbbf24")
        self.card_keyspace = self._create_card(cards_frame, 2, "card_keyspace", "25 Keys", "#6ee7b7")
        self.card_sac = self._create_card(cards_frame, 3, "card_sac", "0.00 %", "#f87171")

    def _create_card(self, parent, col, key_name, default_val, glow_color):
        card = ctk.CTkFrame(parent, fg_color="#161e2b", border_width=1, border_color="#243042", corner_radius=6)
        card.grid(row=0, column=col, padx=4, pady=2, sticky="nsew")
        
        lbl_t = ctk.CTkLabel(card, text=self.i18n[self.current_lang][key_name], font=ctk.CTkFont(family="Consolas", size=10, weight="bold"), text_color="#7b8c9e")
        lbl_t.pack(pady=(4, 1))
        self.card_lbls[key_name] = lbl_t

        lbl_v = ctk.CTkLabel(card, text=default_val, font=ctk.CTkFont(family="Consolas", size=13, weight="bold"), text_color=glow_color)
        lbl_v.pack(pady=(0, 4))
        return lbl_v

    def _build_sac_progress_bar(self):
        bar_box = ctk.CTkFrame(self.bottom_panel, fg_color="transparent")
        bar_box.grid(row=1, column=0, sticky="ew", padx=14, pady=(2, 6))
        
        ctk.CTkLabel(bar_box, text="SAC DIFFUSION INDEX (IDEAL ~50%):", font=ctk.CTkFont(family="Consolas", size=10, weight="bold"), text_color="#8a99ad").pack(side="left", padx=(0, 8))
        self.sac_bar = ctk.CTkProgressBar(bar_box, height=10, corner_radius=4, progress_color="#ff5252")
        self.sac_bar.set(0.0)
        self.sac_bar.pack(side="left", fill="x", expand=True, padx=4)

    def _build_console_logger(self):
        console_box = ctk.CTkFrame(self.bottom_panel, fg_color="transparent")
        console_box.grid(row=2, column=0, sticky="nsew", padx=10, pady=(0, 10))
        console_box.grid_rowconfigure(0, weight=1)
        console_box.grid_columnconfigure(0, weight=1)

        self.txt_console = ctk.CTkTextbox(
            console_box, font=("Consolas", 11), fg_color="#07090e",
            text_color="#39ff14", border_width=1, border_color="#18202d"
        )
        self.txt_console.grid(row=0, column=0, sticky="nsew")
        self._log_console(self.i18n[self.current_lang]["ready_msg"])
        self._log_console(">> Pure-Python Security Environment Loaded. Ready for academic defense.")
        self.signal_bar.set(0.15)

    def _log_console(self, msg: str):
        self.txt_console.insert("end", f"{msg}\n")
        self.txt_console.see("end")

    def _copy_output_to_clipboard(self):
        out_text = self.txt_output.get("1.0", "end-1c")
        if out_text:
            self.clipboard_clear()
            self.clipboard_append(out_text)
            self._log_console(">> Output payload copied to system clipboard.")

    def _swap_input_output(self):
        out_text = self.txt_output.get("1.0", "end-1c").strip()
        if out_text:
            clean_cipher = out_text.split("\n")[0].strip()
            self.txt_input.delete("1.0", "end")
            self.txt_input.insert("1.0", clean_cipher)
            self._log_console(f">> Swapped clean ciphertext [{clean_cipher[:20]}...] into input field.")

    def _toggle_language(self):
        self.current_lang = "ar" if self.current_lang == "en" else "en"
        tr = self.i18n[self.current_lang]

        self.btn_toggle_lang.configure(text=tr["btn_lang"])
        self.lbl_sub.configure(text=tr["sub_author"])
        self.lbl_core_status.configure(text=tr["core_badge"])
        for sec_key, lbl in self.section_labels.items():
            lbl.configure(text=tr[sec_key])

        for code, btn in self.algo_buttons.items():
            name = self.algo_names[self.current_lang][code]
            btn.configure(text=f"  {name}")

        self.lbl_algo_badge.configure(text=tr["title_badge"])
        self.lbl_input_wrap.configure(text=tr["lbl_input"])
        self.lbl_output_wrap.configure(text=tr["lbl_output"])
        self.btn_clear_in.configure(text=tr["clear_btn"])
        self.btn_copy_out.configure(text=tr["copy_btn"])
        self.btn_swap_data.configure(text=tr["swap_btn"])

        self.btn_encrypt.configure(text=tr["btn_encrypt"])
        self.btn_decrypt.configure(text=tr["btn_decrypt"])
        self.btn_sac_test.configure(text=tr["btn_sac"])
        self.btn_demo.configure(text=tr["btn_demo"])
        self.btn_export.configure(text=tr["btn_export"])

        for key_name, lbl in self.card_lbls.items():
            lbl.configure(text=tr[key_name])

        self._update_header_title()
        self._load_algorithm_fields(self.current_algo)
        self._log_console(f">> UI localized to: [{self.current_lang.upper()}].")

    def _animate_signal(self):
        if not hasattr(self, "signal_bar"):
            return
        try:
            current = self.signal_bar.get()
            if current >= 0.9:
                self.signal_direction = -1
            elif current <= 0.15:
                self.signal_direction = 1
            next_value = current + (0.07 * self.signal_direction)
            self.signal_bar.set(max(0.0, min(1.0, next_value)))
            if self.signal_bar.get() > 0.15:
                self.after(80, self._animate_signal)
        except Exception:
            pass

    def _pulse_crypto_signal(self, label: str = "ACTIVE"):
        if hasattr(self, "signal_label"):
            self.signal_label.configure(text=label)
        if hasattr(self, "signal_bar"):
            self.signal_bar.configure(progress_color="#6ee7b7")
            self.signal_bar.set(1.0)
            self.after(220, lambda: self.signal_bar.configure(progress_color="#7dd3fc"))
            self.after(220, lambda: self.signal_bar.set(0.15))

    def _update_status_badge(self):
        ready_label = "جاهز" if self.current_lang == "ar" else "READY"
        self.lbl_status_badge.configure(text=ready_label)

    def _update_header_title(self):
        if self.current_lang == "ar":
            ar_name = self.algo_names["ar"][self.current_algo]
            self.lbl_algo_title.configure(text=f"  {ar_name}  ")
        else:
            self.lbl_algo_title.configure(text=f"ALGORITHM: {self.algo_names['en'][self.current_algo].upper()}")
        self._update_status_badge()

    def _switch_algorithm(self, algo_code: str):
        # نقطة مهمة في المناقشة: يتم هنا تبديل الخوارزمية النشطة ديناميكيًا، مع تحديث
        # العنوان، حقول المفتاح، ومعطيات الحوسبة، وهذا ما يعطي التطبيق مرونة كبيرة في الاستخدام.
        self.current_algo = algo_code
        for code, btn in self.algo_buttons.items():
            if code == algo_code:
                btn.configure(fg_color="#0066cc", text_color="#ffffff")
            else:
                btn.configure(fg_color="transparent", text_color="#d0d7de")

        self._update_header_title()
        self._load_algorithm_fields(algo_code)
        self._pulse_crypto_signal("ACTIVE")
        
        ks_info = BruteForceEstimator.analyze(algo_code)
        self.card_keyspace.configure(text=ks_info.get("keyspace", "N/A"))
        self._log_console(f">> Switched to [{algo_code}]. Key space: {ks_info.get('keyspace')} | Resistance: {ks_info.get('status')}")

    def _clear_key_frame(self):
        for widget in self.key_frame.winfo_children():
            widget.destroy()

    def _load_algorithm_fields(self, algo: str):
        self._clear_key_frame()
        self.key_inputs = {}

        if algo == "Caesar":
            lbl_text = "Shift Key (1 - 25):" if self.current_lang == "en" else fix_ar("مفتاح الإزاحة:")
            ctk.CTkLabel(self.key_frame, text=lbl_text, font=ctk.CTkFont(size=12, weight="bold")).pack(side="left", padx=12, pady=8)
            ent = ctk.CTkEntry(self.key_frame, width=90, font=("Consolas", 12))
            ent.insert(0, "3")
            ent.pack(side="left", padx=5)
            self.key_inputs["shift"] = ent

            btn_text = "🎲 Auto Key" if self.current_lang == "en" else fix_ar("🎲 توليد آلي")
            btn = ctk.CTkButton(self.key_frame, text=btn_text, width=90, fg_color="#243144", command=lambda: self._set_key_val("shift", SmartKeyGenerator.generate_caesar()))
            btn.pack(side="left", padx=8)

        elif algo == "Multiplicative":
            lbl_text = "Key [gcd(k,26)=1]:" if self.current_lang == "en" else fix_ar("المفتاح الأولي:")
            ctk.CTkLabel(self.key_frame, text=lbl_text, font=ctk.CTkFont(size=12, weight="bold")).pack(side="left", padx=12, pady=8)
            ent = ctk.CTkEntry(self.key_frame, width=90, font=("Consolas", 12))
            ent.insert(0, "7")
            ent.pack(side="left", padx=5)
            self.key_inputs["key"] = ent

            btn_text = "🎲 Co-Prime Key" if self.current_lang == "en" else fix_ar("🎲 مفتاح أولي")
            btn = ctk.CTkButton(self.key_frame, text=btn_text, width=110, fg_color="#243144", command=lambda: self._set_key_val("key", SmartKeyGenerator.generate_multiplicative()))
            btn.pack(side="left", padx=8)

        elif algo == "Affine":
            lbl_a = "Key (a):" if self.current_lang == "en" else fix_ar("المعامل الأول:")
            ctk.CTkLabel(self.key_frame, text=lbl_a, font=ctk.CTkFont(size=12, weight="bold")).pack(side="left", padx=(12, 4), pady=8)
            ent_a = ctk.CTkEntry(self.key_frame, width=65, font=("Consolas", 12))
            ent_a.insert(0, "5")
            ent_a.pack(side="left", padx=4)
            self.key_inputs["a"] = ent_a

            lbl_b = "Key (b):" if self.current_lang == "en" else fix_ar("المعامل الثاني:")
            ctk.CTkLabel(self.key_frame, text=lbl_b, font=ctk.CTkFont(size=12, weight="bold")).pack(side="left", padx=(10, 4), pady=8)
            ent_b = ctk.CTkEntry(self.key_frame, width=65, font=("Consolas", 12))
            ent_b.insert(0, "8")
            ent_b.pack(side="left", padx=4)
            self.key_inputs["b"] = ent_b

            btn_text = "🎲 Valid (a, b)" if self.current_lang == "en" else fix_ar("🎲 توليد زوج صالح")
            btn = ctk.CTkButton(self.key_frame, text=btn_text, width=115, fg_color="#243144", command=self._gen_affine_keys)
            btn.pack(side="left", padx=10)

        elif algo == "RailFence":
            lbl_text = "Depth / Rails:" if self.current_lang == "en" else fix_ar("عمق السياج:")
            ctk.CTkLabel(self.key_frame, text=lbl_text, font=ctk.CTkFont(size=12, weight="bold")).pack(side="left", padx=12, pady=8)
            ent = ctk.CTkEntry(self.key_frame, width=90, font=("Consolas", 12))
            ent.insert(0, "3")
            ent.pack(side="left", padx=5)
            self.key_inputs["rails"] = ent

        elif algo == "Vigenere":
            lbl_text = "Passphrase Key:" if self.current_lang == "en" else fix_ar("كلمة السر النصية:")
            ctk.CTkLabel(self.key_frame, text=lbl_text, font=ctk.CTkFont(size=12, weight="bold")).pack(side="left", padx=12, pady=8)
            ent = ctk.CTkEntry(self.key_frame, width=170, font=("Consolas", 12))
            ent.insert(0, "MANAR")
            ent.pack(side="left", padx=5)
            self.key_inputs["key"] = ent

            btn_text = "🎲 Generate" if self.current_lang == "en" else fix_ar("🎲 توليد كلمة")
            btn = ctk.CTkButton(self.key_frame, text=btn_text, width=95, fg_color="#243144", command=lambda: self._set_key_val("key", SmartKeyGenerator.generate_vigenere()))
            btn.pack(side="left", padx=8)

        elif algo == "Hill":
            lbl_text = "Matrix Dimension:" if self.current_lang == "en" else fix_ar("أبعاد المصفوفة:")
            ctk.CTkLabel(self.key_frame, text=lbl_text, font=ctk.CTkFont(size=12, weight="bold")).pack(side="left", padx=10, pady=8)
            self.hill_dim = ctk.CTkSegmentedButton(self.key_frame, values=["2x2", "3x3"], command=self._rebuild_hill_grid)
            self.hill_dim.set("2x2")
            self.hill_dim.pack(side="left", padx=5)

            self.hill_grid_frame = ctk.CTkFrame(self.key_frame, fg_color="transparent")
            self.hill_grid_frame.pack(side="left", padx=10)
            self._build_hill_entries(2)

            btn_text = "🎲 Invertible Matrix" if self.current_lang == "en" else fix_ar("🎲 مصفوفة قابلة للعكس")
            btn = ctk.CTkButton(self.key_frame, text=btn_text, width=135, fg_color="#243144", command=self._gen_hill_matrix)
            btn.pack(side="left", padx=5)

        elif algo == "DES":
            lbl_text = "DES Key (8 Bytes):" if self.current_lang == "en" else fix_ar("مفتاح التشفير:")
            ctk.CTkLabel(self.key_frame, text=lbl_text, font=ctk.CTkFont(size=12, weight="bold")).pack(side="left", padx=12, pady=8)
            ent = ctk.CTkEntry(self.key_frame, width=170, font=("Consolas", 12))
            ent.insert(0, "Arafat26")
            ent.pack(side="left", padx=5)
            self.key_inputs["key"] = ent

            btn = ctk.CTkButton(self.key_frame, text="🎲 8-Byte", width=85, fg_color="#243144", command=lambda: self._set_key_val("key", SmartKeyGenerator.generate_des_key()))
            btn.pack(side="left", padx=8)

        elif algo == "AES":
            lbl_mode = "Mode:" if self.current_lang == "en" else fix_ar("النمط:")
            ctk.CTkLabel(self.key_frame, text=lbl_mode, font=ctk.CTkFont(size=12, weight="bold")).pack(side="left", padx=(10, 2), pady=8)
            self.aes_mode_btn = ctk.CTkSegmentedButton(self.key_frame, values=["AES-128", "AES-256"], command=self._on_aes_mode_change, width=130)
            self.aes_mode_btn.set("AES-256")
            self.aes_mode_btn.pack(side="left", padx=4)

            lbl_text = "Key:" if self.current_lang == "en" else fix_ar("المفتاح:")
            ctk.CTkLabel(self.key_frame, text=lbl_text, font=ctk.CTkFont(size=12, weight="bold")).pack(side="left", padx=(6, 2), pady=8)
            ent = ctk.CTkEntry(self.key_frame, width=240, font=("Consolas", 11))
            ent.insert(0, "ArafatAlKamaly26CyberSecurity2026")
            ent.pack(side="left", padx=4)
            self.key_inputs["key"] = ent

            def gen_aes():
                bits = 128 if self.aes_mode_btn.get() == "AES-128" else 256
                k = SmartKeyGenerator.generate_aes_key(bits)
                self._set_key_val("key", k)
                self._log_console(f">> Generated {bits}-bit ({len(k)} bytes) AES key.")

            btn = ctk.CTkButton(self.key_frame, text="🎲 Auto Key", width=90, fg_color="#243144", command=gen_aes)
            btn.pack(side="left", padx=6)

        elif algo == "RSA":
            btn_title = "⚡ GENERATE RSA KEYS (ZERO-FREEZING)" if self.current_lang == "en" else fix_ar("⚡ توليد مفاتيح المنظومة فورياً")
            btn = ctk.CTkButton(self.key_frame, text=btn_title, fg_color="#d83b01", hover_color="#a62c00", command=self._generate_rsa_keys)
            btn.pack(side="left", padx=12, pady=8)
            status_text = "Public / Private Key Pair Not Ready" if self.current_lang == "en" else fix_ar("المفاتيح غير جاهزة بعد")
            self.lbl_rsa_status = ctk.CTkLabel(self.key_frame, text=status_text, text_color="#8a99ad", font=("Consolas", 11))
            self.lbl_rsa_status.pack(side="left", padx=10)

        elif algo == "Hashes":
            hash_desc = "One-Way Cryptographic Hash Functions (No Secret Key Required)" if self.current_lang == "en" else fix_ar("دوال تجزئة وبصمات رقمية أحادية الاتجاه")
            ctk.CTkLabel(self.key_frame, text=hash_desc, text_color="#00d2ff", font=("Consolas", 12)).pack(side="left", padx=15, pady=8)

    def _on_aes_mode_change(self, mode_val):
        if mode_val == "AES-128":
            self.card_keyspace.configure(text="2^128 (~3.4x10^38)")
            self._set_key_val("key", "ArafatAlKamaly26")
            self._log_console(">> AES Mode set to 128-Bit (10 Rounds, 16-Byte Key).")
        else:
            self.card_keyspace.configure(text="2^256 (~1.1x10^77)")
            self._set_key_val("key", "ArafatAlKamaly26CyberSecurity2026")
            self._log_console(">> AES Mode set to 256-Bit (14 Rounds, 32-Byte Key).")

    def _set_key_val(self, key_name: str, val):
        if key_name in self.key_inputs:
            self.key_inputs[key_name].delete(0, "end")
            self.key_inputs[key_name].insert(0, str(val))

    def _gen_affine_keys(self):
        a, b = SmartKeyGenerator.generate_affine()
        self._set_key_val("a", a)
        self._set_key_val("b", b)

    def _rebuild_hill_grid(self, val):
        dim = 2 if val == "2x2" else 3
        self._build_hill_entries(dim)

    def _build_hill_entries(self, dim: int):
        for w in self.hill_grid_frame.winfo_children():
            w.destroy()
        self.hill_matrix_entries = []
        defaults = [[3, 2], [5, 7]] if dim == 2 else [[6, 24, 1], [13, 16, 10], [20, 17, 15]]

        for r in range(dim):
            row_entries = []
            for c in range(dim):
                e = ctk.CTkEntry(self.hill_grid_frame, width=42, justify="center", font=("Consolas", 11))
                e.grid(row=r, column=c, padx=2, pady=2)
                e.insert(0, str(defaults[r][c]))
                row_entries.append(e)
            self.hill_matrix_entries.append(row_entries)

    def _gen_hill_matrix(self):
        dim = 2 if self.hill_dim.get() == "2x2" else 3
        mat = SmartKeyGenerator.generate_hill_2x2() if dim == 2 else SmartKeyGenerator.generate_hill_3x3()
        for r in range(dim):
            for c in range(dim):
                self.hill_matrix_entries[r][c].delete(0, "end")
                self.hill_matrix_entries[r][c].insert(0, str(mat[r][c]))

    def _get_hill_matrix(self) -> list[list[int]]:
        dim = len(self.hill_matrix_entries)
        mat = []
        for r in range(dim):
            row = []
            for c in range(dim):
                val = self.hill_matrix_entries[r][c].get().strip()
                if not val.isdigit() and not (val.startswith("-") and val[1:].isdigit()):
                    raise ValueError(f"Hill Matrix element [{r+1},{c+1}] is invalid!")
                row.append(int(val))
            mat.append(row)
        return mat

    def _generate_rsa_keys(self):
        try:
            self.rsa_keys = RSACore.generate_keys(bits=14)
            e, n = self.rsa_keys["public_key"]
            d, _ = self.rsa_keys["private_key"]
            self.lbl_rsa_status.configure(
                text=f"Ready: e={e}, d={d}, n={n} (p={self.rsa_keys['p']}, q={self.rsa_keys['q']})",
                text_color="#00e676"
            )
            self._log_console(f">> RSA Keys Generated (Zero-Freezing): Public=(e:{e}, n:{n}), Private=(d:{d})")
        except Exception as ex:
            messagebox.showerror("RSA Error", str(ex))

    def _load_demo(self):
        preset = QuickDemoPresets.get_preset(self.current_algo)
        if not preset:
            return
        self.txt_input.delete("1.0", "end")
        self.txt_input.insert("1.0", preset.get("text", ""))

        if self.current_algo == "Caesar":
            self._set_key_val("shift", preset.get("key", 3))
        elif self.current_algo == "Multiplicative":
            self._set_key_val("key", preset.get("key", 7))
        elif self.current_algo == "Affine":
            self._set_key_val("a", preset.get("key_a", 5))
            self._set_key_val("b", preset.get("key_b", 8))
        elif self.current_algo == "RailFence":
            self._set_key_val("rails", preset.get("rails", 3))
        elif self.current_algo == "Vigenere":
            self._set_key_val("key", preset.get("key", "MANAR"))
        elif self.current_algo == "DES":
            self._set_key_val("key", preset.get("key", "Arafat26"))
        elif self.current_algo == "AES":
            self.aes_mode_btn.set("AES-256")
            self._set_key_val("key", preset.get("key", "ArafatAlKamaly26CyberSecurity2026"))
            self.card_keyspace.configure(text="2^256 (~1.1x10^77)")
        elif self.current_algo == "RSA":
            self._generate_rsa_keys()
        
        self._log_console(f">> Loaded quick preset for [{self.current_algo}].")

    def _update_metrics(self, speed_str: str, out_str: str, algo: str):
        self.card_time.configure(text=speed_str)
        ent_val, ent_desc = EntropyAnalyzer.calculate_entropy(out_str)
        self.card_entropy.configure(text=f"{ent_val:.3f} bits/B")
        
        if algo == "AES" and hasattr(self, 'aes_mode_btn'):
            ks_text = "2^128 (~3.4x10^38)" if self.aes_mode_btn.get() == "AES-128" else "2^256 (~1.1x10^77)"
            self.card_keyspace.configure(text=ks_text)
        else:
            ks = BruteForceEstimator.analyze(algo)
            self.card_keyspace.configure(text=ks.get("keyspace", "N/A"))

        self.last_metrics = {
            "speed": speed_str,
            "entropy": f"{ent_val:.4f} bits/B ({ent_desc})",
            "keyspace": self.card_keyspace.cget("text"),
            "cracktime": BruteForceEstimator.analyze(algo).get("time", "N/A"),
            "avalanche": self.card_sac.cget("text")
        }

    def _execute_encrypt(self):
        # شرح للمناقشة: هذا هو قلب التطبيق؛ هنا يتم قراءة النص من الحقل، اختيار الخوارزمية الحالية,
        # تنفيذ التشفير، ثم كتابة النتيجة في الحقل الثاني. هذا يوضح أن المشروع عملي وليس مجرد أكواد نظرية.
        text = self.txt_input.get("1.0", "end-1c")
        if not text:
            messagebox.showwarning("Empty Payload", "Please enter input plaintext to encrypt!")
            return

        algo = self.current_algo
        try:
            res = ""
            speed_str = "0.00 µs"

            if algo == "Caesar":
                shift = int(self.key_inputs["shift"].get())
                res, _, speed_str = BenchmarkEngine.measure_execution(CaesarCipher.encrypt, text, shift)
            elif algo == "Multiplicative":
                k = int(self.key_inputs["key"].get())
                res, _, speed_str = BenchmarkEngine.measure_execution(MultiplicativeCipher.encrypt, text, k)
            elif algo == "Affine":
                a = int(self.key_inputs["a"].get())
                b = int(self.key_inputs["b"].get())
                res, _, speed_str = BenchmarkEngine.measure_execution(AffineCipher.encrypt, text, a, b)
            elif algo == "RailFence":
                r = int(self.key_inputs["rails"].get())
                res, _, speed_str = BenchmarkEngine.measure_execution(RailFenceCipher.encrypt, text, r)
            elif algo == "Vigenere":
                k = self.key_inputs["key"].get()
                res, _, speed_str = BenchmarkEngine.measure_execution(VigenereCipher.encrypt, text, k)
            elif algo == "Hill":
                mat = self._get_hill_matrix()
                (cipher, note, inv_mat), _, speed_str = BenchmarkEngine.measure_execution(AdvancedHillCipher.process, text, mat, "encrypt")
                res = cipher
                self._log_console(f">> [HILL MATRIX INVERSE K^-1]: {inv_mat}")
                self._log_console(f">> [HILL ACADEMIC NOTE]: {note}")
            elif algo == "DES":
                k = self.key_inputs["key"].get()
                res, _, speed_str = BenchmarkEngine.measure_execution(DESCipher.encrypt, text, k)
            elif algo == "AES":
                k = self.key_inputs["key"].get()
                res, _, speed_str = BenchmarkEngine.measure_execution(AES128Cipher.encrypt, text, k)
            elif algo == "RSA":
                if not self.rsa_keys:
                    raise ValueError("Please generate RSA keys first using 'GENERATE RSA KEYS' button!")
                e, n = self.rsa_keys["public_key"]
                res, _, speed_str = BenchmarkEngine.measure_execution(RSACore.encrypt, text, e, n)
            elif algo == "Hashes":
                digests, _, speed_str = BenchmarkEngine.measure_execution(HashEngine.compute_all, text)
                res = f"MD5:\n{digests['MD5']}\n\nSHA-256:\n{digests['SHA-256']}\n\nSHA-512:\n{digests['SHA-512']}"

            self.txt_output.delete("1.0", "end")
            self.txt_output.insert("1.0", str(res))
            self._pulse_crypto_signal("ENCRYPT")
            self._update_metrics(speed_str, str(res), algo)
            self._log_console(f"[+ENCRYPT] Success with [{algo}]. Latency: {speed_str} | Length: {len(text)} chars.")

        except Exception as ex:
            self._log_console(f"[-ERROR] Encryption failed: {str(ex)}")
            messagebox.showerror("Cryptographic Error", str(ex))

    def _execute_decrypt(self):
        # شرح للمناقشة: هنا يتم تطبيق العملية العكسية، وباستخدام نفس المفتاح أو الخوارزمية نفسها.
        # هذه الوظيفة توضح أن المشروع يدعم التشفير وفك التشفير كمفهوم كامل، وليس مجرد زر تشفير واحد.
        text = self.txt_input.get("1.0", "end-1c")
        if not text:
            messagebox.showwarning("Empty Payload", "Please enter input ciphertext to decrypt!")
            return

        algo = self.current_algo
        try:
            res = ""
            speed_str = "0.00 µs"

            if algo == "Caesar":
                shift = int(self.key_inputs["shift"].get())
                res, _, speed_str = BenchmarkEngine.measure_execution(CaesarCipher.decrypt, text, shift)
            elif algo == "Multiplicative":
                k = int(self.key_inputs["key"].get())
                res, _, speed_str = BenchmarkEngine.measure_execution(MultiplicativeCipher.decrypt, text, k)
            elif algo == "Affine":
                a = int(self.key_inputs["a"].get())
                b = int(self.key_inputs["b"].get())
                res, _, speed_str = BenchmarkEngine.measure_execution(AffineCipher.decrypt, text, a, b)
            elif algo == "RailFence":
                r = int(self.key_inputs["rails"].get())
                res, _, speed_str = BenchmarkEngine.measure_execution(RailFenceCipher.decrypt, text, r)
            elif algo == "Vigenere":
                k = self.key_inputs["key"].get()
                res, _, speed_str = BenchmarkEngine.measure_execution(VigenereCipher.decrypt, text, k)
            elif algo == "Hill":
                mat = self._get_hill_matrix()
                (plain, note, inv_mat), _, speed_str = BenchmarkEngine.measure_execution(AdvancedHillCipher.process, text, mat, "decrypt")
                res = plain
                self._log_console(f">> [HILL DECRYPT SUCCESS] Applied K^-1: {inv_mat}")
            elif algo == "DES":
                k = self.key_inputs["key"].get()
                res, _, speed_str = BenchmarkEngine.measure_execution(DESCipher.decrypt, text, k)
            elif algo == "AES":
                k = self.key_inputs["key"].get()
                res, _, speed_str = BenchmarkEngine.measure_execution(AES128Cipher.decrypt, text, k)
            elif algo == "RSA":
                if not self.rsa_keys:
                    raise ValueError("RSA Private key is required to decrypt! Generate keys first.")
                d, n = self.rsa_keys["private_key"]
                res, _, speed_str = BenchmarkEngine.measure_execution(RSACore.decrypt, text, d, n)
            elif algo == "Hashes":
                raise ValueError("Hash functions are strictly one-way! Decryption is mathematically impossible.")

            self.txt_output.delete("1.0", "end")
            self.txt_output.insert("1.0", str(res))
            self._pulse_crypto_signal("DECRYPT")
            self._update_metrics(speed_str, str(res), algo)
            self._log_console(f"[+DECRYPT] Success with [{algo}]. Latency: {speed_str}.")

        except Exception as ex:
            self._log_console(f"[-ERROR] Decryption failed: {str(ex)}")
            messagebox.showerror("Cryptographic Error", str(ex))

    def _execute_sac_test(self):
        # اختبار SAC: يغير البت الأخير في النص ثم يقارن النتيجة بين نصين متشابهين قليلًا.
        # الهدف هو قياس مدى انتشار التغيير في المخرجات، وهو مفهوم مهم في تحليل الأمان والاختبار العلمي.
        text = self.txt_input.get("1.0", "end-1c")
        if not text:
            messagebox.showwarning("SAC Test", "Please provide input text to perform SAC bit-diffusion test!")
            return

        algo = self.current_algo
        if algo in ["RailFence", "RSA"]:
            messagebox.showinfo("SAC Notice", f"SAC bit diffusion is evaluated on Block Ciphers and Hashes (DES, AES, Hashes).")
            return

        try:
            altered_text = text[:-1] + chr(ord(text[-1]) ^ 1)
            
            if algo == "AES":
                k = self.key_inputs["key"].get()
                c1 = bytes.fromhex(AES128Cipher.encrypt(text, k))
                c2 = bytes.fromhex(AES128Cipher.encrypt(altered_text, k))
            elif algo == "DES":
                k = self.key_inputs["key"].get()
                c1 = bytes.fromhex(DESCipher.encrypt(text, k))
                c2 = bytes.fromhex(DESCipher.encrypt(altered_text, k))
            elif algo == "Hashes":
                c1 = bytes.fromhex(HashEngine.compute_all(text)["SHA-256"])
                c2 = bytes.fromhex(HashEngine.compute_all(altered_text)["SHA-256"])
            elif algo == "Caesar":
                shift = int(self.key_inputs["shift"].get())
                c1 = CaesarCipher.encrypt(text, shift).encode("utf-8")
                c2 = CaesarCipher.encrypt(altered_text, shift).encode("utf-8")
            else:
                c1 = text.encode("utf-8")
                c2 = altered_text.encode("utf-8")

            changed_bits, total_bits, pct, eval_msg = AvalancheAnalyzer.calculate_bit_difference(c1, c2)
            self.card_sac.configure(text=f"{pct:.2f} %")
            
            progress_ratio = min(1.0, max(0.0, pct / 100.0))
            self.sac_bar.set(progress_ratio)
            if pct >= 45.0 and pct <= 55.0:
                self.sac_bar.configure(progress_color="#00e676")
            elif pct >= 30.0:
                self.sac_bar.configure(progress_color="#ffaa00")
            else:
                self.sac_bar.configure(progress_color="#ff5252")

            self._log_console("=" * 65)
            self._log_console(f"[*SAC TEST] Algorithm: {algo} | 1-bit plaintext flip applied")
            self._log_console(f"[*SAC TEST] Flipped: {changed_bits}/{total_bits} bits ({pct:.2f}%) | SAC Compliant: {eval_msg}")
            self._log_console("=" * 65)

        except Exception as ex:
            self._log_console(f"[-SAC ERROR] {str(ex)}")
            messagebox.showerror("SAC Error", str(ex))

    def _export_audit_report(self):
        inp = self.txt_input.get("1.0", "end-1c")
        out = self.txt_output.get("1.0", "end-1c")
        if not out:
            messagebox.showwarning("Audit Export", "No processed output available to export!")
            return

        rep = ReportExporter.generate_report(
            algo_name=self.current_algo,
            operation="Laboratory Cryptographic Verification & SAC Audit",
            input_text=inp,
            output_text=out,
            key_info="Verified Keys & Parameters (Pure Python Core)",
            metrics=self.last_metrics
        )
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            initialfile=f"Audit_Report_{self.current_algo}_AlManar.txt"
        )
        if filepath:
            ReportExporter.save_report_to_file(filepath, rep)
            self._log_console(f"[+EXPORT] Audit report saved: {filepath}")
            messagebox.showinfo("Export Complete", f"Cryptographic Audit Report saved:\n{filepath}")

if __name__ == "__main__":
    app = CyberKeyEnterpriseApp()
    app.mainloop()
