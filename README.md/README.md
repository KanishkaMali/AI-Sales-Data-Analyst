# 📊 AI Sales Data Analyst using Generative AI

> An AI-powered Business Intelligence application that combines **Python**, **Power BI**, **Streamlit**, and **Google Gemini AI** to transform raw sales data into interactive dashboards, automated insights, and natural language business analysis.

---

# 📖 Project Overview

Modern organizations generate thousands of sales transactions every day. Although these datasets contain valuable business information, extracting meaningful insights often requires technical knowledge in SQL, Business Intelligence tools, or programming.

This project bridges the gap between traditional data analytics and Generative AI by allowing users to explore business data using natural language.

The application performs complete business analysis, generates interactive visualizations, answers business questions using AI, and produces downloadable reports—all through a simple web interface.

Instead of manually searching through dashboards, users can simply ask questions like:

- Which state generated the highest sales?
- Which category is the most profitable?
- Show the top 10 customers.
- Which products are making losses?
- What are the business recommendations?

The application automatically analyzes the data and returns accurate business insights along with tables and visualizations.

---

# 🎯 Business Problem

Retail businesses generate a massive amount of transactional data every day. This data contains valuable information about customers, products, sales, profits, discounts, and regional performance.

However, most organizations face several challenges:

- Business users cannot easily analyze large datasets.
- Traditional dashboards require manual exploration.
- Decision-makers often depend on analysts for reports.
- Static reports cannot answer new business questions instantly.
- Non-technical users cannot write SQL queries or Python code.
- Identifying trends, losses, and opportunities takes significant time.

As a result, businesses may miss opportunities to improve profitability and make faster data-driven decisions.

---

# 💡 Proposed Solution

The AI Sales Data Analyst solves these challenges by combining Business Intelligence with Generative AI.

The system:

- Cleans and preprocesses raw sales data.
- Performs Exploratory Data Analysis (EDA).
- Creates interactive Power BI dashboards.
- Builds an AI-powered Streamlit web application.
- Converts natural language questions into structured business analysis.
- Generates AI-powered explanations using Google Gemini.
- Allows users to download reports and analysis results.

This enables both technical and non-technical users to interact with business data more efficiently.

---

# 🎯 Project Objectives

The primary objectives of this project are:

- Perform end-to-end sales data analysis.
- Clean and preprocess raw business data.
- Build interactive dashboards for decision-making.
- Analyze sales, profit, customers, products, and regional performance.
- Integrate Generative AI into the analytics workflow.
- Enable natural language business queries.
- Generate automated business insights and recommendations.
- Simplify business analytics for non-technical users.

---

# ✨ Key Features

## 📂 Data Processing

- Data Cleaning
- Missing Value Handling
- Duplicate Detection
- Date Conversion
- Feature Engineering

---

## 📊 Business Analytics

- Sales Analysis
- Profit Analysis
- Customer Analysis
- Product Analysis
- State Analysis
- Regional Analysis
- Time Series Analysis

---

## 📈 Interactive Dashboards

- KPI Cards
- Interactive Plotly Charts
- Power BI Dashboard
- Dynamic Filtering
- Business Visualizations

---

## 🤖 AI Features

- Natural Language Question Answering
- AI Business Insights
- Intelligent Business Recommendations
- Google Gemini Integration
- AI Router
- AI Explanation Engine

---

## 📄 Export Features

- Download CSV Results
- Download AI Analysis Report
- Business Summary Generation

---

# 🚀 End-to-End Workflow

Raw Dataset

⬇

Data Cleaning (Pandas)

⬇

Exploratory Data Analysis (Jupyter Notebook)

⬇

Interactive Dashboard (Power BI)

⬇

Streamlit Web Application

⬇

Business Analysis Engine

⬇

AI Router

⬇

Google Gemini AI

⬇

Business Insights & Reports

# 📂 Dataset Information

The project uses the **Sample Superstore Dataset**, a widely used retail sales dataset for learning Data Analytics, Business Intelligence, and Data Visualization.

## Dataset Details

| Attribute | Description |
|-----------|-------------|
| Dataset Name | Sample Superstore |
| Source | Kaggle |
| File Format | CSV |
| Total Rows | 9,994 |
| Total Columns | 21 |
| Time Period | 2014 – 2017 |
| Domain | Retail Sales |

