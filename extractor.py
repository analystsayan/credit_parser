import fitz
import re

def extract_text_from_pdf(pdf_path):
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text


def parse_sbi_statement(text):
    text = text.replace('\r', '').replace('\n', ' ')

    # Extract card number
    card_match = re.search(r'(XXXX XXXX XXXX \w{2,4})', text)
    card_number = card_match.group(1) if card_match else "Not found"

    # Start parsing only after card number to avoid junk
    start_index = text.find(card_number)
    relevant_text = text[start_index:] if start_index != -1 else text

    # Amounts and dates
    amounts = re.findall(r'[\d,]+\.\d{2}', relevant_text)
    dates = re.findall(r'\d{1,2} \w{3} \d{4}', relevant_text)

    def get(i): return amounts[i] if len(amounts) > i else "Not found"

    return {
        "Bank": "SBI",
        "Credit Card Number": card_number,
        "Total Amount Due": get(0),
        "Minimum Amount Due": get(1),
        "Credit Limit": get(2),
        "Cash Limit": get(3),
        "Available Credit Limit": get(4),
        "Available Cash Limit": get(5),
        "Payments & Reversals": get(6),
        "Additions": get(7),
        "Fee/Tax/Interest": get(8),
        "Statement Date": dates[0] if len(dates) > 0 else "Not found",
        "Payment Due Date": dates[1] if len(dates) > 1 else "Not found",
        "Previous Balance": get(9),
        "Total Outstanding": get(10),
    }


def parse_axis_statement(text):
    # Normalize the text
    clean_text = (
        text.replace('\r', ' ')
            .replace('\n', ' ')
            .replace('\xa0', ' ')
            .replace('₹', '')
            .replace(',', '')
            .strip()
    )

    def extract(pattern, label, flags=re.IGNORECASE):
        match = re.search(pattern, clean_text, flags)
        return match.group(1).strip() if match else f"{label} not found"

    def extract_due(label):
        match = re.search(fr'{label}\s*([\d]+\.\d{{2}})\s*(Cr|Dr)?', clean_text, re.IGNORECASE)
        if match:
            amount = match.group(1)
            suffix = match.group(2)
            if suffix and suffix.lower() == 'cr':
                return f"₹0.00 (Credit Balance ₹{amount})"
            else:
                return f"₹{amount}"
        return f"{label} not found"

    return {
        "Bank": "Axis",
        "Credit Card Number": extract(r'Card No[:\s]*([0-9Xx*\s]+)', "Credit Card Number"),
        "Statement Date": extract(r'Statement Period\s*\d{2}/\d{2}/\d{4}\s*-\s*(\d{2}/\d{2}/\d{4})', "Statement Date"),
        "Payment Due Date": extract(r'Payment Due Date[:\s]*([0-9/]+)', "Payment Due Date"),
        "Total Amount Due": extract_due("Total Payment Due"),
        "Minimum Amount Due": extract_due("Minimum Payment Due"),
        "Credit Limit": extract(r'Credit Limit\s*([\d]+\.\d{2})', "Credit Limit"),
        "Available Credit Limit": extract(r'Available Credit Limit\s*([\d]+\.\d{2})', "Available Credit Limit"),
        "Available Cash Limit": extract(r'Available Cash Limit\s*([\d]+\.\d{2})', "Available Cash Limit"),
        "Opening Balance": extract(r'Previous Balance.*?(\d+\.\d{2})\s*Dr', "Opening Balance")
    }



