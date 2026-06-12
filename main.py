import json
import re
import pandas as pd

from services.ocr_service import extract_text
from agents.extraction_agent import extract_invoice_data
from agents.validation_agent import validate_invoice
from agents.fraud_agent import detect_fraud
from agents.approval_agent import approve_invoice


def main():

    invoice_path = "invoices/invoice.jpeg"

    print("Reading Invoice...")

    invoice_text = extract_text(invoice_path)

    print("OCR Completed")

    extraction_result = extract_invoice_data(invoice_text)

    print("Extraction Completed")

    try:
        json_string = re.search(
            r"\{.*\}",
            extraction_result,
            re.DOTALL
        ).group()

        invoice_data = json.loads(json_string)

    except Exception as e:
        print("JSON Parsing Failed")
        print(extraction_result)
        return

    validation_report = validate_invoice(invoice_data)

    print("Validation Completed")

    fraud_report = detect_fraud(invoice_data)

    print("Fraud Analysis Completed")

    approval_report = approve_invoice(
        invoice_data,
        validation_report,
        fraud_report
    )

    print("Approval Completed")

    df = pd.DataFrame([invoice_data])

    df["validation"] = validation_report
    df["fraud_report"] = fraud_report
    df["approval"] = approval_report

    df.to_csv(
        "outputs/processed_invoice.csv",
        index=False
    )

    print("\n===== FINAL RESULT =====")

    print("\nInvoice Data:")
    print(invoice_data)

    print("\nValidation:")
    print(validation_report)

    print("\nFraud Analysis:")
    print(fraud_report)

    print("\nApproval:")
    print(approval_report)

    print("\nCSV Saved -> outputs/processed_invoice.csv")


if __name__ == "__main__":
    main()