---

## Dataset Features

The dataset contains transactional information such as:

| Column | Description |
|---------|-------------|
| Order ID | Unique Order Identifier |
| Order Date | Date when order was placed |
| Ship Date | Shipping Date |
| Ship Mode | Shipping Method |
| Customer ID | Unique Customer Identifier |
| Customer Name | Customer Name |
| Segment | Customer Segment |
| Country | Customer Country |
| City | Customer City |
| State | Customer State |
| Postal Code | Postal Code |
| Region | Sales Region |
| Product ID | Product Identifier |
| Category | Product Category |
| Sub-Category | Product Sub Category |
| Product Name | Product Name |
| Sales | Sales Amount |
| Quantity | Quantity Ordered |
| Discount | Discount Given |
| Profit | Profit Earned |
| Row ID | Record Identifier |

---

# 🛠️ Technology Stack

The project combines Business Intelligence, Data Analytics, Web Development, and Generative AI.

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Pandas | Data Cleaning & Analysis |
| NumPy | Numerical Operations |
| Plotly | Interactive Charts |
| Streamlit | Web Application |
| Power BI | Interactive Dashboard |
| Google Gemini AI | AI Business Insights |
| Jupyter Notebook | Exploratory Data Analysis |
| Git | Version Control |
| GitHub | Project Repository |
| VS Code | Development Environment |

---

# 🏗️ Project Architecture

The project follows a modular architecture where each component has a specific responsibility.

```text
                    Sample Superstore CSV
                             │
                             ▼
                     Data Cleaning (Pandas)
                             │
                             ▼
              Exploratory Data Analysis (EDA)
                             │
                             ▼
                  Power BI Dashboard
                             │
                             ▼
                  Streamlit Web Application
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
 Business Analyzer      Chart Generator      AI Router
        │                    │                    │
        └────────────────────┼────────────────────┘
                             ▼
                     Google Gemini AI
                             │
                             ▼
                 AI Insights & Recommendations
                             │
                             ▼
          CSV Export • AI Report • Business Dashboard
```

---

# 📁 Project Folder Structure

```text
AI_Data_Analyst_Project/
│
├── app/
│   ├── app.py                 # Main Streamlit Application
│   ├── analysis.py            # Business Analysis Engine
│   ├── ai_router.py           # Converts Natural Language into Structured Analysis
│   ├── ai_explainer.py        # AI Explanation Generator using Gemini
│   ├── charts.py              # Plotly Chart Functions
│   ├── data_loader.py         # Dataset Loading & Preprocessing
│   ├── utils.py               # Helper Functions
│   ├── config.py              # Project Configuration
│   ├── requirements.txt       # Python Dependencies
│   └── .env                   # Gemini API Key (Not uploaded to GitHub)
│
├── Data/
│   └── Sample - Superstore.csv
│
├── notebooks/
│   ├── 01_Data_Loading.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_Exploratory_Data_Analysis.ipynb
│
├── PowerBI/
│   └── Sales_Dashboard.pbix
│
├── Reports/
│   ├── AI_Report.txt
│   └── Business_Insights.pdf
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🔄 Data Flow

The complete project follows the workflow below:

```text
CSV Dataset
      │
      ▼
Load Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Business KPIs
      │
      ▼
Power BI Dashboard
      │
      ▼
Streamlit Application
      │
      ▼
User asks a Question
      │
      ▼
AI Router identifies:
 • Metric
 • Dimension
 • Filters
 • Aggregation
      │
      ▼
Business Analyzer
      │
      ▼
Pandas executes analysis
      │
      ▼
Result Table + Plotly Chart
      │
      ▼
Google Gemini AI
      │
      ▼
Business Explanation
      │
      ▼
