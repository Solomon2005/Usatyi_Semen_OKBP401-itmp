import ast
import keyword
import re
import tokenize
from io import StringIO


# Задание 1
def get_name_style(name):
    name = name.strip("_")

    if re.fullmatch(r"[a-z][a-z0-9_]*", name):
        return "snake_case"
    if re.fullmatch(r"[A-Z][A-Z0-9_]*", name):
        return "UPPER_CASE"
    if re.fullmatch(r"[a-z][A-Za-z0-9]*[A-Z][A-Za-z0-9]*", name):
        return "camelCase"
    if re.fullmatch(r"[A-Z][A-Za-z0-9]*", name):
        return "PascalCase"

    return "unknown"


def check_naming_style(names):
    return {name: get_name_style(name) for name in names}


print("Задание 1")
print(check_naming_style(["my_var", "myVar", "MyClass", "MAX_SIZE", "bad-name"]))


# Задание 2
def is_valid_python_identifier(name, kind):
    styles = {
        "variable": "snake_case",
        "function": "snake_case",
        "class": "PascalCase",
        "constant": "UPPER_CASE"
    }

    if kind not in styles:
        return False

    return (
        name.isidentifier()
        and not keyword.iskeyword(name)
        and get_name_style(name) == styles[kind]
    )


print("Задание 2")
print(is_valid_python_identifier("my_name", "variable"))
print(is_valid_python_identifier("MyClass", "class"))


# Задание 3
def split_into_words(name):
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return name.lower().split("_")


def to_pep8_name(name, kind):
    words = [word for word in split_into_words(name) if word]

    if kind == "class":
        return "".join(word.capitalize() for word in words)
    if kind == "constant":
        return "_".join(words).upper()

    return "_".join(words)


print("Задание 3")
print(to_pep8_name("UserName", "variable"))
print(to_pep8_name("user_name", "class"))
print(to_pep8_name("userName", "constant"))


# Задание 4
def check_indentation(code, indent_size=4):
    result = []

    for number, line in enumerate(code.splitlines(), 1):
        if not line.strip():
            continue

        spaces = len(line) - len(line.lstrip(" "))
        tabs = len(line) - len(line.lstrip("\t"))

        if spaces and tabs:
            result.append(f"Строка {number}: смешаны пробелы и табы")
        elif spaces % indent_size != 0:
            result.append(
                f"Строка {number}: отступ {spaces} пробелов не кратен {indent_size}"
            )

    return result


print("Задание 4")
print(check_indentation("def f():\n   x = 1\n"))


# Задание 5
def find_magic_numbers(code):
    result = []

    for number, line in enumerate(code.splitlines(), 1):
        line = line.split("#")[0]

        for value in re.findall(r"(?<![A-Za-z_])-?\d+", line):
            number_value = int(value)

            if number_value not in (0, 1, -1):
                if not re.search(r"[A-Z][A-Z0-9_]*\s*=\s*" + re.escape(value), line):
                    result.append((number, number_value))

    return result


print("Задание 5")
print(find_magic_numbers("x = 5\ny = 0\nz = -7\n"))


# Задание 6
def extract_module_structure(code):
    tree = ast.parse(code)

    result = {
        "imports": [],
        "constants": [],
        "functions": [],
        "classes": []
    }

    for node in tree.body:
        if isinstance(node, ast.Import):
            result["imports"] += [item.name for item in node.names]

        elif isinstance(node, ast.ImportFrom):
            result["imports"].append(node.module or "")

        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            result["functions"].append(node.name)

        elif isinstance(node, ast.ClassDef):
            result["classes"].append(node.name)

        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and get_name_style(target.id) == "UPPER_CASE":
                    result["constants"].append(target.id)

    return result


print("Задание 6")
print(extract_module_structure(
    "import os\nMAX_SIZE = 10\ndef hello(): pass\nclass Test: pass"
))


# Задание 7
def check_docstrings(code):
    tree = ast.parse(code)
    result = {}

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            result[node.name] = ast.get_docstring(node) is not None

    return result


print("Задание 7")
print(check_docstrings(
    'def hello():\n    """Привет."""\n\ndef test():\n    pass'
))


# Задание 8
def generate_module_template(module_name, functions, classes):
    result = [f"# Модуль: {module_name}", ""]

    for name in functions:
        result += [
            f"def {name}():",
            f'    """Описание функции {name}."""',
            "    pass",
            ""
        ]

    for name in classes:
        result += [
            f"class {name}:",
            f'    """Описание класса {name}."""',
            "    pass",
            ""
        ]

    return "\n".join(result)


print("Задание 8")
print(generate_module_template("demo", ["load"], ["Parser"]))


# Задание 9
def add_main_guard(code, main_function="main"):
    if 'if __name__ == "__main__":' in code:
        return code

    return code.rstrip() + f'\n\nif __name__ == "__main__":\n    {main_function}()\n'


print("Задание 9")
print(add_main_guard("def main():\n    print('Hello')"))


# Задание 10
def line_length_stats(code, max_length=79):
    lines = code.splitlines()

    if not lines:
        return {
            "total_lines": 0,
            "lines_over_max": 0,
            "max_line_length": 0,
            "average_line_length": 0
        }

    lengths = [len(line) for line in lines]

    return {
        "total_lines": len(lines),
        "lines_over_max": sum(length > max_length for length in lengths),
        "max_line_length": max(lengths),
        "average_line_length": round(sum(lengths) / len(lengths), 2)
    }


print("Задание 10")
print(line_length_stats("hello\n" + "x" * 80))


