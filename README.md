# Automated Birthday Wisher

This project is an **Automated Birthday Wisher** built using **Python**. It automatically sends birthday wishes via email to individuals listed in a CSV file on their special day.

---

## 📜 How It Works

- The script reads a CSV file called `birthdays.csv` containing details like **Name, Email, Month, and Day**.
- It checks if **today's date matches any birthday in the CSV file**.
- If a match is found, it picks a random letter template from the `letter_templates` folder (e.g., `letter_1.txt`, `letter_2.txt`, `letter_3.txt`).
- It **replaces [NAME] in the template** with the birthday person's name.
- It sends an email with the customized message to the recipient using **smtplib**.

---

## 🗂️ File Structure

```
project_folder/
│
├── birthdays.csv
│
├── birthday_wisher.py  # This is the main script
│
├── letter_templates/
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
```

---

## 📝 Sample `birthdays.csv`

| name   | email             | month | day |
|--------|--------------------|-------|-----|
| John   | john@example.com   | 2     | 16  |
| Alice  | alice@example.com  | 3     | 25  |

---

## 📝 Sample `letter_1.txt`

```
Happy Birthday [NAME]!
Have a wonderful year ahead!
```

---

## 🚀 How to Run

1. **Replace the placeholders in `birthday_wisher.py` with your email credentials:**
   ```python
   my_email = "your_email@example.com"
   password = "your_app_password"
   ```

2. **Ensure you have allowed Less Secure Apps in your email settings** or **created an App Password** if using Gmail.

3. **Install pandas library (if not already installed):**
   ```bash
   pip install pandas
   ```

4. **Run the script:**
   ```bash
   python birthday_wisher.py
   ```

---

## ⚠️ Important Notes

- **Do not upload your personal email credentials to GitHub.** Always use placeholders like `your_email@example.com` and `your_app_password` before pushing the code.
- **Use Two Emails:**
  - **Sender Email (Your Email):** This is the email you are using to send birthday wishes.
  - **Recipient Email:** Comes from the `birthdays.csv` file.

---

## 🛠️ Requirements

- Python
- pandas
- smtplib (built-in)
- datetime (built-in)

---

## 🌟 Project Outcome

When the script detects a birthday match, you should see the message:
```
Message sent successfully
```
The birthday person will receive a personalized email with a birthday message.


## Can modify this and send different types of mails :)