CSV Export & AI Report
```

---

# 📌 Project Modules

| Module | Description |
|---------|-------------|
| Data Loader | Loads and preprocesses the dataset |
| Business Analyzer | Executes business calculations using Pandas |
| AI Router | Converts natural language questions into structured JSON |
| Chart Engine | Creates interactive Plotly visualizations |
| AI Explainer | Generates business insights using Gemini AI |
| Streamlit UI | User interface for analytics and AI interaction |
| Power BI | Executive dashboards and business reporting |

---

# 🎯 Key Capabilities

✅ Data Cleaning & Preprocessing

✅ Exploratory Data Analysis (EDA)

✅ KPI Calculation

✅ Interactive Plotly Charts

✅ Power BI Dashboards

✅ AI-Powered Business Question Answering

✅ Dynamic Business Analysis

✅ AI Generated Business Recommendations

✅ CSV Export

✅ AI Report Download

✅ Interactive Web Application

# 🧹 Data Cleaning & Exploratory Data Analysis (EDA)

Data Cleaning and Exploratory Data Analysis (EDA) form the foundation of every successful data analytics project. Before building dashboards or generating AI insights, the dataset was carefully examined, cleaned, and transformed to ensure accuracy and reliability.

The cleaning process was performed using **Python** and the **Pandas** library in **Jupyter Notebook**.

---

# 📋 Data Cleaning Process

The following steps were performed to prepare the dataset for analysis.

## 1️⃣ Dataset Loading

The Sample Superstore dataset was loaded into a Pandas DataFrame.

```python
import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", encoding="cp1252")
```

---

## 2️⃣ Dataset Inspection

The structure of the dataset was examined using:

- `df.head()`
- `df.info()`
- `df.describe()`
- `df.shape`
- `df.columns`

These functions helped understand:

- Number of records
- Data types
- Missing values
- Numerical statistics
- Column names

---

## 3️⃣ Missing Value Analysis

The dataset was checked for missing values.

```python
df.isnull().sum()
```

### Observation

The Sample Superstore dataset contains **no missing values**, allowing further analysis without imputation.

---

## 4️⃣ Duplicate Record Check

Duplicate rows were identified using:

```python
df.duplicated().sum()
```

### Action Taken

Duplicate records (if any) were removed to avoid incorrect calculations.

```python
df.drop_duplicates(inplace=True)
```

---

## 5️⃣ Date Conversion

The Order Date and Ship Date columns were converted into datetime format.

```python
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
```

This enabled:

- Monthly analysis
- Yearly analysis
- Time series visualization

---

## 6️⃣ Feature Engineering

Additional columns were created for business analysis.

Example:

```python
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.strftime("%B")
```

These features simplify filtering and trend analysis.

---

## 7️⃣ Data Validation

The cleaned dataset was verified by checking:

- Correct data types
- Duplicate removal
- Proper date conversion
- Numerical summaries
- Dataset dimensions

The final cleaned dataset was then used for all dashboards and AI analysis.

---

# 📊 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand business performance across different dimensions.

The analysis focuses on identifying:

- Sales trends
- Profitability
- Customer behavior
- Product performance
- Regional performance
- Time-based trends

---

# 📈 Sales by Category

The total sales generated by each product category were analyzed.

### Purpose

Identify which product category contributes the highest revenue.

### Key Insight

- Technology generated the highest sales.
- Furniture contributed significant sales but lower profitability.
- Office Supplies produced consistent sales.

> 📷 **Insert Screenshot:** Sales by Category Plotly Bar Chart

---

# 🌍 Sales by Region

Sales were analyzed across the four business regions.

### Purpose

Evaluate regional business performance.

### Key Insight

- West Region generated the highest sales.
- East Region followed closely.
- Central and South regions showed comparatively lower revenue.

> 📷 **Insert Screenshot:** Sales by Region Pie Chart

---

# 🗺️ State-wise Sales Analysis

Sales performance was analyzed at the state level.

### Purpose

Identify the highest-performing states.

### Key Insight

- California generated the highest sales.
- New York was among the top-performing states.
- Several states showed relatively lower sales.

> 📷 **Insert Screenshot:** State Sales Chart

---

# 👥 Customer Analysis

Customer purchasing behavior was analyzed.

### Purpose

Identify high-value customers contributing the most revenue.

### Key Insight

- A small number of customers contributed a significant share of total sales.
- Identifying these customers enables loyalty and retention strategies.

> 📷 **Insert Screenshot:** Top Customers Chart

---

# 📦 Product Analysis

Product-wise sales performance was evaluated.

### Purpose

Identify the best-selling products.

### Key Insight

- A few products generated exceptionally high sales.
- These products represent major revenue contributors.

> 📷 **Insert Screenshot:** Top Products Chart

---

# 💰 Profit Analysis

Profit was analyzed across different product categories.

### Purpose

Determine which categories generate the highest profit.

### Key Insight

- Technology generated the highest overall profit.
- Furniture showed lower profitability despite strong sales.
- Some categories included products with negative profit.

> 📷 **Insert Screenshot:** Profit by Category Chart

---

# 📉 Loss Analysis

The dataset contains both positive and negative profit values.

Negative profit values indicate that a product or transaction resulted in a **business loss**.

Possible reasons include:

- High discounts
- Low selling price
- High operational cost
- Shipping expenses

This analysis helps identify products requiring business attention.

---

# 📅 Time Series Analysis

Monthly sales trends were analyzed over the available time period.

### Purpose

Understand seasonal sales behavior.

### Key Insight

- Sales varied across months.
- Certain months consistently recorded higher revenue.
- Time-based analysis helps businesses forecast future demand.

> 📷 **Insert Screenshot:** Monthly Sales Trend

---

# 📌 Summary of Business Insights

The exploratory analysis revealed several important business findings:

- Technology is the highest-performing category in terms of both sales and profit.
- California contributes the largest share of overall sales.
- The West region is the strongest-performing sales region.
- A limited number of customers generate a large portion of revenue.
- Several products and transactions result in business losses due to high discounts.
- Monthly sales patterns indicate seasonal demand variations.

These insights formed the foundation for the interactive Power BI dashboard and the AI-powered analytics application.

---

# 📚 Libraries Used During EDA

The following Python libraries were used during data cleaning and exploratory analysis:

- Pandas
- NumPy
- Plotly Express
- Matplotlib (if applicable)
- Jupyter Notebook

---

# 📌 Outcome of EDA

The cleaned dataset and analytical insights obtained during EDA were subsequently used to:

- Build interactive Power BI dashboards
- Develop the Streamlit web application
- Train the Business Analysis Engine
- Generate AI-powered business insights using Google Gemini
- Enable natural language querying of business data

# 📊 Power BI Dashboard Documentation

To provide an interactive business intelligence experience, Microsoft Power BI was used to create dynamic dashboards from the cleaned sales dataset.

The dashboards enable users to explore sales performance, customer behavior, product performance, and business trends through interactive visualizations and filters.

The dashboard was designed following Business Intelligence (BI) best practices, allowing users to quickly identify business opportunities and make data-driven decisions.

---

# 🎯 Dashboard Objectives

The Power BI dashboard was developed to:

- Monitor business performance using KPIs.
- Identify top-performing products and customers.
- Analyze sales across regions and states.
- Understand customer purchasing behavior.
- Track monthly sales trends.
- Compare profitability across categories.
- Enable interactive filtering for deeper analysis.

---

# 📌 Dashboard 1 – Executive Sales Overview

The Executive Dashboard provides a high-level summary of overall business performance.

It is intended for business managers and decision-makers who need a quick overview of sales and profitability.

## Key Performance Indicators (KPIs)

The dashboard displays the following KPI cards:

- 💰 Total Sales
- 📈 Total Profit
- 📦 Total Orders
- 👥 Total Customers

These KPIs provide an instant snapshot of overall business performance.

---

## Visualizations

The Executive Dashboard includes the following interactive visuals:

### 📍 Sales by Region

Displays total sales generated by each region.

Purpose:

- Compare regional performance.
- Identify the strongest sales region.

Business Insight:

The West region generated the highest sales, followed by the East region.

---

### 👥 Sales by Segment

Shows sales contribution by customer segment.

Segments include:

- Consumer
- Corporate
- Home Office

Purpose:

Understand which customer segment contributes the most revenue.

---

### 🗺️ Sales by State (Map)

Displays sales geographically across different states.

Purpose:

- Identify high-performing states.
- Analyze geographical sales distribution.

Business Insight:

California contributes the highest sales among all states.

---

### 📦 Top 10 Products

Displays the top-selling products based on total sales.

Purpose:

Identify products driving the highest revenue.

Business Value:

Helps inventory planning and marketing decisions.

---

### 👤 Top 10 Customers

Displays customers contributing the highest sales.

Purpose:

Identify valuable customers for loyalty programs and targeted marketing.

---

### 🎛️ Interactive Filters

The dashboard includes slicers for:

- Year
- Region
- Category
- Segment

Users can dynamically filter the dashboard without changing the underlying data.

---

> 📷 **Insert Screenshot:** Executive Dashboard

---

# 👥 Dashboard 2 – Customer Analytics

This dashboard focuses on customer purchasing behavior and customer performance.

The objective is to understand customer contribution, buying patterns, and customer segmentation.

---

## Visualizations

### 🏆 Top Customers by Sales

Ranks customers based on total sales.

Purpose:

Identify the highest-value customers.

---

### 💰 Customer Profit Analysis

Displays customer contribution to total profit.

Purpose:

Determine which customers are most profitable.

---

### 👥 Customer Segment Analysis

Analyzes sales distribution among:

- Consumer
- Corporate
- Home Office

Purpose:

Understand customer segmentation.

---

### 📦 Customer Purchase Quantity

Displays total quantity purchased by customers.

Purpose:

Identify customers placing large-volume orders.

---

### 📊 Customer Sales Distribution

Shows overall customer contribution using interactive charts.

Purpose:

Identify customer concentration.

---

### Business Insights

- A small number of customers contribute a significant portion of total revenue.
- Consumer segment generates the highest sales.
- High-value customers can be targeted for loyalty programs.

---

> 📷 **Insert Screenshot:** Customer Analytics Dashboard

---

# 📦 Dashboard 3 – Product Analytics

This dashboard focuses on product performance.

It helps businesses understand which products generate the highest revenue and profit.

---

## Visualizations

### 🏆 Top Selling Products

Ranks products based on sales.

Purpose:

Identify best-selling products.

---

### 💰 Profit by Category

Compares profitability among:

- Furniture
- Office Supplies
- Technology

Purpose:

Determine the most profitable category.

---

### 📊 Sales by Category

Displays category-wise sales.

Purpose:

Compare product categories.

---

### 📦 Sales by Sub-Category

Shows detailed performance of each sub-category.

Examples:

- Phones
- Chairs
- Storage
- Tables
- Binders

Purpose:

Identify strong and weak-performing sub-categories.

---

### 📉 Discount Analysis

Analyzes discounts offered across product categories.

Purpose:

Understand the impact of discounts on profitability.

---

### Business Insights

- Technology generates the highest profit.
- Furniture produces strong sales but relatively lower profit.
- High discounts reduce profitability.

---

> 📷 **Insert Screenshot:** Product Analytics Dashboard

---

# 📈 Dashboard 4 – Time Series Analysis

The Time Series Dashboard analyzes sales trends over time.

This dashboard enables businesses to understand seasonal trends and long-term performance.

---

## Visualizations

### 📅 Monthly Sales Trend

Displays monthly sales using a line chart.

Purpose:

Monitor sales performance over time.

---

### 📈 Monthly Profit Trend

Shows profit variation across months.

Purpose:

Analyze seasonal profitability.

---

### 📦 Monthly Order Trend

Displays order volume over time.

Purpose:

Identify periods of high customer activity.

---

### 📊 Year-wise Sales Comparison

Compares yearly sales performance.

Purpose:

Evaluate business growth.

---

### Business Insights

- Sales fluctuate across different months.
- Certain months consistently record higher revenue.
- Time-series analysis helps businesses forecast future demand.

---

> 📷 **Insert Screenshot:** Time Series Dashboard

---

# 🎛️ Dashboard Interactivity

Power BI provides several interactive capabilities.

The dashboards support:

- Cross-filtering
- Cross-highlighting
- Interactive slicers
- Drill-down analysis
- Dynamic filtering

Users can analyze data from multiple perspectives without modifying the dataset.

---

# 📊 Business Value of the Dashboard

The Power BI dashboard transforms raw transactional data into meaningful business insights.

Key business benefits include:

- Faster decision-making.
- Improved sales monitoring.
- Customer performance analysis.
- Product profitability analysis.
- Regional sales comparison.
- Interactive reporting.
- Executive-level business visualization.

---

# 📈 Dashboard Workflow

```text
Cleaned CSV Dataset
        │
        ▼
