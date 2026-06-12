from services.groq_service import ask_groq

def validate_invoice(invoice_data):

    prompt = f"""
    You are a Validation Agent.

    Check:

    1. Missing fields
    2. Invalid dates
    3. Negative amounts
    4. Missing invoice number

    Invoice:

    {invoice_data}

    Return a validation report.
    """

    return ask_groq(prompt)