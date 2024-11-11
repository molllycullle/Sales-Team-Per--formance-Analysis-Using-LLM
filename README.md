Sales Performance Analysis API
This API application provides an interface to analyze sales performance data of individual representatives and the overall team. It uses a pre-trained language model from Hugging Face's API to generate feedback based on sales data.

Features
Individual Performance Analysis: Get feedback on the performance of a specific sales representative.
Team Performance Analysis: Get a summary and insights on overall team performance.
Sales Trends and Forecast: Analyze sales trends and generate a forecast based on historical data.
Requirements
Python 3.7 or above
Hugging Face API key
Falcon-7B model or another supported model on Hugging Face's API
Setup
Clone the repository:
git clone https://github.com/molllycullle/Sales-Team-Per--formance-Analysis-Using-LLM.git
cd sales-performance-api


Test Individual Sales Representative Performance Open Postman, set the method to GET. Use the URL: http://127.0.0.1:5000/api/rep_performance?rep_id=183. Click Send to get feedback on the specified representative. Test Team Performance Analysis Open Postman, set the method to GET. Use the URL: http://127.0.0.1:5000/api/team_performance. Click Send to get insights on the overall team performance. Test Sales Trends and Forecast Open Postman, set the method to GET. Use the URL: http://127.0.0.1:5000/api/performance_trends. Click Send to get a sales trends forecast based on the provided data. Folder Structure app.py: Main application file. utils.py: Utility functions for loading data, creating prompts, and calling the LLM API. data.csv: Sales data file. Adjust the file path in the code as needed.
