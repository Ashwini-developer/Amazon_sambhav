import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset for 20 products with RODTEP remission rates
data = [
    {"Product Code": 6203, "Product Name": "Garments", "Scheme Name": "RODTEP", "Duty Drawback Info": "Refund on duties paid", "RODTEP Info": "5% rebate on export value", "Remission Rate": 5, "Export Policy Info": "Must comply with quality standards", "Start Date": "01-Jan-2024", "End Date": "Ongoing", "Conditions": "Must comply with export norms"},
    {"Product Code": 8703, "Product Name": "Auto Parts", "Scheme Name": "Duty Drawback", "Duty Drawback Info": "Refund on customs duty", "RODTEP Info": "N/A", "Remission Rate": None, "Export Policy Info": "Must register with DGFT", "Start Date": "01-Apr-2023", "End Date": "31-Mar-2024", "Conditions": "Register with Exporter Board"},
    {"Product Code": 1006, "Product Name": "Wheat", "Scheme Name": "Export Policy", "Duty Drawback Info": "N/A", "RODTEP Info": "N/A", "Remission Rate": None, "Export Policy Info": "No duties on export", "Start Date": "01-Jan-2023", "End Date": "31-Dec-2023", "Conditions": "Subject to government approval"},
    {"Product Code": 7113, "Product Name": "Gold Jewelry", "Scheme Name": "RODTEP", "Duty Drawback Info": "Tax remission on export", "RODTEP Info": "2% tax remission on export value", "Remission Rate": 2, "Export Policy Info": "BIS compliance required", "Start Date": "01-Feb-2024", "End Date": "Ongoing", "Conditions": "BIS certification mandatory"},
    {"Product Code": 5502, "Product Name": "Rice", "Scheme Name": "Duty Drawback", "Duty Drawback Info": "Refund on customs duties", "RODTEP Info": "N/A", "Remission Rate": None, "Export Policy Info": "Eligible for export", "Start Date": "01-Mar-2023", "End Date": "31-Mar-2024", "Conditions": "Subject to quality testing"},
    {"Product Code": 6403, "Product Name": "Footwear", "Scheme Name": "RODTEP", "Duty Drawback Info": "Refund of tax duties", "RODTEP Info": "4% rebate on export value", "Remission Rate": 4, "Export Policy Info": "Must comply with export norms", "Start Date": "01-Apr-2023", "End Date": "31-Dec-2023", "Conditions": "Comply with international standards"},
    {"Product Code": 3004, "Product Name": "Pharmaceuticals", "Scheme Name": "Duty Drawback", "Duty Drawback Info": "Refund on custom duties", "RODTEP Info": "N/A", "Remission Rate": None, "Export Policy Info": "Subject to FDA approval", "Start Date": "01-Jul-2023", "End Date": "30-Jun-2024", "Conditions": "FDA clearance required"},
    {"Product Code": 8401, "Product Name": "Engines", "Scheme Name": "Export Policy", "Duty Drawback Info": "N/A", "RODTEP Info": "N/A", "Remission Rate": None, "Export Policy Info": "Eligible for export", "Start Date": "01-Jan-2023", "End Date": "31-Dec-2023", "Conditions": "Comply with safety norms"},
    {"Product Code": 8708, "Product Name": "Motorcycles", "Scheme Name": "RODTEP", "Duty Drawback Info": "Refund on duties paid", "RODTEP Info": "3% rebate on export value", "Remission Rate": 3, "Export Policy Info": "Comply with quality standards", "Start Date": "01-Jan-2024", "End Date": "Ongoing", "Conditions": "Subject to registration with Export Board"},
    {"Product Code": 8302, "Product Name": "Locks", "Scheme Name": "Duty Drawback", "Duty Drawback Info": "Refund on duties paid", "RODTEP Info": "N/A", "Remission Rate": None, "Export Policy Info": "Eligible for export", "Start Date": "01-Apr-2023", "End Date": "31-Mar-2024", "Conditions": "Comply with standards"},
    {"Product Code": 7306, "Product Name": "Steel Pipes", "Scheme Name": "RODTEP", "Duty Drawback Info": "Refund of customs duties", "RODTEP Info": "5% rebate on export value", "Remission Rate": 5, "Export Policy Info": "Must comply with manufacturing norms", "Start Date": "01-Jan-2023", "End Date": "Ongoing", "Conditions": "Comply with quality testing"},
    {"Product Code": 1102, "Product Name": "Sugar", "Scheme Name": "Duty Drawback", "Duty Drawback Info": "Refund of customs duties", "RODTEP Info": "N/A", "Remission Rate": None, "Export Policy Info": "Eligible for export", "Start Date": "01-Mar-2023", "End Date": "31-Mar-2024", "Conditions": "Subject to government approval"},
    {"Product Code": 4707, "Product Name": "Wood Pulp", "Scheme Name": "RODTEP", "Duty Drawback Info": "Refund on export duties", "RODTEP Info": "3% rebate on export value", "Remission Rate": 3, "Export Policy Info": "Comply with environmental standards", "Start Date": "01-Apr-2023", "End Date": "Ongoing", "Conditions": "Environmental compliance mandatory"},
    {"Product Code": 2515, "Product Name": "Marble", "Scheme Name": "Duty Drawback", "Duty Drawback Info": "Refund of duties paid", "RODTEP Info": "N/A", "Remission Rate": None, "Export Policy Info": "Eligible for export", "Start Date": "01-Jan-2023", "End Date": "31-Dec-2023", "Conditions": "Comply with export standards"},
    {"Product Code": 6802, "Product Name": "Stones", "Scheme Name": "RODTEP", "Duty Drawback Info": "Tax remission on export duties", "RODTEP Info": "2% tax rebate on export value", "Remission Rate": 2, "Export Policy Info": "Eligible for export", "Start Date": "01-May-2023", "End Date": "Ongoing", "Conditions": "Compliance with quality standards"},
    {"Product Code": 1001, "Product Name": "Barley", "Scheme Name": "Export Policy", "Duty Drawback Info": "N/A", "RODTEP Info": "N/A", "Remission Rate": None, "Export Policy Info": "No duties on export", "Start Date": "01-Jan-2023", "End Date": "31-Dec-2023", "Conditions": "Subject to government approval"},
    {"Product Code": 7311, "Product Name": "Cables", "Scheme Name": "RODTEP", "Duty Drawback Info": "Refund of custom duties", "RODTEP Info": "4% rebate on export value", "Remission Rate": 4, "Export Policy Info": "Comply with international norms", "Start Date": "01-Jul-2023", "End Date": "Ongoing", "Conditions": "Compliance with export standards"},
    {"Product Code": 7117, "Product Name": "Silver Jewelry", "Scheme Name": "Duty Drawback", "Duty Drawback Info": "Refund on duties paid", "RODTEP Info": "N/A", "Remission Rate": None, "Export Policy Info": "Comply with BIS certification", "Start Date": "01-Feb-2024", "End Date": "Ongoing", "Conditions": "BIS certification required"},
    {"Product Code": 8402, "Product Name": "Machinery Parts", "Scheme Name": "RODTEP", "Duty Drawback Info": "Refund on duties paid", "RODTEP Info": "3% rebate on export value", "Remission Rate": 3, "Export Policy Info": "Comply with export regulations", "Start Date": "01-Mar-2023", "End Date": "Ongoing", "Conditions": "Comply with export regulations"}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Streamlit UI
st.title("Export Policy, RODTEP, and Duty Drawback Information")

# Sidebar for tabs
tabs = st.sidebar.radio("Choose a Tab", ['Visualization', 'Search by Product Code', 'RODTEP and Duty Drawback Info'])

# Visualization Tab
if tabs == 'Visualization':
    st.subheader("Product Distribution Visualization")
    
    # Bar chart of Product Codes by Scheme Name
    st.subheader("Number of Products per Scheme")
    scheme_counts = df['Scheme Name'].value_counts()
    st.bar_chart(scheme_counts)
    
    # Line chart of Number of Products per Start Date
    st.subheader("Number of Products per Start Date")
    df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
    start_date_counts = df['Start Date'].dt.to_period('M').value_counts().sort_index()
    st.line_chart(start_date_counts)

# Search by Product Code Tab
elif tabs == 'Search by Product Code':
    st.subheader("Search for Product Information by Product Code")
    
    # Product Code search box
    product_code_search = st.text_input("Enter Product Code to search:")
    
    # Filter the DataFrame based on inputted Product Code
    if product_code_search:
        filtered_product = df[df["Product Code"].astype(str) == product_code_search]
        if not filtered_product.empty:
            st.write(filtered_product)
        else:
            st.write("No product found for the entered product code.")

# RODTEP and Duty Drawback Info Tab
elif tabs == 'RODTEP and Duty Drawback Info':
    st.subheader("RODTEP and Duty Drawback Information")
    
    # Dropdown to select product from the dataset
    product_dropdown = st.selectbox("Select a Product", df['Product Name'].unique())
    
    # Filter the DataFrame based on selected product
    selected_product = df[df['Product Name'] == product_dropdown]
    
    # Display the selected product details in an expanded format
    st.dataframe(selected_product[['Product Code', 'Product Name', 'Scheme Name', 'Duty Drawback Info', 'RODTEP Info', 'Remission Rate', 'Export Policy Info', 'Start Date', 'End Date', 'Conditions']])

