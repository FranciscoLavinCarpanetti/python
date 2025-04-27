text = "aajrjrjjrjrjrjrjrjrj"

def check_is_balanced(text: str) -> bool:
    text = text.lower()
    count_r = text.count("r")
    count_j = text.count("j")
    print(f"Count of 'r': {count_r}, Count of 'j': {count_j}")
    return count_r == count_j

is_balanced = check_is_balanced(text)
print(f"Is the text balanced? {is_balanced}")