Power BI Import
        │
        ▼
Data Modeling
        │
        ▼
KPI Calculation
        │
        ▼
Interactive Visualizations
        │
        ▼
Business Filters
        │
        ▼
Interactive Dashboards
        │
        ▼
Business Insights
```

---

# 📌 Outcome

The Power BI dashboards provide a comprehensive Business Intelligence solution that enables users to monitor sales performance, analyze customer behavior, evaluate product profitability, and identify business trends through interactive visualizations.

These dashboards serve as the analytical foundation for the AI-powered Streamlit application, where users can further explore the data using natural language queries powered by Google Gemini AI.

# 🤖 AI Sales Analyst

The AI Sales Analyst is the core component of this project. It combines traditional data analytics with Generative AI to enable users to analyze business data using natural language instead of manually exploring dashboards.

Rather than navigating multiple charts or writing SQL queries, users can simply ask business questions in plain English, and the application automatically performs the required analysis and provides an AI-generated explanation.

Examples of supported questions include:

- Which state generated the highest sales?
- Show the top 10 customers by profit.
- Which category has the highest profit?
- Show sales in the West region during 2017.
- Which products are making losses?
- Compare Technology and Furniture sales.
- Show the monthly sales trend.
- Which customer segment generates the highest revenue?

The application automatically understands the question, performs the analysis using Pandas, and generates business-friendly insights using Google Gemini AI.

---

# 🎯 AI Module Objectives

The AI module was developed to achieve the following objectives:

- Allow users to interact with business data using natural language.
- Eliminate the need for SQL knowledge.
- Automatically perform business calculations.
- Generate business insights using Generative AI.
- Explain analytical results in simple language.
- Produce downloadable reports for business users.
- Make data analytics accessible to non-technical users.

---

# ⚙️ AI Workflow

The application follows a modular workflow for processing every user query.

```text
User Question
      │
      ▼
