# 🍽️ Food Management Dashboard  

A **Streamlit + Supabase powered application** for managing food donations, claims, and provider–receiver interactions. The project provides **CRUD functionality** (Create, Read, Update, Delete) for food providers, receivers, food listings, and claims, along with **SQL-driven insights** to minimize food wastage.  

---

## 📌 Features  
- **CRUD Operations**:  
  - Add, view, update, and delete providers, receivers, food listings, and claims.  
- **SQL Queries for Insights**:  
  - Food providers and receivers by city  
  - Provider type contribution trends  
  - Expiry analysis of food listings  
  - Claims analysis (completed, pending, canceled)  
  - Most active providers and receivers  
- **Interactive Dashboard**:  
  - Built with **Streamlit** for a user-friendly interface  
  - Real-time database interaction with **Supabase**  
- **Data Analysis & Reporting**:  
  - Identify food wastage patterns  
  - Generate city-wise and provider-wise insights  

---

## 🚀 Tech Stack  
- **Frontend/UI**: [Streamlit](https://streamlit.io/)  
- **Backend/Database**: [Supabase (PostgreSQL)](https://supabase.com/)  
- **Programming Language**: Python  
- **Libraries**:  
  - `supabase-py` – Supabase client for Python  
  - `pandas` – Data manipulation  
  - `streamlit` – Dashboard interface  

---

## 🗂️ Project Structure  
```
food_management_dashboard/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Project dependencies
└── .streamlit/
    └── secrets.toml      # Supabase credentials
```

---

## ⚙️ Setup Instructions  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/food-management-dashboard.git
cd food-management-dashboard
```

### 2. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3. Configure Supabase  
Create a file at `.streamlit/secrets.toml` with your Supabase credentials:  
```toml
SUPABASE_URL = "https://your-project-ref.supabase.co"
SUPABASE_ANON_KEY = "your-anon-key"
SUPABASE_SERVICE_ROLE_KEY = "your-service-role-key"
```

### 4. Run the App  
```bash
streamlit run app.py
```

---

## 📊 SQL Queries Implemented  
- Total number of providers, receivers, and food listings  
- Food providers by type (restaurants, grocery stores, etc.)  
- Listings about to expire within 3 days  
- Claims per receiver  
- Most active provider and receiver  
- Unclaimed food listings  
- Claims by provider type  
- Expired but unclaimed food  
- City with most providers/receivers  

---

## 💡 Insights & Recommendations  
- Supermarkets and grocery stores contribute the largest share of food donations.  
- Significant proportion of food expires unclaimed → early alert system needed.  
- High-density listing cities should be prioritized for faster logistics.  
- Equitable distribution recommended to prevent over-claiming by few receivers.  

---

## 📌 Future Enhancements  
- Add **predictive analytics** for supply-demand forecasting.  
- Implement **email/SMS notifications** for food nearing expiry.  
- Expand role-based access (providers, receivers, admins).  
- Deploy the app on **Streamlit Cloud / Heroku / Supabase Edge Functions**.  

---

## 🏆 Conclusion  
The Food Management Dashboard demonstrates how **data-driven solutions** can reduce food waste, improve food distribution efficiency, and support sustainability. With real-time CRUD operations and analytical insights, the system connects providers and receivers seamlessly, ensuring surplus food reaches those in need.  
