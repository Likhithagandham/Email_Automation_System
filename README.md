# 📧 Email Automation System

A comprehensive Python-based email automation system designed to streamline business communication and save time on routine email tasks.

## 🚀 Features

- ✅ **Single Email Sending**: Send personalized emails to individual recipients
- ✅ **Batch Email Processing**: Send emails to multiple recipients from CSV files
- ✅ **Email Scheduling**: Automate email delivery at specific times and dates
- ✅ **Business Templates**: Pre-built templates for common business communications
- ✅ **Error Handling**: Comprehensive error catching and logging
- ✅ **Email Logging**: Track all sent emails with timestamps and status

## 📋 Project Objectives

This project was developed to:
1. Automate routine email communications for businesses
2. Provide customizable email templates for different purposes
3. Schedule emails for future delivery
4. Reduce time spent on repetitive email tasks
5. Maintain logs of all email activities

## 🛠️ Technologies Used

- **Python 3.x**
- **smtplib** - For SMTP email sending
- **email.mime** - For email formatting
- **schedule** - For email scheduling
- **csv** - For batch processing from CSV files

## 📦 Installation

### Prerequisites
- Python 3.8 or higher installed
- Gmail account with 2-Step Verification enabled
- Gmail App Password generated

### Setup Steps

1. **Download the project files**

2. **Create a virtual environment:**
```bash
   python -m venv venv
```

3. **Activate the virtual environment:**
   - **Windows:**
```bash
     venv\Scripts\activate
```
   - **Mac/Linux:**
```bash
     source venv/bin/activate
```

4. **Install required packages:**
```bash
   pip install schedule
```

5. **Configure your Gmail credentials:**
   - Open the Python files in a text editor
   - Replace `your_email@gmail.com` with your Gmail address
   - Replace `your_app_password_here` with your Gmail App Password

### 🔑 Getting Gmail App Password

1. Go to https://myaccount.google.com/
2. Click **Security** → Enable **2-Step Verification** (if not enabled)
3. Go back to Security → **2-Step Verification** → **App passwords**
4. Select **Mail** for app and **Other** for device
5. Generate password and **save it securely**
6. Use this password in the Python scripts

## 📖 Usage

### Basic Email Automation System
```bash
python email_automation_system.py
```

**Menu Options:**
1. Send a single email now
2. Send batch emails to multiple recipients
3. Start scheduled email service
4. View email log
5. Exit

### Business Email Automation System
```bash
python business_email_automation.py
```

**Additional Features:**
- Professional email templates (Client Follow-up, Weekly Report, Meeting Reminder, Thank You, Project Update)
- CSV batch processing
- Advanced scheduling options
- Business-focused communications

## 📧 Email Templates Available

| Template | Purpose | Use Case |
|----------|---------|----------|
| Client Follow-up | Post-meeting communications | After client meetings |
| Weekly Report | Regular status updates | Weekly team updates |
| Meeting Reminder | Upcoming meeting notifications | Day before meetings |
| Thank You | Appreciation emails | Client appreciation |
| Project Update | Project status communications | Project milestones |

## 📂 CSV Format for Batch Sending

Create a CSV file with this format:
```csv
email,name,template_type,custom_message
client@example.com,John Smith,client_followup,Discussed Q4 objectives and timeline
partner@example.com,Sarah Johnson,weekly_report,All projects are on track this week
team@example.com,Mike Davis,meeting_reminder,Project kickoff meeting at 2 PM
```

**To generate a sample CSV:**
- Run the business automation system
- Select option 2: "Create sample CSV file"

## 🔒 Security Best Practices

- ⚠️ **Never share your app password publicly**
- ✅ Use environment variables for credentials in production
- ✅ Keep 2-Step Verification enabled
- ✅ Regularly rotate app passwords
- ✅ Don't commit credentials to version control

## 📊 Project Structure
```
email-automation-system/
│
├── email_automation_system.py      # Basic automation system
├── business_email_automation.py    # Business-focused system with templates
├── recipients.csv                  # Sample recipient data (generated)
├── email_log.txt                   # Log file (auto-generated)
├── business_email_log.txt          # Business log file (auto-generated)
└── README.md                       # Documentation
```

## ⚠️ Troubleshooting

### Common Issues:

**1. "ModuleNotFoundError: No module named 'schedule'"**
```bash
pip install schedule
```

**2. "Authentication failed" error:**
- Verify 2-Step Verification is enabled on Gmail
- Generate a new app password
- Double-check email and password in code

**3. "Connection refused" error:**
- Check internet connection
- Verify firewall isn't blocking port 587
- Confirm using smtp.gmail.com:587

**4. Unicode/Encoding errors on Windows:**
- All files use UTF-8 encoding
- Logging functions include `encoding="utf-8"`

**5. Emails going to spam:**
- Add delay between batch emails (already implemented)
- Verify sender email reputation
- Ask recipients to whitelist your email

## 🎯 Project Requirements Met

✅ **Objective 1:** Developed Python script for automated email sending using smtplib  
✅ **Objective 2:** Customized email content based on recipient and purpose with templates  
✅ **Objective 3:** Scheduled emails for specific dates and times using schedule library  
✅ **Goal 1:** Successfully sends customized emails to 3+ recipients  
✅ **Goal 2:** Implemented scheduling functionality for future delivery  
✅ **Goal 3:** Error handling and logging for failed deliveries  
✅ **Scope:** Complete documentation and usage instructions  

## 🔧 Technical Implementation

### Core Technologies:
- **SMTP Protocol**: Uses Gmail's SMTP server (smtp.gmail.com:587)
- **TLS Encryption**: Secure email transmission with starttls()
- **MIME**: Multi-purpose email formatting for headers and body
- **Schedule Library**: Cron-like job scheduling for Python
- **CSV Processing**: Bulk email handling from structured data

### Key Functions:
- `send_email()` - Core email sending with error handling
- `send_batch_emails()` - Multiple recipient processing
- `save_log()` - Transaction logging with timestamps
- `load_recipients_from_csv()` - CSV data import
- Schedule tasks - Automated time-based sending

## 📈 Future Enhancements

Potential improvements:
- [ ] HTML email support with attachments
- [ ] Email tracking and open rates
- [ ] Integration with CRM systems
- [ ] More advanced scheduling (monthly, quarterly)
- [ ] Email template builder interface
- [ ] Dashboard for analytics
- [ ] Support for other email providers

## 👨‍💻 Author

**Likhitha**
- Project: Email Automation System
- Purpose: Academic/Professional Development

## 🙏 Acknowledgments

- Python smtplib documentation
- Schedule library by Dan Bader
- Gmail SMTP service
- Python community

## 📞 Support

For questions or issues:
1. Review the Troubleshooting section above
2. Check that all prerequisites are met
3. Verify Gmail app password is correctly configured

---

## 📄 License

This project is available for educational and personal use.
