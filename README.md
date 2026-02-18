# Amazon Price Alert Automation

## Overview

This project monitors the price of a specified Amazon product and automatically sends an email notification when the price drops below a defined threshold.

It demonstrates real-world automation using web scraping, secure environment configuration, and SMTP-based notifications.

Built as part of #90DaysOfCode, this project focuses on practical automation workflows and secure credential handling.

---

## Technologies Used

- Python
- requests
- BeautifulSoup (bs4)
- smtplib
- dotenv
- Environment variable management

---

## Key Concepts Demonstrated

- HTTP request handling with custom headers
- HTML parsing using CSS selectors
- Dynamic price extraction and cleaning
- Threshold-based conditional logic
- Secure secret management using `.env`
- Automated email notifications via SMTP
- Production-style environment configuration

---

## Environment Variables

Create a `.env` file with the following:
```
SMTP_ADDRESS=smtp.gmail.com
EMAIL_ADDRESS=your_email@example.com

EMAIL_PASSWORD=your_app_password
```

⚠ Use an app-specific password for Gmail.

---

## Installation

```
pip install requests beautifulsoup4 python-dotenv
```

---
# How It Works

Sends a request to the Amazon product page.

Extracts product title and price.

Cleans and converts price to float.

Compares with predefined threshold.

Sends email notification if condition is met.

---
# How to Run
```
python main.py
```

---

# Why This Project Matters

This project demonstrates:

Real-world web automation

Conditional monitoring systems

Secure configuration management

Notification system design

Backend scripting for real utility use cases

It reflects practical automation engineering rather than theoretical scripting.

---
# Author

Faiz Hasan

Python Automation & Backend Developer
