class ProductVaildator:
    """ Validator class for products """
    @staticmethod
    def Validate_PdtName(pdt_name ):
        """ method validates the product name """
        return isinstance(pdt_name, str)

    @staticmethod
    def Validate_Price(pdt_price):
        """ method validates the product price """
        return isinstance(price, float)


# Validating images 
    # @staticmethod
    # def validate_image(pdt_image):
    #     """Method validates metadata of images"""
    #     title = "title"
    #     url = 'url'
    #     keys = []
    #     value = []
    #     for key, values in pdt_image.items():
    #         key.

