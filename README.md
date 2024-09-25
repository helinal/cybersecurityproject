# Cyber Security Base 2024, project I

## Flaw 1 - Cross Site Request Forgery

### Locations

https://github.com/helinal/cybersecurityproject/blob/b89aa8900b0f3748bc106cce46b2bdef86451cce/mysite/polls/templates/polls/detail.html#L9
https://github.com/helinal/cybersecurityproject/blob/b89aa8900b0f3748bc106cce46b2bdef86451cce/mysite/polls/templates/polls/add.html#L7
https://github.com/helinal/cybersecurityproject/blob/d863ed17413b0de3121df8eb52608f8800fb13ce/mysite/polls/templates/polls/login.html#L3
https://github.com/helinal/cybersecurityproject/blob/0c8948b9bfa611fcc8a07173d84e438f810c82c0/mysite/polls/templates/polls/register.html#L3

### Description

Cross-site Request Forgery (or CSRF) is an attack where an attacker tricks the user into performing actions on a website without their knowledge. The attacker's goal is to trick the user into submitting malicious web requests to a website that the user has priviledged access to. 
The malicious request can contain, for example, URL parameters, cookies or other data that apper normal to the target web application. Web applications are at risk if they act on input from trusted users without additional authorization. An authenticated user could unintentionally send a request to a trusted site, causing unwanted actions due to the user's trusted cookie in their browser.

### How to fix

To fix the flaw in this app, all we have to do is add CSRF tags ({% csrf_token %}) to all forms of this application (logging in, registering, creating new polls and voting). The tags help the server to verify the requests: that they are legitimate and made by an authenticated user. In the links above the CSRF tags are already added, as Django has built-in CSRF defences by default and the app will not run without them.


## Flaw 2 - Broken Access Control

### Locations

https://github.com/helinal/cybersecurityproject/blob/0c8948b9bfa611fcc8a07173d84e438f810c82c0/mysite/polls/views.py#L67
https://github.com/helinal/cybersecurityproject/blob/0c8948b9bfa611fcc8a07173d84e438f810c82c0/mysite/polls/views.py#L82

### Description

Broken access control occurs when users can access data or perform actions outside their intended permissions. This could involve accessing or modifying unauthorized resources by altering urls, viewing  another user's data or bypassing authentication checks entirely. These problems can arise when when proper restrictions on what users can do or see are not enforced properly. Prevention methods could include enforcing strict user permissions and checking user privileges consistently, for example. In this app, it is intended that only users that are logged in would be able to vote or add new polls. However, currently anyone can access the */add/* endpoint to create a poll, for example.

### How to fix

The fix for this vulnerability is simple: Django has a built-in user authentication to restrict access to certain endpoints. In the views.py file (locations linked above), the *@loginrequired* decorator should be added before the *vote* and *add* functions.


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


## Flaw 5 -

### Location


### Description


### How to fix


