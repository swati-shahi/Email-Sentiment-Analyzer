from flask import Flask, render_template, request
from textblob import TextBlob

# Initialize Flask App
app = Flask(__name__)

# Route for homepage
@app.route("/", methods=["GET", "POST"])
def home():
    sentiment_result = None
    polarity_score = None

    if request.method == "POST":
        # Get the text from the form
        email_text = request.form.get("email_text")

        # Check if text is not empty
        if email_text.strip():
            # Analyze sentiment using TextBlob
            analysis = TextBlob(email_text)
            polarity_score = analysis.sentiment.polarity

            # Determine sentiment category
            if polarity_score > 0:
                sentiment_result = "Positive (Ham/Normal Email)"
            elif polarity_score < 0:
                sentiment_result = "Negative (Spam Email)"
            else:
                sentiment_result = "Neutral"

    # Render the UI with result
    return render_template("index.html",
                           sentiment=sentiment_result,
                           polarity=polarity_score)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
