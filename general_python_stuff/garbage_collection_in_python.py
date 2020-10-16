# Video - https://www.youtube.com/watch?v=eqoy0iwUAA4&ab_channel=InterviewBit

# Example
# values = []
# for i in range(100000):
#     .....
#     print(i)

# but what happens is, at a certain value, the program pauses
# let say at 1490
# ...
# ... smoothly runs
# ....
# then again at 45000
# ....

# If we are working on a producer/consumer problem, in the consumer side, and if the consumer pauses
# the queue may overflow. We dont want that

# NOTE: This is caused by Python's GC.