AI Router
      │
      ▼
Structured JSON
      │
      ▼
Business Analyzer
      │
      ▼
Pandas Data Analysis
      │
      ▼
Analysis Result
      │
      ▼
Google Gemini AI
      │
      ▼
Business Explanation
      │
      ▼
Download Report / CSV
```

---

# 🧠 AI Router

The AI Router is responsible for converting natural language questions into structured instructions that the Business Analysis Engine can understand.

Instead of directly asking Gemini to analyze the dataset, the router first extracts:

- Metric
- Dimension
- Filters
- Aggregation
- Top/Bottom values
- Sorting
- Required output

Example:

User Question:

```
Show the top 5 states by sales.
```

Router Output:

```json
{
    "metric": "Sales",
    "dimension": "State",
    "aggregation": "sum",
    "top": 5,
    "sort": "desc"
}
```

This structured format makes the application more accurate, scalable, and reliable.

---

# 📊 Business Analysis Engine

The Business Analysis Engine is implemented using **Pandas**.

Instead of sending the complete dataset to Gemini, the analysis engine performs all calculations locally.

Responsibilities include:

- Sales Analysis
- Profit Analysis
- Customer Analysis
- Product Analysis
- Regional Analysis
- State Analysis
- Category Analysis
- Time Series Analysis
- Filtering
- Grouping
- Aggregation
- Sorting

This approach improves performance, reduces API usage, and ensures that calculations are based on the actual dataset.

---

# 💬 Google Gemini AI Integration

Google Gemini AI is used to transform numerical analysis into human-readable business insights.

The AI does not perform calculations directly. Instead, it receives the structured analysis generated by the Business Analysis Engine and explains the results in a clear and professional manner.

Example:

Analysis Result:

| State | Sales |
|-------|-------:|
| California | 457687 |

Gemini Explanation:

> California generated the highest sales among all states. This indicates a strong customer base and high market demand in the region. Businesses may consider expanding operations and marketing efforts in California while identifying opportunities to improve performance in lower-performing states.

---

# 🌐 Streamlit Web Application

The complete analytics system is deployed using **Streamlit**.

The application provides an interactive web interface where users can:

- View KPI Cards
- Explore Plotly Charts
- Ask AI-powered business questions
- Download CSV files
- Download AI-generated reports
- View previous questions
- Analyze business performance in real time

---

# 📊 Interactive Visualizations

The application includes multiple Plotly visualizations:

- Sales by Category
- Sales by Region
- Monthly Sales Trend
- State-wise Sales
- Top Customers
- Top Products
- Profit by Category

All visualizations update automatically based on the processed dataset.

---

# 📁 Modular Project Structure

The project follows a modular software architecture to improve readability, maintainability, and scalability.

| File | Responsibility |
|------|----------------|
| `app.py` | Main Streamlit User Interface |
| `analysis.py` | Business Analysis Engine |
| `ai_router.py` | Converts user questions into structured JSON |
| `ai_explainer.py` | Generates business explanations using Gemini AI |
| `charts.py` | Creates Plotly visualizations |
| `data_loader.py` | Loads and preprocesses the dataset |
| `utils.py` | Common utility functions |
| `config.py` | Stores application configuration |

---

# 🔄 Query Processing Example

The following example illustrates how the system processes a user query.

### Step 1

User enters:

```
Which state generated the highest sales?
```

↓

### Step 2

AI Router identifies:

- Metric → Sales
- Dimension → State
- Aggregation → Sum
- Sorting → Descending

↓

### Step 3

Business Analyzer executes the required Pandas operations.

↓

### Step 4

The resulting table is displayed in the Streamlit application.

↓

### Step 5

Gemini AI explains the findings in natural language.

↓

### Step 6

The user can download the results as a CSV file or generate an AI report.

---

# 📄 Report Generation

The application allows users to export analysis results for documentation and sharing.

Supported exports include:

- 📥 CSV Download
- 📄 AI Business Report
- 📊 Analysis Tables

The generated report contains:

- User Question
- Router Output
- Analysis Result
- AI Explanation

---

# 🚀 Key AI Features

- Natural Language Querying
- AI Business Insights
- Intelligent Data Analysis
- Modular AI Architecture
- Business Recommendation Generation
- Downloadable Reports
- CSV Export
- Interactive Dashboard
- Google Gemini Integration
- Scalable Business Analysis Engine

---

# 🎯 Business Benefits

The AI Sales Analyst provides significant value to businesses by:

- Reducing manual analysis time.
- Allowing non-technical users to explore business data.
- Generating faster and more consistent insights.
- Improving decision-making through AI-assisted analytics.
- Combining Business Intelligence with Generative AI in a single platform.

---

# 📌 Outcome

The AI Sales Analyst transforms raw sales data into meaningful business intelligence by combining Python, Pandas, Streamlit, Plotly, Power BI, and Google Gemini AI.

The modular architecture ensures scalability, maintainability, and ease of future enhancements while providing users with an intuitive and intelligent analytics experience.

# ⚙️ Installation & Setup

Follow the steps below to run the project on your local machine.

---

# 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Sales-Data-Analyst.git
```

