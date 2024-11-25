# **Export Policy, RODTEP & Duty Drawback Dashboard with AI-Powered Q&A**

Welcome to the **Export Policy, RODTEP, and Duty Drawback Dashboard**, a powerful web app built with **Streamlit** that allows you to interact with and explore the latest data on export policies, remission rates, and duty drawbacks for various products. The app also includes an AI-powered Q&A system that uses **Retrieval-Augmented Generation (RAG)** to answer user queries based on real-time data!

---

## 🚀 **Features**:

### 1. **Interactive Product Visualizations**
   - **Product Distribution by Scheme**: A bar chart showing the number of products per scheme (e.g., RODTEP, Duty Drawback, etc.).
   - **Start Date Trends**: A line chart tracking the number of products launched over time.

### 2. **Product Code Search**
   - **Search Products by Code**: Quickly find detailed product information using the product code.

### 3. **Detailed RODTEP & Duty Drawback Info**
   - **Product Details**: Get information on remission rates, export policy, and duty drawback options for selected products.
   - **Dropdown Menu**: Choose from a list of products and view their related export policy, RODTEP, and Duty Drawback details.

### 4. **AI-Powered Q&A**
   - **Ask Questions**: Powered by **OpenAI** or **Amazon Bedrock**, ask specific questions about RODTEP, Duty Drawback, or export policy, and get intelligent responses based on the latest product data.
   - **RAG-based Retrieval**: The system retrieves relevant product data before querying the LLM, ensuring accurate and context-driven answers.

---

## 🌍 **How to Use**:

### **1. Visualize Product Data**:
   - On the **Visualization** tab, view product trends and distributions, including the number of products per scheme and launch trends.

### **2. Search Products by Code**:
   - Use the **Search by Product Code** tab to enter a product code and retrieve detailed information on the product's export policy, remission rate, and duty drawback.

### **3. Explore RODTEP and Duty Drawback Info**:
   - In the **RODTEP and Duty Drawback Info** tab, select a product from the dropdown menu and explore detailed information regarding remission rates, export policies, and more.

### **4. Ask Your Questions**:
   - The **Ask a Question** tab allows you to type in any query regarding the dataset, such as "What is the remission rate for Garments?" or "What is the export policy for Auto Parts?" The app uses **AI-powered responses** to answer your questions based on the data.

---

## 🔧 **Tech Stack**:

- **Frontend**: Streamlit
- **Backend**: Python, Pandas
- **AI Integration**: OpenAI API (for LLM-based Q&A), Amazon Bedrock (optional)
- **Data**: Custom export product dataset with RODTEP, Duty Drawback, and Export Policy information
- **Visualization**: Streamlit charts for visual insights

---

## 🏗 **How to Run Locally**:

1. **Clone the Repository**:
   ```bash
   git clone https:[https://github.com/Ashwini-developer/Amazon_sambhav]
   cd export-policy-dashboard
   ```

2. **Install the Required Libraries**:
   Make sure to have Python 3.7+ installed, then install the necessary libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI or AWS Bedrock API**:
   - For **OpenAI API**: Set your `OPENAI_API_KEY`.
   - For **Amazon Bedrock**: Configure AWS credentials using **boto3**.

4. **Run the App**:
   Start the app with the following command:
   ```bash
   streamlit run app.py
   ```

5. **Access the Dashboard**:
   Open your browser and visit `http://localhost:8501` to explore the interactive dashboard.

---

## 📊 **Example Use Cases**:

- **Export Managers**: Stay up-to-date on the latest export policies, remission rates, and duty drawbacks for products.
- **Data Analysts**: Easily analyze and visualize product trends and the impact of export schemes over time.
- **Business Owners**: Get quick insights into export policies and schemes for optimizing your export operations.
- **AI Enthusiasts**: See how AI (through RAG-based LLM) can help retrieve and answer real-time data queries in a business context.

---

## 🤝 **Contributing**:

We welcome contributions to improve this dashboard. Whether it's a bug fix, a feature request, or an improvement to the AI model, feel free to create a pull request or open an issue. Here’s how you can contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Push to your fork and create a pull request

---

## 💡 **Future Enhancements**:

- **Export Data API**: Integrate with external sources like the Indian Trade Portal for real-time data updates.
- **Multi-Language Support**: Extend AI-powered Q&A to support multiple languages for global users.
- **Advanced Data Analytics**: Implement more sophisticated data analysis features like regression models and predictive analytics for export policy impacts.

---

## ⚖️ **Disclaimer**:

This app uses sample data and models to provide insights and answers. While we strive to keep the data accurate, always consult official sources like the Indian Trade Portal or government announcements for up-to-date and authoritative information.

---

