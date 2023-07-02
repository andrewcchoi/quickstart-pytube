import os

email_host = os.environ.get("EMAIL_HOST", None)
email_port = os.environ.get("EMAIL_PORT", None)
email_sender = os.environ.get("EMAIL_SENDER", None)
email_distribution = os.environ.get("EMAIL_DISTRIBUTION", None)
email_user = os.environ.get("EMAIL_USER", None)
email_password = os.environ.get("EMAIL_PASSWORD", None)