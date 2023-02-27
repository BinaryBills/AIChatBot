#Author: BinaryBills
#Creation Date: January 8, 2022
#Date Modified: January 17, 2022
#Purpose: Declaration of SQL Tables for the database and helper functions to make using the tables minimal work.


history = "CREATE TABLE IF NOT EXISTS conversations (id INT AUTO_INCREMENT PRIMARY KEY, message TEXT, response TEXT, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"


