from services.groq_service import ask_groq

def approve_invoice(
    invoice_data,
    validation_report,
    fraud_report
):

    prompt = f"""
    Invoice:

    {invoice_data}

    Validation:

    {validation_report}

    Fraud Analysis:

    {fraud_report}

    Decide:

    APPROVED
    REJECTED
    REVIEW REQUIRED

    Explain your decision.
    """

    return ask_groq(prompt)