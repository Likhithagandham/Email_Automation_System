import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from datetime import datetime
import json

# ==================== CONFIGURATION ====================
sender_email = "your_email@gmail.com"  # Replace with your Gmail
sender_password = "your_app_password_here"  # Replace with your app password

# ==================== EMAIL SENDING FUNCTION ====================
def send_email(receiver_email, receiver_name, custom_message, email_subject):
    """
    Sends a personalized email to a recipient
    Returns: True if successful, False if failed
    """
    
    body = f"""
    Hello {receiver_name},
    
    {custom_message}
    
    Best regards,
    Automated Email System
    """
    
    # Create email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = email_subject
    message.attach(MIMEText(body, "plain"))
    
    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send email
        server.send_message(message)
        server.quit()
        
        # Log success
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"✓ [{current_time}] SUCCESS: Email sent to {receiver_name} ({receiver_email})"
        print(log_message)
        save_log(log_message)
        return True
        
    except Exception as e:
        # Log failure
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"✗ [{current_time}] FAILED: Email to {receiver_name} ({receiver_email}) - Error: {e}"
        print(log_message)
        save_log(log_message)
        return False

# ==================== LOGGING FUNCTION ====================
def save_log(message):
    """Saves log messages to a file"""
    with open("email_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")

# ==================== BATCH EMAIL FUNCTION ====================
def send_batch_emails(recipients_list):
    """
    Sends emails to multiple recipients at once
    recipients_list: List of dictionaries with email, name, message, subject
    """
    print("\n" + "="*50)
    print("BATCH EMAIL SENDING STARTED")
    print("="*50 + "\n")
    
    success_count = 0
    fail_count = 0
    
    for recipient in recipients_list:
        result = send_email(
            recipient["email"],
            recipient["name"],
            recipient["message"],
            recipient["subject"]
        )
        
        if result:
            success_count += 1
        else:
            fail_count += 1
        
        time.sleep(2)  # Wait 2 seconds between emails to avoid spam detection
    
    # Print summary
    print("\n" + "="*50)
    print("BATCH SENDING SUMMARY")
    print("="*50)
    print(f"Total emails attempted: {success_count + fail_count}")
    print(f"Successfully sent: {success_count}")
    print(f"Failed: {fail_count}")
    print("="*50 + "\n")

# ==================== SCHEDULED EMAIL TASKS ====================
def scheduled_task_1():
    """Morning greeting email"""
    send_email(
        "likhithakrishna19@gmail.com",
        "John",
        "Good morning! This is your scheduled morning email.",
        "Morning Greeting"
    )

def scheduled_task_2():
    """Afternoon reminder email"""
    send_email(
        "likhithakrishna19@gmail.com",
        "Sarah",
        "This is your scheduled afternoon reminder.",
        "Afternoon Reminder"
    )

def scheduled_task_3():
    """Evening report email"""
    send_email(
        "likhithakrishna19@gmail.com",
        "Mike",
        "This is your scheduled evening report.",
        "Evening Report"
    )

# ==================== MAIN MENU ====================
def show_menu():
    """Displays the main menu"""
    print("\n" + "="*50)
    print("EMAIL AUTOMATION SYSTEM")
    print("="*50)
    print("1. Send a single email now")
    print("2. Send batch emails to multiple recipients")
    print("3. Start scheduled email service")
    print("4. View email log")
    print("5. Exit")
    print("="*50)

def send_single_email():
    """Interactive function to send a single email"""
    print("\n--- Send Single Email ---")
    receiver_email = input("Enter recipient email: ")
    receiver_name = input("Enter recipient name: ")
    subject = input("Enter email subject: ")
    message = input("Enter email message: ")
    
    send_email(receiver_email, receiver_name, message, subject)

def send_batch():
    """Interactive function to send batch emails"""
    print("\n--- Send Batch Emails ---")
    
    # Example recipients (you can customize this)
    recipients = [
        {
            "email": "likhithakrishna19@gmail.com",
            "name": "John",
            "message": "Thank you for being a valued client!",
            "subject": "Thank You"
        },
        {
            "email": "likhithakrishna19@gmail.com",
            "name": "Sarah",
            "message": "We appreciate your partnership!",
            "subject": "Partnership Appreciation"
        },
        {
            "email": "likhithakrishna19@gmail.com",
            "name": "Mike",
            "message": "Looking forward to our next meeting!",
            "subject": "Meeting Follow-up"
        }
    ]
    
    send_batch_emails(recipients)

def start_scheduler():
    """Starts the email scheduler"""
    print("\n--- Starting Email Scheduler ---")
    
    # Schedule emails (customize times as needed)
    schedule.every().day.at("01:05").do(scheduled_task_1)  
    schedule.every().day.at("01:05").do(scheduled_task_2)  
    schedule.every().day.at("01:05").do(scheduled_task_3)  
    
    print("\nScheduled emails:")
    print("- Task 1: Every day at 01:05 AM")
    print("- Task 2: Every day at 01:05 AM")
    print("- Task 3: Every day at 01:05 AM")
    print("\nScheduler is running... (Press Ctrl+C to stop)")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n\nScheduler stopped.")

def view_log():
    """Displays the email log"""
    print("\n--- Email Log ---")
    try:
        with open("email_log.txt", "r") as log_file:
            logs = log_file.read()
            if logs:
                print(logs)
            else:
                print("No logs yet.")
    except FileNotFoundError:
        print("No log file found. Send some emails first!")

# ==================== MAIN PROGRAM ====================
def main():
    """Main program loop"""
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            send_single_email()
        elif choice == "2":
            send_batch()
        elif choice == "3":
            start_scheduler()
        elif choice == "4":
            view_log()
        elif choice == "5":
            print("\nExiting Email Automation System. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter 1-5.")

# ==================== START THE PROGRAM ====================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("WELCOME TO EMAIL AUTOMATION SYSTEM")
    print("="*50)
    main()
