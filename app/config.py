# ==========================================================
# config.py
# Central configuration file for the project
# ==========================================================

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==========================================================
# PROJECT PATHS
# ==========================================================

# app folder
APP_DIR = Path(__file__).resolve().parent

# project root folder
ROOT_DIR = APP_DIR.parent

# Data folder
DATA_DIR = ROOT_DIR / "Data"

# CSV file
DATA_FILE = DATA_DIR / "Sample - Superstore.csv"

# ==========================================================
# GEMINI API
# ==========================================================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ==========================================================
# APP SETTINGS
# ==========================================================

APP_TITLE = "📊 AI Sales Data Analyst"

PAGE_ICON = "📊"

LAYOUT = "wide"