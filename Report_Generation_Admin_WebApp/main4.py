import streamlit as st
from google.cloud import firestore
import pandas as pd
from google.cloud.firestore import FieldFilter
from io import BytesIO
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
import time
import zipfile
import os
import pytz
import random
from scipy import signal
from scipy.stats import skew, kurtosis
from collections import defaultdict
import matplotlib.dates as mdates
import plotly.express as px
import plotly.graph_objects as go
from google.api_core.exceptions import ResourceExhausted, RetryError
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Line
import tempfile
import plotly.io as pio
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

st.set_page_config(page_title="Login", layout="wide")

# Initialize authentication state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None

def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "MUKUND" and password == "Muk2025$$":  # Replace with actual credentials
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success("Login successful! Redirecting...")
            st.rerun()  # Refresh the page to apply authentication state
        else:
            st.error("Invalid credentials")

# Run the login function
login()

# Redirect to main page after successful login
if st.session_state["authenticated"]:
    st.switch_page("pages/main5.py")
