"""
Q3. University Registration Validation using Regular Expressions

This program validates student registration details and generates
a final registration status report.
"""

import re


def validate_register_number(register_number: str) -> tuple[bool, str]:
    pattern = re.compile(r"^21[A-Z]{3}\d{4}$")
    if pattern.fullmatch(register_number):
        return True, "Valid register number."
    return False, "Invalid register number. Expected format: 21AID1234."


def validate_institutional_email(email: str) -> tuple[bool, str]:
    pattern = re.compile(r"^[a-z][a-z0-9._-]*@saveetha\.ac\.in$", re.IGNORECASE)
    if pattern.fullmatch(email):
        return True, "Valid institutional email address."
    return False, "Invalid email. Use institutional domain: saveetha.ac.in."


def validate_course_code(course_code: str) -> tuple[bool, str]:
    pattern = re.compile(r"^[A-Z]{3}\d{2}$")
    if pattern.fullmatch(course_code):
        return True, "Valid course code."
    return False, "Invalid course code. Expected format: DSA03."


def validate_semester(semester: str) -> tuple[bool, str]:
    pattern = re.compile(r"^(?:Sem(?:ester)?[-\s]?)?[1-8]$", re.IGNORECASE)
    if pattern.fullmatch(semester):
        return True, "Valid semester information."
    return False, "Invalid semester. Enter a semester from 1 to 8."


def validate_mobile_number(mobile_number: str) -> tuple[bool, str]:
    pattern = re.compile(r"^(?:\+91[-\s]?)?[6-9]\d{9}$")
    if pattern.fullmatch(mobile_number):
        return True, "Valid mobile number."
    return False, "Invalid mobile number. Enter a valid Indian mobile number."


def validate_registration(student: dict[str, str]) -> dict[str, object]:
    field_results = {
        "Register Number": validate_register_number(student["register_number"]),
        "Institutional Email": validate_institutional_email(student["email"]),
        "Course Code": validate_course_code(student["course_code"]),
        "Semester": validate_semester(student["semester"]),
        "Mobile Number": validate_mobile_number(student["mobile_number"]),
    }

    registration_successful = all(result[0] for result in field_results.values())
    return {
        "student_name": student["name"],
        "field_results": field_results,
        "registration_successful": registration_successful,
    }


def display_registration_report(report: dict[str, object]) -> None:
    print("-" * 60)
    print(f"Student Name: {report['student_name']}")
    for field, result in report["field_results"].items():
        is_valid, message = result
        print(f"{field:20}: {'Valid' if is_valid else 'Invalid'} - {message}")

    status = "Successful" if report["registration_successful"] else "Unsuccessful"
    print(f"Final Registration Status: {status}")


def main() -> None:
    students = [
        {
            "name": "Ananya Sharma",
            "register_number": "21AID1234",
            "email": "ananya123@saveetha.ac.in",
            "course_code": "DSA03",
            "semester": "Semester 5",
            "mobile_number": "+91 9876543210",
        },
        {
            "name": "Rahul Menon",
            "register_number": "AID1234",
            "email": "rahul@gmail.com",
            "course_code": "DSA3",
            "semester": "Semester 10",
            "mobile_number": "1234567890",
        },
    ]

    print("UNIVERSITY REGISTRATION VALIDATION REPORT")
    for student in students:
        report = validate_registration(student)
        display_registration_report(report)


if __name__ == "__main__":
    main()
