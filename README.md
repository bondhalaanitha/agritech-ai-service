# 🌾 AgriTech – Intelligent Farm-to-Market Decision System

An AI-powered farm-to-market decision platform designed to help small farmers make better post-harvest selling decisions by considering more than just the current market price.

## 📌 Problem Statement

Small farmers often face difficult decisions after harvesting their crops.

Choosing a buyer only because they offer the highest price may not result in the highest actual profit. Farmers also need to consider:

- Current and expected market prices
- Market demand
- Quantity of produce
- Produce quality
- Shelf life
- Transportation cost
- Travel time
- Buyer capacity
- Competing supply
- Spoilage risk
- Available transportation

AgriTech combines these factors to provide an intelligent selling recommendation.

---

## 💡 Our Solution

AgriTech analyzes farmer and market information and generates a data-driven selling decision.

Instead of simply answering:

> "Which market gives the highest price?"

the system considers:

> "Which selling option can provide the best practical outcome after considering price, demand, transportation, spoilage, and other market conditions?"

---

## 🚀 Key Features

### 1. 🧠 Intelligent Selling Decision

The system analyzes multiple parameters such as:

- Crop type
- Quantity
- Crop age
- Produce quality
- Current price
- Expected price
- Demand
- Shelf life
- Transportation cost
- Travel time
- Market conditions

It then generates a selling recommendation for the farmer.

---

### 2. 📈 Price Prediction

The AI service uses historical agricultural market data to predict expected crop prices.

This helps farmers understand whether:

- Selling now may be suitable
- Waiting may provide a better opportunity
- A different market may provide a better return

---

### 3. 📊 Demand Prediction

The system predicts market demand using available agricultural and market information.

Demand prediction helps identify markets where the farmer's produce may have better selling opportunities.

---

### 4. 🥬 Spoilage Risk Analysis

Perishable crops can lose value while waiting for a buyer.

AgriTech considers factors such as:

- Crop age
- Shelf life
- Travel time
- Produce quality

to estimate the risk associated with delaying or transporting the produce.

---

### 5. 🚚 Farm Pooling

One of the key features of AgriTech is **Farm Pooling**.

Nearby farmers can connect their produce when they have compatible transportation requirements.

For example:

```text
Farmer A ──┐
           ├──► Shared Transport ──► Market/Buyer
Farmer B ──┘
Instead of arranging separate transportation, farmers can coordinate a shared shipment.

This can help reduce:

Transportation cost
Empty vehicle capacity
Repeated trips
Transportation-related emissions
6. 🤝 Buyer & Market Matching

The system considers buyer requirements and available market conditions while evaluating possible selling options.

Factors can include:

Buyer capacity
Required quantity
Produce quality
Price
Location
Demand
7. 🗣️ Farmer-Friendly Assistance

The platform is designed with farmers who may not be comfortable with English in mind.

Voice-based assistance can help farmers understand the information required on different pages and enter values more easily.

8. 💡 AI Explanation

Instead of displaying only a recommendation, the system provides an explanation of the important factors behind the decision.

For example:

Recommended Action: Sell Now

Reason:
• Current price is favorable
• Demand is high
• Produce has limited remaining shelf life
• Waiting increases spoilage risk
• Available transportation is suitable

This makes the AI decision easier for farmers to understand.

🏗️ System Architecture
                    ┌──────────────────────┐
                    │      Farmer          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   React Frontend     │
                    │     Web Platform     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Node.js / Express  │
                    │       Backend        │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    │                      │
                    ▼                      ▼
          ┌──────────────────┐   ┌──────────────────┐
          │     MongoDB      │   │   Python AI      │
          │     Database     │   │     Service      │
          └──────────────────┘   └────────┬─────────┘
                                         │
                           ┌─────────────┼─────────────┐
                           │             │             │
                           ▼             ▼             ▼
                     Price Model   Demand Model   Decision Engine
                           │             │             │
                           └─────────────┼─────────────┘
                                         ▼
                                AI Recommendation
                                         │
                                         ▼
                                  Farmer Dashboard
🤖 AI Service

The ai-service contains the machine learning and decision-making components.

Current AI Components
app/
├── ai_pipeline.py
├── decision_engine.py
├── demand_prediction.py
├── explanation_engine.py
├── main.py
├── price_prediction.py
├── spoilage_prediction.py
│
├── test_ai_pipeline.py
├── test_decision.py
├── test_demand.py
├── test_price.py
└── test_spoilage.py
Machine Learning Models
models/
├── demand_model.pkl
└── price_model.pkl
Dataset
data/
└── datasets/
    ├── agri_price_1000_records.csv
    └── market_data.csv
🛠️ Technology Stack
Frontend
React.js
JavaScript
HTML
CSS
Backend
Node.js
Express.js
Database
MongoDB
AI / Machine Learning
Python
Scikit-learn
Pandas
NumPy
Pickle
Development Tools
Git
GitHub
VS Code
📂 Project Structure
AgriTech/
│
├── frontend/
│
├── backend/
│
└── ai-service/
    │
    ├── app/
    │   ├── ai_pipeline.py
    │   ├── decision_engine.py
    │   ├── demand_prediction.py
    │   ├── explanation_engine.py
    │   ├── main.py
    │   ├── price_prediction.py
    │   ├── spoilage_prediction.py
    │   └── test_*.py
    │
    ├── data/
    │   └── datasets/
    │
    ├── models/
    │   ├── demand_model.pkl
    │   └── price_model.pkl
    │
    └── notebooks/
⚙️ AI Service Setup
1. Clone the repository
git clone https://github.com/bondhalaanitha/agritech-ai-service.git
cd agritech-ai-service
2. Create a virtual environment

Windows:

python -m venv venv

Activate it:

venv\Scripts\activate
3. Install dependencies

If a requirements.txt file is available:

pip install -r requirements.txt
4. Run the AI service
python app/main.py
🧪 Testing

The project contains separate test files for important AI components.

test_ai_pipeline.py
test_decision.py
test_demand.py
test_price.py
test_spoilage.py

Run tests using:

pytest
🌱 Future Enhancements

Possible future improvements include:

Real-time market price APIs
Weather-based prediction
More crop-specific ML models
Real-time transportation availability
Advanced route optimization
Dynamic farm-pooling recommendations
Multilingual voice interaction
Mobile application
Government market integration
More historical agricultural datasets
Explainable AI dashboards
👥 Team

Developed as a collaborative college project.

Project

AgriTech – From Harvest to Value: Intelligent Farm-to-Market Decisions

Goal

To use AI, machine learning, and full-stack technologies to help small farmers make more informed post-harvest selling and transportation decisions.

📄 License

This project is licensed under the MIT License.

### One important change before you put this README on GitHub

Your current GitHub repository is specifically:

**`agritech-ai-service`**

So I would **not** put claims in this README about frontend/backend features that aren't actually present in this repository unless you clearly label them as part of the larger AgriTech system.

For the **AI-service GitHub repo**, the most professional README would focus mainly on:

**AI Pipeline → Price Prediction → Demand Prediction → Spoilage Analysis → Decision Engine → Explanation Engine → Models → Dataset → API/Setup.**

If you want, I can also give you a **:contentReference[oaicite:0]{index=0}**, which will look much better to a Microsoft recruiter than a very long college-project README.
