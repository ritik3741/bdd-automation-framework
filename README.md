# 🚀 Automated BDD Test Framework (Python + Behave)

## 📌 Overview
This project is an **Automated Test Framework** built using **Behavior Driven Development (BDD)** principles with **Python and Behave**.  
It supports **API testing**, **OMS-style order lifecycle testing**, **tag-based execution**, **HTML reporting**, and **CI/CD integration using GitHub Actions**.

The framework is designed to simulate **real-world automation scenarios** used in QA, SDET, and trading system environments.

---

## 🧠 Key Features
- BDD-based testing using **Gherkin (Given–When–Then)**
- API automation using **Python requests**
- OMS-style **Order Lifecycle Testing** (New → Modify → Cancel)
- Tag-based execution (`@api`, `@regression`, `@oms`)
- Professional **HTML test reports**
- **CI/CD integration** with GitHub Actions
- Linux-compatible execution

---

## 🛠 Tech Stack
- **Language:** Python 3.10+
- **BDD Framework:** Behave
- **API Testing:** requests
- **Reporting:** behave-html-formatter
- **Version Control:** Git & GitHub
- **CI/CD:** GitHub Actions
- **OS:** Windows / Linux

---

## 📂 Project Structure
```

bdd_test_framework/
│
├── features/
│   ├── login.feature
│   ├── api_login.feature
│   ├── oms_order.feature
│   │
│   └── steps/
│       ├── login_steps.py
│       ├── api_login_steps.py
│       └── oms_order_steps.py
│
├── reports/
│   ├── api_report.html
│   └── regression_report.html
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/bdd-automation-framework.git
cd bdd-automation-framework
````

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install behave requests behave-html-formatter
```

---

## ▶️ Running Tests

### 🔹 Run All Tests

```bash
behave
```

---

### 🔹 Run API Tests Only

```bash
behave --tags=api
```

---

### 🔹 Run OMS Order Lifecycle Tests

```bash
behave --tags=oms --no-capture
```

---

### 🔹 Debug with Console Logs

```bash
behave --tags=api --no-capture
```

---

## 📊 Generate HTML Reports

### 🔹 API Test Report

```bash
behave --tags=api -f behave_html_formatter:HTMLFormatter -o reports/api_report.html
```

### 🔹 Full Regression Report

```bash
behave -f behave_html_formatter:HTMLFormatter -o reports/regression_report.html
```

📌 Open the report by double-clicking the HTML file inside the `reports` folder.

---

## 🔁 CI/CD Integration (GitHub Actions)

The project includes a CI/CD pipeline that:

* Runs tests automatically on every push
* Executes in a Linux environment
* Generates HTML reports
* Uploads reports as build artifacts

### 📄 CI/CD Workflow File

Path:

```
.github/workflows/ci.yml
```

Pipeline includes:

* Code checkout
* Python setup
* Dependency installation
* Automated test execution
* HTML report upload

---

## 🚀 Future Enhancements

* Order execution / partial fills
* Negative OMS test scenarios
* Environment-based configuration
* Logging and config management
* Dockerized execution

---

## 👤 Author

**Ritik Kumar**
Automation | QA | SDET 

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or improve it!

```


