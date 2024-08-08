from plyer import notification

# Create a notification
notification.notify(
    title='Task Complete!',
    message='Your task has been successfully completed.',
    app_name='Zohaib Portfolio',  # Change the app name here
    timeout=10  # The notification will disappear after 10 seconds
)
