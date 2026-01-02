# 🛑 IR-GEN v1.0: Recon-Based Incident Response Playbook Generator

**Defensive Recon + Incident Response Streamlit App**
***Tool Completion Date***December 2025

IR-GEN is a **defensive-only cybersecurity tool** designed to analyze reconnaissance `.txt` files, detect potential incidents and vulnerability indicators, and generate structured incident response playbooks — all without generating exploits or offensive payloads.

> ⚠️ **Warning:** Use only on systems you own or are explicitly authorized to test.

---

## 🧠 Features

* **Vulnerability Detection:** Detects stack traces, verbose errors, directory listings, API exposures, weak authentication, missing rate limiting, exposed remote services, and sensitive data exposure.
* **Incident Inference:** Maps vulnerabilities to potential incidents, impact, and severity levels.
* **Structured IR Playbook:** Generates step-by-step incident response including detection, containment, eradication, recovery, evidence preservation, and post-incident hardening.
* **LLaMA-Powered Analysis:** Single-shot LLaMA request produces a professional, defensive response.
* **Streamlit Dashboard:** Interactive interface to view detected incidents, vulnerabilities, and playbook.
* **Downloadable TXT:** Export structured incident response playbooks as `.txt` files.

---

## ⚙️ Installation

```bash
pip install streamlit pandas huggingface_hub
```

---

## ▶️ Usage

1. Run the Streamlit app:

```bash
streamlit run ir_gen.py
```

2. Upload your reconnaissance `.txt` file.
3. Adjust LLaMA temperature slider to control the creativity of the IR playbook.
4. Review detected incidents and inferred severity, impact, and indicators.
5. Generate and view the Incident Response Playbook.
6. Download the structured TXT report.

---

## 🔍 How It Works

Recon TXT File
↓
Vulnerability Detection (keywords, misconfigurations, exposures)
↓
Incident Inference (map to potential incidents, severity, impact)
↓
Risk & Evidence Analysis
↓
LLaMA Incident Response Playbook Generation
↓
Streamlit Dashboard & TXT Export

---

## 👤 Author

Khin La Pyae Woon
AI-Enhanced Ethical Hacking | Cybersecurity | Digital Forensic | Analyze | Developing

🌐 Portfolio: https://khinlapyaewoon-cyberdev.vercel.app
🔗 LinkedIn: www.linkedin.com/in/khin-la-pyae-woon-ba59183a2
💬 WhatsApp: https://wa.me/qr/MJYX74CQ5VA4D1

---

## 📜 License & Ethics

This tool is released for educational, defensive, and research purposes only.
Any offensive or unauthorized usage is strictly prohibited.
