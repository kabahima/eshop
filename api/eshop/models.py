import datetime

class Products:
    def __init__(self, pdt_id, pdt_name, seller_id, description,
                 price, image_urls, video_urls, available_colors,
                 weight,  creation_date,  is_available=False ):
                 self.pdt_id = pdt_id
                 self.pdt_name = pdt_name
                 self.creation_date = creation_date.datetime.now()
                 self.seller_id = seller_id
                 self.description = description
                 self.price = price
                 self.image_urls = image_urls
                 self.video_urls = video_urls
                 self.available_colors = available_colors
                 self.weight = weight



class Seller:
    """
    Model class for  sellers
    """

    def __init__(self, name, seller_id, conactname,
                 email, address, comment):
                 
                 self.name = name
                 self.location = location
                 self.seller_id = seller_id
                 self.conactname = conactname
                 self.email = email
                 self.address = address

class orders:
    """
    Model class for the orders
    """

    def __init__(self):
        pass

class Users:
    def __init__(self, user_id, user_name, password, user_email, user_role):
        self.user_id =user_id  # user id
        self.user_name =user_name  # user name
        self.password =password  # user's password
        self.user_email =user_email  # user email
        self.user_role =user_role  #  what does the user acutally do
