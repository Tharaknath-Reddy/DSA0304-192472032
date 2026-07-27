"""
Q2. Product Search System using Regular Expressions

This program performs exact, prefix, suffix, partial, and case-insensitive
searches on product names and generates a match-count report.
"""

import re


def search_products(products: list[str], keyword: str, search_type: str) -> dict[str, object]:
    escaped_keyword = re.escape(keyword)

    regex_patterns = {
        "exact": rf"^{escaped_keyword}$",
        "prefix": rf"^{escaped_keyword}",
        "suffix": rf"{escaped_keyword}$",
        "partial": rf"{escaped_keyword}",
        "case_insensitive": rf"{escaped_keyword}",
    }

    if search_type not in regex_patterns:
        raise ValueError("Invalid search type.")

    flags = re.IGNORECASE if search_type == "case_insensitive" else 0
    pattern = re.compile(regex_patterns[search_type], flags)
    matches = [product for product in products if pattern.search(product)]

    return {
        "search_type": search_type,
        "keyword": keyword,
        "matching_products": matches,
        "total_matches": len(matches),
    }


def display_search_report(report: dict[str, object]) -> None:
    print("-" * 60)
    print(f"Search Type      : {report['search_type']}")
    print(f"Keyword          : {report['keyword']}")
    print(f"Total Matches    : {report['total_matches']}")
    print("Matching Products:")
    if report["matching_products"]:
        for product in report["matching_products"]:
            print(f"  - {product}")
    else:
        print("  No matching products found.")


def main() -> None:
    products = [
        "Python Programming Book",
        "Wireless Mouse",
        "Gaming Mouse",
        "Bluetooth Speaker",
        "SQL Handbook",
        "Machine Learning Course",
        "Laptop Stand",
        "mouse pad",
    ]

    searches = [
        ("Wireless Mouse", "exact"),
        ("Lap", "prefix"),
        ("Mouse", "suffix"),
        ("Book", "partial"),
        ("mouse", "case_insensitive"),
        ("Camera", "partial"),
    ]

    print("PRODUCT SEARCH SYSTEM REPORT")
    for keyword, search_type in searches:
        report = search_products(products, keyword, search_type)
        display_search_report(report)


if __name__ == "__main__":
    main()
