from services.groq_service import ask_groq

def detect_fraud(invoice_data):

    prompt = f"""
    You are a Fraud Detection Agent.

    Analyze:

    - Fake invoice indicators
    - Duplicate invoice possibility
    - Suspicious amount
    - Vendor authenticity concerns

    Invoice:

    {invoice_data}

    Give:

    Risk Score (0-100)

    Findings
    """

    return ask_groq(prompt)