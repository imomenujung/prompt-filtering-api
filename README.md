# Prompt Filter API

This project implements a FastAPI-based API that filters input prompts using a combination of keyword matching and embeddings-based similarity. It checks if a prompt contains sensitive keywords or exceeds a threshold similarity with the provided keywords.

## Requirements

Before running this application, make sure you have the following dependencies installed:

- Python 3.6+
- FastAPI
- Sentence-Transformers
- PyTorch
- Uvicorn (for running the FastAPI app)

You can install the required dependencies by running:

```bash
pip install fastapi sentence-transformers torch uvicorn
```

## Setup

1. **Download the necessary model**:
   The app uses the `all-MiniLM-L6-v2` model from the `sentence-transformers` library to compute embeddings. The model will automatically be downloaded when you run the app for the first time.

2. **Create `filter_keywords.json` file**:
   This file contains a list of sensitive keywords that the app will check against. Here is an example of the JSON format:

   ```json
   {
     "keywords": [
       "sensitive term 1",
       "sensitive term 2",
       "confidential phrase"
     ]
   }
   ```

   The app will load these keywords to check if they exist in the input prompt.

## Running the Application

To run the FastAPI app locally, execute the following command in the project directory:

```bash
uvicorn your_script_name:app --host 0.0.0.0 --port 8000
```

This will start a local server at `http://127.0.0.1:8000`.

For production use, the app is deployed on Render and can be accessed via the following URL:

[https://prompt-filtering-api.onrender.com](https://prompt-filtering-api.onrender.com)

## API Endpoint

The app exposes the following API endpoint:

### POST `/check_prompt`

This endpoint checks if a given prompt is safe. It performs two checks:
1. **Embedding similarity check**: Compares the prompt embedding with the embeddings of the keywords.
2. **Keyword matching check**: Checks if any of the sensitive keywords appear in the prompt text.

#### Request Body

```json
{
  "prompt": "Your input prompt here"
}
```

- `prompt`: The input text to be evaluated.

#### Response

The response will be a simplified JSON object indicating whether the prompt is safe or not, with just the `safe` key:

```json
{
  "safe": true
}
```

If the prompt contains sensitive keywords or exceeds the similarity threshold, the response will be:

```json
{
  "safe": false
}
```

If the prompt is missing or invalid, you will get an error response:

```json
{
  "error": "Prompt is required"
}
```

In case of other errors:

```json
{
  "error": "Error message here"
}
```
## Customizing the Threshold

The similarity threshold used to compare embeddings is set to `0.5` by default. You can modify it in the function `is_prompt_safe_with_embeddings`:

```python
def is_prompt_safe_with_embeddings(prompt, keywords, threshold=0.5):
```

Change the `threshold` value to a higher or lower number to adjust the sensitivity of the check.

## Testing the API

You can test the API using tools like **Postman** or **cURL**.

### Example with cURL:

```bash
curl -X POST https://prompt-filtering-api.onrender.com/check_prompt \
-H "Content-Type: application/json" \
-d '{"prompt": "example sensitive term"}'
```

### Example with Postman:

1. Set the HTTP method to `POST`.
2. Enter the URL `https://prompt-filtering-api.onrender.com/check_prompt`.
3. In the body section, choose **raw** and **JSON** format.
4. Add your input data:
   ```json
   {
     "prompt": "example sensitive term"
   }
   ```
5. Send the request and check the response.

## Example with Python
```python
import requests

# URL endpoint API yang di-deploy di Render
url = "https://<your-app-name>.onrender.com/check_prompt"

# Data yang akan dikirimkan ke API
data = {"prompt": "Contoh teks yang ingin diperiksa keamanan"}

# Memanggil API dengan metode POST
response = requests.post(url, json=data)

# Menampilkan hasil dari response API
if response.status_code == 200:
    print("Response from API:", response.json())
else:
    print("Failed to call API. Status code:", response.status_code)
```