Navigate to the project directory:

```bash
cd AI-Sales-Data-Analyst
```

---

# 2️⃣ Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Activate the environment

Command Prompt

```bash
venv\Scripts\activate
```

PowerShell

```bash
venv\Scripts\Activate.ps1
```

---

# 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4️⃣ Configure Gemini API

Create a file named

```
.env
```

Add your API key

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

You can obtain your API key from:

https://aistudio.google.com/

---

# 5️⃣ Run Streamlit

Navigate to the app folder

```bash
cd app
```

Run

```bash
streamlit run app.py
```

The application will open automatically in your browser.

Default URL

```
http://localhost:8501
```

---

# 💻 Software Requirements

- Python 3.10+
- Visual Studio Code
- Jupyter Notebook
- Power BI Desktop
- Git
- GitHub
- Google Gemini API Key

---

# 📦 Python Libraries

The project uses the following libraries:

- streamlit
- pandas
- numpy
- plotly
- python-dotenv
- google-genai
- openpyxl

Install them using:

```bash
pip install -r requirements.txt
```

---

# 📁 Project Requirements

The following files are required:

```
Sample - Superstore.csv

.env

requirements.txt
```

---

# ▶️ How to Use the Application

1. Start the Streamlit server.
2. Load the dataset automatically.
3. View KPI Cards.
4. Explore interactive charts.
5. Ask business questions.
6. Download CSV results.
7. Download AI reports.

