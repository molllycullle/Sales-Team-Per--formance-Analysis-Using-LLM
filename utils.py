
import pandas as pd
import requests

def load_data(file_path):
    """Load sales data from a CSV file and calculate metrics."""
    data = pd.read_csv(file_path)
    data['tours_per_lead'] = data['tours_booked'] / data['lead_taken']
    data['apps_per_tour'] = data['applications'] / data['tours_booked']
    return data

def create_rep_prompt(rep_data):
    """Generate concise prompt for individual sales representative performance."""
    return (f"Evaluate the performance of {rep_data['employee_name']} (Employee ID: {rep_data['employee_id']}): "
            f"Leads: {rep_data['lead_taken']}, Tours: {rep_data['tours_booked']}, "
            f"Applications: {rep_data['applications']}, Confirmed revenue: ${rep_data['revenue_confirmed']}, "
            f"Pending revenue: ${rep_data['revenue_pending']}, Average deal value: ${rep_data['avg_deal_value_30_days']}, "
            f"Close rate: {rep_data['avg_close_rate_30_days']}%. Provide feedback.")

def create_team_prompt(data):
    """Generate concise prompt for team performance analysis."""
    return (f"Analyze team performance: Total leads: {data['lead_taken'].sum()}, "
            f"Tours booked: {data['tours_booked'].sum()}, Confirmed revenue: ${data['revenue_confirmed'].sum()}, "
            f"Pending revenue: ${data['revenue_pending'].sum()}. Provide insights.")

def create_trend_prompt(data):
    """Generate concise prompt for sales trends and forecast."""
    return "Analyze sales trends and provide a forecast based on leads, tours, and revenue."

def call_llm(prompt):
    """Call the Hugging Face API to get analysis based on the prompt."""
    api_key = "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"  # Replace with your Hugging Face API Key
    headers = {"Authorization": f"Bearer {api_key}"}
    model_id = "tiiuae/falcon-7b-instruct"  # Using Falcon-7B model as a free alternative

    response = requests.post(
        f"https://api-inference.huggingface.co/models/{model_id}",
        headers=headers,
        json={"inputs": prompt}
    )

    # Check and log the status code and content
    if response.status_code == 200:
        return response.json()[0].get("generated_text", "No response text available.")
    else:
        print(f"Error: {response.status_code}, Response: {response.text}")
        return f"Error in response: {response.status_code}"

# Example Usage:
# data = load_data("sales_data.csv")
# prompt = create_rep_prompt(data.iloc[0])
# result = call_llm(prompt)
# print(result)
