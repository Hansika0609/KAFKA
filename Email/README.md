# 📧 Kafka Email Processor

## 🚀 Overview
This project demonstrates how to use **Apache Kafka** with Python to process email inputs. It consists of a **Kafka Producer** that takes an email input, stores it in an Excel file, and sends it to a Kafka topic. A **Kafka Consumer** listens to this topic and retrieves the email for further processing.

---

## 🛠️ Features
✅ Accepts email input from the user  
✅ Stores emails in an **Excel file** (`emails.xlsx`)  
✅ **Kafka Producer** sends email to Kafka topic  
✅ **Kafka Consumer** listens and retrieves emails  
✅ Uses **Kafka** for real-time data streaming  

---

## 📌 Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- **Kafka** (Running Locally or Remotely)
- Required Python libraries:
  ```sh
  pip install kafka-python pandas openpyxl
  ```

---

## ⚙️ Setup & Usage

### 1️⃣ Start Kafka & Zookeeper
Before running the program, ensure that Kafka and Zookeeper are running:
```sh
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
```

### 2️⃣ Run the Kafka Producer
The producer takes an email input, saves it in an Excel file, and sends it to Kafka.
```sh
python producer.py
```
📌 **Input Example:**
```
Enter email: example@email.com
```

### 3️⃣ Run the Kafka Consumer
The consumer listens to the Kafka topic and retrieves emails in real-time.
```sh
python consumer.py
```
📌 **Output Example:**
```
Listening for messages on topic email_topic...
Received Email: example@email.com
```

---

## 📜 Code Explanation

### **Producer (`producer.py`)**
- Accepts an email as input from the user.
- Stores the email in an **Excel file** (`emails.xlsx`).
- Sends the email data to **Kafka Topic (`email_topic`)**.

### **Consumer (`consumer.py`)**
- Subscribes to **Kafka Topic (`email_topic`)**.
- Receives and processes emails in real-time.

---

## 📂 Project Structure
```
📂 kafka-email-processor
│── producer.py  # Kafka Producer Script
│── consumer.py  # Kafka Consumer Script
│── emails.xlsx  # Stored Emails (Generated automatically)
│── README.md    # Project Documentation
```

---

## 🎯 Future Enhancements
🔹 Add a **database** (MySQL/PostgreSQL) for email storage.  
🔹 Implement **email validation** before storing and sending.  
🔹 Create a **GUI** to enhance user interaction.  
🔹 Deploy using **Docker** for scalability.  

---

## 🤝 Contributing
Feel free to fork this repository, submit issues, or contribute improvements! 🚀

---

## 📞 Contact
For any queries or suggestions, reach out via email: **hansikarastogi99@gmail.com**

🌟 If you like this project, give it a ⭐ on GitHub! 🎉

