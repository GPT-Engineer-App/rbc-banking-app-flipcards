# rbc-banking-app-flipcards

Develop a web application for RBC (Royal Bank of Canada) using Python, Flask, HTML, CSS, and JS. The goal is to create a user-friendly and visually appealing app based on the provided "RBC Banking App" image template. Follow the instructions below to build the app:
Web App Structure and Navigation:
Implement a primary navigation system for easy access between the account summary page and the offers detail page.
Ensure smooth navigation between pages and maintain a consistent UI theme based on the provided RBC app design.
First Page: Account Summary:
Design the main screen to display account summaries using flip cards.
Style each card to match RBC's brand colors and logos, as shown in the "RBC Banking App" image.
Use CSS and JS code to create animations for flipping the cards.
Account Flip Cards:
Chequing Account Card:
Display basic account details such as the account number and current balance.
Use the chequing account card image from this link: "https://www.rbcroyalbank.com/banking-services/_assets-custom/images/debit-card.png".
On flip, show the last 3 transactions by default and provide a clickable link titled "more details" to a detailed transaction page.
The detailed page should list the last 30 days' transactions, highlighting recurrent transactions like payroll deposits and grocery/utility transactions. Use the table format from the "RBC Banking App" image.
Credit Card Account Card:
Display the remaining balance and current payment due date.
Use the credit card account card image from this link: "https://www.rbcroyalbank.com/credit-cards/_assets-custom/images/cards/iav_infiniteavion_en_sm@2x.png".
On flip, showcase available credit card promotions or offers and include a clickable link labeled "learn more" to the offers detail page.
Offers Detail Page:
List all available offers that can be redeemed using RBC Avion points.
Provide concise but detailed descriptions of each offer, including instructions on how users can redeem them at specific locations using NFC or QR codes.
QR Code Integration:
When a user selects to redeem an offer using a QR code, generate a QR code dynamically using a Python library.
The QR code should be based on specific offer details and ready to scan.
Display the QR code on the screen along with usage instructions.
Technical Specifications:
Use Python 3 with Flask as the web framework.
Utilize libraries such as Werkzeug for utilities and qrcode for generating QR codes.
Implement a secure mechanism to store QR code images in a dedicated folder accessible by the app.
Data Handling and Security:
Use dummy data that mimics real banking transactions and account details.
Ensure data privacy guidelines are followed, especially during development and testing phases.
Design and Accessibility:
Match the font, color, and layout design according to RBC's existing app guidelines, as shown in the "RBC Banking App" image.
Ensure the app is accessible, including text readability, screen reader support, and easy navigation for all users.
Generate HTML, CSS, and JS code for each page, incorporating all the provided details. Create dummy data to make the website ready for customer use. Double-check for any errors in the code during development. Take a step-by-step approach to ensure all pages are included and the website functions properly.

## Collaborate with GPT Engineer

This is a [gptengineer.app](https://gptengineer.app)-synced repository 🌟🤖

Changes made via gptengineer.app will be committed to this repo.

If you clone this repo and push changes, you will have them reflected in the GPT Engineer UI.

## Tech stack

This project is built with React and Chakra UI.

- Vite
- React
- Chakra UI

## Setup

```sh
git clone https://github.com/GPT-Engineer-App/rbc-banking-app-flipcards.git
cd rbc-banking-app-flipcards
npm i
```

```sh
npm run dev
```

This will run a dev server with auto reloading and an instant preview.

## Requirements

- Node.js & npm - [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating)
