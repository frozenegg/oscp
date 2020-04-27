#!/usr/bin/python

import scanner

target_url = "http://testphp.vulnweb.com/"
links_to_ignore = ["http://192.168.2.114/dvwa/logout.php"]
# data_dict = {"username": "admin", "password": "password", "Login": "submit"}

vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
# response = vuln_scanner.session.post("http://192.168.2.114/dvwa/login.php", data=data_dict)

vuln_scanner.crawl()

# forms = vuln_scanner.extract_forms(target_url)
# print(forms)

# response = vuln_scanner.submit_form(forms[0], "testtest", "[url]")
# print(response.content)

# response = vuln_scanner.test_xss_in_form(forms[0], "[url]")
# print(response)

vuln_scanner.run_scanner()
