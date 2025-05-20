# Flask AI Study Helper (Render Setup)

## 🧾 Requirements
This project requires:
- Flask
- Gunicorn

## 🚀 Deployment on Render
1. Push this project to GitHub.
2. On [https://render.com](https://render.com), create a new Web Service.
3. Use the following settings:
   - Environment: **Python**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Root Directory: `ai_study_helper`

4. Make sure `app.py` contains:

```python
import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

5. Done! Your API will be available at `https://<your-app-name>.onrender.com/api/analyze`
