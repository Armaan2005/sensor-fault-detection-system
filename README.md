# 🚀 Wafer Fault Detection System  
### End-to-End Machine Learning System with AI Explainability, Monitoring & CI/CD Deployment

---

## 📌 Project Overview

This project is a production-grade Machine Learning system designed to detect faulty semiconductor wafers using sensor data.  
It goes beyond model training and covers the complete ML lifecycle, including:

- Data ingestion from MongoDB
- Feature transformation
- Model training & evaluation
- Batch prediction
- Real-time monitoring dashboard
- AI-powered explanation using Groq LLM
- Dockerized deployment with CI/CD on AWS EC2

👉 This project simulates real-world industrial ML systems used in manufacturing quality control.

---

## 🧠 Problem Statement

In semiconductor manufacturing, faulty wafers lead to:
- Production loss
- Increased operational cost
- Quality degradation

The goal is to:
> Automatically classify wafers as Good or Bad using sensor readings  
> and provide explainable insights for engineers.

---

## 🏗️ System Architecture (High Level)

📌 End-to-End Flow
## 🏗️ System Architecture

### Data Ingestion
![Data Ingestion Architecture](<images/Data Ingestion.png>)

### Data Transformation
![Data Transformation Architecture](<images/Data Transformation.png>)

### Model Training
![Model Training Architecture](<images/Model Trainer.png>)

### Prediction Pipeline
![Data Transformation Architecture](<images/Prediction Pipeline.png>)

├── src
│   ├── components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │
│   ├── pipeline
│   │   ├── train_pipeline.py
│   │   ├── predict_pipeline.py
│   │
│   ├── monitoring
│   │   └── metrics_utils.py
│   │
│   ├── ai
│   │   └── groq_assistant.py
│   │
│   ├── utils
│   │   └── main_utils.py
│   │
│   ├── exception.py
│   ├── logger.py
│
├── artifacts
│   ├── model.pkl
│   ├── preprocessor.pkl
│   └── metrics
│       └── prediction_metrics.json
│
├── templates
│   ├── home.html
│   ├── upload_file.html
│   ├── dashboard.html
│
├── static
│   ├── css
│   └── js
│
├── Dockerfile
├── requirements.txt
├── app.py
├── README.md



⚙️ ML Pipeline Explanation
1️⃣ Data Ingestion
Data fetched from MongoDB Atlas
Raw sensor data exported as CSV
Stored inside artifacts/
2️⃣ Data Transformation
Missing value handling
Scaling using RobustScaler
Train-test split
Preprocessor saved as .pkl
3️⃣ Model Training
Multiple models evaluated:
XGBoost
Random Forest
Gradient Boosting
SVM
Best model selected using validation accuracy
Hyperparameter tuning using GridSearchCV
4️⃣ Prediction Pipeline
Batch CSV upload
Preprocessor + model loaded
Predictions generated
Output CSV downloaded
Metrics updated for dashboard
📊 Monitoring Dashboard
The dashboard provides real-time ML monitoring, including:
Total predictions
Good vs Bad wafer count
Health score (% Good wafers)
Risk indicator bar
Trend analysis charts
Model name visibility
📌 Metrics are batch-wise (non-cumulative) for consistency.
🤖 AI Explainability (Groq LLM)
An AI assistant is integrated to explain prediction results.
LLM Provider: Groq
Model Used: llama-3.1-70b-versatile
Explains:
Why wafers are classified as bad
Overall quality insights
Engineering-friendly explanations
📌 AI runs independently of ML predictions (no hallucination).
☁️ Deployment & CI/CD
🐳 Docker
Complete application containerized
Same behavior across environments
🔁 CI/CD Pipeline (GitHub Actions)
Triggered on every push
Steps:
Build Docker image
Push to AWS ECR
Deploy to AWS EC2 using self-hosted runner
☁️ AWS
EC2 (Ubuntu) as production server
ECR for Docker image registry
App exposed via public IP
▶️ How to Run Locally
Copy code
Bash
# Clone repository
git clone <repo-url>
cd wafer-fault-detection

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py
🧪 How to Use
Open home page
Click Train Model
Upload CSV file for prediction
Download prediction results
Open Dashboard
Ask AI for explanation
🧠 Key Engineering Learnings
Built a full ML system, not just a model
Solved real-world bugs (metrics inflation, AI config issues)
Designed modular, scalable architecture
Integrated AI explainability
Implemented CI/CD & cloud deployment

🙌 Author
Armaan Joshi
Aspiring Data Scientist | Machine Learning | Computer Vision | MLOps
📌 This project demonstrates industry-level ML engineering practices.

