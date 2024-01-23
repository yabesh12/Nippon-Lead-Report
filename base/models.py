# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class OcAddress(models.Model):
    address_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    company = models.CharField(max_length=40)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    custom_field = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_address'


class OcAffiliate(models.Model):
    affiliate_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    company = models.CharField(max_length=40)
    website = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    code = models.CharField(max_length=64)
    commission = models.DecimalField(max_digits=4, decimal_places=2)
    tax = models.CharField(max_length=64)
    payment = models.CharField(max_length=6)
    cheque = models.CharField(max_length=100)
    paypal = models.CharField(max_length=64)
    bank_name = models.CharField(max_length=64)
    bank_branch_number = models.CharField(max_length=64)
    bank_swift_code = models.CharField(max_length=64)
    bank_account_name = models.CharField(max_length=64)
    bank_account_number = models.CharField(max_length=64)
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate'


class OcAffiliateActivity(models.Model):
    affiliate_activity_id = models.IntegerField()
    affiliate_id = models.IntegerField()
    key = models.CharField(max_length=64)
    data = models.TextField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate_activity'


class OcAffiliateLogin(models.Model):
    affiliate_login_id = models.IntegerField()
    email = models.CharField(max_length=96)
    ip = models.CharField(max_length=40)
    total = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate_login'


class OcAffiliateTransaction(models.Model):
    affiliate_transaction_id = models.IntegerField()
    affiliate_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate_transaction'


class OcApi(models.Model):
    api_id = models.IntegerField()
    name = models.CharField(max_length=64)
    key = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_api'


class OcApiIp(models.Model):
    api_ip_id = models.IntegerField()
    api_id = models.IntegerField()
    ip = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'oc_api_ip'


class OcApiSession(models.Model):
    api_session_id = models.IntegerField()
    api_id = models.IntegerField()
    token = models.CharField(max_length=32)
    session_id = models.CharField(max_length=32)
    session_name = models.CharField(max_length=32)
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_api_session'


class OcAttribute(models.Model):
    attribute_id = models.IntegerField()
    attribute_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_attribute'


class OcAttributeDescription(models.Model):
    attribute_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_attribute_description'


class OcAttributeGroup(models.Model):
    attribute_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_attribute_group'


class OcAttributeGroupDescription(models.Model):
    attribute_group_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_attribute_group_description'


class OcBanner(models.Model):
    banner_id = models.IntegerField()
    name = models.CharField(max_length=64)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_banner'


class OcBannerImage(models.Model):
    banner_image_id = models.IntegerField()
    banner_id = models.IntegerField()
    language_id = models.IntegerField()
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_banner_image'


class OcC4CApiLog(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    request = models.TextField()
    http_code = models.CharField(max_length=10)
    response = models.TextField()
    created_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_c4c_api_log'


class OcCart(models.Model):
    cart_id = models.PositiveIntegerField()
    api_id = models.IntegerField()
    customer_id = models.IntegerField()
    session_id = models.CharField(max_length=32)
    product_id = models.IntegerField()
    recurring_id = models.IntegerField()
    option = models.TextField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_cart'


class OcCategory(models.Model):
    category_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    top = models.IntegerField()
    column = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_category'


class OcCategoryDescription(models.Model):
    category_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_category_description'


class OcCategoryDescriptionOld(models.Model):
    category_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_category_description_old'


class OcCategoryFilter(models.Model):
    category_id = models.IntegerField()
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_filter'


class OcCategoryFilterOld(models.Model):
    category_id = models.IntegerField()
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_filter_old'


class OcCategoryOld(models.Model):
    category_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    top = models.IntegerField()
    column = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_category_old'


class OcCategoryPath(models.Model):
    category_id = models.IntegerField()
    path_id = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_path'


class OcCategoryPathOld(models.Model):
    category_id = models.IntegerField()
    path_id = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_path_old'


class OcCategoryToLayout(models.Model):
    category_id = models.IntegerField()
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_to_layout'


class OcCategoryToLayoutOld(models.Model):
    category_id = models.IntegerField()
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_to_layout_old'


class OcCategoryToStore(models.Model):
    category_id = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_to_store'


class OcCategoryToStoreOld(models.Model):
    category_id = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_to_store_old'


class OcCities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    state_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_cities'


class OcConnectRegistrations(models.Model):
    reg_id = models.IntegerField()
    post_id = models.IntegerField()
    name = models.CharField(max_length=300)
    email_id = models.CharField(max_length=155)
    mobile_no = models.CharField(max_length=20)
    company_name = models.CharField(max_length=155)
    comments = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_connect_registrations'


class OcCountry(models.Model):
    country_id = models.IntegerField()
    name = models.CharField(max_length=128)
    iso_code_2 = models.CharField(max_length=2)
    iso_code_3 = models.CharField(max_length=3)
    address_format = models.TextField()
    postcode_required = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_country'


class OcCoupon(models.Model):
    coupon_id = models.IntegerField()
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=20)
    type = models.CharField(max_length=1)
    discount = models.DecimalField(max_digits=15, decimal_places=4)
    logged = models.IntegerField()
    shipping = models.IntegerField()
    total = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()
    uses_total = models.IntegerField()
    uses_customer = models.CharField(max_length=11)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_coupon'


class OcCouponCategory(models.Model):
    coupon_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_category'


class OcCouponHistory(models.Model):
    coupon_history_id = models.IntegerField()
    coupon_id = models.IntegerField()
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_history'


class OcCouponProduct(models.Model):
    coupon_product_id = models.IntegerField()
    coupon_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_product'


class OcCurrency(models.Model):
    currency_id = models.IntegerField()
    title = models.CharField(max_length=32)
    code = models.CharField(max_length=3)
    symbol_left = models.CharField(max_length=12)
    symbol_right = models.CharField(max_length=12)
    decimal_place = models.CharField(max_length=1)
    value = models.FloatField()
    status = models.IntegerField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_currency'


