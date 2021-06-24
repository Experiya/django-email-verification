
## Django-email-verify

Very simple and easy way to verify email address before authentication in Django.

## Demo

https://django-email-verify.herokuapp.com/

## Download the code and use it. Just simple idea how it works

- Create a temporary email
- Cnable less secure apps. This is the very important thing do do before moving before moving forward. 
- How to enable it ?? 
    
    * Open your gmail

    * Go to security option
    
    * Scroll down a bit. You will see an option for less secure app. just enable it. Nothing to wory about this.

settings.py

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = 'your password'
```

views.py

```python
def send_mail_to_verify(email,token):
  
  subject="Account verification"
  
  message=f"""to verify your account please click here -
  
  http://127.0.0.1:8000/verify/{token}"""
  
  email_from = settings.EMAIL_HOST_USER
  
  recipient_list=[email]
  
  send_mail(subject,message,email_from,recipient_list)
```
what to import in views.py
```bash
from django.core.mail import send_mail
```

Ths above fucntion ( you can named it anything).


*Soon i will write small notes how it works actually. You dont need use the whole django packages, you can simply use this fucntionality in normal python programm too.*
## Screenshots

![App Screenshot](https://github.com/Experiya/snapshot/blob/main/verify-email/Screenshot%20(521).png?raw=true)

![App Screenshot](https://github.com/Experiya/snapshot/blob/main/verify-email/Screenshot%20(523).png?raw=true)
![App Screenshot](https://github.com/Experiya/snapshot/blob/main/verify-email/Screenshot%20(516).png?raw=true)
![App Screenshot](https://github.com/Experiya/snapshot/blob/main/verify-email/Screenshot%20(517).png?raw=true)
![App Screenshot](https://github.com/Experiya/snapshot/blob/main/verify-email/Screenshot%20(518).png?raw=true)
![App Screenshot](https://github.com/Experiya/snapshot/blob/main/verify-email/Screenshot%20(519).png?raw=true)
![App Screenshot](https://github.com/Experiya/snapshot/blob/main/verify-email/Screenshot%20(520).png?raw=true)

