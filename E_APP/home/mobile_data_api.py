
from .models import Laptops
from .data import mobiles_details

def phone_details():
    created_objects = []
    data = mobiles_details()

    for dt in data:
        try:
            obj, created = Laptops.objects.get_or_create(
                brand_name=dt["brand Name"],
                price=dt["price"],
                discription=dt["discription"],
                reviews=dt["reviews"],
            )
            created_objects.append(obj)
        except Exception as e:
            # Handle the exception, log it, or perform other actions based on your requirements.
            print(f"Error occurred while creating object: {e}")

    return created_objects
