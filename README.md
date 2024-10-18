# Cyber Security Base 2024, project I

This app is a very simple polls app, created for the Cyber Security Base 2024 course by the University of Helsinki. The app has five different security flaws from the [OWASP 2021 Top Ten llst](https://owasp.org/www-project-top-ten/) ( + added CSRF).

*Do not use this app or parts of it anywhere as it's extremely unsecure!*

### Installation

1. Clone the project files to your desired location
2. To set up the database, run the commands below in the folder where *manage.py* is located
   
```
python manage.py makemigrations
python manage.py migrate
```

3. Finally, start the app with the command

```
python manage.py runserver
```


## Flaw 1 - Cross Site Request Forgery

### Location

https://github.com/helinal/cybersecurityproject/blob/3c4d8d9c200acb1e47602047a5bf59e60959d1ee/mysite/mysite/settings.py#L45

### Description

Cross-site Request Forgery (or CSRF) is an attack where the attacker tricks the user into performing actions on a website without their knowledge. The attacker's goal is to trick the user into submitting malicious web requests to a website that the user has priviledged access to. The malicious request can contain, for example, URL parameters, cookies or other data that appear normal to the target web application. Web applications are at risk if they act on input from trusted users without additional authorization. An authenticated user could unintentionally send a request to a trusted site, causing unwanted actions due to the user's trusted cookie in their browser. In this app, Django's built-in CSRF middleware that usually protects the app from CSRF attacks is disabled, making the app vulnerable.

### How to fix

To fix this flaw all we have to do is add the CSRF middleware back. This can be done in settings.py (in the location above) by adding *'django.middleware.csrf.CsrfViewMiddleware'* in MIDDLEWARE. Usually, this is enabled by default when coding with Django. *CSRFViewMiddleware*'s job is to validate POST requests to check if the contain a valid CSRF token - deleting it means that the backend doesn't validate CSRF tokens at all, allowing possible malicious requests.


## Flaw 2 - Broken Access Control

### Locations

https://github.com/helinal/cybersecurityproject/blob/0c8948b9bfa611fcc8a07173d84e438f810c82c0/mysite/polls/views.py#L67
https://github.com/helinal/cybersecurityproject/blob/0c8948b9bfa611fcc8a07173d84e438f810c82c0/mysite/polls/views.py#L82

### Description

Broken access control occurs when users can access data or perform actions outside their intended permissions. This could involve accessing or modifying unauthorized resources by altering urls, viewing  another user's data or bypassing authentication checks entirely. These problems can arise when when proper restrictions on what users can do or see are not enforced properly. Prevention methods include enforcing strict user permissions and checking user privileges consistently, for example. In this app, it is intended that only users that are logged in would be able to vote or add new polls. However, currently anyone can access the */add/* endpoint to create a poll, for example.

### How to fix

The fix for this vulnerability is simple: Django has a built-in user authentication to restrict access to certain endpoints. In the views.py file (locations linked above), the *@loginrequired* decorator should be added before the *vote* and *add* functions. By adding the decorator, only logged in users can access the */vote/* and */add/* endpoints.


## Flaw 3 - Injection (XSS)

### Location

https://github.com/helinal/cybersecurityproject/blob/d1b389255673ae3eb5682763ff20780ba063d554/mysite/polls/templates/polls/detail.html#L4

### Description

Injection can occur when an application processes user data in a way that allows attackers to manipulate the application's behaviour. This often happens when the data is directly used in commands or queries without proper validation, sanitization or filtering. The most common injection "types" include SQL injection, Cross-site Scripting (XSS) and External Control of File Name or Path. For example, in SQL injection, malicious inputs are able to alter database queries, leading to unauthorized data access and/or modification. To prevent different types of injection, coders should use safe APIs with parameterized queries (like Django) and validate inputs on the server side, for example. In this case, the app is vulnerable to XSS (Cross-Site Scripting). At the app's current state, a user could add a new poll question with malicious content as *question_text* (like a Javascript script) which would then be executed by the browser instead of rendering it as plain text.

### How to fix

Currently in detail.html, the *question_text* is displayed with the insecure *{{ question.question_text|safe }}*. We can make the code secure from XSS by just removing the *|safe* filter, like so: *{{ question.question_text }}*. One should avoid using the *|safe* filter alogether unless one is 100% certain that the content is sanitized and safe to render.


## Flaw 4 - Cryptographic Failure

### Location

https://github.com/helinal/cybersecurityproject/blob/0c8948b9bfa611fcc8a07173d84e438f810c82c0/mysite/polls/views.py#L34

### Description

Cryptographic Failures (previously known as Sensitive Data Exposure) refer to vulnerabilities that stem from insufficient protection of sensitive data such as passwords and credit card information. These vulnerabilities can lead to serious consequences, like indentity theft and financial fraud, for example. Common cryptrographic issues include using weak or outdated encryption methods, transmitting data as plain text or failing to encrypt sensitive data adequetly. 
There is a severe cryptographic failure in this app: when creating a new user, the application stores the created password as plain text by assigning the password directly to the *user.password* field without using Django's secure *set_password* method, for example. This, of course, is a significant security risk, as all the user passwords can be accessed in plain text if the database is compromised and also violates the best practices for data security.

### How to fix

Instead of storing passwords as plain text, one should always hash them. When using Django, for example, one could use the aforementioned *set_password* method or use Django's built-in form *UserCreationForm* that handles password validation and hashing automatically. In the linked location above, the secure version of the *register* method that uses *UserCreationForm* can be found below the insecure one. 


## Flaw 5 - Security Misconfiguration

### Location

https://github.com/helinal/cybersecurityproject/blob/3db799851ebc8c9863c8aac52c74f04dc7920a42/mysite/mysite/settings.py#L25

### Description

Security Misconfiguration refers to weaknesses in the configuration of an application's components or structure that can leave it vulnerable to attacks. This category is quite broad and includes issues like using outdated software libraries, not changing default passwords and poorly configured servers. In this case, in the Django's automatically generated *settings.py* file, the *DEBUG* variable is set to *True* by default. The debug mode is meant to be used just for development. If the app would now be deployed to production with these settings, this would count as a security misconfiguration issue.

### How to fix

The fix to the security misconfiguration mentioned above is simple. The only thing we have to do is to change *DEBUG = True* to *DEBUG = False* in the settings.py file (linked above). Setting the *DEBUG* as *False* helps preventing, for example, sensitive information leaking to unwanted users. This is because when *DEBUG* is set to *False*, Django displays detailed error essages that could include file paths, database queries and sensitive environment variables etc. When *DEBUG = False*, these diagnostics are not shown to the end user, reducing the risk of accidentally exposing sensitive data.

