

# 驼峰转下划线
def hump_turn_underline(filed):
    temp_name = ""
    lst = []
    for index, char in enumerate(filed):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)

    return "".join(lst).lower()


if __name__ == "__main__":
    print(hump_turn_underline("npi_test_project"))