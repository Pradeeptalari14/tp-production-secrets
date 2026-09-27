# Production Secrets & Rotation Studio

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![SRE CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/sre-validation.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Manim Community](https://img.shields.io/badge/Manim-4K_Animation-orange.svg)](https://www.manim.community/)
[![Interactive Studio](https://img.shields.io/badge/Interactive_Studio-Live-purple.svg)](https://talaripradeep.info/tools/production-secrets/)

Enterprise credentials management and dynamic key rotation with HashiCorp Vault dynamic leases, AWS/GCP Secret Manager, Kubernetes External Secrets Operator (ESO), and 3Blue1Brown/Manim programmatic video animation.

---

## 🏛️ Architecture Flow Diagram

![Architecture Flow Diagram](docs/production_secrets_flow.png)

---

## 🎬 3Blue1Brown / Manim Programmatic Video Generator

This repository includes a production-grade **Manim** (`manim_flow.py`) programmatic video animation script that renders a 60fps technical visualization of this architecture.

```bash
# 1. Install Manim community edition
pip install manim

# 2. Render fast 480p preview (quick review)
manim -pql manim_flow.py ProductionSecretsArchitectureScene

# 3. Render 1080p 60fps Full HD (production quality)
manim -pqh manim_flow.py ProductionSecretsArchitectureScene

# 4. Render Ultra HD 4K 60fps (keynote / presentation quality)
manim -pqk manim_flow.py ProductionSecretsArchitectureScene
```

---

## 🚀 Quickstart & Validation

```bash
# Clone the repository
git clone https://github.com/Pradeeptalari14/tp-production-secrets.git
cd tp-production-secrets

# Install dependencies
pip install -r requirements.txt

# Run validation checks
bash scripts/validate.sh
```

---

## 📂 Repository Layout

```text
├── .github/workflows/
│   └── sre-validation.yml
├── docs/
│   └── production_secrets_flow.png
├── scripts/
│   └── validate.sh
├── docker-compose.yml
├── requirements.txt
├── package.json
├── manim_flow.py
├── LICENSE
├── SECURITY.md
└── README.md
```

---

## 📄 License & Security

- **License:** [MIT License](LICENSE)
- **Security:** See [SECURITY.md](SECURITY.md) for vulnerability disclosure.
