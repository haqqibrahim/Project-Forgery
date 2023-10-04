# PROJECT FORGERY
# An Automated CSRF Exploit Generator

A tool for generating Cross-Site Request Forgery (CSRF) exploit HTML for security testing.

## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Usage](#usage)

## Walkthrough Article
https://medium.com/@enessyibrahim/project-forgery-automating-csrf-exploit-generation-fd953ca8186a

## About

The CSRF Exploit Generator is a security testing tool designed to assist in the identification and testing of Cross-Site Request Forgery (CSRF) vulnerabilities in web applications. It simplifies the process of generating CSRF exploit HTML for both POST and GET requests.

### Why CSRF Exploit Generator?

Web applications are susceptible to CSRF attacks when they trust requests made by authenticated users without proper verification. To uncover these vulnerabilities, security professionals and developers often need to craft CSRF exploits. The CSRF Exploit Generator streamlines this process, making it easier to demonstrate and test the potential impact of CSRF vulnerabilities.

### Key Features

- **Automatic HTML Generation:** Quickly create CSRF exploit HTML for POST and GET requests.
- **Parameter Customization:** Customize parameter names and values to match your target application.
- **User-Friendly Interface:** The command-line tool provides an easy-to-use interface for generating exploits.

Whether you're a security researcher, penetration tester, or developer, the CSRF Exploit Generator is a valuable addition to your security testing toolkit.

## Installation

```bash
pip install -r requirements.txt
```
### Usage
```bash
python3 csrf_script.py
```
### POST Request Usage
![image](https://github.com/haqqibrahim/Project-Forgery/assets/68786496/8e914c02-4958-4b24-bc29-854fee7f6f9f)
### GET Request Usage
![image](https://github.com/haqqibrahim/Project-Forgery/assets/68786496/be0b067d-c562-4b6c-9ee4-a1507273f5ac)
### POST Request Exploit Script
![image](https://github.com/haqqibrahim/Project-Forgery/assets/68786496/dab09475-2d8c-4ee5-a5fc-d93d0f886906)
### GET Request Exploit Script
![image](https://github.com/haqqibrahim/Project-Forgery/assets/68786496/1908d023-231d-4275-a6c1-cc88b59bba9b)





