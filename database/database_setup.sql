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