class OcCustomField(models.Model):
    custom_field_id = models.IntegerField()
    type = models.CharField(max_length=32)
    value = models.TextField()
    validation = models.CharField(max_length=255)
    location = models.CharField(max_length=7)
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field'


class OcCustomFieldCustomerGroup(models.Model):
    custom_field_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field_customer_group'


class OcCustomFieldDescription(models.Model):
    custom_field_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_custom_field_description'


class OcCustomFieldValue(models.Model):
    custom_field_value_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field_value'


class OcCustomFieldValueDescription(models.Model):
    custom_field_value_id = models.IntegerField()
    language_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_custom_field_value_description'


class OcCustomer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_group_id = models.IntegerField()
    store_id = models.IntegerField()
    language_id = models.IntegerField()
    user_type = models.CharField(max_length=30)
    category = models.CharField(max_length=50)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    alter_telephone = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    state = models.CharField(max_length=40)
    region = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    company = models.CharField(max_length=225)
    company_email = models.CharField(max_length=225)
    company_website = models.CharField(max_length=225)
    spouse_name = models.CharField(max_length=225)
    spouse_dob = models.DateField()
    child_1_name = models.CharField(max_length=225)
    child_1_dob = models.DateField()
    child_2_name = models.CharField(max_length=225)
    child_2_dob = models.DateField()
    date_of_anniversary = models.DateField()
    area_of_interest = models.CharField(max_length=225)
    salt = models.CharField(max_length=9)
    cart = models.TextField(blank=True, null=True)
    wishlist = models.TextField(blank=True, null=True)
    newsletter = models.IntegerField()
    address_id = models.IntegerField()
    custom_field = models.TextField()
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    safe = models.IntegerField()
    token = models.TextField()
    code = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer'


class OcCustomer91618(models.Model):
    customer_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    store_id = models.IntegerField()
    language_id = models.IntegerField()
    user_type = models.CharField(max_length=30)
    category = models.CharField(max_length=50)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    alter_telephone = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    state = models.CharField(max_length=40)
    region = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    company = models.CharField(max_length=225)
    company_email = models.CharField(max_length=225)
    company_website = models.CharField(max_length=225)
    spouse_name = models.CharField(max_length=225)
    spouse_dob = models.DateField()
    child_1_name = models.CharField(max_length=225)
    child_1_dob = models.DateField()
    child_2_name = models.CharField(max_length=225)
    child_2_dob = models.DateField()
    date_of_anniversary = models.DateField()
    area_of_interest = models.CharField(max_length=225)
    salt = models.CharField(max_length=9)
    cart = models.TextField(blank=True, null=True)
    wishlist = models.TextField(blank=True, null=True)
    newsletter = models.IntegerField()
    address_id = models.IntegerField()
    custom_field = models.TextField()
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    safe = models.IntegerField()
    token = models.TextField()
    code = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_9-16-18'


class OcCustomerActivity(models.Model):
    customer_activity_id = models.IntegerField()
    customer_id = models.IntegerField()
    key = models.CharField(max_length=64)
    data = models.TextField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_activity'


class OcCustomerGroup(models.Model):
    customer_group_id = models.IntegerField()
    approval = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customer_group'


class OcCustomerGroupDescription(models.Model):
    customer_group_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_customer_group_description'


class OcCustomerHistory(models.Model):
    customer_history_id = models.IntegerField()
    customer_id = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_history'


class OcCustomerIp(models.Model):
    customer_ip_id = models.IntegerField()
    customer_id = models.IntegerField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_ip'


class OcCustomerLogin(models.Model):
    customer_login_id = models.IntegerField()
    email = models.CharField(max_length=96)
    mobile_no = models.CharField(max_length=20)
    ip = models.CharField(max_length=40)
    total = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_login'


class OcCustomerLoyalty(models.Model):
    customer_loyalty_id = models.IntegerField()
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    points = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)
    store_id = models.IntegerField()
    email_id = models.CharField(max_length=300)
    user_type = models.CharField(max_length=30)
    category = models.CharField(max_length=155)
    import_type = models.CharField(max_length=1)
    recommender = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    pushed_to_c4c = models.IntegerField()
    c4c_contact_id = models.CharField(max_length=20)
    c4c_error_msg = models.CharField(max_length=150)
    date_added = models.DateTimeField()
    excess_points_used = models.IntegerField(blank=True, null=True)
    points_compensated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_customer_loyalty'


class OcCustomerLoyalty12Dec2020(models.Model):
    customer_loyalty_id = models.IntegerField()
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    points = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)
    store_id = models.IntegerField()
    email_id = models.CharField(max_length=300)
    user_type = models.CharField(max_length=30)
    category = models.CharField(max_length=155)
    import_type = models.CharField(max_length=1)
    recommender = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    pushed_to_c4c = models.IntegerField()
    c4c_contact_id = models.CharField(max_length=20)
    c4c_error_msg = models.CharField(max_length=150)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_loyalty_12dec2020'


class OcCustomerLoyalty21Mar2020(models.Model):
    customer_loyalty_id = models.IntegerField()
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    points = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)
    store_id = models.IntegerField()
    email_id = models.CharField(max_length=300)
    user_type = models.CharField(max_length=30)
    category = models.CharField(max_length=155)
    import_type = models.CharField(max_length=1)
    recommender = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    pushed_to_c4c = models.IntegerField()
    c4c_contact_id = models.CharField(max_length=20)
    c4c_error_msg = models.CharField(max_length=150)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_loyalty_21mar2020'


class OcCustomerLoyalty91618(models.Model):
    customer_loyalty_id = models.IntegerField()
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    points = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)
    store_id = models.IntegerField()
    email_id = models.CharField(max_length=300)
    user_type = models.CharField(max_length=30)
    category = models.CharField(max_length=155)
    import_type = models.CharField(max_length=1)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_loyalty_9-16-18'


