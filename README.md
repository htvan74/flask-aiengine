# Flask AI Engine

This project includes AI-powered Flask apps for educational use.

## Apps

- `ai_study_helper/`: Main Flask app
- `ai_study_analysis/`: Analysis module (upcoming)

## Run locally

```bash
cd ai_study_helper
pip install -r requirements.txt
python app.py
```

## Deploy

If using Heroku:
- Ensure `Procfile` contains:
  ```
  web: python ai_study_helper/app.py
  ```
