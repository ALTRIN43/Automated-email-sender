# Birthday Wisher Project

## Overview
This project is a simple automated birthday wisher built using Python. It reads birthday data from a CSV file and sends personalized birthday wishes via email.

## How It Works
1. The script reads birthdays from `birthdays.csv`.
2. It checks if today's date matches any birthday.
3. If a match is found, it randomly selects a birthday message template from the `letter_templates` folder.
4. The email is sent to the birthday person with the personalized message.

## Files
- `birthdays.csv`: A CSV file containing the name, email, year, month, and day of the birthday persons.
- `letter_templates/letter_1.txt`, `letter_templates/letter_2.txt`, `letter_templates/letter_3.txt`: Sample letter templates with `[NAME]` placeholder.
- `birthday_wisher.py`: The main Python script.

## Running on PythonAnywhere
1. Create a free account on [PythonAnywhere](https://www.pythonanywhere.com/).
2. Open a Bash console and clone your repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
3. Navigate to your project directory:
   ```bash
   cd your-repo
   ```
4. Create a scheduled task in PythonAnywhere to run the script daily:
   - Go to the 'Tasks' tab.
   - Click 'Add a new scheduled task'.
   - Enter the path to your script (e.g., `/home/your-username/your-repo/birthday_wisher.py`).
   - Set the time and frequency for the task to run.

## Running Locally
1. Install required libraries (if not already installed):
   ```bash
   pip install pandas
   ```
2. Replace the following fields in `birthday_wisher.py` with your own details:
   ```python
   my_email = "example@example.com"  # Replace with your email
   password = "yourpassword"  # Replace with your password
   ```
3. Run the script:
   ```bash
   python birthday_wisher.py
   ```

## Sample CSV File
```csv
name,email,year,month,day
John Doe,john.doe@example.com,1990,2,18
Jane Smith,jane.smith@example.com,1995,3,15
Bob Johnson,bob.johnson@example.com,1988,4,10
```

## Sample Letter Templates
### letter_1.txt
```
Dear [NAME],

Wishing you a fantastic birthday filled with joy and happiness!
Have a wonderful year ahead.

Best regards,
Your Friend
```
### letter_2.txt
```
Happy Birthday [NAME]!

Hope this day brings you lots of laughter, love, and cheer.
Enjoy your special day to the fullest!

Cheers,
Your Friend
```
### letter_3.txt
```
Hello [NAME],

On this wonderful day, I just want to remind you how special you are to me.
Have a great birthday and an amazing year ahead!

With love,
Your Friend
```

## Important Notes
- Make sure to enable 'Less secure app access' in your Gmail account settings if using Gmail. Alternatively, use an app password for better security.
- Do not share your email credentials in public repositories. Consider using environment variables or a `.env` file to secure your credentials.
