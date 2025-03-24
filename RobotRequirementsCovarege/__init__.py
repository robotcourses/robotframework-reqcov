import csv
import os
import sys
from datetime import datetime
from .coverage_template import REPORT_HTML
from robot.libraries.BuiltIn import BuiltIn

class RobotRequirementsCovarege:

    ROBOT_LISTENER_API_VERSION = 3
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '1.2.0'

    def __init__(self, requirements_file, min_coverage=0, output_dir=None):
        """
            Load the CSV file with the list of requirements
        """

        self.total_requirements = {}
        self.requirements_file = requirements_file
        self.output_dir = output_dir
        self.min_coverage = float(min_coverage)

        with open(self.requirements_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)    # Skip CSV header
            for row in reader:
                self.total_requirements[row[0]] = {
                    "description": row[1],
                    "tests": 0,  # Initially, no test covers this requirement
                }

        self.tested_requirements = set()  # Requirements covered by tests

        self.reset_color = "\033[0m"
        self.status_color = {
            "PASS": "\033[92m",  # Green
            "FAIL": "\033[91m"   # Red
        }

    def start_test(self, name, attrs):
        """
            Captures tested requirements (tags starting with 'REQ')
        """

        if self.output_dir is None:
            self.output_dir = BuiltIn().get_variable_value("${OUTPUT DIR}")
        else:
            os.makedirs(self.output_dir, exist_ok=True)

        tags = set(attrs.tags)

        for tag in tags:
            if tag in tags:
                self.tested_requirements.add(tag)
                self.total_requirements[tag]["tests"] += 1  # Increment test counter

    def end_suite(self, name, attrs):
        """
            At the end of the execution of each test suite, calculate the coverage
        """

        self.total = len(self.total_requirements)
        self.tested = len(self.tested_requirements)
        self.coverage = (self.tested / self.total) * 100 if self.total > 0 else 0
        self.not_coverage = 100-self.coverage

        if self.min_coverage > 0:
            if self.coverage < self.min_coverage:
                self.status = "FAIL"
            else:
                self.status = "PASS"

    def close(self):
        """
            Displays the analysis result in the console
        """
        
        LINE_WIDTH = 78
        if self.min_coverage > 0:
            status_plain = f"| {self.status} |"
            status_colored = f"{self.status_color[self.status]}{self.status}{self.reset_color}"
        
        print("=" * LINE_WIDTH)
        print("Requirements Coverage Result")
        print("=" * LINE_WIDTH)

        if self.min_coverage > 0:
            print(F"Minimum requirement coverage: {self.min_coverage}%")
        else:
            print("No minimum requirement coverage value was defined")
        
        coverage_text = f"Requirements coverage: {self.tested}/{self.total} ({self.coverage:.2f}%)"

        if self.min_coverage > 0:
            padding_size = LINE_WIDTH - len(coverage_text) - len(status_plain)
            print(coverage_text + " " * padding_size + "| " + status_colored + " |", flush=True)
        else:
            print(coverage_text, flush=True)

        print("-" * LINE_WIDTH)

        if self.tested < self.total:
            print("Requirements not covered:", flush=True)
            for req, data in self.total_requirements.items():
                if req not in self.tested_requirements:
                    print(f"{req}: {data['description']}", flush=True)
            print("-" * LINE_WIDTH)

        report_content = REPORT_HTML.replace("{coverage-percent}", f"{self.coverage:.2f}")
        report_content = report_content.replace("{not-covered-percent}", f"{self.not_coverage:.2f}")
        report_content = report_content.replace("{generated-date}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        report_content = report_content.replace("{project-name}", f"{(os.path.basename(os.getcwd())).title()}")
        
        if self.min_coverage > 0:
            report_content = report_content.replace("{status-class}", "pass" if self.status == "PASS" else "fail")
            report_content = report_content.replace("{min-coverage}", f"{self.min_coverage:.2f}%")
        else:
            report_content = report_content.replace("{status-class}", "pass")
            report_content = report_content.replace("{min-coverage}", "No minimum requirement coverage value was defined")

        requirements_table = ""
        for req, data in self.total_requirements.items():
            status_tested = "Yes" if req in self.tested_requirements else "No"
            covered_class = "covered-yes" if status_tested == "Yes" else "covered-no"
            requirements_table += f"""
                <tr>
                    <td>{req}</td>
                    <td>{data["description"]}</td>
                    <td class="{covered_class}">{status_tested}</td>
                    <td>{data["tests"]}</td>
                </tr>
                """
        
        report_content = report_content.replace("<!-- Rows will be dynamically inserted -->", requirements_table)
        
        html_path = os.path.join(self.output_dir, "coverage_report.html")
        with open(html_path, "w", encoding="utf-8") as report_file:
            report_file.write(report_content)
        
        print(f"Output Coverage: {html_path}", flush=True)
        print("=" * LINE_WIDTH)

        if self.min_coverage > 0:
            if self.status == 'FAIL':
                sys.exit(1)