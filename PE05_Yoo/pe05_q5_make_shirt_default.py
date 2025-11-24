# PE05 Q5 - make_shirt with default values

def make_shirt(size="large", message="I love Python"):
    """Print a summary of the shirt that is going to be made.
    Default size is large and default message is 'I love Python'.
    """
    print(f"Making a {size} shirt with the message: '{message}'")


# 1) 기본 메시지로 large 셔츠 만들기
make_shirt()  # size와 message 둘 다 기본값 사용

# 2) 기본 메시지로 medium 셔츠 만들기
make_shirt(size="medium")

# 3) 아무 사이즈나 지정하고 다른 메시지 사용하기
make_shirt(size="small", message="CS11A is awesome")
