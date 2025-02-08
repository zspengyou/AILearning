from utl import get_column_values

current_path = "/Users/JayZhou/PycharmProjects/AILearning/veeva/"

case_fields = set(get_column_values(current_path + "case_version__v.html", 2))
subject_fields = get_column_values(current_path + "cdms_subject_information__v.html", 2)
subject_fields.sort()


def find_match_nonMatchName() -> tuple[list,list]:
    matched = []
    not_matched = []
    for subject_field in subject_fields:
        if subject_field in case_fields:
            matched.append(subject_field)
        else:
            not_matched.append(subject_field)
    return matched,not_matched



matched: list
non_matched: list
matched, non_matched = find_match_nonMatchName()


def print_field_name_with_without_vc(field_names: list):
    field_name_without_cv = []
    for field in field_names:
        if field.endswith("__c") or field.endswith("__v"):
            field_name_without_cv.append(field[:-3])
        else:
            field_name_without_cv.append(field)
    for field in field_name_without_cv:
        print(field)
    print(field_names)
    print(len(field_names))
print("===================matched:")
print_field_name_with_without_vc(matched)
print("===================not matched:")
print_field_name_with_without_vc(non_matched)


