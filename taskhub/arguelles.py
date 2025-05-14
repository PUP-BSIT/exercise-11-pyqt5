from faker import Faker

def generate_fake_user():
    fake = Faker()
    
    print(f"Name: {fake.name()}")
    print(f"Birthdate: {fake.date_of_birth()}")
    print(f"Email: {fake.email()}")
    print(f"Contact Number: {fake.phone_number()}")