The application performs the analysis automatically.

# 📊 Project Results

The project successfully combines Business Intelligence with Generative AI to create an intelligent analytics platform.

The application can:

✅ Analyze retail sales data

✅ Generate interactive dashboards

✅ Answer business questions

✅ Produce AI-generated insights

✅ Create downloadable reports

---

# 📈 Business Insights Obtained

Some key insights identified during analysis include:

- Technology is the highest revenue-generating category.
- California contributes the highest sales.
- The West region performs better than other regions.
- A small number of customers generate a significant share of revenue.
- Several products incur losses due to high discounts.
- Monthly sales exhibit seasonal trends.
- Profitability varies across categories and regions.

These insights help organizations make informed business decisions.

---

# 📷 Project Screenshots

## Dashboard

Insert Screenshot

```
images/dashboard.png
```

---

## Power BI Dashboard

Insert Screenshot

```
images/powerbi.png
```

---

## AI Question Answering

Insert Screenshot

```
<img width="1596" height="809" alt="image" src="https://github.com/user-attachments/assets/92671548-42da-43a8-9cd6-dec474eeb60b" />

```

---

## Business Analysis

Insert Screenshot

```
images/analysis.png
```

---

## Download Report

Insert Screenshot

```
images/report.png
```

---

# ⚠️ Challenges Faced

