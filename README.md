# SeleniumMorningPeaceBot 🌞🤖

### Tired of accidentally starting family or girlfriend drama before you've had your coffee or while at work? Meet SeleniumMorningPeaceBot—your friendly, drama-avoiding, personal assistant! This bot wishes your family and friends a cheerful "Good Morning" so you don't have to—keeping your mornings peaceful and your group chats or personal chats free of accidental drama bombs.

### Because nothing says "I love you" quite like letting a bot do the talking 🌅😂

### Created using Python + Selenium (yes you heard that right the Testing Framework Selenium)

## Automate Message Sending

### Use a Scheduler:
##### Windows Task Scheduler: Schedule the script to run every day at a specific time.
##### Linux/Mac Cron Job: Use a cron job to run the script at a designated time.
##### Example Cron Job:
##### To edit the crontab file, type the following command in the terminal:
```bash
crontab -e
```
##### To send the message at 10:00 AM every day, add the following line to your crontab:
```bash
0 10 * * * /usr/bin/python3 /path/to/your/script.py >> /home/user/cron.log 2>&1
```
##### Overview of setting up a cron job 
```bash
* * * * * /path/to/command arg1 arg2
- - - - -
| | | | |
| | | | +----- Day of the week (0 - 7) (Sunday=0 or 7)
| | | +------- Month (1 - 12)
| | +--------- Day of the month (1 - 31)
| +----------- Hour (0 - 23)
+------------- Minute (0 - 59)
```
##### /usr/bin/python3 - path to your interpreter that you used to execute the script in the code editor 
##### >> /home/user/cron.log 2>&1 - helps you log standard output and error to cron.log 
##### After adding your cron job, save the file and exit the editor:
