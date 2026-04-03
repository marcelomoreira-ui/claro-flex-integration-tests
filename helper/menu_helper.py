from typing import List, Dict

# Extracting section IDs
def get_section_ids(response_json: dict) -> list:
    sections = response_json.get("content", {}).get("sections", [])
    return [section.get("id") for section in sections]

# Assertion helper to check if expected sections are present in the actual sections list
def assert_sections_present(actual_sections: list, expected_sections: list):

    missing_sections = [section for section in expected_sections if section not in actual_sections]

    assert not missing_sections, (
        f"Missing sections: {missing_sections}"
        f"Available sections: {actual_sections}")