class OcCustomerLoyaltyError(models.Model):
    customer_loyalty_error_id = models.IntegerField()
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    points = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)
    store_id = models.IntegerField()
    email_id = models.CharField(max_length=300)
    user_type = models.CharField(max_length=30)
    category = models.CharField(max_length=155)
    import_type = models.CharField(max_length=1)
    recommender = models.CharField(max_length=100)
    error_fields = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_loyalty_error'


class OcCustomerLoyaltyOld21Mar2020(models.Model):
    customer_loyalty_id = models.IntegerField()
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    points = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)
    store_id = models.IntegerField()
    email_id = models.CharField(max_length=300)
    user_type = models.CharField(max_length=30)
    category = models.CharField(max_length=155)
    import_type = models.CharField(max_length=1)
    recommender = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    pushed_to_c4c = models.IntegerField()
    c4c_contact_id = models.CharField(max_length=20)
    c4c_error_msg = models.CharField(max_length=150)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_loyalty_old_21mar2020'


class OcCustomerOnline(models.Model):
    ip = models.CharField(max_length=40)
    customer_id = models.IntegerField()
    url = models.TextField()
    referer = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_online'


class OcCustomerOtp(models.Model):
    customer_otp_id = models.IntegerField()
    mobile_no = models.CharField(max_length=25)
    store_id = models.IntegerField()
    otp = models.CharField(max_length=25)
    added_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_otp'


class OcCustomerReward(models.Model):
    customer_reward_id = models.IntegerField()
    customer_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    order_id = models.IntegerField()
    customer_loyalty_fk = models.IntegerField()
    store_id = models.IntegerField()
    mobile_no = models.CharField(max_length=20)
    description = models.TextField()
    points = models.IntegerField()
    points_type = models.CharField(max_length=100)
    used_points = models.IntegerField()
    total = models.IntegerField()
    date_added = models.DateTimeField()
    remarks = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'oc_customer_reward'


class OcCustomerReward03Dec2020(models.Model):
    customer_reward_id = models.IntegerField()
    customer_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    order_id = models.IntegerField()
    customer_loyalty_fk = models.IntegerField()
    store_id = models.IntegerField()
    mobile_no = models.CharField(max_length=20)
    description = models.TextField()
    points = models.IntegerField()
    points_type = models.CharField(max_length=100)
    used_points = models.IntegerField()
    total = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_reward_03dec2020'


class OcCustomerReward03July2021(models.Model):
    customer_reward_id = models.IntegerField()
    customer_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    order_id = models.IntegerField()
    customer_loyalty_fk = models.IntegerField()
    store_id = models.IntegerField()
    mobile_no = models.CharField(max_length=20)
    description = models.TextField()
    points = models.IntegerField()
    points_type = models.CharField(max_length=100)
    used_points = models.IntegerField()
    total = models.IntegerField()
    date_added = models.DateTimeField()
    remarks = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'oc_customer_reward_03july2021'


class OcCustomerReward21Mar2020(models.Model):
    customer_reward_id = models.IntegerField()
    customer_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    order_id = models.IntegerField()
    customer_loyalty_fk = models.IntegerField()
    store_id = models.IntegerField()
    mobile_no = models.CharField(max_length=20)
    description = models.TextField()
    points = models.IntegerField()
    points_type = models.CharField(max_length=100)
    used_points = models.IntegerField()
    total = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_reward_21mar2020'


class OcCustomerReward23Sep2020(models.Model):
    customer_reward_id = models.IntegerField()
    customer_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    order_id = models.IntegerField()
    customer_loyalty_fk = models.IntegerField()
    store_id = models.IntegerField()
    mobile_no = models.CharField(max_length=20)
    description = models.TextField()
    points = models.IntegerField()
    points_type = models.CharField(max_length=100)
    used_points = models.IntegerField()
    total = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_reward_23sep2020'


class OcCustomerReward24May2021(models.Model):
    customer_reward_id = models.IntegerField()
    customer_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    order_id = models.IntegerField()
    customer_loyalty_fk = models.IntegerField()
    store_id = models.IntegerField()
    mobile_no = models.CharField(max_length=20)
    description = models.TextField()
    points = models.IntegerField()
    points_type = models.CharField(max_length=100)
    used_points = models.IntegerField()
    total = models.IntegerField()
    date_added = models.DateTimeField()
    remarks = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'oc_customer_reward_24may2021'


class OcCustomerReward28012020(models.Model):
    customer_reward_id = models.IntegerField()
    customer_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    order_id = models.IntegerField()
    customer_loyalty_fk = models.IntegerField()
    store_id = models.IntegerField()
    mobile_no = models.CharField(max_length=20)
    description = models.TextField()
    points = models.IntegerField()
    points_type = models.CharField(max_length=100)
    used_points = models.IntegerField()
    total = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_reward_28_01_2020'


class OcCustomerReward5Feb2021(models.Model):
    customer_reward_id = models.IntegerField()
    customer_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    order_id = models.IntegerField()
    customer_loyalty_fk = models.IntegerField()
    store_id = models.IntegerField()
    mobile_no = models.CharField(max_length=20)
    description = models.TextField()
    points = models.IntegerField()
    points_type = models.CharField(max_length=100)
    used_points = models.IntegerField()
    total = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_reward_5feb2021'


class OcCustomerReward91618(models.Model):
    customer_reward_id = models.IntegerField()
    customer_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    order_id = models.IntegerField()
    customer_loyalty_fk = models.IntegerField()
    store_id = models.IntegerField()
    mobile_no = models.CharField(max_length=20)
    description = models.TextField()
    points = models.IntegerField()
    points_type = models.CharField(max_length=100)
    used_points = models.IntegerField()
    total = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_reward_9-16-18'


class OcCustomerRewardArchive(models.Model):
    archive_id = models.IntegerField()
    customer_reward_id = models.IntegerField()
    customer_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    order_id = models.IntegerField()
    customer_loyalty_fk = models.IntegerField()
    store_id = models.IntegerField()
    mobile_no = models.CharField(max_length=20)
    description = models.TextField()
    points = models.IntegerField()
    points_type = models.CharField(max_length=100)
    used_points = models.IntegerField()
    total = models.IntegerField()
    date_added = models.DateTimeField()
    remarks = models.CharField(max_length=100)
    archive_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_reward_archive'


