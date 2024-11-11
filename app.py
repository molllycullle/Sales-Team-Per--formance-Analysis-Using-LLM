from flask import Flask, jsonify, request
from utils import load_data, create_rep_prompt, create_team_prompt, create_trend_prompt, call_llm

app = Flask(__name__)

# Load the data once when the application starts
data = load_data("C:\\Users\\Sarmad\\Desktop\\llmCSV\\data.csv")  # Ensure your CSV file is in the "data" directory

@app.route("/api/rep_performance", methods=["GET"])
def rep_performance():
    rep_id = int(request.args.get("rep_id"))
    rep_data = data[data["employee_id"] == rep_id].iloc[0].to_dict()
    prompt = create_rep_prompt(rep_data)
    feedback = call_llm(prompt)
    return jsonify({"performance_feedback": feedback})

@app.route("/api/team_performance", methods=["GET"])
def team_performance():
    prompt = create_team_prompt(data)
    feedback = call_llm(prompt)
    return jsonify({"team_performance_summary": feedback})

@app.route("/api/performance_trends", methods=["GET"])
def performance_trends():
    prompt = create_trend_prompt(data)
    feedback = call_llm(prompt)
    return jsonify({"sales_trends_forecast": feedback})

if __name__ == "__main__":
    app.run(debug=True)
