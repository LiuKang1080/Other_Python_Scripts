def chicken():
    return egg()


def egg():
    return chicken()


print(chicken(), "Came first.")

# What will happen?
