CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL CHECK (full_name <> ''), -- cannot be empty
    phone_number VARCHAR(12) NOT NULL UNIQUE
);

CREATE TABLE transaction_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_type VARCHAR(25) NOT NULL
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    amount DECIMAL(10,2) NOT NULL CHECK (amount > 0),  -- this will reject 0 or negative amounts for transactions
    date TIMESTAMP NOT NULL,
    balance_after DECIMAL(10,2) NOT NULL CHECK (balance_after >= 0), -- balance cannot go negative
    body TEXT NOT NULL,
    CONSTRAINT fk_transactions_category
        FOREIGN KEY (category_id) REFERENCES transaction_categories(id)
        ON DELETE SET NULL
);

CREATE TABLE transaction_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id INT NOT NULL,
    user_id INT NOT NULL,
    user_role ENUM('sender', 'receiver', 'payer') NOT NULL,
    UNIQUE (transaction_id, user_id),  -- only one transaction per user
    CONSTRAINT fk_txn_users_txn
        FOREIGN KEY (transaction_id) REFERENCES transactions(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_txn_users_user
        FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
);

CREATE TABLE system_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    action TEXT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_transactions_date 
    ON transactions(date);

CREATE INDEX idx_transaction_users_transaction_id 
    ON transaction_users(transaction_id);

CREATE INDEX idx_transaction_users_user_id 
    ON transaction_users(user_id);

CREATE INDEX idx_transactions_category_id 
    ON transactions(category_id);


INSERT INTO users (full_name, phone_number) VALUES --AI used to generate sample data
('Kwizera Jean Bosco', '250781111111'),
('Uwamahoro Aline', '250782222222'),
('Nshimiyimana Eric', '250783333333'),
('Mukamana Claudine', '250784444444'),
('Habimana Patrick', '250785555555');

INSERT INTO transaction_categories (category_type) VALUES
('MOMO_OUT'),
('MOMO_IN'),
('BANK_DEPOSIT'),
('AIRTIME_OR_UTILITIES'),
('MERCHANT_PAYMENT'),
('AGENT_WITHDRAWAL');

INSERT INTO transactions (category_id, amount, date, balance_after, body) VALUES
(1, 15000.00, '2025-09-01 10:15:00', 85000.00, 'TxId: 73214484437. Your payment of 15,000 RWF to Jane Smith 12845 has been completed at 2024-05-10 16:31:39. Your new balance: 1,000 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije.'),
(2, 20000.00, '2025-09-02 14:20:00', 2000.00, 'You have received 20000 RWF from Jane Smith (*013) on your mobile money account at 2024-05-10 16:30:51. Message from sender: . Your new balance:2000 RWF. Financial Transaction Id: 76662021700.'),
(3, 5000.00,  '2025-09-03 09:30:00', 5000.00, 'Funded wallet with 5000 RWF'),
(4, 1000.00,  '2025-09-04 12:45:00', 1000.00, 'Purchased airtime of 1000 RWF'),
(5, 2500.00,  '2025-09-05 18:10:00', 2500.00, 'Paid electricity bill of 2500 RWF'),
(6, 2500.00,  '2025-09-05 18:10:00', 20000.00, 'You Abebe Chala CHEBUDIE (*036) have via agent: Agent Sophia (250790777777), withdrawn 2500 RWF from your mobile money account');

INSERT INTO transaction_users (transaction_id, user_id, user_role) VALUES
(1, 1, 'sender'),
(1, 2, 'receiver'),
(2, 3, 'sender'),
(2, 1, 'receiver'),
(3, 1, 'payer');
