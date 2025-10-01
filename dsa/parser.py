import xml.etree.ElementTree as ET
import re

# path to the xml file


def parse_transactions(raw_xml_data_path):
    tree = ET.parse(raw_xml_data_path)
    root = tree.getroot()

# regex to extract specified fields
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

# initialize list to store all parsed records as dictionaries
    transactions = []
    transaction_id = 1

# loop through sms record
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