class OcCustomerSearch(models.Model):
    customer_search_id = models.IntegerField()
    store_id = models.IntegerField()
    language_id = models.IntegerField()
    customer_id = models.IntegerField()
    keyword = models.CharField(max_length=255)
    category_id = models.IntegerField(blank=True, null=True)
    sub_category = models.IntegerField()
    description = models.IntegerField()
    products = models.IntegerField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_search'


class OcCustomerTransaction(models.Model):
    customer_transaction_id = models.IntegerField()
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_transaction'


class OcCustomerWishlist(models.Model):
    customer_id = models.IntegerField()
    product_id = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_wishlist'


class OcDownload(models.Model):
    download_id = models.IntegerField()
    filename = models.CharField(max_length=160)
    mask = models.CharField(max_length=128)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_download'


class OcDownloadDescription(models.Model):
    download_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_download_description'


class OcEvent(models.Model):
    event_id = models.IntegerField()
    code = models.CharField(max_length=32)
    trigger = models.TextField()
    action = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_event'


class OcExtension(models.Model):
    extension_id = models.IntegerField()
    type = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_extension'


class OcFilter(models.Model):
    filter_id = models.IntegerField()
    filter_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_filter'


class OcFilterDescription(models.Model):
    filter_id = models.IntegerField()
    language_id = models.IntegerField()
    filter_group_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_filter_description'


class OcFilterGroup(models.Model):
    filter_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_filter_group'


class OcFilterGroupDescription(models.Model):
    filter_group_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_filter_group_description'


class OcGeoZone(models.Model):
    geo_zone_id = models.IntegerField()
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    date_modified = models.DateTimeField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_geo_zone'


class OcInformation(models.Model):
    information_id = models.IntegerField()
    bottom = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information'


class OcInformationDescription(models.Model):
    information_id = models.IntegerField()
    language_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_information_description'


class OcInformationToLayout(models.Model):
    information_id = models.IntegerField()
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information_to_layout'


class OcInformationToStore(models.Model):
    information_id = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information_to_store'


class OcLanguage(models.Model):
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=5)
    locale = models.CharField(max_length=255)
    image = models.CharField(max_length=64)
    directory = models.CharField(max_length=32)
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_language'


class OcLayout(models.Model):
    layout_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_layout'


class OcLayoutModule(models.Model):
    layout_module_id = models.IntegerField()
    layout_id = models.IntegerField()
    code = models.CharField(max_length=64)
    position = models.CharField(max_length=14)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_layout_module'


class OcLayoutRoute(models.Model):
    layout_route_id = models.IntegerField()
    layout_id = models.IntegerField()
    store_id = models.IntegerField()
    route = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_layout_route'


class OcLead(models.Model):
    lead_no = models.IntegerField(primary_key=True)
    lead_id = models.CharField(max_length=10)
    unqiue_id = models.CharField(max_length=10)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    user_mobile = models.CharField(max_length=25)
    user_type = models.CharField(max_length=30)
    user_group_id = models.IntegerField()
    user_group = models.CharField(max_length=20)
    project_name = models.CharField(max_length=100)
    project_location = models.CharField(max_length=50)
    project_city = models.CharField(max_length=50)
    builder_name = models.CharField(max_length=50)
    builder_mobile_no = models.CharField(max_length=20)
    sales_person_name = models.CharField(max_length=150)
    date_from = models.DateField()
    date_to = models.DateField()
    tot_paintable_area = models.FloatField()
    chk_tot_paintable_area = models.FloatField()
    boq = models.CharField(max_length=100)
    lead_status_id = models.IntegerField()
    approval_status = models.CharField(max_length=30)
    admin_status = models.CharField(max_length=50)
    sale_head_status = models.CharField(max_length=30)
    remarks = models.TextField()
    uploaded_by = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead'


class OcLead24May2021(models.Model):
    lead_no = models.IntegerField()
    lead_id = models.CharField(max_length=10)
    unqiue_id = models.CharField(max_length=10)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    user_mobile = models.CharField(max_length=25)
    user_type = models.CharField(max_length=30)
    user_group_id = models.IntegerField()
    user_group = models.CharField(max_length=20)
    project_name = models.CharField(max_length=100)
    project_location = models.CharField(max_length=50)
    project_city = models.CharField(max_length=50)
    builder_name = models.CharField(max_length=50)
    builder_mobile_no = models.CharField(max_length=20)
    sales_person_name = models.CharField(max_length=150)
    date_from = models.DateField()
    date_to = models.DateField()
    tot_paintable_area = models.FloatField()
    chk_tot_paintable_area = models.FloatField()
    boq = models.CharField(max_length=100)
    lead_status_id = models.IntegerField()
    approval_status = models.CharField(max_length=30)
    admin_status = models.CharField(max_length=50)
    sale_head_status = models.CharField(max_length=30)
    remarks = models.TextField()
    uploaded_by = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_24may2021'


class OcLeadArchive(models.Model):
    archive_id = models.IntegerField()
    lead_no = models.IntegerField()
    lead_id = models.CharField(max_length=10)
    unqiue_id = models.CharField(max_length=10)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    user_mobile = models.CharField(max_length=25)
    user_type = models.CharField(max_length=30)
    user_group_id = models.IntegerField()
    user_group = models.CharField(max_length=20)
    project_name = models.CharField(max_length=100)
    project_location = models.CharField(max_length=50)
    project_city = models.CharField(max_length=50)
    builder_name = models.CharField(max_length=50)
    builder_mobile_no = models.CharField(max_length=20)
    sales_person_name = models.CharField(max_length=150)
    date_from = models.DateField()
    date_to = models.DateField()
    tot_paintable_area = models.FloatField()
    chk_tot_paintable_area = models.FloatField()
    boq = models.CharField(max_length=100)
    lead_status_id = models.IntegerField()
    approval_status = models.CharField(max_length=30)
    admin_status = models.CharField(max_length=50)
    sale_head_status = models.CharField(max_length=30)
    remarks = models.TextField()
    uploaded_by = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    archive_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_archive'


