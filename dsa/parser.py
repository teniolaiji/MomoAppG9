import xml.etree.ElementTree as ET
import re

def parse_transactions(raw_xml_data_path):
    tree = ET.parse(raw_xml_data_path)
    root = tree.getroot()

# regex for specified fields
    AIRTIME_OR_UTILITIES = re.compile(r"(\d{1,3}(?:,\d{3})*|\d+) RWF")
    MOMO_IN = re.compile(r"received (\d+) RWF from (.+?) \(")
    MOMO_OUT = re.compile(
        r"(\d{1,3}(?:,\d{3})*|\d+) RWF transferred to (.+?) \(")
    MERCHANT_PAYMENT = re.compile(
        r"payment of (\d{1,3}(?:,\d{3})*|\d+) RWF to (.+?) ")
    BANK_DEPOSIT = re.compile(r"deposit of (\d+) RWF")
    AGENT_WITHDRAWAL = re.compile(r"withdrawn (\d+) RWF.*?via agent: (.+?) ")
    BUSINESS_PAYMENT = re.compile(r"transaction of (\d+) RWF by (.+?) ")
    timestamp_pattern = re.compile(r"at (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")

# list to store all parsed records as dictionaries
    transactions = []
    transaction_id = 1


    for sms in root:

        body = sms.attrib.get('body')
        record = {
            "id": transaction_id,
            "transaction_type": None,
            "amount": None,
            "sender": None,
            "receiver": None,
            "timestamp": None,
            "raw_text": body
        }

        body_lower = body.lower()
        ts_match = timestamp_pattern.search(body)
        if ts_match is not None:
            record["timestamp"] = ts_match.group(1)
        # classifying records by transaction type
        if "you have received" in body_lower:
            record["transaction_type"] = "MOMO_IN"
            match = MOMO_IN.search(body)
            if match:
                record["amount"] = int(match.group(1).replace(",", ""))
                record["sender"] = match.group(2)

        elif "transferred to" in body_lower:
            record["transaction_type"] = "MOMO_OUT"
            match = MOMO_OUT.search(body)
            if match:
                record["amount"] = int(match.group(1).replace(",", ""))
                record["receiver"] = match.group(2)

        elif "deposit of" in body_lower:
            record["transaction_type"] = "BANK_DEPOSIT"
            match = BANK_DEPOSIT.search(body)
            if match:
                record["amount"] = int(match.group(1))
                record["sender"] = "Own Account"

        elif "your payment of" in body_lower and "airtime" not in body_lower and "cash power" not in body_lower:
            record["transaction_type"] = "MERCHANT_PAYMENT"
            match = MERCHANT_PAYMENT.search(body)
            if match:
                record["amount"] = int(match.group(1).replace(",", ""))
                record["receiver"] = match.group(2)

        elif "airtime" in body_lower or "cash power" in body_lower:
            record["transaction_type"] = "AIRTIME_OR_UTILITIES"
            match = AIRTIME_OR_UTILITIES.search(body)
            if match:
                record["amount"] = int(match.group(1).replace(",", ""))

        elif "withdrawn" in body_lower and "agent" in body_lower:
            record["transaction_type"] = "AGENT_WITHDRAWAL"
            match = AGENT_WITHDRAWAL.search(body)
            if match:
                record["amount"] = int(match.group(1).replace(",", ""))
                record["receiver"] = match.group(2)

        elif "transaction of" in body_lower and "by" in body_lower:
            record["transaction_type"] = "BUSINESS_PAYMENT"
            match = BUSINESS_PAYMENT.search(body)
            if match:
                record["amount"] = int(match.group(1).replace(",", ""))
                record["receiver"] = match.group(2)
        else:
            continue  
        transactions.append(record)
        transaction_id += 1
    return transactions 
