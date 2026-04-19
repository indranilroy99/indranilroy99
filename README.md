# Indranil | vo1d

```
48 65 6c 6c 6f 20 63 75 72 69 6f 75 73 20 68 61 63 6b 65 72 2c 0a
77 65 6c 63 6f 6d 65 20 74 6f 20 6d 79 20 64 69 67 69 74 61 6c 20 6c 61 62 2e
```

Detection engineer, malware analyst, red team operator. Building defensive capabilities around adversary behavior.

[LinkedIn](https://linkedin.com/in/indranil-roy) • [Twitter](https://x.com/vo1dx0)

---

## Live Metrics

| Metric | Value |
|--------|-------|
| Detection Rules (SIGMA/YARA) | ![](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/indranilroy99/.github/main/metrics.json&label=Rules&query=$.detection_rules&color=2ea44f) |
| Malware Samples Analyzed | ![](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/indranilroy99/.github/main/metrics.json&label=Samples&query=$.malware_samples&color=yellow) |
| Incident Reports | ![](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/indranilroy99/.github/main/metrics.json&label=IRs&query=$.incident_reports&color=blue) |
| Threat Intel Artifacts | ![](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/indranilroy99/.github/main/metrics.json&label=TI&query=$.threat_intel&color=orange) |

---

## Skills

| Domain | Experience | Primary Tools |
|--------|------------|----------------|
| **Purple Teaming** | Advanced | C2 evasion, detection validation, adversary simulation |
| **Security Operations** | Advanced | SIEM (Splunk/ELK), endpoint monitoring, log analysis |
| **Detection Engineering** | Expert | SIGMA/YARA rules, KQL, SPL, detection logic |
| **AI Security** | Intermediate | LLM safety, prompt injection testing, model reconnaissance |
| **Incident Response** | Advanced | Timeline analysis, forensics, containment, post-mortems |
| **Malware Analysis** | Expert | Static/dynamic analysis, reverse engineering, behavioral profiling |

---

## Working On

- **detection-engineering** — Production SIGMA and YARA signatures
- **malware-analysis** — Sample triage, behavioral analysis, write-ups
- **security-operations** — Threat hunting queries and detection strategies
- **purple-team-ops** — Detection evasion and validation tools
- **ai-security** — LLM attack surface mapping and mitigations
- **incident-response** — Case studies and forensic automation

---

## Setup

How to automatically track your metrics:

### 1. Create `.github/workflows/update-metrics.yml`

```yaml
name: Update Metrics

on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:
  push:
    paths:
      - '**.sigma'
      - '**.yara'
      - 'detection-engineering/**'
      - 'malware-analysis/**'
      - 'incident-response/**'

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Count artifacts
        run: |
          mkdir -p /tmp/metrics
          
          # Count SIGMA rules
          SIGMA_RULES=$(find detection-engineering -name "*.sigma" -o -name "*.yml" | grep -i sigma | wc -l)
          
          # Count YARA rules
          YARA_RULES=$(find detection-engineering -name "*.yara" -o -name "*.yar" | wc -l)
          
          # Count malware samples analyzed
          MALWARE_SAMPLES=$(find malware-analysis -name "*.md" -o -name "analysis-*.txt" | wc -l)
          
          # Count incident reports
          INCIDENT_REPORTS=$(find incident-response -name "*.md" -o -name "ir-*.txt" | wc -l)
          
          # Count threat intel artifacts
          THREAT_INTEL=$(find . -path ./.git -prune -o -name "*ioc*" -o -name "*indicators*" | grep -v ".git" | wc -l)
          
          TOTAL_RULES=$((SIGMA_RULES + YARA_RULES))
          
          cat > /tmp/metrics.json << EOF
          {
            "detection_rules": $TOTAL_RULES,
            "sigma_rules": $SIGMA_RULES,
            "yara_rules": $YARA_RULES,
            "malware_samples": $MALWARE_SAMPLES,
            "incident_reports": $INCIDENT_REPORTS,
            "threat_intel": $THREAT_INTEL,
            "updated_at": "$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
          }
          EOF
          
          cat /tmp/metrics.json

      - name: Push metrics
        run: |
          mkdir -p .github
          cp /tmp/metrics.json .github/metrics.json
          
          git config user.name "Metrics Bot"
          git config user.email "metrics@github.com"
          git add .github/metrics.json
          git commit -m "chore: update live metrics" || true
          git push

```

### 2. Create `.github/metrics.json` (initial)

```json
{
  "detection_rules": 0,
  "sigma_rules": 0,
  "yara_rules": 0,
  "malware_samples": 0,
  "incident_reports": 0,
  "threat_intel": 0,
  "updated_at": "2026-04-19T00:00:00Z"
}
```

### 3. Repo Structure

Organize your work so it auto-counts:

```
detection-engineering/
├── sigma-rules/
│   ├── web-attacks.sigma
│   ├── c2-communication.sigma
│   └── credential-access.sigma
├── yara-rules/
│   ├── ransomware-family.yara
│   └── infostealer.yara
└── README.md

malware-analysis/
├── APT28-backdoor-analysis.md
├── Emotet-behavioral-study.md
└── samples/
    └── iocs-identified.txt

incident-response/
├── IR-2025-001-ransomware.md
├── IR-2025-002-lateral-movement.md
└── playbooks/

security-operations/
├── threat-hunting-kql/
├── detection-strategies/
└── siem-dashboards/

purple-team-ops/
├── detection-evasion-tests/
├── adversary-simulation-plans/
└── validation-reports/

ai-security/
├── llm-attack-surface/
├── prompt-injection-tests/
└── research/
```

### 4. Update the metrics.json reference in README

The badges pull from `.github/metrics.json` automatically. Just push code matching the directory structure, and the workflow updates metrics daily.

---

## Contact

For detection reviews, threat intel collaboration, or incident response discussions:

- LinkedIn: [indranil-roy](https://linkedin.com/in/indranil-roy)
- Twitter: [@vo1dx0](https://x.com/vo1dx0)
