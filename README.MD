Overview
Selenium Google Scraper is a Python-based tool I developed to automate scraping Google search results. It uses Selenium to handle dynamic page loading, bypassing basic anti-bot measures, and extracts structured data like titles, links, snippets, and metadata. Ideal for research, SEO analysis, or data collection, this project highlights my experience with web automation, handling JavaScript-heavy sites, and ethical scraping practices.
Important Disclaimer: Respect Google's Terms of Service and robots.txt. Use responsibly—e.g., with delays between requests and proxies for high volume. This is for educational purposes only; not for commercial spam or violation of policies.
Features

Dynamic Scraping: Handles infinite scroll and AJAX-loaded results with Selenium WebDriver.
Customizable Queries: Search by keywords, location, or filters (e.g., images, news).
Data Extraction: Parses results into JSON/CSV with fields like title, URL, description, and rank.
Error Handling: Built-in retries, headless mode, and proxy support to avoid blocks.
Modular Design: Easy to extend for other search engines or custom parsers.
Output Options: Save to file, database, or return as Python dict for integration.

Tech Stack

Language: Python 3.8+
Key Libraries:

selenium for browser automation.
webdriver-manager for automatic ChromeDriver setup.
beautifulsoup4 for HTML parsing (optional fallback).
pandas for data export to CSV/Excel.


No external services required beyond a web browser.

Getting Started
Prerequisites

Python 3.8 or higher.
Chrome browser installed (for WebDriver).
Git for cloning.

Installation

Clone the repository:
bashgit clone https://github.com/abd0o0/selenium-googlescrap.git
cd selenium-googlescrap

Create a virtual environment and install dependencies:
bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

(Optional) Set up a .env file for configs:
textPROXY_SERVER=your_proxy_if_needed
USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
DELAY_SECONDS=2  # Time between requests


Usage

Basic Search via CLI:
bashpython scraper.py --query "python selenium tutorial" --num_results 10 --output results.json
This fetches the top 10 results and saves them as JSON.
Programmatic Use (in a Python script):
pythonfrom scraper import GoogleScraper
import json

# Initialize scraper (headless mode for background runs)
scraper = GoogleScraper(headless=True, delay=2)

# Perform search
results = scraper.search("machine learning trends 2025", num_results=20)

# Print or save results
print(json.dumps(results, indent=2))
# Example output: [{"title": "Top ML Trends...", "url": "https://...", "snippet": "..."}]

Advanced Options:

Add --filter images for Google Images.
Use --proxy your_proxy:port to rotate IPs.
Run python scraper.py --help for full flags.



Examples and sample output are in the /examples folder. See /docs for handling CAPTCHAs or scaling.
Project Structure
textselenium-googlescrap/
├── scraper/           # Core scraping logic
│   ├── __init__.py
│   ├── google_scraper.py  # Main Selenium class
│   └── parsers.py     # HTML result extraction
├── examples/          # Sample scripts and data
│   └── sample_search.py
├── tests/             # Unit tests (run with `pytest`)
├── requirements.txt   # Dependencies
├── .env.example       # Config template
├── scraper.py         # CLI entry point
└── README.md          # This file
Contributing
Feedback or enhancements welcome! To contribute:

Fork the repo.
Create a branch (git checkout -b feature/add-bing-support).
Commit changes (git commit -m "Add proxy rotation").
Push and open a pull request.

Follow PEP 8 for code style. Test with pytest before submitting.
