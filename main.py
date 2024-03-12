def is_valid_parentheses(s: str) -> (bool, list):
    brackets = []
    check_brackets = {')': '(', '}': '{', ']': '['}
    mismatched_indices = []

    if len(s) == 1:
        if s[0] in ('(', ')'):
            return False, [0]
        return False, []

    if '(' not in s and ')' not in s:
        return False, []

    for i, symbol in enumerate(s):
        if symbol in ('(', ')'):
            mismatched_indices.append(i)
        # If the symbol is a closing bracket and there is a corresponding opening bracket in brackets, we remove it
        if symbol in check_brackets:
            if not brackets or brackets[-1] != check_brackets[symbol]:
                continue
            brackets.pop()
        # If the symbol is an opening bracket, we add it to the 'open_brackets' stack
        elif symbol in check_brackets.values():
            brackets.append(symbol)
    if ('(' not in brackets and ')' not in brackets) and (len(mismatched_indices) > 1 and (mismatched_indices[0] - mismatched_indices[1] % 2 != 0)):
        return True, []
    else:
        return False, mismatched_indices


if __name__ == "__main__":
    # Valid strings
    assert is_valid_parentheses("()") == (True, [])
    assert is_valid_parentheses("[()]") == (True, [])
    assert is_valid_parentheses("{([])}") == (True, [])

    assert is_valid_parentheses("()[") == (True, [])
    assert is_valid_parentheses("()}") == (True, [])
    assert is_valid_parentheses("{()}[") == (True, [])
    assert is_valid_parentheses("{()}]") == (True, [])
    assert is_valid_parentheses("()[]{}") == (True, [])
    assert is_valid_parentheses("[({})]") == (True, [])
    assert is_valid_parentheses("{[()]}") == (True, [])
    assert is_valid_parentheses("({})[]{}") == (True, [])

    # Invalid strings
    assert is_valid_parentheses("{[}]") == (False, [])
    assert is_valid_parentheses("(]") == (False, [0])
    assert is_valid_parentheses("[(])") == (False, [1, 3])

    assert is_valid_parentheses("(") == (False, [0])
    assert is_valid_parentheses(")") == (False, [0])
    assert is_valid_parentheses(")(") == (False, [0, 1])
    assert is_valid_parentheses("[") == (False, [])
    assert is_valid_parentheses("]") == (False, [])
    assert is_valid_parentheses("{") == (False, [])
    assert is_valid_parentheses("}") == (False, [])
    assert is_valid_parentheses("[]") == (False, [])
    assert is_valid_parentheses("{}") == (False, [])
    assert is_valid_parentheses("[(") == (False, [1])
    assert is_valid_parentheses("([)]") == (False, [0, 2])
    assert is_valid_parentheses("({[}])") == (False, [0, 5])
    assert is_valid_parentheses("{{{{{{") == (False, [])
    assert is_valid_parentheses("}}}}}}") == (False, [])
    assert is_valid_parentheses("[[[[[[") == (False, [])
    assert is_valid_parentheses("]]]]]]") == (False, [])
    assert is_valid_parentheses("()(") == (False, [0, 1, 2])
