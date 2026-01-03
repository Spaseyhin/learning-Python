def get_hidden_card(cart, hidden=4):
    return '*' * hidden + cart[-4:]

print(get_hidden_card('1234567890123456', 10))  # => '****3456'