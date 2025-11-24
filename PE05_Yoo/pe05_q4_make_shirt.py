# PE05 Q4 - make_shirt(size, message)

def make_shirt(size, message):
    """Print a summary of the shirt that is going to be made."""
    print(f"Making a {size} shirt with the message: '{message}'")


# 1) 위치 인자(positional arguments)로 호출
make_shirt("large", "Hello CS11A")

# 2) 키워드 인자(keyword arguments)로 호출
make_shirt(size="medium", message="Python is fun")
