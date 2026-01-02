#!/usr/bin/env python3
"""
IR-GEN v1.0
Recon-Based Incident Response Playbook Generator
Input: Recon TXT
Output: Structured Incident Response Playbook
"""

import os
import streamlit as st
from huggingface_hub import InferenceClient

# ==================================================
# 🔐 CLEAR PROXIES
# ==================================================
for k in ["HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY"]:
    os.environ[k] = ""

# ==================================================
# 🔐 HF CONFIG
# ==================================================
HF_TOKEN = "HF_TOKEN"
MODEL = "meta-llama/Llama-3.1-8B-Instruct"
client = InferenceClient(model=MODEL, token=HF_TOKEN)

# ==================================================
# 🧠 VULNERABILITY → INCIDENT DATABASE
# ==================================================
VULN_INCIDENT_DB = {
    "Information Disclosure": {
        "keywords": ["stack trace", "verbose error", "directory listing", "swagger"],
        "incident": "Unauthorized information exposure",
        "impact": "Attack surface expansion and attacker reconnaissance",
        "severity": "Medium",
    },
    "Weak Authentication": {
        "keywords": ["basic auth", "default login", "no auth", "login endpoint"],
        "incident": "Unauthorized account access",
        "impact": "Account compromise and privilege misuse",
        "severity": "High",
    },
    "API Exposure": {
        "keywords": ["openapi", "/api/", "graphql"],
        "incident": "Abuse of exposed APIs",
        "impact": "Data manipulation or service abuse",
        "severity": "High",
    },
    "Sensitive Data Exposure": {
        "keywords": [".env", "backup", "dump", "exposed"],
        "incident": "Sensitive data leakage",
        "impact": "Credential exposure and compliance risk",
        "severity": "Critical",
    },
    "Missing Rate Limiting": {
        "keywords": ["no rate limit", "429 missing"],
        "incident": "Automated abuse or DoS",
        "impact": "Service degradation or outage",
        "severity": "High",
    },
    "Exposed Remote Services": {
        "keywords": ["ssh", "rdp", "open port"],
        "incident": "Unauthorized remote access attempt",
        "impact": "Lateral movement or persistence",
        "severity": "High",
    },
}

# ==================================================
# 🔎 VULNERABILITY DETECTION
# ==================================================
def detect_incident_sources(text):
    text = text.lower()
    findings = {}

    for vuln, meta in VULN_INCIDENT_DB.items():
        hits = [kw for kw in meta["keywords"] if kw in text]
        if hits:
            findings[vuln] = {
                "indicators": hits,
                "incident": meta["incident"],
                "impact": meta["impact"],
                "severity": meta["severity"],
            }
    return findings

# ==================================================
# 🧠 LLaMA INCIDENT RESPONSE PLAYBOOK
# ==================================================
def generate_ir_playbook(findings, temperature):
    summary = ""
    for v, d in findings.items():
        summary += f"""
Vulnerability: {v}
Potential Incident: {d['incident']}
Severity: {d['severity']}
Impact: {d['impact']}
Indicators: {', '.join(d['indicators'])}
"""

    prompt = f"""
You are a senior Incident Response lead.

Based on the following potential incidents inferred from reconnaissance data:

{summary}

Create a STRUCTURED INCIDENT RESPONSE PLAYBOOK including:
1. Incident description
2. Detection & validation steps
3. Immediate containment actions
4. Eradication steps
5. Recovery procedures
6. Evidence & logging to preserve
7. Post-incident hardening actions

Rules:
- Defensive response only
- No attacker instructions
- No exploit details
"""

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a defensive incident response expert."},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=2600,
    )

    return response.choices[0].message.content.strip()

# ==================================================
# 🖥️ STREAMLIT UI
# ==================================================
st.set_page_config(page_title="IR-GEN v1.0", layout="wide")
st.title("🛑 IR-GEN v1.0 – Recon-Based Incident Response Playbook")

temperature = st.slider("LLaMA Temperature", 0.0, 1.0, 0.3, 0.05)
uploaded = st.file_uploader("Upload Recon TXT File", type=["txt"])

if uploaded:
    recon_text = uploaded.read().decode(errors="ignore")
    findings = detect_incident_sources(recon_text)

    if not findings:
        st.warning("No incident-relevant vulnerability signals detected.")
        st.stop()

    st.subheader("⚠️ Potential Incidents Identified")
    for v, d in findings.items():
        st.markdown(f"""
**{v}**
- Potential Incident: {d['incident']}
- Severity: {d['severity']}
- Impact: {d['impact']}
- Indicators: {', '.join(d['indicators'])}
""")

    with st.spinner("Generating Incident Response Playbook..."):
        playbook = generate_ir_playbook(findings, temperature)

    st.subheader("📘 Incident Response Playbook")
    st.text_area("IR Playbook", playbook, height=450)
