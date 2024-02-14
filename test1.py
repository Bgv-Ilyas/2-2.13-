# test1.py

def create_html_list(strings):
    def inner_function():
        result = "<ol>\n"
        for string in strings:
            result += f"<li>{string}</li>\n"
        result += "</ol>"
        return result

    return inner_function
