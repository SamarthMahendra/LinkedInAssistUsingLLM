from flask import Flask, request, jsonify
from LLMIntegration.url_maker import LinkedInURLRecreator
from LLMIntegration.json_creator import JobFilterAssistant

app = Flask(__name__)


@app.route("/get_new_url", methods=["POST"])
def get_new_url():
    data = request.json  # Get JSON data from the request
    url = data.get("url")  # Extract 'url' from JSON data
    prompt = data.get("prompt")  # Extract 'prompt' from JSON data

    if not url or not prompt:
        return jsonify({"error": "Missing 'url' or 'prompt' in request"}), 400

    # Assuming you have defined api_key and base_url somewhere
    api_key = "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"
    new_params = {}  # Define new_params according to your requirements

    assistant = JobFilterAssistant(api_key)
    json_response = assistant.filter_jobs(prompt)
    # convert json from str to dict
    json_response = eval(json_response)
    recreator = LinkedInURLRecreator(url)
    new_url = recreator.recreate_url(json_response)

    return jsonify({"url": new_url})


if __name__ == "__main__":
    app.run()