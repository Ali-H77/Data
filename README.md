# Chatbot 
This project is a Streamlit-based chatbot that answers natural language questions about **Data**, using data from an Excel file and powered by **Groq's LLaMA 3.3-70B Versatile model**.

---

## 📚 Table of Contents
- [📊 Featuers](#🚀Features)
- [📁 Files](#📁Files)
- [🗂️ Data Source ](#-🗂️-Data-Source)
- [🛠️ Requirements](#️🛠️-Requirements)
- [🚀 Setup and Local Installation](#-setup-and-local-installation)
- [📄 License](#-license)

---

## 🚀 Features

- 📈 Loads and analyzes sentiment-labeled Excel data
- 🤖 Uses Groq's LLaMA 3.3 for natural language understanding
- 💬 Supports chat-based question answering
- 🧠 Understands dataset insights (e.g., review counts, sentiment scores)
- 🪄 Simple Streamlit interface

---
## 📁 Files

| File              | Description                                 |
|-------------------|---------------------------------------------|
| `Chatbot.py`      | Main Streamlit chatbot app                  |
| `reviews_with_sentiment.xlsx` | Excel file containing the sentiment data |
| `amazon_product_reviews.xlsx` | Excel file containing the review data |
| `clear data.ipynb`| clear data using python                     |
| `README.md`       | Project documentation                       |

---
## 🗂️ Data Source
<details> <summary>Click to expand</summary>
- product_id: Unique identifier for each product
- product_name: Full name of the product
- category: Product category (can include multiple levels separated by "
- discounted_price: Price after applying the discount
- actual_price: Original price before discount
- discount_percentage: Discount as a percentage
- rating: Average product rating
- rating_count: Total number of ratings received
- about_product: Short product description
- user_id: Unique identifier of the reviewer
- user_name: Name of the reviewer
- review_id: Unique ID of the review
- review_title: Title or summary of the review
- review_content: Full text of the review
- img_link: Link to the product image
- product_link: Link to the product page
</details>
## 🛠️ Requirements

- Python 3.8+
- Groq API key (Free signup at [https://console.groq.com](https://console.groq.com))
- The following Python packages:
  - `streamlit`
  - `pandas`
  - `openpyxl`
  - `groq`

---

## 🚀 Setup and Local Installation
1- Install Anaconda: https://www.anaconda.com/download

2- Install Visual Studio Code

3- Install Extantion of Jupyter note

4- Create Environment 
```
conda create --name Anyname python=3.10

```
5- Activate the Environment 
```
conda activate (The Name you Added before)

```
6- Install all packages required

```
pip install -r requirements.txt
```

7- Run the Streamlit app

```
streamlit run app.py
```

---

## 📄 License

- This project is licensed under the MIT License.

## Author 
Ali H Alhussain
