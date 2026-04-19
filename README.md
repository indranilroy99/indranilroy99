```
48 65 6c 6c 6f 20 63 75 72 69 6f 75 73 20 68 61 63 6b 65 72 2c 0a
77 65 6c 63 6f 6d 65 20 74 6f 20 6d 79 20 64 69 67 69 74 61 6c 20 6c 61 62 2e
```

---

<h1 align="center">Indranil | Security Operations & Threat Intelligence</h1>

<p align="center">
  <strong>Detection Engineer | Red Team Analyst | Malware Researcher</strong><br>
  Building resilient defenses through adversary-centric threat hunting and operational security.
</p>

<p align="center">
  <a href="https://linkedin.com/in/indranil-roy" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://x.com/vo1dx0?s=21" target="_blank">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white" />
  </a>
  <a href="mailto:your-email@example.com" target="_blank">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
</p>

---

## 🎯 Live Telemetry: Security Operations

| Metric | Count |
|--------|-------|
| ![Detection Rules](https://img.shields.io/badge/Detection%20Rules-42-2ea44f?style=flat-square) | SIGMA/Yara Signatures |
| ![Malware Samples](https://img.shields.io/badge/Malware%20Samples%20Analyzed-127-yellow?style=flat-square) | APT/Commodity Threats |
| ![Incidents Handled](https://img.shields.io/badge/Incidents%20Handled-18-red?style=flat-square) | IR Case Studies |
| ![Threat Intel Reports](https://img.shields.io/badge/Threat%20Reports-9-blue?style=flat-square) | TTPs & IOCs |

<details>
<summary><b>📊 How to maintain these metrics</b></summary>

Create a file `.github/metrics.json` in your repo:

```json
{
  "detection_rules": 42,
  "malware_samples": 127,
  "incidents_handled": 18,
  "threat_reports": 9
}
```

Then reference these values in your README using Shields.io dynamic badges:
```
https://img.shields.io/badge/Detection%20Rules-{YOUR_COUNT}-2ea44f
```

For **automated updates**, use GitHub Actions to pull data from your projects:

```yaml
name: Update Metrics
on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: |
          python scripts/update_metrics.py
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add .
          git commit -m "chore: update live metrics" || exit 0
          git push
```

</details>

---

## 🛡️ Operational Skills Matrix

```
                     Red Teaming
                         ▲
                        /█\
                       / █ \
                      /  █  \
                     /████████\
        Exploitation ◄────████────► Penetration Testing
                     \████████/
                      \  █  /
                       \ █ /
                        \█/
                         ▼
                  Incident Response
                  
    Malware Analysis: ████████░░ 85%
    Security Ops:    ███████░░░  75%
```

| Domain | Proficiency | Tools & Frameworks |
|--------|-------------|-------------------|
| **Red Teaming** | Expert | Cobalt Strike, Metasploit, Impacket, PowerShell Empire |
| **Penetration Testing** | Expert | Burp Suite, Nessus, Qualys, Custom Exploit Dev |
| **Incident Response** | Advanced | Velociraptor, osquery, YARA, Splunk, ELK |
| **Malware Analysis** | Expert | Ghidra, IDA Pro, x64dbg, Wireshark, ANY.RUN |
| **Security Ops** | Advanced | SIEM (Splunk/ELK), EDR (CrowdStrike/Sentinel One), SOAR |
| **Threat Hunting** | Expert | KQL, SPL, YARA, SIGMA Rules, Custom Scripts |

---

## 🔧 Tech Stack & Arsenal

```yaml
Languages:
  - Python (automation, tooling, malware analysis)
  - Bash/Zsh (incident response, data processing)
  - PowerShell (Windows forensics, C2 post-exploitation)
  - Go (high-performance tools, detection engineering)

Security Platforms:
  - SIEM: Splunk, ELK Stack, Azure Sentinel
  - EDR: CrowdStrike Falcon, Microsoft Defender, Velociraptor
  - Threat Intelligence: MISP, Shodan, AlienVault OTX
  - Reverse Engineering: Ghidra, IDA Pro, Binary Ninja

Detection Engineering:
  - YARA Rules (malware signatures)
  - SIGMA Rules (generic SIEM detection)
  - KQL / SPL (detection queries)
  - Custom detection pipelines

Infrastructure:
  - Docker, Kubernetes (lab environments)
  - Terraform (IaC for threat labs)
  - Git (version control for detections & IOCs)
```

---

## 📚 Current Research & Projects

### Featured Repositories

```
├── detection-engineering/
│   ├── sigma-rules/          Advanced detection logic for APT campaigns
│   ├── yara-signatures/      Malware family identification rules
│   └── threat-hunting-kql/   Azure Sentinel hunting queries
│
├── incident-response/
│   ├── forensic-timeline/    Windows event log correlation
│   ├── memory-analysis/      Volatility3 scripts for RAM analysis
│   └── malware-triage/       Rapid response playbooks
│
└── threat-intelligence/
    ├── apt-profiles/        Adversary TTPs & IOC databases
    ├── c2-indicators/       C2 infrastructure tracking
    └── phishing-analysis/   Email-based attack patterns
```

<details>
<summary><b>📖 View detailed project descriptions</b></summary>

- **detection-engineering**: Production-ready SIGMA and YARA rules battle-tested against live incident data
- **incident-response**: Automated IR toolchain for rapid triage and containment
- **threat-intelligence**: Structured adversary profiles with MITRE ATT&CK mappings

</details>

---

## 🎓 Threat Hunting Playbooks

| Threat Actor | TTPs | Detection Focus |
|--------------|------|-----------------|
| APT28 | T1566 (Phishing), T1059 (Execution) | Email gateways, Process creation logs |
| Lazarus | T1190 (Exploit), T1486 (Encryption) | Web app logs, File system monitoring |
| FIN7 | T1078 (Cred Access), T1110 (Brute Force) | Authentication logs, MFA bypass indicators |
| Wizard Spider | T1657 (Persistence), T1009 (Data Staging) | Registry monitoring, Exfil patterns |

---

## 💭 Philosophy

> "Defense isn't about knowing every attack—it's about understanding every attacker's constraints, resources, and objectives. Turn that intel into friction."

**My Approach:**
- **Adversary-Centric**: Map defenses to real threat actor TTPs, not fear-mongering
- **Detection-First**: Every incident is a blind spot; every blind spot becomes a detection rule
- **Operational Reality**: Solutions that work at 3 AM during an active breach, not just in presentations
- **Continuous Iteration**: Threat landscape shifts weekly; detection strategy shifts monthly

---

## 🚀 Let's Connect

Security is a team sport. Whether you're:
- **Hunting threats** and need collaborative intel
- **Building detections** and want to review rules
- **Responding to incidents** and need an extra set of eyes
- **Researching TTPs** and want to compare notes

📧 Reach out via [LinkedIn](https://linkedin.com/in/indranil-roy) or [@vo1dx0](https://x.com/vo1dx0)

---

<p align="center">
  <i>"The attacker only needs to find one hole. The defender must protect them all."</i><br>
  Last updated: 2026-04-19
</p>
```
