# SHL Assessment Recommendation System

An intelligent recommendation engine designed to assist hiring managers in selecting the most relevant SHL assessments based on natural language job descriptions or queries.

## 🚀 Overview

The system simplifies the assessment selection process by analyzing job descriptions or plain queries and recommending the most relevant SHL assessments. It returns up to 10 recommended tests with detailed attributes, leveraging modern NLP and LLM techniques for relevance matching.

## 🛠 Features

- 🔍 Accepts free-text job descriptions or URLs
- 🤖 Uses AI to find the best-matching SHL assessments
- 🧾 Returns:
  - Assessment name (linked to SHL catalog)
  - Remote testing support (Yes/No)
  - Adaptive/IRT support (Yes/No)
  - Duration
  - Test type
- 🧠 Evaluated using Mean Recall@3 and MAP@3
- 🌐 Web-based demo and API available

## 💻 Tech Stack

- Python
- OpenAI/Gemini APIs (LLMs)
- BeautifulSoup / Scrapy (optional for catalog crawling)
- FAISS / Chroma / Weaviate (vector search)
- Streamlit / Gradio (demo UI)
- FastAPI / Flask (API)
- GitHub + Replit / Render / Vercel (deployment)

## ⚙️ Installation & Usage

```bash
# Clone the repo
git clone https://github.com/yourusername/shl-assessment-recommender.git
cd shl-assessment-recommender

# Create a virtual environment & activate
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py  # or python app.py if using Flask
