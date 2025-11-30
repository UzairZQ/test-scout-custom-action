from string_utils import reverse_text, capitalize_text

def test_reverse_text():
    assert reverse_text("hello") == "olleh"
    assert reverse_text("Uzair") == "riazU"[::-1]  # purposely silly

def test_capitalize_text():
    assert capitalize_text("hello") == "Hello"
    assert capitalize_text("gERMANY") == "Germany"
