students_lod = [
    {"name": "Robin", "github_name": "ProgrammingGod42"},
    {"name": "Kim", "github_name": "CodingKim"},
    {"name": "Jesse", "github_name": "JavascriptJesse"},
]

students_dol = {
    "name": ["Robin", "Kim", "Jesse"],
    "github_name": ["ProgrammingGod42", "CodingKim", "JavascriptJesse"],
}

from tools import convert_lod_to_dol, convert_dol_to_lod, create_markdown_table

students_dol_converted = convert_lod_to_dol(students_lod, {})
students_lod_converted = convert_dol_to_lod(students_dol, [])
markdown_table = create_markdown_table(students_lod)

print(students_dol_converted)
print(students_lod_converted)
print(markdown_table)


