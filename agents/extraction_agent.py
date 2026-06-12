from services.groq_service import ask_groq

def extract_invoice_data(invoice_text):

    prompt = f"""
    You are an Invoice Extraction Agent.

    Extract:

    Vendor Name
    Invoice Number
    Invoice Date
    Due Date
    Tax Amount
    Total Amount
    Currency

    Return ONLY valid JSON.

    Invoice Text:

    {invoice_text}
    """

    return ask_groq(prompt)