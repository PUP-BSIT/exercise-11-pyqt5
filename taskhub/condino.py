import pyjokes

def make_me_laugh():
    joke = pyjokes.get_joke()
    print("Here's a joke for you:")
    print(joke)
    