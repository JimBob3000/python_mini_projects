# From 1 to 5
for i in range(1, 6):
    for j in range(i):
        # Override default print statement's new line via end=" "
        print(i, end=" ")
    # Print new line only
    print()