class OcLeadAssigned(models.Model):
    assign_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    sale_head_id = models.IntegerField()
    sale_head_name = models.CharField(max_length=50)
    sale_head_status = models.CharField(max_length=30)
    sales_head_remarks = models.TextField()
    sale_engg_id = models.IntegerField()
    sale_engg_name = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    remarks = models.TextField()
    edit_status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_assigned'


class OcLeadAssignedArchive(models.Model):
    archive_id = models.IntegerField()
    assign_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    sale_head_id = models.IntegerField()
    sale_head_name = models.CharField(max_length=50)
    sale_head_status = models.CharField(max_length=30)
    sales_head_remarks = models.TextField()
    sale_engg_id = models.IntegerField()
    sale_engg_name = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    remarks = models.TextField()
    edit_status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    archive_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_assigned_archive'


class OcLeadBrand(models.Model):
    lead_brand_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    type_id = models.IntegerField()
    type_name = models.CharField(max_length=50)
    brand_id_fk = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    paintable_area = models.FloatField()
    chk_paintable_area = models.FloatField()

    class Meta:
        managed = False
        db_table = 'oc_lead_brand'


class OcLeadBrandArchive(models.Model):
    archive_id = models.IntegerField()
    lead_brand_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    type_id = models.IntegerField()
    type_name = models.CharField(max_length=50)
    brand_id_fk = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    paintable_area = models.FloatField()
    chk_paintable_area = models.FloatField()
    archive_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_brand_archive'


class OcLeadCopy21Jan2019(models.Model):
    lead_no = models.IntegerField()
    lead_id = models.CharField(max_length=10)
    unqiue_id = models.CharField(max_length=10)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    user_type = models.CharField(max_length=30)
    user_group_id = models.IntegerField()
    user_group = models.CharField(max_length=20)
    project_name = models.CharField(max_length=100)
    project_location = models.CharField(max_length=50)
    project_city = models.CharField(max_length=50)
    builder_name = models.CharField(max_length=50)
    builder_mobile_no = models.CharField(max_length=20)
    sales_person_name = models.CharField(max_length=150)
    date_from = models.DateField()
    date_to = models.DateField()
    tot_paintable_area = models.FloatField()
    chk_tot_paintable_area = models.FloatField()
    boq = models.CharField(max_length=100)
    lead_status_id = models.IntegerField()
    approval_status = models.CharField(max_length=30)
    admin_status = models.CharField(max_length=50)
    sale_head_status = models.CharField(max_length=30)
    remarks = models.TextField()
    uploaded_by = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_copy_21jan2019'


class OcLeadHistory(models.Model):
    history_id = models.BigIntegerField()
    lead_no_fk = models.IntegerField()
    user_id = models.IntegerField()
    status_id = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_history'


class OcLeadHistoryArchive(models.Model):
    archive_id = models.IntegerField()
    history_id = models.BigIntegerField()
    lead_no_fk = models.IntegerField()
    user_id = models.IntegerField()
    status_id = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()
    archive_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_history_archive'


class OcLeadLog(models.Model):
    lead_log_id = models.IntegerField()
    lead_no = models.CharField(max_length=20)
    specifier_name = models.CharField(max_length=150)
    specifier_mobile = models.CharField(max_length=15)
    specifier_user_type = models.CharField(max_length=150)
    specifier_category = models.CharField(max_length=150)
    project_name = models.CharField(max_length=150)
    project_location = models.CharField(max_length=150)
    project_city = models.CharField(max_length=150)
    tentative_from_date = models.CharField(max_length=15)
    tentative_to_date = models.CharField(max_length=15)
    builder_name = models.CharField(max_length=150)
    builder_mobile_no = models.CharField(max_length=15)
    sales_person_name = models.CharField(max_length=150)
    total_paintable_area = models.DecimalField(max_digits=10, decimal_places=2)
    error_fields = models.TextField()
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_log'


class OcLeadLogBrand(models.Model):
    lead_log_brand_id = models.IntegerField()
    lead_log_id = models.IntegerField()
    lead_no = models.CharField(max_length=50)
    category_id = models.IntegerField()
    brand_id = models.IntegerField()
    paintable_area = models.CharField(max_length=50)
    error_fields = models.TextField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_log_brand'


class OcLeadReward(models.Model):
    reward_id = models.IntegerField()
    customer_id_fk = models.IntegerField()
    sale_person_id = models.IntegerField()
    sale_id_fk = models.IntegerField(blank=True, null=True)
    lead_no_fk = models.IntegerField()
    reward_name = models.CharField(max_length=50)
    reward_point = models.FloatField()
    reward_status = models.CharField(max_length=30)
    invoice_amt = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_reward'


class OcLeadReward21Mar2020(models.Model):
    reward_id = models.IntegerField()
    customer_id_fk = models.IntegerField()
    sale_person_id = models.IntegerField()
    lead_no_fk = models.IntegerField()
    reward_name = models.CharField(max_length=50)
    reward_point = models.FloatField()
    reward_status = models.CharField(max_length=30)
    invoice_amt = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'oc_lead_reward_21mar2020'


class OcLeadReward24May2021(models.Model):
    reward_id = models.IntegerField()
    customer_id_fk = models.IntegerField()
    sale_person_id = models.IntegerField()
    sale_id_fk = models.IntegerField(blank=True, null=True)
    lead_no_fk = models.IntegerField()
    reward_name = models.CharField(max_length=50)
    reward_point = models.FloatField()
    reward_status = models.CharField(max_length=30)
    invoice_amt = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_reward_24may2021'


