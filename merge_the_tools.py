def remove_all_duplicates(s):
    result = ""
    for i in range(len(s)):
        if s[i] not in result:
            result += s[i]
    return result

def merge_the_tools(string, k):
    parts_of_string = []
    for i in range(0,len(string),k ):
        string_to_append = string[i:i+k]
        string_to_append = remove_all_duplicates(string_to_append)
        parts_of_string.append(string_to_append)
    for string in parts_of_string:
        print(string )

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)