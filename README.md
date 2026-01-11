# AI-Powered Selenium Test Automation Framework

AI-driven test automation using Google Gemini AI, n8n workflow orchestration, GitHub Actions CI/CD, and LambdaTest cloud execution.

## 🚀 Quick Start Guide

### Prerequisites (All FREE Tiers)
- GitHub account
- LambdaTest account (free tier)
- n8n Cloud account (free tier)
- Google account (for Sheets & Gemini API)

### Step 1: Configure LambdaTest Credentials (5 minutes)

1. **Get LambdaTest Credentials:**
   - Go to https://accounts.lambdatest.com/dashboard
   - Click your profile → Settings → Access Keys
   - Copy your `LT_USERNAME` and `LT_ACCESS_KEY`

2. **Add to GitHub Secrets:**
   - Go to this repository → Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Add secret name: `LT_USERNAME`, value: your username
   - Add secret name: `LT_ACCESS_KEY`, value: your access key

### Step 2: Configure GitHub Token for n8n (5 minutes)

1. **Generate GitHub Personal Access Token:**
   - Go to https://github.com/settings/tokens/new
   - Set note: "n8n Workflow Access"
   - Select scopes:
     - ✓ `repo` (Full control of private repositories)
     - ✓ `workflow` (Update GitHub Action workflows)
   - Click "Generate token"
   - **COPY THE TOKEN NOW** (you won't see it again!)

2. **Update n8n Workflow:**
   - Go to your n8n workflow
   - Click on "HTTP Request1" node (GitHub Actions trigger)
   - In the Authorization header, replace:
     ```
     Bearer ghp_YOUR_GITHUB_TOKEN_HERE
     ```
     with:
     ```
     Bearer YOUR_ACTUAL_TOKEN
     ```
   - Save the workflow

### Step 3: Run Your First Test (2 minutes)

1. **Trigger the n8n webhook** (or use the workflow trigger)
2. **Check GitHub Actions tab** to see test execution
3. **View results in Google Sheets** (AI Test Results - LambdaTest)

## 📊 Architecture

```
Webhook → n8n (Gemini AI) → GitHub Actions → LambdaTest → Results → Google Sheets
```

## 🛠️ Components

- **AI Layer:** Google Gemini (test generation & analysis)
- **Orchestration:** n8n Cloud Workflow
- **CI/CD:** GitHub Actions
- **Test Execution:** LambdaTest Cloud Grid
- **Reporting:** Google Sheets
- **Version Control:** GitHub

## 📁 Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── test_runner.yml    # GitHub Actions workflow
├── tests/
│   ├── __init__.py
│   └── test_tummytales.py     # Sample Selenium tests
└── README.md
```

## 💰 Cost: $0/month

All services use FREE tiers:
- ✅ GitHub Actions (unlimited for public repos)
- ✅ n8n Cloud (200 executions/month)
- ✅ LambdaTest (limited free minutes)
- ✅ Google Sheets (free)
- ✅ Gemini API (60 req/min free)

## 🧪 Test File Structure

See `tests/test_tummytales.py` for example test structure using:
- Pytest framework
- LambdaTest Remote WebDriver
- Selenium WebDriver

## 📝 Notes

- Tests run on Windows 10 + Chrome (latest)
- Results automatically logged to Google Sheets
- Execution time varies based on test complexity
- LambdaTest free tier has monthly minute limits

## 🚧 Status

**Current:** Architecture complete, requires credential configuration
**Next:** Add more test cases, enhance AI test generation

## 📚 Resources

- [LambdaTest Documentation](https://www.lambdatest.com/support/docs/)
- [n8n Documentation](https://docs.n8n.io/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Pytest Selenium](https://pytest-selenium.readthedocs.io/)

---
**Built with ❤️ for automated testing excellence**