During development, several challenges were encountered:

- Understanding Streamlit architecture.
- Connecting Google Gemini API.
- Designing an AI Router.
- Handling dynamic business questions.
- Creating reusable business analysis functions.
- Building modular project architecture.
- Managing API errors and version updates.
- Designing interactive Plotly visualizations.

Each challenge was addressed through iterative development and testing.

---

# 🔮 Future Scope

Future enhancements planned for the project include:

- Upload custom CSV and Excel files.
- Voice-based business questions.
- PDF report generation.
- Advanced Power BI integration.
- Authentication and user login.
- SQL database support.
- Multi-dataset analysis.
- Real-time dashboard updates.
- Forecasting using Machine Learning.
- Sales prediction models.
- Customer churn prediction.
- Inventory optimization.
- Chat history storage.
- Dark mode interface.
- Deployment on Streamlit Community Cloud.
- Docker containerization.

---

# 🎯 Learning Outcomes

This project helped strengthen practical skills in:

- Python Programming
- Data Cleaning
- Exploratory Data Analysis
- Data Visualization
- Business Intelligence
- Power BI
- Streamlit
- Plotly
- Google Gemini API
- Prompt Engineering
- AI Integration
- Git
- GitHub
- Software Architecture
- Modular Programming

This project demonstrates an end-to-end Data Analytics workflow from raw data to AI-powered business insights.

# 📄 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project for educational and personal purposes.

---

# 👩‍💻 Author

## Kanishka Jagdish Mali

Software Engineer | Data Analyst | Python Developer

Fresh Graduate passionate about building AI-powered Data Analytics applications using Python, Business Intelligence, and Generative AI.

---

# 🛠 Skills

- Python
- SQL
- Pandas
- NumPy
- Plotly
- Streamlit
- Power BI
- Google Gemini AI
- Data Analytics
- Machine Learning (Learning)
- Git
- GitHub

---

# 📬 Contact

LinkedIn

```
https://www.linkedin.com/in/kanishka-mali/
```



Email

```
kanishkamali874@gmail.com
```

---



# ⭐ If You Like This Project

If you found this project useful,

⭐ Star this repository

🍴 Fork it

📢 Share it

Your support is greatly appreciated!

---

# 📌 Repository Statistics

Project Type

```
End-to-End AI Data Analytics Project
```

Domain

```
Retail Sales Analytics
```

Dataset

```
Sample Superstore
```

Technologies

```
Python
Pandas
Plotly
Power BI
Streamlit
Google Gemini AI
Git
GitHub
```

Architecture

```
Modular
```

Programming Language

```
Python
```

License

```
MIT
```

---

# 🚀 Thank You for Visiting!

Thank you for exploring this project.

Feedback, suggestions, and contributions are always welcome.
