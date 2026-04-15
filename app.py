from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyDwBejnvr00w2EBE7P_s0hmZKNeLcQsZ84")
model = genai.GenerativeModel("gemini-1.5-flash")

# Allow GET for opening page
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Separate POST API for Gemini
@app.route("/ai-route", methods=["POST"])
def ai_route():
    data = request.get_json()

    source = data.get("source", "")
    destination = data.get("destination", "")
    distance = data.get("distance", "")
    eta = data.get("eta", "")
    traffic = data.get("traffic", "")

    prompt = f"""
    Give smart travel advice for:
    {source} to {destination}
    Distance: {distance}
    ETA: {eta}
    Traffic: {traffic}

    Include route tip, safety tip, best timing, budget ride.
    Keep short and professional.
    """

    try:
        response = model.generate_content(prompt)
        result = response.text
    except Exception as e:
        result = "AI unavailable"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)