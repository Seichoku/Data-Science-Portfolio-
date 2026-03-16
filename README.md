# Emeka Ichoku — Data Science & Analytics Portfolio

**Senior Data Analyst | Analytics Engineer | Data Scientist**  
Calgary, AB, Canada · [LinkedIn](https://www.linkedin.com/in/emeka-ichoku-11685277/) · [Email](mailto:ichokues@gmail.com)

---

## About Me

I'm a Senior Data Analyst and Analytics Engineer with 5+ years of experience building trusted, scalable analytics solutions across retail, supply chain, fintech, SaaS, and public sector environments. I specialise in translating complex business problems into production-ready data solutions — from dbt transformation pipelines and machine learning models through to executive dashboards and A/B testing frameworks.

My technical toolkit centres on **SQL**, **Python**, and **Power BI / Looker**, with hands-on experience across **dbt**, **Snowflake**, **GCP**, **AWS**, and **Git-based workflows**. I'm equally comfortable as a hands-on data engineer and a strategic stakeholder advisor.

**MSc, Applied Data Science & Artificial Intelligence** — University of Southampton, UK  
**BSc, Physics** — Ogun State University, Nigeria

---

## Featured Projects

---

### 🛒 [E-Commerce Sales Analytics Pipeline](https://github.com/Seichoku/ecommerce-analytics-pipeline)
> **SQL · dbt · Python · Looker-ready · Snowflake-compatible**

End-to-end analytics engineering pipeline built on a synthetic e-commerce dataset of 20,000 orders, 5,000 customers, and 38,000+ line items across 3 years.

**What's inside:**
- **dbt staging models** — typed, cleaned, business-rule-applied views for orders, customers, and line items
- **dbt mart models** — production fact and dimension tables including `fct_orders`, `dim_customers` with RFM scoring and LTV, `mart_monthly_sales` with MoM growth and YTD revenue, and `mart_product_performance` with category ranking
- **Python analysis pipeline** — EDA, monthly revenue trend + 3-month linear forecast, cohort retention heatmap, RFM segmentation, and product/category performance
- **4 publication-quality dashboards** covering sales performance, customer cohorts, RFM segments, and category analytics

**Key metrics uncovered:** $23.1M revenue · 51.4% gross margin · 91.2% repeat customer rate · Champions segment averaging $7,524 revenue per customer

**Skills demonstrated:** Analytics engineering · dbt modeling · SQL window functions · Python (pandas, matplotlib) · Cohort analysis · RFM segmentation · Forecasting

---

### 📊 [Product Funnel & Retention Analysis](https://github.com/Seichoku/product-funnel-retention)
> **Python · SQL · scipy · A/B Testing · SaaS Product Analytics**

Comprehensive SaaS product analytics project simulating a B2B platform with 8,000 users, 93K events, 102K sessions, and a controlled experiment — covering the full user lifecycle from acquisition through churn.

**What's inside:**
- **Acquisition funnel analysis** — 8-step funnel from Sign Up → Subscription Upgraded with step-over-step drop-off rates and channel segmentation
- **Cohort retention heatmap** — Monthly retention matrix across 12 cohorts and 12 months, segmented by plan type
- **A/B test — Onboarding Flow V2** — Statistically rigorous experiment analysis using two-proportion z-test with confidence intervals
- **Churn analysis** — Rate by plan and channel, time-to-churn distributions, and a 4-quadrant engagement vs tenure risk matrix
- **MRR analysis** — Monthly recurring revenue trend with MoM growth and plan-level breakdown
- **3 production SQL models** — Funnel progression, cohort retention matrix, and A/B significance model with z-score and CI built directly in SQL

**A/B Test Result:**

| Metric | Control | Variant | Lift | Significant? |
|---|---|---|---|---|
| Activation Rate | 48.2% | 60.4% | +25.2% | ✓ Yes (p<0.0001) |
| 7-Day Retention | 58.3% | 71.4% | +22.5% | ✓ Yes (p<0.0001) |
| Time to Activate | 4.8 days | 3.1 days | −1.7d | ✓ Yes (p<0.001) |

**Skills demonstrated:** Funnel analysis · Cohort retention · A/B testing · Statistical significance · Churn modelling · MRR analysis · Product-led growth metrics

---

### 🤖 [Emaj ChatBot](https://github.com/Seichoku/Data-Science-Portfolio-)
> **Python · PyTorch · NLP · Neural Networks**

An intent-classification chatbot built from scratch using a feedforward neural network trained on custom intent data. Demonstrates NLP preprocessing (tokenisation, stemming, bag-of-words) and PyTorch model training.

**What's inside:**
- Custom NLP pipeline — tokenisation, stemming, and bag-of-words vectorisation using NLTK
- PyTorch feedforward neural network for intent classification
- Training pipeline with loss tracking and model persistence (`data.pth`)
- GUI interface for interactive conversation

**Skills demonstrated:** NLP · PyTorch · Neural network architecture · Model training & serialisation · Python OOP

---

## Skills & Technologies

| Category | Tools |
|---|---|
| **Languages** | Python (pandas, numpy, scikit-learn, matplotlib, PyTorch) · SQL (advanced) |
| **Analytics Engineering** | dbt · Snowflake · Google PLX · BigQuery |
| **BI & Visualisation** | Power BI (DAX, RLS, semantic models) · Looker · Tableau · Google Sheets |
| **Cloud Platforms** | GCP · AWS (Redshift, Lambda) · Azure |
| **Data Pipelines** | Airflow · AWS Glue · Step Functions · AppScript |
| **Machine Learning** | scikit-learn · PyTorch · regression · classification · clustering · NLP |
| **Statistical Methods** | A/B testing · hypothesis testing · regression analysis · causal inference |
| **Workflow** | Git · dbt · Docker (familiar) · Jupyter · VS Code |

---

## Work Experience Highlights

**Senior Data Analyst** — Astreya *(Remote, Canada · 2025)*  
Built dbt pipelines and Looker dashboards for Supply Chain and Finance teams on GCP. Saved 20+ hours/month through automated reporting.

**Data & Insight Analyst** — DHL *(United Kingdom · 2023–2024)*  
Delivered enterprise Power BI solutions for fleet, sales, and operations. Built AWS-based data pipelines and implemented RLS governance frameworks.

**Analytics Engineer** — Byte Cognition *(Remote · 2022–2023)*  
Built ML pipelines and Snowflake-compatible data models for B2B SaaS clients. Designed A/B testing and experimentation frameworks.

**BI Manager / Data Analyst** — Bank *(Lagos, Nigeria · 2018–2022)*  
Led BI delivery for revenue, risk, and operations. Built financial forecasting models and KPI dashboards for executive decision-making.

---

## Currently Building

- 🔄 **Customer Churn Prediction** — scikit-learn ML pipeline with feature engineering, SHAP explainability, and Snowflake-ready scoring output
- 🔄 **Supply Chain Performance Analytics** — SQL + Python pipeline with demand forecasting and anomaly detection

---

## Get in Touch

I'm always open to interesting data problems, collaboration, and new opportunities.

📧 [ichokues@gmail.com](mailto:ichokues@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/emeka-ichoku-11685277/)  
📍 Calgary, AB, Canada