# Задание 11
def check_imports_order(code):
    tree = ast.parse(code)
    result = []
    found_definition = False

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            found_definition = True

        elif found_definition and isinstance(node, (ast.Import, ast.ImportFrom)):
            result.append(f"Строка {node.lineno}: импорт стоит после определения")

    return result


print("Задание 11")
print(check_imports_order("import os\ndef test(): pass\nimport sys"))


# Задание 12
def max_nesting_level(code):
    max_level = 0

    for line in code.splitlines():
        if line.strip():
            spaces = len(line) - len(line.lstrip())
            max_level = max(max_level, spaces // 4)

    return max_level


print("Задание 12")
print(max_nesting_level(
    "def f():\n"
    "    for x in data:\n"
    "        if x:\n"
    "            print(x)"
))


# Задание 13
def fix_spaces_around_operators(line):
    line = re.sub(r"\s*(==|!=|<=|>=|//=|\*\*=|\+=|-=|\*=|/=|%=|=|\+|-|\*|/|%|<|>)\s*",
                  r" \1 ", line)
    line = re.sub(r"\s+", " ", line)
    return line.strip()


print("Задание 13")
print(fix_spaces_around_operators("x=a+b*2"))


# Задание 14
def analyze_comments(code):
    comments = sum(
        1 for token in tokenize.generate_tokens(StringIO(code).readline)
        if token.type == tokenize.COMMENT
    )

    docstrings = 0
    tree = ast.parse(code)

    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.ClassDef)):
            doc = ast.get_docstring(node, clean=False)
            if doc:
                docstrings += len(doc.splitlines())

    total_lines = len(code.splitlines())

    return {
        "total_comments": comments,
        "docstring_lines": docstrings,
        "comment_ratio": round(comments / total_lines, 3) if total_lines else 0
    }


print("Задание 14")
print(analyze_comments(
    '"""Модуль."""\n# комментарий\nx = 1  # ещё комментарий'
))


# Задание 15
def find_long_functions(code, max_lines=50):
    tree = ast.parse(code)
    result = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            lines = node.end_lineno - node.lineno + 1
            if lines > max_lines:
                result.append((node.name, lines))

    return result


print("Задание 15")
print(find_long_functions("def test():\n    x = 1\n    y = 2\n", max_lines=2))


# Задание 16
def normalize_blank_lines_between_functions(code):
    lines = code.splitlines()
    result = []

    for line in lines:
        if line.startswith(("def ", "class ")) and result:
            while result and not result[-1].strip():
                result.pop()
            result += ["", ""]

        result.append(line)

    return "\n".join(result) + "\n"


print("Задание 16")
print(normalize_blank_lines_between_functions(
    "x = 1\ndef first():\n    pass\ndef second():\n    pass"
))


# Задание 17
def simple_linter(code):
    messages = []

    messages += check_indentation(code)

    for number, line in enumerate(code.splitlines(), 1):
        if len(line) > 79:
            messages.append(f"Строка {number}: слишком длинная строка")

    try:
        tree = ast.parse(code)
    except SyntaxError as error:
        return [f"Строка {error.lineno}: синтаксическая ошибка"]

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if ast.get_docstring(node) is None:
                messages.append(f"Строка {node.lineno}: у функции нет docstring")

            if get_name_style(node.name) != "snake_case":
                messages.append(f"Строка {node.lineno}: имя функции не в snake_case")

    for line, number in find_magic_numbers(code):
        messages.append(f"Строка {line}: магическое число {number}")

    return messages


print("Задание 17")
bad_code = "def BadFunction(x):\n   return x * 100"
for message in simple_linter(bad_code):
    print(message)


# Задание 18
def style_report(code, module_name):
    stats = line_length_stats(code)
    structure = extract_module_structure(code)
    docs = check_docstrings(code)

    coverage = 100
    if docs:
        coverage = round(sum(docs.values()) / len(docs) * 100, 1)

    return (
        f"Module: {module_name}\n"
        f"Total lines: {stats['total_lines']}\n"
        f"Functions: {len(structure['functions'])}\n"
        f"Classes: {len(structure['classes'])}\n"
        f"Docstring coverage: {coverage}%\n"
        f"Lines over 79 chars: {stats['lines_over_max']}\n"
        f"Magic numbers found: {len(find_magic_numbers(code))}"
    )


print("Задание 18")
print(style_report(
    'def hello():\n    """Привет."""\n    return 42',
    "example"
))


# Задание 19
def refactor_bad_code(code):
    lines = []

    for line in code.splitlines():
        line = line.strip()
        if not line:
            lines.append("")
            continue

        line = re.sub(r"\b([A-Z][A-Za-z0-9]*)\b",
                      lambda m: split_into_words(m.group()).__str__(), line)

        line = line.replace(" ", " ")
        line = re.sub(r"\s*([=+*<>])\s*", r" \1 ", line)
        lines.append(line)

    return "\n".join(lines)


print("Задание 19")
print(refactor_bad_code(
    "def AreaIfLarge(w,h):\n  totalArea=w*h\n  return totalArea"
))


# Задание 20
def compare_module_versions(old_code, new_code):
    old = extract_module_structure(old_code)
    new = extract_module_structure(new_code)

    return {
        "added_functions": [x for x in new["functions"] if x not in old["functions"]],
        "removed_functions": [x for x in old["functions"] if x not in new["functions"]],
        "added_classes": [x for x in new["classes"] if x not in old["classes"]],
        "removed_classes": [x for x in old["classes"] if x not in new["classes"]]
    }


print("Задание 20")
old_code = "def load(): pass\nclass Parser: pass"
new_code = "def load(): pass\ndef export(): pass\nclass Report: pass"
print(compare_module_versions(old_code, new_code))
