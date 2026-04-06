from typing import List, Dict

# Extracting section IDs
def get_section_ids(response_json: dict) -> list:
    sections = response_json.get("content", {}).get("sections", [])
    return [section.get("id") for section in sections]

# Extracting items from the GENERAL section
def get_itens_from_general_section(response_json: dict) -> List[Dict]:
    sections = response_json.get("content", {}).get("sections", [])
    for section in sections:
        if section.get("id") == "GENERAL":
            return [item.get("action") for item in section.get("items", [])]
    return []

# Assertion helper to check if expected sections are present in the actual sections list
def assert_sections_present(actual_sections: list, expected_sections: list):

    missing_sections = [section for section in expected_sections if section not in actual_sections]

    assert not missing_sections, (
        f"Missing sections: {missing_sections}"
        f"Available sections: {actual_sections}")

# Assertion helper to check if unexpected sections are not present in the actual sections list
def assert_section_not_present(actual_sections: list, unexpected_sections: list):
    present_sections = [section for section in unexpected_sections if section in actual_sections]
    assert not present_sections, (
        f"Unexpected sections found: {present_sections}"
        f"Available sections: {actual_sections}"
    )

# Assertion helper to check if expected items are present in the actual items list
def assert_itens_present(actual_itens: list, expected_itens: list):
    missing_itens = [item for item in expected_itens if item not in actual_itens]
    assert not missing_itens, (
        f"Missing items: {missing_itens}"
        f"Available items: {actual_itens}")