# 📄 Offer Letter PDF Generator

This Python web app provides an on-the-fly PDF generation service for custom offer letters using Flask and ReportLab.

## 🚀 Features
- PDF generated dynamically based on user input
- No file saved server-side
- Downloadable offer letters directly in the browser

## 📦 Requirements
- Python 3.x
- Required libraries:
  ```bash
  pip install -r requirements.txt
  ```

## ▶️ Run the Server
```bash
python app.py
```

## 🛠️ Example Usage

Make a `POST` request to `/generate-offer` with form data:

- `name`: Candidate name
- `position`: Job title
- `company`: Company name
- `date`: Offer date

## 🧪 Testing with curl
```bash
curl -X POST http://127.0.0.1:5000/generate-offer -F "name=Alice" -F "position=Developer" -F "company=TechCorp" -F "date=2025-06-12" --output offer_letter.pdf
```

---

Happy generating! 📃✨
