
from .models import Laptops,Mobiles
from .data import mobiles_details,One_plus_data

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

def Mobile_data():
    created_obj = []
    data = One_plus_data()

    for dt in data:
        try:
            obj , created = Mobiles.objects.get_or_create(
                Product_Name = dt['Product_Name'],
                Product_Price = dt['Product_Price'],
                Product_Reviews = dt['Product_Reviews'],
            )
            created_obj.append(obj)
        except Exception as e:
            # Handle the exception, log it, or perform other actions based on your requirements.
            print(f"Error occurred while creating object: {e}")

