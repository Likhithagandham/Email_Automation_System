import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from datetime import datetime
import csv
import os

# ==================== CONFIGURATION ====================
sender_email = "your_email@gmail.com"  # Replace with your Gmail
sender_password = "your_app_password_here"  # Replace with your app password

# ==================== EMAIL TEMPLATES ====================
EMAIL_TEMPLATES = {
    "client_followup": {
        "subject": "Follow-up on Our Recent Meeting",
        "body": """Hello {name},

Thank you for taking the time to meet with us. We wanted to follow up on the discussion points and next steps.

{custom_message}

We look forward to continuing our partnership.

Best regards,
{company_name}"""
    },
    "weekly_report": {
        "subject": "Weekly Status Report - {date}",
        "body": """Hello {name},

Here is your weekly status report for the week ending {date}.

{custom_message}

Please let us know if you have any questions.

Best regards,
{company_name}"""
    },
    "meeting_reminder": {
        "subject": "Reminder: Upcoming Meeting on {date}",
        "body": """Hello {name},

This is a friendly reminder about our scheduled meeting:

Date & Time: {date}
Topic: {custom_message}

Looking forward to speaking with you.

Best regards,
{company_name}"""
    },
    "thank_you": {
        "subject": "Thank You for Your Business",
        "body": """Hello {name},

We want to express our sincere gratitude for your continued partnership.

{custom_message}

Thank you for choosing us.

Best regards,
{company_name}"""
    },
    "project_update": {
        "subject": "Project Update - {date}",
        "body": """Hello {name},

Here's an update on your project status:

{custom_message}

We'll continue to keep you informed of any developments.

Best regards,
{company_name}"""
    }
}

# ==================== EMAIL SENDING FUNCTION ====================
def send_email(receiver_email, receiver_name, template_type, custom_message, company_name="Your Company"):
    """
    Sends a business email using predefined templates
    """
    
    # Get template
    template = EMAIL_TEMPLATES.get(template_type)
    if not template:
        print(f"✗ Template '{template_type}' not found!")
        return False
    
    # Format email content
    current_date = datetime.now().strftime("%B %d, %Y")
    subject = template["subject"].format(name=receiver_name, date=current_date)
    body = template["body"].format(
        name=receiver_name,
        custom_message=custom_message,
        company_name=company_name,
        date=current_date
    )
    
    # Create email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        server.quit()
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{current_time}] SUCCESS: {template_type} email sent to {receiver_name} ({receiver_email})"
        print(f"✓ {log_message}")
        save_log(log_message)
        return True
        
    except Exception as e:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{current_time}] FAILED: Email to {receiver_name} - Error: {e}"
        print(f"✗ {log_message}")
        save_log(log_message)
        return False

# ==================== LOGGING FUNCTION ====================
def save_log(message):
    """Saves log messages to a file"""
    with open("business_email_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")

# ==================== CSV FUNCTIONS ====================
def load_recipients_from_csv(filename):
    """
    Loads recipient data from CSV file
    CSV Format: email,name,template_type,custom_message
    """
    recipients = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                recipients.append({
                    'email': row['email'],
                    'name': row['name'],
                    'template_type': row['template_type'],
                    'custom_message': row['custom_message']
                })
        print(f"✓ Loaded {len(recipients)} recipients from {filename}")
        return recipients
    except FileNotFoundError:
        print(f"✗ File '{filename}' not found!")
        return []
    except Exception as e:
        print(f"✗ Error reading CSV: {e}")
        return []

