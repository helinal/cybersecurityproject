# Cyber Security Base 2024, project I

## Flaw 1 - Cross Site Request Forgery

### Locations

https://github.com/helinal/cybersecurityproject/blob/b89aa8900b0f3748bc106cce46b2bdef86451cce/mysite/polls/templates/polls/detail.html#L9
https://github.com/helinal/cybersecurityproject/blob/b89aa8900b0f3748bc106cce46b2bdef86451cce/mysite/polls/templates/polls/add.html#L7
https://github.com/helinal/cybersecurityproject/blob/d863ed17413b0de3121df8eb52608f8800fb13ce/mysite/polls/templates/polls/login.html#L3
https://github.com/helinal/cybersecurityproject/blob/d863ed17413b0de3121df8eb52608f8800fb13ce/mysite/polls/templates/polls/register.html#L3

### Description

Cross-site Request Forgery (or CSRF) is an attack where an attacker tricks the user into performing actions on a website without their knowledge. The attacker's goal is to trick the user into submitting malicious web requests to a website that the user has priviledged access to. 
The malicious request can contain, for example, URL parameters, cookies or other data that apper normal to the target web application. Web applications are at risk if they act on input from trusted users without additional authorization. An authenticated user could unintentionally send a request to a trusted site, causing unwanted actions due to the user's trusted cookie in their browser.

### How to fix

To fix the flaw, all we have to do is add CSRF tags ({% csrf_token %}) to all forms of this application (logging in, registering, creating new polls and voting). In the links above the tags are already added, as Django has built-in CSRF defences by default and the app will not run without them.


## Flaw 2 - Broken Access Control

### Locations

https://github.com/helinal/cybersecurityproject/blob/fb569c2bfd3dd58b4d821beedc094606162f605f/mysite/polls/views.py#L43
https://github.com/helinal/cybersecurityproject/blob/fb569c2bfd3dd58b4d821beedc094606162f605f/mysite/polls/views.py#L58

### Description

Broken access control occurs when users can access data or perform actions outside their intended permissions. This could involve accessing or modifying unauthorized resources by altering urls, viewing  another user's data or bypassing authentication checks entirely. These problems can arise when when proper restrictions on what users can do or see are not enforced properly. Prevention methods could include enforcing strict user permissions and checking user privileges consistently, for example.

### How to fix

In this app, it is intended that only users that are logged in would be able to vote or add new polls. However, currently anyone can access the */add/* endpoint to create a poll, for example.
Luckily, Django has a built-in user authentication to restrict access to certain endpoints. In the views.py file (locations linked above), the *@loginrequired* decorator should be added before the *vote* and *add* functions.


## Flaw 3 - Injection (XSS)

### Location

https://github.com/helinal/cybersecurityproject/blob/d1b389255673ae3eb5682763ff20780ba063d554/mysite/polls/templates/polls/detail.html#L4

### Description

Injection can occur when an application processes user data in a way that allows attackers to manipulate the application's behaviour. This often happens when the data is directly used in commands or queries without proper validation, sanitization or filtering. The most common injection "types" include SQL injection, Cross-site Scripting (XSS) and External Control of File Name or Path. For example, in SQL injection, malicious inputs are able to alter database queries, leading to unauthorized data access and/or modification. To prevent different types of injection, coders should use safe APIs with parameterized queries (like Django) and validate inputs on the server side, for example.

### How to fix

In this case, the app is vulnerable to XSS (Cross-Site Scripting). At the app's current state, a user could add a new poll question with malicious content as *question_text* (like a Javascript script, for example) which would then be executed by the browser instead of rendering it as plain text. Currently, in detail.html, the *question_text* is displayed with *{{ question.question_text|safe }}*. We can make the code secure from XSS by just removing the *|safe* filter, like so: *{{ question.question_text }}*. One should avoid using the *|safe* filter alogether unless one is 100% certain that the content is sanitized and safe to render.


## Flaw 4 -

### Location


### Description


### How to fix



## Flaw 5 -

### Location


### Description


### How to fix


