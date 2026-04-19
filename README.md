<div align="center">

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Groq-allam--2--7b-00A67E?style=for-the-badge&logo=groq&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>

<br/><br/>

```
  █████╗ ██╗     ██████╗ ██████╗ ██████╗ ███████╗
 ██╔══██╗██║    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
 ███████║██║    ██║     ██║   ██║██║  ██║█████╗  
 ██╔══██║██║    ██║     ██║   ██║██║  ██║██╔══╝  
 ██║  ██║██║    ╚██████╗╚██████╔╝██████╔╝███████╗
 ╚═╝  ╚═╝╚═╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
        A S S I S T A N T
```

### ⚡ A beautiful AI-powered code assistant built with Groq + Streamlit

[Features](#-features) · [Installation](#-installation) · [Usage](#-usage) · [Modes](#-modes) · [Project Structure](#-project-structure) · [Contributing](#-contributing)

<br/>

</div>

---

## ✨ Features

- 🐛 **Debug & Fix** — Paste broken code, get it fixed with explanations
- 🚀 **Improve** — Refactor and optimize your code to production quality
- ⚙️ **Generate** — Describe what you want, get clean runnable code
- 🎨 **UI Helper** — Build and design beautiful UI components
- 💡 **Idea Generator** — Brainstorm your next big project
- 📊 **Explainer** — Understand any code with step-by-step visual breakdowns
- ⚡ **Powered by Groq** — Ultra-fast inference with `allam-2-7b`
- 🎯 **Modular architecture** — Each mode is a clean, independent Python class
- 🌊 **Streaming responses** — See answers appear in real time

---

## 🖼️ Preview

```
┌─────────────────────────────────────────────────────┐
│  AI  AI Code Assistant                    GROQ-3    │
├─────────────────────────────────────────────────────┤
│                                                     │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│   │ 🐛 Error │  │🚀 Improve│  │⚙️ Generate│        │
│   │ Fix bugs │  │ Refactor │  │ From desc│        │
│   └──────────┘  └──────────┘  └──────────┘        │
│                                                     │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│   │ 🎨  UI  │  │ 💡 Ideas │  │📊 Explain│        │
│   │ Design  │  │Brainstorm│  │Visualize │        │
│   └──────────┘  └──────────┘  └──────────┘        │
│                                                     │
│  ┌─────────────────────────────────────────────┐   │
│  │  Type your message...                   ⚡  │   │
│  └─────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

---

## 📦 Installation

### Prerequisites
- Python 3.10+
- A free [Groq API key](https://console.groq.com) 

### 1. Clone the repository

```bash
git clone https://github.com/Abdullah3021-ace/Python-Code-Assistant.git
cd Python-Code-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your API key

Create a `.env` file in the project root:

```bash
touch .env
```

Add your Groq API key inside it:

```env
GROQ_API_KEY=your-groq-api-key-here
```

> 🔑 Get your free API key at [console.groq.com](https://console.groq.com)  
> ⚠️ **Never commit your `.env` file** — it's already in `.gitignore`

---

## 🚀 Usage

```bash
streamlit run app.py
```

The app will open at **http://localhost:8501**

---

## 🎯 Modes

| Mode | Icon | What it does |
|------|:----:|---|
| **Error** | 🐛 | Identifies all bugs, explains root causes, provides fixed code |
| **Improve** | 🚀 | Refactors code for performance, readability, and best practices |
| **Generate** | ⚙️ | Writes complete, production-ready code from a description |
| **UI** | 🎨 | Designs and builds UI components (Streamlit, HTML, Tkinter, etc.) |
| **Ideas** | 💡 | Brainstorms project concepts with tech stacks and MVP scopes |
| **Explain** | 📊 | Breaks down code step-by-step with ASCII diagrams and flowcharts |

---

## 📁 Project Structure

```
Python-Code-Assistant/
│
├── app.py                  # 🖥️  Streamlit UI — main entry point
├── config.py               # ⚙️  API settings and tag configuration
├── grok_client.py          # 🔌  Groq API handler (streaming)
├── router.py               # 🔀  Routes selected mode to correct module
├── utils.py                # 🛠️  Shared helpers (prompt loader, formatters)
├── requirements.txt        # 📦  Python dependencies
├── .env                    # 🔑  Your API key (not committed)
├── .gitignore
│
├── modules/                # 🧩  One class per mode
│   ├── __init__.py
│   ├── error_handler.py    # 🐛  Fix & debug
│   ├── code_improver.py    # 🚀  Optimize & refactor
│   ├── code_generator.py   # ⚙️   Generate from description
│   ├── ui_helper.py        # 🎨  UI/UX components
│   ├── idea_generator.py   # 💡  Brainstorm ideas
│   └── explainer.py        # 📊  Visual explanations
│
└── prompts/                # 📝  System prompts for each mode
    ├── error.txt
    ├── improve.txt
    ├── generate.txt
    ├── ui.txt
    ├── ideas.txt
    └── explain.txt
```

---

## 🔧 PyCharm Setup

1. Open the project folder in **PyCharm**
2. Go to **File → Settings → Python Interpreter → Add Interpreter → Virtualenv**
3. Select the `.venv` folder created above
4. Open the terminal inside PyCharm and run:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```
5. Or create a **Run Configuration**:
   - Script path: path to `streamlit` in your venv
   - Parameters: `run app.py`
   - Working directory: project root

---

## 🛠️ Customising Prompts

Every mode is driven by a plain-text prompt in the `prompts/` folder. Edit any `.txt` file to change how the AI behaves. For example, edit `prompts/explain.txt` to make explanations more beginner-friendly, or `prompts/generate.txt` to always generate type-annotated code.

---

## 🔄 Switching Models

Open `config.py` and change:

```python
GROK_MODEL = "allam-2-7b"   # change to any Groq-supported model
```

Popular Groq models:
| Model | Speed | Best for |
|---|---|---|
| `allam-2-7b` | ⚡⚡⚡ | Arabic + English code tasks |
| `llama3-70b-8192` | ⚡⚡ | Complex reasoning |
| `llama3-8b-8192` | ⚡⚡⚡ | Fast general use |
| `mixtral-8x7b-32768` | ⚡⚡ | Long context tasks |

---

## 📋 Requirements

```
streamlit>=1.32.0
openai>=1.30.0
groq>=0.9.0
python-dotenv>=1.0.0
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m "Add amazing feature"`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Built with ❤️ using [Groq](https://groq.com) · [Streamlit](https://streamlit.io) · Python

⭐ Star this repo if you found it useful!

</div>