class OcLeadRewardArchive(models.Model):
    archive_id = models.IntegerField()
    reward_id = models.IntegerField()
    customer_id_fk = models.IntegerField()
    sale_person_id = models.IntegerField()
    sale_id_fk = models.IntegerField(blank=True, null=True)
    lead_no_fk = models.IntegerField()
    reward_name = models.CharField(max_length=50)
    reward_point = models.FloatField()
    reward_status = models.CharField(max_length=30)
    invoice_amt = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    archive_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_reward_archive'


class OcLeadRewardMaster(models.Model):
    reward_master_id = models.IntegerField()
    reward_name = models.CharField(max_length=40)
    architect = models.FloatField()
    designer = models.FloatField()
    engineer = models.FloatField()
    others = models.FloatField()
    green_consultant = models.FloatField()

    class Meta:
        managed = False
        db_table = 'oc_lead_reward_master'


class OcLeadRewardMasterOld20(models.Model):
    reward_master_id = models.IntegerField()
    reward_name = models.CharField(max_length=40)
    architect = models.FloatField()
    designer = models.FloatField()
    engineer = models.FloatField()

    class Meta:
        managed = False
        db_table = 'oc_lead_reward_master_old_20'


class OcLeadSales(models.Model):
    sale_id = models.IntegerField(primary_key=True)
    sale_person_id = models.IntegerField()
    sale_person_name = models.CharField(max_length=50)
    lead_no_fk = models.IntegerField()
    lead_id = models.CharField(max_length=15)
    recommend_brand_id = models.IntegerField()
    recommend_brand = models.CharField(max_length=100)
    purchase_brand_id = models.IntegerField()
    purchase_brand = models.CharField(max_length=100)
    purchase_product_id = models.IntegerField()
    purchase_product = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    product_range = models.IntegerField()
    price_per_qty = models.FloatField()
    qty = models.IntegerField()
    product_details = models.TextField()
    total_products = models.IntegerField()
    invoice_amount = models.FloatField()
    invoice_premium_amount = models.FloatField()
    invoice_no = models.CharField(max_length=10)
    invoice_file = models.CharField(max_length=200)
    purchase_date = models.DateField(blank=True, null=True)
    dealer_name = models.CharField(max_length=30)
    dealer_code = models.CharField(max_length=50)
    status = models.IntegerField()
    sale_status = models.CharField(max_length=30)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_sales'


class OcLeadSalesArchive(models.Model):
    archive_id = models.IntegerField()
    sale_id = models.IntegerField()
    sale_person_id = models.IntegerField()
    sale_person_name = models.CharField(max_length=50)
    lead_no_fk = models.IntegerField()
    lead_id = models.CharField(max_length=15)
    recommend_brand_id = models.IntegerField()
    recommend_brand = models.CharField(max_length=100)
    purchase_brand_id = models.IntegerField()
    purchase_brand = models.CharField(max_length=100)
    purchase_product_id = models.IntegerField()
    purchase_product = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    product_range = models.IntegerField()
    price_per_qty = models.FloatField()
    qty = models.IntegerField()
    product_details = models.TextField()
    total_products = models.IntegerField()
    invoice_amount = models.FloatField()
    invoice_premium_amount = models.FloatField()
    invoice_no = models.CharField(max_length=10)
    invoice_file = models.CharField(max_length=200)
    purchase_date = models.DateField(blank=True, null=True)
    dealer_name = models.CharField(max_length=30)
    dealer_code = models.CharField(max_length=50)
    status = models.IntegerField()
    sale_status = models.CharField(max_length=30)
    date_added = models.DateTimeField()
    archive_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_lead_sales_archive'


class OcLeadStatus(models.Model):
    lead_status_id = models.IntegerField()
    status_name = models.CharField(max_length=30)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'oc_lead_status'


class OcLeadStatusOld20(models.Model):
    lead_status_id = models.IntegerField()
    status_name = models.CharField(max_length=30)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'oc_lead_status_old_20'


class OcLengthClass(models.Model):
    length_class_id = models.IntegerField()
    value = models.DecimalField(max_digits=15, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'oc_length_class'


class OcLengthClassDescription(models.Model):
    length_class_id = models.IntegerField()
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'oc_length_class_description'


class OcLocation(models.Model):
    location_id = models.IntegerField()
    name = models.CharField(max_length=32)
    address = models.TextField()
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    geocode = models.CharField(max_length=32)
    image = models.CharField(max_length=255, blank=True, null=True)
    open = models.TextField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_location'


class OcLoyaltyRegister(models.Model):
    loyalty_register_id = models.IntegerField()
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    comments = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_loyalty_register'


class OcManufacturer(models.Model):
    manufacturer_id = models.IntegerField()
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_manufacturer'


class OcManufacturerToStore(models.Model):
    manufacturer_id = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_manufacturer_to_store'


class OcMarketing(models.Model):
    marketing_id = models.IntegerField()
    name = models.CharField(max_length=32)
    description = models.TextField()
    code = models.CharField(max_length=64)
    clicks = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_marketing'


class OcMenu(models.Model):
    menu_id = models.IntegerField()
    store_id = models.IntegerField()
    type = models.CharField(max_length=6)
    link = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_menu'


class OcMenuDescription(models.Model):
    menu_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_menu_description'


class OcMenuModule(models.Model):
    menu_module_id = models.IntegerField()
    menu_id = models.IntegerField()
    code = models.CharField(max_length=64)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_menu_module'


class OcModification(models.Model):
    modification_id = models.IntegerField()
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    version = models.CharField(max_length=32)
    link = models.CharField(max_length=255)
    xml = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_modification'


class OcModule(models.Model):
    module_id = models.IntegerField()
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=32)
    setting = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_module'


class OcNewslettersubscription(models.Model):
    subscription_id = models.IntegerField()
    email = models.CharField(max_length=128)
    status = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_newslettersubscription'


class OcOption(models.Model):
    option_id = models.IntegerField()
    type = models.CharField(max_length=32)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_option'


class OcOptionDescription(models.Model):
    option_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_option_description'


class OcOptionValue(models.Model):
    option_value_id = models.IntegerField()
    option_id = models.IntegerField()
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_option_value'


