MAX_VALUE :int = 10000

curr_term = 0
next_term = 1

while curr_term <= MAX_VALUE:
    print(curr_term, end = " ")
    after_next = curr_term + next_term
    curr_term = next_term
    next_term = after_next