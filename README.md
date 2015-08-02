cs_python_proj
==============

This README will detail instructions for how to run the tests.
The main parts of this project is that:
- we will try to load the landing page of every section of a web site
- page load times will be measured and stored in MySQL
- results will show as a history
- print out an executive summary

Assumptions
--------------

The following software is installed:
- Python 2.7
- Selenium Webdriver
- MySQL

You will also need to ensure python dependencies are installed:
```
pip install -r requirements.txt
```

Components of the history
--------------

The data measured per run will be:
- date and timestamp of run start
- date and timestamp of run end
- number of pages successfully loaded
- number of pages unsucessfully loaded
- page load time of each page

The pages to be measured will be:
- Company
  - Team
  - Board of Directors
  - Join our Team
  - News
  - Contact Us
- Products
  - Falcon Host
  - Falcon Intelligence
  - Falcon DNS
  - Crowdstrike as a Service
- Services
  - Incident Response
  - Proactive Services
- Resources
- CSIX
- See Demo
- Community Tools
- Blog

History will have three tables:
 1. mapping numerical page_keys to page_names as strings
 2. mapping page_keys to load_times in seconds
 3. mapping page_keys to load_status success or failure

Components of the executive report
--------------

We will want to show:
- number of pages successfully/unsuccessfully loaded of the current run
- min/median/average/max time to load each page of the current run
- median time to load over all previous runs stored in the database