class OcOptionValueDescription(models.Model):
    option_value_id = models.IntegerField()
    language_id = models.IntegerField()
    option_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_option_value_description'


class OcOrder(models.Model):
    order_id = models.IntegerField()
    invoice_no = models.IntegerField()
    invoice_prefix = models.CharField(max_length=26)
    store_id = models.IntegerField()
    store_name = models.CharField(max_length=64)
    store_url = models.CharField(max_length=255)
    customer_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    custom_field = models.TextField()
    payment_firstname = models.CharField(max_length=32)
    payment_lastname = models.CharField(max_length=32)
    payment_company = models.CharField(max_length=60)
    payment_address_1 = models.CharField(max_length=128)
    payment_address_2 = models.CharField(max_length=128)
    payment_city = models.CharField(max_length=128)
    payment_postcode = models.CharField(max_length=10)
    payment_country = models.CharField(max_length=128)
    payment_country_id = models.IntegerField()
    payment_zone = models.CharField(max_length=128)
    payment_zone_id = models.IntegerField()
    payment_address_format = models.TextField()
    payment_custom_field = models.TextField()
    payment_method = models.CharField(max_length=128)
    payment_code = models.CharField(max_length=128)
    shipping_firstname = models.CharField(max_length=32)
    shipping_lastname = models.CharField(max_length=32)
    shipping_company = models.CharField(max_length=40)
    shipping_address_1 = models.CharField(max_length=128)
    shipping_address_2 = models.CharField(max_length=128)
    shipping_city = models.CharField(max_length=128)
    shipping_postcode = models.CharField(max_length=10)
    shipping_country = models.CharField(max_length=128)
    shipping_country_id = models.IntegerField()
    shipping_zone = models.CharField(max_length=128)
    shipping_zone_id = models.IntegerField()
    shipping_address_format = models.TextField()
    shipping_custom_field = models.TextField()
    shipping_method = models.CharField(max_length=128)
    shipping_code = models.CharField(max_length=128)
    comment = models.TextField()
    total = models.DecimalField(max_digits=15, decimal_places=4)
    total_points = models.IntegerField()
    order_status_id = models.IntegerField()
    affiliate_id = models.IntegerField()
    commission = models.DecimalField(max_digits=15, decimal_places=4)
    marketing_id = models.IntegerField()
    tracking = models.CharField(max_length=64)
    language_id = models.IntegerField()
    currency_id = models.IntegerField()
    currency_code = models.CharField(max_length=3)
    currency_value = models.DecimalField(max_digits=15, decimal_places=8)
    ip = models.CharField(max_length=40)
    forwarded_ip = models.CharField(max_length=40)
    user_agent = models.CharField(max_length=255)
    accept_language = models.CharField(max_length=255)
    viewed = models.IntegerField()
    viewed_sh = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order'


class OcOrderCustomField(models.Model):
    order_custom_field_id = models.IntegerField()
    order_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    custom_field_value_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=32)
    location = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'oc_order_custom_field'


class OcOrderHistory(models.Model):
    order_history_id = models.IntegerField()
    order_id = models.IntegerField()
    order_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_history'


class OcOrderOption(models.Model):
    order_option_id = models.IntegerField()
    order_id = models.IntegerField()
    order_product_id = models.IntegerField()
    product_option_id = models.IntegerField()
    product_option_value_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_order_option'


class OcOrderProduct(models.Model):
    order_product_id = models.IntegerField()
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    total = models.DecimalField(max_digits=15, decimal_places=4)
    points = models.IntegerField()
    points_total = models.IntegerField()
    tax = models.DecimalField(max_digits=15, decimal_places=4)
    reward = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_order_product'


class OcOrderRecurring(models.Model):
    order_recurring_id = models.IntegerField()
    order_id = models.IntegerField()
    reference = models.CharField(max_length=255)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_quantity = models.IntegerField()
    recurring_id = models.IntegerField()
    recurring_name = models.CharField(max_length=255)
    recurring_description = models.CharField(max_length=255)
    recurring_frequency = models.CharField(max_length=25)
    recurring_cycle = models.SmallIntegerField()
    recurring_duration = models.SmallIntegerField()
    recurring_price = models.DecimalField(max_digits=10, decimal_places=4)
    trial = models.IntegerField()
    trial_frequency = models.CharField(max_length=25)
    trial_cycle = models.SmallIntegerField()
    trial_duration = models.SmallIntegerField()
    trial_price = models.DecimalField(max_digits=10, decimal_places=4)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_recurring'


class OcOrderRecurringTransaction(models.Model):
    order_recurring_transaction_id = models.IntegerField()
    order_recurring_id = models.IntegerField()
    reference = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_recurring_transaction'


class OcOrderStatus(models.Model):
    order_status_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_order_status'


class OcOrderTotal(models.Model):
    order_total_id = models.IntegerField()
    order_id = models.IntegerField()
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=15, decimal_places=4)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_order_total'


class OcOrderVoucher(models.Model):
    order_voucher_id = models.IntegerField()
    order_id = models.IntegerField()
    voucher_id = models.IntegerField()
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    from_name = models.CharField(max_length=64)
    from_email = models.CharField(max_length=96)
    to_name = models.CharField(max_length=64)
    to_email = models.CharField(max_length=96)
    voucher_theme_id = models.IntegerField()
    message = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'oc_order_voucher'


class OcPaintBrand(models.Model):
    brand_id = models.IntegerField()
    brand_name = models.CharField(max_length=155)
    category_id = models.IntegerField()
    avg_litre = models.IntegerField()
    price_per_sqft = models.FloatField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_paint_brand'


class OcPaintBrand156(models.Model):
    brand_id = models.IntegerField()
    brand_name = models.CharField(max_length=155)
    category_id = models.IntegerField()
    avg_litre = models.IntegerField()
    price_per_sqft = models.FloatField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_paint_brand_15_6'


