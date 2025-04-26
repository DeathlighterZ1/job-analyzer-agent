import requests

def analyze_cv_text(text):
    # Grammar check
    lt_response = requests.post(
        "https://api.languagetool.org/v2/check",
        data={"text": text, "language": "en-US"}
    )
    errors = lt_response.json()["matches"]

    # Content check
    cohere_api_key = "7EbGyC3eo428U18a1T0h5uaS059NxW5h4t98WCou"
    cohere_url = "https://api.cohere.ai/v1/generate"
    cohere_headers = {
        "Authorization": f"Bearer {cohere_api_key}",
        "Content-Type": "application/json"
    }
    cohere_data = {
        "prompt": f"Analyze this CV text and tell missing important parts like photo, contact, skills:\n\n{text}",
        "model": "command",
        "max_tokens": 300
    }
    cohere_response = requests.post(cohere_url, headers=cohere_headers, json=cohere_data)

    if cohere_response.status_code == 200:
        cohere_feedback = cohere_response.json()["generations"][0]["text"]
    else:
        cohere_feedback = "Could not analyze CV content. Please check API key or limits."

    score = 100 - len(errors)*2
    score = max(score, 0)

    return (f"Grammar Errors: {len(errors)}\n\nSuggestions:\n{cohere_feedback}", score)
