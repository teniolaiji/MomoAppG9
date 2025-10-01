import random
import timeit

list_of_transactions = [
    {
        "id": 1,
        "transaction_type": "MOMO_IN",
        "amount": 2000,
        "sender": "Jane Smith",
        "receiver": None,
        "timestamp": "2024-05-10 16:30:51",
        "raw_text": "You have received 2000 RWF from Jane Smith (*********013) on your mobile money account at 2024-05-10 16:30:51. Message from sender: . Your new balance:2000 RWF. Financial Transaction Id: 76662021700."
    },
    {
        "id": 2,
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 1000,
        "sender": None,
        "receiver": "Jane",
        "timestamp": "2024-05-10 16:31:39",
        "raw_text": "TxId: 73214484437. Your payment of 1,000 RWF to Jane Smith 12845 has been completed at 2024-05-10 16:31:39. Your new balance: 1,000 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "id": 3,
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 600,
        "sender": None,
        "receiver": "Samuel",
        "timestamp": "2024-05-10 21:32:32",
        "raw_text": "TxId: 51732411227. Your payment of 600 RWF to Samuel Carter 95464 has been completed at 2024-05-10 21:32:32. Your new balance: 400 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "id": 4,
        "transaction_type": "BANK_DEPOSIT",
        "amount": 40000,
        "sender": "Own Account",
        "receiver": None,
        "timestamp": "2024-05-11 18:43:49",
        "raw_text": "*113*R*A bank deposit of 40000 RWF has been added to your mobile money account at 2024-05-11 18:43:49. Your NEW BALANCE :40400 RWF. Cash Deposit::CASH::::0::250795963036.Thank you for using MTN MobileMoney.*EN#"
    },
    {
        "id": 5,
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 2000,
        "sender": None,
        "receiver": "Samuel",
        "timestamp": "2024-05-11 18:48:42",
        "raw_text": "TxId: 17818959211. Your payment of 2,000 RWF to Samuel Carter 14965 has been completed at 2024-05-11 18:48:42. Your new balance: 38,400 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "id": 6,
        "transaction_type": "MOMO_OUT",
        "amount": 10000,
        "sender": None,
        "receiver": "Samuel Carter",
        "timestamp": "2024-05-11 20:34:47",
        "raw_text": "*165*S*10000 RWF transferred to Samuel Carter (250791666666) from 36521838 at 2024-05-11 20:34:47 . Fee was: 100 RWF. New balance: 28300 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "id": 7,
        "transaction_type": "MOMO_OUT",
        "amount": 1000,
        "sender": None,
        "receiver": "Samuel Carter",
        "timestamp": "2024-05-12 03:47:33",
        "raw_text": "*165*S*1000 RWF transferred to Samuel Carter (250790777777) from 36521838 at 2024-05-12 03:47:33 . Fee was: 20 RWF. New balance: 27280 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "id": 8,
        "transaction_type": "AIRTIME_OR_UTILITIES",
        "amount": 2000,
        "sender": None,
        "receiver": None,
        "timestamp": "2024-05-12 11:41:28",
        "raw_text": "*162*TxId:13913173274*S*Your payment of 2000 RWF to Airtime with token  has been completed at 2024-05-12 11:41:28. Fee was 0 RWF. Your new balance: 25280 RWF . Message: - -. *EN#"
    },
    {
        "id": 9,
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 10900,
        "sender": None,
        "receiver": "Jane",
        "timestamp": "2024-05-12 13:26:13",
        "raw_text": "TxId: 45434420466. Your payment of 10,900 RWF to Jane Smith 59543 has been completed at 2024-05-12 13:26:13. Your new balance: 14,380 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "id": 10,
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 3500,
        "sender": None,
        "receiver": "Alex",
        "timestamp": "2024-05-12 13:34:25",
        "raw_text": "TxId: 82113964658. Your payment of 3,500 RWF to Alex Doe 43810 has been completed at 2024-05-12 13:34:25. Your new balance: 10,880 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "id": 11,
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 1000,
        "sender": None,
        "receiver": "Robert",
        "timestamp": "2024-05-12 17:58:15",
        "raw_text": "TxId: 26614842768. Your payment of 1,000 RWF to Robert Brown 41193 has been completed at 2024-05-12 17:58:15. Your new balance: 9,880 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "id": 12,
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 5000,
        "sender": None,
        "receiver": "Linda",
        "timestamp": "2024-05-12 18:08:58",
        "raw_text": "TxId: 70497610538. Your payment of 5,000 RWF to Linda Green 75028 has been completed at 2024-05-12 18:08:58. Your new balance: 4,880 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "id": 13,
        "transaction_type": "MOMO_OUT",
        "amount": 1700,
        "sender": None,
        "receiver": "Samuel Carter",
        "timestamp": "2024-05-12 19:23:50",
        "raw_text": "*165*S*1700 RWF transferred to Samuel Carter (250788999999) from 36521838 at 2024-05-12 19:23:50 . Fee was: 100 RWF. New balance: 3080 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "id": 14,
        "transaction_type": "MOMO_OUT",
        "amount": 2000,
        "sender": None,
        "receiver": "Alex Doe",
        "timestamp": "2024-05-12 20:49:30",
        "raw_text": "*165*S*2000 RWF transferred to Alex Doe (250791666666) from 36521838 at 2024-05-12 20:49:30 . Fee was: 100 RWF. New balance: 980 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "id": 15,
        "transaction_type": "BANK_DEPOSIT",
        "amount": 5000,
        "sender": "Own Account",
        "receiver": None,
        "timestamp": "2024-05-14 09:10:29",
        "raw_text": "*113*R*A bank deposit of 5000 RWF has been added to your mobile money account at 2024-05-14 09:10:29. Your NEW BALANCE :5980 RWF. Cash Deposit::CASH::::0::250795963036.Thank you for using MTN MobileMoney.*EN#"
    },
    {
        "id": 16,
        "transaction_type": "MOMO_OUT",
        "amount": 1800,
        "sender": None,
        "receiver": "Robert Brown",
        "timestamp": "2024-05-14 09:11:32",
        "raw_text": "*165*S*1800 RWF transferred to Robert Brown (250788999999) from 36521838 at 2024-05-14 09:11:32 . Fee was: 100 RWF. New balance: 4080 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "id": 17,
        "transaction_type": "MOMO_OUT",
        "amount": 2500,
        "sender": None,
        "receiver": "Jane Smith",
        "timestamp": "2024-05-14 09:27:40",
        "raw_text": "*165*S*2500 RWF transferred to Jane Smith (250791666666) from 36521838 at 2024-05-14 09:27:40 . Fee was: 100 RWF. New balance: 1480 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "id": 18,
        "transaction_type": "MOMO_OUT",
        "amount": 500,
        "sender": None,
        "receiver": "Samuel Carter",
        "timestamp": "2024-05-14 14:01:57",
        "raw_text": "*165*S*500 RWF transferred to Samuel Carter (250790777777) from 36521838 at 2024-05-14 14:01:57 . Fee was: 20 RWF. New balance: 960 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "id": 19,
        "transaction_type": "BANK_DEPOSIT",
        "amount": 5000,
        "sender": "Own Account",
        "receiver": None,
        "timestamp": "2024-05-14 19:06:03",
        "raw_text": "*113*R*A bank deposit of 5000 RWF has been added to your mobile money account at 2024-05-14 19:06:03. Your NEW BALANCE :5960 RWF. Cash Deposit::CASH::::0::250795963036.Thank you for using MTN MobileMoney.*EN#"
    },
    {
        "id": 20,
        "transaction_type": "MOMO_OUT",
        "amount": 1800,
        "sender": None,
        "receiver": "Alex Doe",
        "timestamp": "2024-05-14 19:21:16",
        "raw_text": "*165*S*1800 RWF transferred to Alex Doe (250791666666) from 36521838 at 2024-05-14 19:21:16 . Fee was: 100 RWF. New balance: 4060 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    }
]

dict_of_transactions = {
    1: {
        "transaction_type": "MOMO_IN",
        "amount": 2000,
        "sender": "Jane Smith",
        "receiver": None,
        "timestamp": "2024-05-10 16:30:51",
        "raw_text": "You have received 2000 RWF from Jane Smith (*********013) on your mobile money account at 2024-05-10 16:30:51. Message from sender: . Your new balance:2000 RWF. Financial Transaction Id: 76662021700."
    },
    2: {
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 1000,
        "sender": None,
        "receiver": "Jane",
        "timestamp": "2024-05-10 16:31:39",
        "raw_text": "TxId: 73214484437. Your payment of 1,000 RWF to Jane Smith 12845 has been completed at 2024-05-10 16:31:39. Your new balance: 1,000 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    3: {
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 600,
        "sender": None,
        "receiver": "Samuel",
        "timestamp": "2024-05-10 21:32:32",
        "raw_text": "TxId: 51732411227. Your payment of 600 RWF to Samuel Carter 95464 has been completed at 2024-05-10 21:32:32. Your new balance: 400 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    4: {
        "transaction_type": "BANK_DEPOSIT",
        "amount": 40000,
        "sender": "Own Account",
        "receiver": None,
        "timestamp": "2024-05-11 18:43:49",
        "raw_text": "*113*R*A bank deposit of 40000 RWF has been added to your mobile money account at 2024-05-11 18:43:49. Your NEW BALANCE :40400 RWF. Cash Deposit::CASH::::0::250795963036.Thank you for using MTN MobileMoney.*EN#"
    },
    5: {
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 2000,
        "sender": None,
        "receiver": "Samuel",
        "timestamp": "2024-05-11 18:48:42",
        "raw_text": "TxId: 17818959211. Your payment of 2,000 RWF to Samuel Carter 14965 has been completed at 2024-05-11 18:48:42. Your new balance: 38,400 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    6: {
        "transaction_type": "MOMO_OUT",
        "amount": 10000,
        "sender": None,
        "receiver": "Samuel Carter",
        "timestamp": "2024-05-11 20:34:47",
        "raw_text": "*165*S*10000 RWF transferred to Samuel Carter (250791666666) from 36521838 at 2024-05-11 20:34:47 . Fee was: 100 RWF. New balance: 28300 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    7: {
        "transaction_type": "MOMO_OUT",
        "amount": 1000,
        "sender": None,
        "receiver": "Samuel Carter",
        "timestamp": "2024-05-12 03:47:33",
        "raw_text": "*165*S*1000 RWF transferred to Samuel Carter (250790777777) from 36521838 at 2024-05-12 03:47:33 . Fee was: 20 RWF. New balance: 27280 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    8: {
        "transaction_type": "AIRTIME_OR_UTILITIES",
        "amount": 2000,
        "sender": None,
        "receiver": None,
        "timestamp": "2024-05-12 11:41:28",
        "raw_text": "*162*TxId:13913173274*S*Your payment of 2000 RWF to Airtime with token  has been completed at 2024-05-12 11:41:28. Fee was 0 RWF. Your new balance: 25280 RWF . Message: - -. *EN#"
    },
    9: {
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 10900,
        "sender": None,
        "receiver": "Jane",
        "timestamp": "2024-05-12 13:26:13",
        "raw_text": "TxId: 45434420466. Your payment of 10,900 RWF to Jane Smith 59543 has been completed at 2024-05-12 13:26:13. Your new balance: 14,380 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    10: {
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 3500,
        "sender": None,
        "receiver": "Alex",
        "timestamp": "2024-05-12 13:34:25",
        "raw_text": "TxId: 82113964658. Your payment of 3,500 RWF to Alex Doe 43810 has been completed at 2024-05-12 13:34:25. Your new balance: 10,880 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    11: {
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 1000,
        "sender": None,
        "receiver": "Robert",
        "timestamp": "2024-05-12 17:58:15",
        "raw_text": "TxId: 26614842768. Your payment of 1,000 RWF to Robert Brown 41193 has been completed at 2024-05-12 17:58:15. Your new balance: 9,880 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    12: {
        "transaction_type": "MERCHANT_PAYMENT",
        "amount": 5000,
        "sender": None,
        "receiver": "Linda",
        "timestamp": "2024-05-12 18:08:58",
        "raw_text": "TxId: 70497610538. Your payment of 5,000 RWF to Linda Green 75028 has been completed at 2024-05-12 18:08:58. Your new balance: 4,880 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    13: {
        "transaction_type": "MOMO_OUT",
        "amount": 1700,
        "sender": None,
        "receiver": "Samuel Carter",
        "timestamp": "2024-05-12 19:23:50",
        "raw_text": "*165*S*1700 RWF transferred to Samuel Carter (250788999999) from 36521838 at 2024-05-12 19:23:50 . Fee was: 100 RWF. New balance: 3080 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    14: {
        "transaction_type": "MOMO_OUT",
        "amount": 2000,
        "sender": None,
        "receiver": "Alex Doe",
        "timestamp": "2024-05-12 20:49:30",
        "raw_text": "*165*S*2000 RWF transferred to Alex Doe (250791666666) from 36521838 at 2024-05-12 20:49:30 . Fee was: 100 RWF. New balance: 980 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    15: {
        "transaction_type": "BANK_DEPOSIT",
        "amount": 5000,
        "sender": "Own Account",
        "receiver": None,
        "timestamp": "2024-05-14 09:10:29",
        "raw_text": "*113*R*A bank deposit of 5000 RWF has been added to your mobile money account at 2024-05-14 09:10:29. Your NEW BALANCE :5980 RWF. Cash Deposit::CASH::::0::250795963036.Thank you for using MTN MobileMoney.*EN#"
    },
    16: {
        "transaction_type": "MOMO_OUT",
        "amount": 1800,
        "sender": None,
        "receiver": "Robert Brown",
        "timestamp": "2024-05-14 09:11:32",
        "raw_text": "*165*S*1800 RWF transferred to Robert Brown (250788999999) from 36521838 at 2024-05-14 09:11:32 . Fee was: 100 RWF. New balance: 4080 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    17: {
        "transaction_type": "MOMO_OUT",
        "amount": 2500,
        "sender": None,
        "receiver": "Jane Smith",
        "timestamp": "2024-05-14 09:27:40",
        "raw_text": "*165*S*2500 RWF transferred to Jane Smith (250791666666) from 36521838 at 2024-05-14 09:27:40 . Fee was: 100 RWF. New balance: 1480 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    18: {
        "transaction_type": "MOMO_OUT",
        "amount": 500,
        "sender": None,
        "receiver": "Samuel Carter",
        "timestamp": "2024-05-14 14:01:57",
        "raw_text": "*165*S*500 RWF transferred to Samuel Carter (250790777777) from 36521838 at 2024-05-14 14:01:57 . Fee was: 20 RWF. New balance: 960 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    19: {
        "transaction_type": "BANK_DEPOSIT",
        "amount": 5000,
        "sender": "Own Account",
        "receiver": None,
        "timestamp": "2024-05-14 19:06:03",
        "raw_text": "*113*R*A bank deposit of 5000 RWF has been added to your mobile money account at 2024-05-14 19:06:03. Your NEW BALANCE :5960 RWF. Cash Deposit::CASH::::0::250795963036.Thank you for using MTN MobileMoney.*EN#"
    },
    20: {
        "transaction_type": "MOMO_OUT",
        "amount": 1800,
        "sender": None,
        "receiver": "Alex Doe",
        "timestamp": "2024-05-14 19:21:16",
        "raw_text": "*165*S*1800 RWF transferred to Alex Doe (250791666666) from 36521838 at 2024-05-14 19:21:16 . Fee was: 100 RWF. New balance: 4060 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    }
}


target = random.randint(1, 20)


def linear_search():
    for transaction in list_of_transactions:
        if transaction["id"] == target:
            return transaction


def dict_lookup():
    return dict_of_transactions[target]


repeat = 20
number = 200

list_time = timeit.repeat(
    "linear_search()", globals=globals(), repeat=repeat, number=number)
dict_time = timeit.repeat(
    "dict_lookup()", globals=globals(), repeat=repeat, number=number)

print("avg time list:", sum(list_time)/len(list_time))
print("avg time dict:", sum(dict_time)/len(dict_time))

print(list_time > dict_time)
