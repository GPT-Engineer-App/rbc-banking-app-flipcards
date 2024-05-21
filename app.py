from flask import Flask, render_template, url_for, redirect, request
import qrcode
import os

app = Flask(__name__)

# Dummy data
accounts = {
    "chequing": {
        "account_number": "123456789",
        "balance": "$5,000.00",
        "transactions": [
            {"date": "2023-10-01", "description": "Payroll Deposit", "amount": "$2,000.00"},
            {"date": "2023-09-28", "description": "Grocery Store", "amount": "$150.00"},
            {"date": "2023-09-25", "description": "Utility Bill", "amount": "$100.00"},
            # Add more transactions here
        ]
    },
    "credit": {
        "balance": "$1,200.00",
        "due_date": "2023-10-15",
        "offers": [
            {"title": "Travel Offer", "description": "Get 20% off on flights", "points": 2000},
            {"title": "Dining Offer", "description": "Get 10% off at select restaurants", "points": 1000},
            # Add more offers here
        ]
    }
}

@app.route('/')
def account_summary():
    return render_template('account_summary.html', accounts=accounts)

@app.route('/transaction_details')
def transaction_details():
    return render_template('transaction_details.html', transactions=accounts["chequing"]["transactions"])

@app.route('/offers_detail')
def offers_detail():
    return render_template('offers_detail.html', offers=accounts["credit"]["offers"])

@app.route('/generate_qr/<offer_title>')
def generate_qr(offer_title):
    offer = next((offer for offer in accounts["credit"]["offers"] if offer["title"] == offer_title), None)
    if offer:
        qr_data = f"Offer: {offer['title']}\nDescription: {offer['description']}\nPoints: {offer['points']}"
        qr_img = qrcode.make(qr_data)
        qr_path = os.path.join('qr_codes', f"{offer_title}.png")
        qr_img.save(qr_path)
        return render_template('qr_code.html', qr_path=qr_path)
    return redirect(url_for('offers_detail'))

if __name__ == '__main__':
    if not os.path.exists('qr_codes'):
        os.makedirs('qr_codes')
    app.run(debug=True)