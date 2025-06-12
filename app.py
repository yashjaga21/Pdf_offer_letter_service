from flask import Flask, request, send_file, make_response
from io import BytesIO
from reportlab.pdfgen import canvas
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/generate-offer', methods=['POST'])
def generate_offer():
    try:
        # Get form data
        name = request.form.get('name', 'Candidate')
        position = request.form.get('position', 'Intern')
        company = request.form.get('company', 'Your Company')
        date = request.form.get('date', '2025-06-12')

        # Generate PDF in memory
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        p.setFont("Helvetica", 12)
        p.drawString(100, 750, f"Offer Letter")
        p.drawString(100, 730, f"Dear {name},")
        p.drawString(100, 710, f"We are pleased to offer you the position of {position} at {company}.")
        p.drawString(100, 690, f"Start Date: {date}")
        p.drawString(100, 670, "Please contact us if you have any questions.")
        p.drawString(100, 650, "Sincerely,")
        p.drawString(100, 630, f"{company} HR Team")
        p.showPage()
        p.save()
        buffer.seek(0)

        logging.info("Generated offer letter for: %s", name)

        # Return PDF directly without saving
        response = make_response(send_file(buffer, as_attachment=True, download_name=f"{name}_offer_letter.pdf"))
        response.headers["Content-Type"] = "application/pdf"
        return response

    except Exception as e:
        logging.error("PDF generation failed: %s", e)
        return {"error": "Internal server error"}, 500

if __name__ == "__main__":
    app.run(debug=True)
