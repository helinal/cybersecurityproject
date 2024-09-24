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
To fix the flaw, the only thing we have to do is add CSRF tags ({% csrf_token %}) to all forms of this application (logging in, registering, creating new polls and voting). In the links above the tags are already added, as Django has built-in CSRF defences by default and the app will not run without them.

## Flaw 2 - Broken Access Control

### Locations

### Description

### How to fix

## Flaw 3 -

## Flaw 4 -

## Flaw 5 -
