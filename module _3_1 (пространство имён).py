calls=0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)

info = string_info("Capybara")
print(info)

exists = is_contains("urban", ["Urban", "City", "Town"])
print(exists)

another_info = string_info("Armageddon")
print(another_info)

not_exists = is_contains("test", ["check", "example"])
print(not_exists)

print("Количество вызовов функций:", calls)