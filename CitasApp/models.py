from django.db import models

# Enum type for user_auth_provider
class UserAuthProvider(models.TextChoices):
    INTERNAL = 'Internal'
    FACEBOOK = 'Facebook'
    IOS = 'iOS'
    GOOGLE = 'Google'

# Enum type for payment_method
class PaymentMethod(models.TextChoices):
    STRIPE = 'Stripe'
    PAYPAL = 'Paypal'

# Enum type for payment_status
class PaymentStatus(models.TextChoices):
    COMPLETED = 'Completed'
    PENDING = 'Pending'
    FAILED = 'Failed'

class ClientAccount(models.Model):
    id_user = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=80, null=True, blank=True)
    user_auth_provider = models.CharField(max_length=20, choices=UserAuthProvider.choices, default=UserAuthProvider.INTERNAL)
    user_auth_provider_id = models.CharField(max_length=255, null=True, blank=True)
    name_api = models.CharField(max_length=100, null=True, blank=True)

class SupplierAccount(models.Model):
    id_supplier_account = models.AutoField(primary_key=True)
    supplier_email = models.CharField(max_length=100)
    supplier_password = models.CharField(max_length=100)
    supplier_phone = models.CharField(max_length=255)

class Supplier(models.Model):
    id_supplier = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=50)
    supplier_rating = models.FloatField(default=0)
    supplier_address = models.CharField(max_length=100)
    supplier_state = models.CharField(max_length=50)
    supplier_city = models.CharField(max_length=50)
    supplier_zip_code = models.CharField(max_length=10)
    supplier_company_name = models.CharField(max_length=100)
    id_supplier_account = models.ForeignKey(SupplierAccount, on_delete=models.CASCADE)

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(ClientAccount, on_delete=models.CASCADE)
    client_firstname = models.CharField(max_length=50)
    client_lastname = models.CharField(max_length=50)
    client_phone = models.CharField(max_length=20)

class ClientAddress(models.Model):
    id_address = models.AutoField(primary_key=True)
    client_address = models.CharField(max_length=100)
    client_city = models.CharField(max_length=50)
    client_state = models.CharField(max_length=50)
    client_zip_code = models.CharField(max_length=10)
    client_address_additional_information = models.CharField(max_length=100)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=100)
    product_price = models.FloatField(default=0)
    product_stock = models.IntegerField(default=0)
    product_image = models.CharField(max_length=255)
    product_width = models.FloatField(default=0)
    product_height = models.FloatField(default=0)
    product_thickness = models.FloatField(default=0)
    product_material = models.CharField(max_length=50)
    id_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_address = models.ForeignKey(ClientAddress, on_delete=models.CASCADE)
    order_date = models.DateTimeField()

class OrderItem(models.Model):
    id_order_item = models.AutoField(primary_key=True)
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_at_purchase = models.FloatField()

class Shipment(models.Model):
    id_shipment = models.AutoField(primary_key=True)
    shipment_tracking_number = models.CharField(max_length=50)
    shipment_carrier = models.CharField(max_length=50)
    shipment_status = models.CharField(max_length=50)
    shipment_date = models.DateTimeField()
    shipment_estimated_delivery_date = models.DateTimeField()
    shipment_actual_delivery_date = models.DateTimeField(null=True, blank=True)
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Payment(models.Model):
    id_payment = models.AutoField(primary_key=True)
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices)
    payment_amount = models.FloatField()
    payment_date = models.DateTimeField()
    payment_status = models.CharField(max_length=20, choices=PaymentStatus.choices)
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)

class ShoppingCart(models.Model):
    id_cart = models.AutoField(primary_key=True)
    cart_product_quantity = models.IntegerField(default=1)
    cart_added_date = models.DateTimeField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)

class WishItem(models.Model):
    id_wish = models.AutoField(primary_key=True)
    wish_date_added = models.DateTimeField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)

class PasswordReset(models.Model):
    id_reset = models.AutoField(primary_key=True)
    reset_code = models.CharField(max_length=10)
    reset_expiration_time = models.DateTimeField()
    id_user = models.ForeignKey(ClientAccount, on_delete=models.CASCADE, null=True, blank=True)
    id_supplier_account = models.ForeignKey(SupplierAccount, on_delete=models.CASCADE, null=True, blank=True)

class Recycler(models.Model):
    id_recycler = models.AutoField(primary_key=True)
    recycler_name = models.CharField(max_length=100)
    recycler_description = models.CharField(max_length=255)
    recycler_image = models.CharField(max_length=255)
    recycler_number = models.IntegerField()
    recycler_address = models.CharField(max_length=100)