class OcPaintBrand20210326(models.Model):
    brand_id = models.IntegerField()
    brand_name = models.CharField(max_length=155)
    category_id = models.IntegerField()
    avg_litre = models.IntegerField()
    price_per_sqft = models.FloatField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_paint_brand_2021-03-26'


class OcPaintBrand522018(models.Model):
    brand_id = models.IntegerField()
    brand_name = models.CharField(max_length=155)
    avg_litre = models.IntegerField()
    price_per_sqft = models.FloatField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_paint_brand_5_2_2018'


class OcPaintCategory(models.Model):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=155)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_paint_category'


class OcPaintCategory156(models.Model):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=155)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_paint_category_15_6'


class OcPaintCategory20210326(models.Model):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=155)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_paint_category_2021-03-26'


class OcPaintProduct(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=155)
    product_sku = models.CharField(max_length=55)
    description = models.TextField()
    brand = models.IntegerField()
    product_range = models.IntegerField()
    category = models.IntegerField()
    avg_coverage = models.DecimalField(max_digits=15, decimal_places=3)
    avg_price = models.DecimalField(max_digits=15, decimal_places=3)
    pack_size = models.IntegerField()
    price_mrp = models.DecimalField(max_digits=15, decimal_places=3)
    price_project = models.DecimalField(max_digits=15, decimal_places=3)
    price_retail = models.DecimalField(max_digits=15, decimal_places=3)
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_paint_product'


class OcPaintProduct156(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=155)
    product_sku = models.CharField(max_length=55)
    description = models.TextField()
    brand = models.IntegerField()
    product_range = models.IntegerField()
    category = models.IntegerField()
    avg_coverage = models.DecimalField(max_digits=15, decimal_places=3)
    avg_price = models.DecimalField(max_digits=15, decimal_places=3)
    pack_size = models.IntegerField()
    price_mrp = models.DecimalField(max_digits=15, decimal_places=3)
    price_project = models.DecimalField(max_digits=15, decimal_places=3)
    price_retail = models.DecimalField(max_digits=15, decimal_places=3)
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_paint_product_15_6'


class OcPaintProduct20201028(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=155)
    product_sku = models.CharField(max_length=55)
    description = models.TextField()
    brand = models.IntegerField()
    product_range = models.IntegerField()
    category = models.IntegerField()
    avg_coverage = models.DecimalField(max_digits=15, decimal_places=3)
    avg_price = models.DecimalField(max_digits=15, decimal_places=3)
    pack_size = models.IntegerField()
    price_mrp = models.DecimalField(max_digits=15, decimal_places=3)
    price_project = models.DecimalField(max_digits=15, decimal_places=3)
    price_retail = models.DecimalField(max_digits=15, decimal_places=3)
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_paint_product_2020-10-28'


class OcPaintProduct20210326(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=155)
    product_sku = models.CharField(max_length=55)
    description = models.TextField()
    brand = models.IntegerField()
    product_range = models.IntegerField()
    category = models.IntegerField()
    avg_coverage = models.DecimalField(max_digits=15, decimal_places=3)
    avg_price = models.DecimalField(max_digits=15, decimal_places=3)
    pack_size = models.IntegerField()
    price_mrp = models.DecimalField(max_digits=15, decimal_places=3)
    price_project = models.DecimalField(max_digits=15, decimal_places=3)
    price_retail = models.DecimalField(max_digits=15, decimal_places=3)
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_paint_product_2021-03-26'


class OcPaintProductImage(models.Model):
    product_image_id = models.IntegerField()
    product_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    image_name = models.TextField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_paint_product_image'


class OcPaintProductRemove29Oct2020(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=155)
    product_sku = models.CharField(max_length=55)
    description = models.TextField()
    brand = models.IntegerField()
    product_range = models.IntegerField()
    category = models.IntegerField()
    avg_coverage = models.DecimalField(max_digits=15, decimal_places=3)
    avg_price = models.DecimalField(max_digits=15, decimal_places=3)
    pack_size = models.IntegerField()
    price_mrp = models.DecimalField(max_digits=15, decimal_places=3)
    price_project = models.DecimalField(max_digits=15, decimal_places=3)
    price_retail = models.DecimalField(max_digits=15, decimal_places=3)
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_paint_product_remove_29oct2020'


class OcPaintRange(models.Model):
    range_id = models.IntegerField()
    range_name = models.CharField(max_length=155)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_paint_range'


class OcPointCompensatedHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    user_mobile = models.CharField(max_length=15)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    lead_no_fk = models.IntegerField()
    sale_id_fk = models.IntegerField()
    points_compensated = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_point_compensated_history'


class OcProduct(models.Model):
    product_id = models.IntegerField()
    model = models.CharField(max_length=64)
    sku = models.CharField(max_length=64)
    upc = models.CharField(max_length=12)
    ean = models.CharField(max_length=14)
    jan = models.CharField(max_length=13)
    isbn = models.CharField(max_length=17)
    mpn = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    quantity = models.IntegerField()
    stock_status_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_id = models.IntegerField()
    shipping = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    points = models.IntegerField()
    tax_class_id = models.IntegerField()
    date_available = models.DateField()
    weight = models.DecimalField(max_digits=15, decimal_places=8)
    weight_class_id = models.IntegerField()
    length = models.DecimalField(max_digits=15, decimal_places=8)
    width = models.DecimalField(max_digits=15, decimal_places=8)
    height = models.DecimalField(max_digits=15, decimal_places=8)
    length_class_id = models.IntegerField()
    subtract = models.IntegerField()
    minimum = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    viewed = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_product'


class OcProductAttribute(models.Model):
    product_id = models.IntegerField()
    attribute_id = models.IntegerField()
    language_id = models.IntegerField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_product_attribute'


class OcProductAttributeOld(models.Model):
    product_id = models.IntegerField()
    attribute_id = models.IntegerField()
    language_id = models.IntegerField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_product_attribute_old'


class OcProductDescription(models.Model):
    product_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField()
    tag = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_product_description'