def create_sample_csv():
    """Creates a sample CSV file with example data"""
    sample_data = [
        ['email', 'name', 'template_type', 'custom_message'],
        ['likhithakrishna19@gmail.com', 'John Smith', 'client_followup', 'We discussed the Q4 objectives and timeline.'],
        ['likhithakrishna19@gmail.com', 'Sarah Johnson', 'weekly_report', 'All projects are on track this week.'],
        ['likhithakrishna19@gmail.com', 'Mike Davis', 'meeting_reminder', 'Project kickoff meeting']
    ]
    
    with open('recipients.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)
    
    print("✓ Sample CSV file 'recipients.csv' created!")

# ==================== BATCH SENDING ====================
def send_batch_from_csv(filename, company_name="Your Company"):
    """Sends emails to all recipients in CSV file"""
    recipients = load_recipients_from_csv(filename)
    
    if not recipients:
        return
    
    print(f"\n{'='*60}")
    print("BATCH EMAIL SENDING STARTED")
    print(f"{'='*60}\n")
    
    success = 0
    failed = 0
    
    for recipient in recipients:
        result = send_email(
            recipient['email'],
            recipient['name'],
            recipient['template_type'],
            recipient['custom_message'],
            company_name
        )
        
        if result:
            success += 1
        else:
            failed += 1
        
        time.sleep(2)  # Prevent spam detection
    
    print(f"\n{'='*60}")
    print("BATCH SENDING COMPLETE")
    print(f"{'='*60}")
    print(f"Successfully sent: {success}")
    print(f"Failed: {failed}")
    print(f"{'='*60}\n")

# ==================== SCHEDULED TASKS ====================
def weekly_client_update():
    """Sends weekly updates to clients every Monday at 9 AM"""
    recipients = load_recipients_from_csv('recipients.csv')
    for recipient in recipients:
        if recipient['template_type'] == 'weekly_report':
            send_email(
                recipient['email'],
                recipient['name'],
                'weekly_report',
                recipient['custom_message']
            )

def daily_meeting_reminders():
    """Sends meeting reminders every day at 8 AM"""
    recipients = load_recipients_from_csv('recipients.csv')
    for recipient in recipients:
        if recipient['template_type'] == 'meeting_reminder':
            send_email(
                recipient['email'],
                recipient['name'],
                'meeting_reminder',
                recipient['custom_message']
            )

# ==================== MENU SYSTEM ====================
def show_menu():
    print(f"\n{'='*60}")
    print("BUSINESS EMAIL AUTOMATION SYSTEM")
    print(f"{'='*60}")
    print("1. Send single business email")
    print("2. Create sample CSV file")
    print("3. Send batch emails from CSV")
    print("4. Start scheduled email service")
    print("5. View available email templates")
    print("6. View email log")
    print("7. Exit")
    print(f"{'='*60}")

def send_single_business_email():
    print("\n--- Send Single Business Email ---")
    print("\nAvailable templates:")
    for i, template in enumerate(EMAIL_TEMPLATES.keys(), 1):
        print(f"{i}. {template}")
    
    template_choice = input("\nEnter template name: ")
    if template_choice not in EMAIL_TEMPLATES:
        print("✗ Invalid template!")
        return
    
    receiver_email = input("Recipient email: ")
    receiver_name = input("Recipient name: ")
    custom_message = input("Custom message: ")
    company_name = input("Company name (press Enter for 'Your Company'): ") or "Your Company"
    
    send_email(receiver_email, receiver_name, template_choice, custom_message, company_name)

def view_templates():
    print(f"\n{'='*60}")
    print("AVAILABLE EMAIL TEMPLATES")
    print(f"{'='*60}")
    for name, template in EMAIL_TEMPLATES.items():
        print(f"\nTemplate: {name}")
        print(f"Subject: {template['subject']}")
        print(f"Preview: {template['body'][:100]}...")
        print("-" * 60)

def start_scheduler():
    print("\n--- Starting Scheduled Email Service ---")
    
    # Schedule weekly reports every Monday at 9:00 AM
    schedule.every().monday.at("09:00").do(weekly_client_update)
    
    # Schedule daily meeting reminders at 8:00 AM
    schedule.every().day.at("08:00").do(daily_meeting_reminders)
    
    print("\nScheduled Tasks:")
    print("- Weekly client updates: Every Monday at 9:00 AM")
    print("- Daily meeting reminders: Every day at 8:00 AM")
    print("\n✓ Scheduler is running... (Press Ctrl+C to stop)\n")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n\n✓ Scheduler stopped.")

def view_log():
    print(f"\n{'='*60}")
    print("EMAIL LOG")
    print(f"{'='*60}\n")
    try:
        with open("business_email_log.txt", "r", encoding="utf-8") as log_file:
            logs = log_file.read()
            if logs:
                print(logs)
            else:
                print("No logs yet.")
    except FileNotFoundError:
        print("No log file found. Send some emails first!")

# ==================== MAIN PROGRAM ====================
def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == "1":
            send_single_business_email()
        elif choice == "2":
            create_sample_csv()
        elif choice == "3":
            filename = input("Enter CSV filename (or press Enter for 'recipients.csv'): ") or "recipients.csv"
            company_name = input("Enter company name (or press Enter for 'Your Company'): ") or "Your Company"
            send_batch_from_csv(filename, company_name)
        elif choice == "4":
            start_scheduler()
        elif choice == "5":
            view_templates()
        elif choice == "6":
            view_log()
        elif choice == "7":
            print("\n✓ Exiting Business Email Automation System. Goodbye!")
            break
        else:
            print("\n✗ Invalid choice! Please enter 1-7.")

# ==================== START ====================
if __name__ == "__main__":
    print(f"\n{'='*60}")
    print("WELCOME TO BUSINESS EMAIL AUTOMATION SYSTEM")
    print(f"{'='*60}")
    main()
