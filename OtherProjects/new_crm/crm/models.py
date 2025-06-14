from django.db import models
from datetime import datetime
from datetime import date
from django.utils import timezone

# python manage.py migrate crm 0043 --fake
# python manage.py migrate --fake crm

# Create your models here.
class Add_Product(models.Model):
    Id = models.AutoField(primary_key=True)
    Product_Name = models.CharField(max_length=50,null=False)
    HSN_Code = models.CharField(max_length=50,null=False)
    GST_Number = models.CharField(max_length=50,null=False)

class tbl_roles(models.Model):
    roleId = models.CharField(primary_key=True, max_length=50)
    role = models.CharField(max_length=50)
    
    class Meta:
        # Specify the actual table name
        db_table = 'tbl_roles'

class tbl_users(models.Model):
    userId = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=50) 
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    roleId = models.CharField(max_length=50)
    dp_id = models.CharField(max_length=255)  # Adjust the max_length as needed

    # def get_departments(self):
    #     return self.dp_id.split(',')

    # def set_departments(self, departments):
    #     self.dp_id = ','.join(map(str, departments))
    head_id = models.CharField(max_length=50)
    createdDtm = models.DateTimeField(default=datetime.now)
    company_id = models.CharField(max_length=50)
    add_by_name = models.CharField(max_length=50)
    add_by_id = models.CharField(max_length=50)
    updated_by_id = models.CharField(max_length=50)
    updated_by_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    login_logout = models.CharField(max_length=50)
    
    # departments = models.ManyToManyField('departments')
    # roles = models.ManyToManyField('roles')
    class Meta:
        # Specify the actual table name
        db_table = 'tbl_users'
        
class tbl_users2(models.Model):
    userId = models.AutoField(primary_key=True)  # Automatically increments
    password = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)

    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)

    mobile = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True, db_collation='latin1_general_ci')
    role_id = models.CharField(max_length=50, null=True, blank=True)
    role_name = models.CharField(max_length=200, null=True, blank=True)
    # is_admin = models.BooleanField(default=False, null=True, blank=True)  # Changed to BooleanField for better readability
    # is_deleted = models.BooleanField(default=False, null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    created_dtm = models.DateTimeField(null=True, blank=True)  # Automatically set on create
    updated_by_id = models.IntegerField(null=True, blank=True)
    updated_dtm = models.DateTimeField(null=True, blank=True)
    w_s_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    user_type = models.CharField(max_length=10, null=True, blank=True)  # Renamed to avoid conflict with built-in function
    status = models.CharField(max_length=10, null=True, blank=True)
    add_by_id = models.IntegerField(null=True, blank=True)
    add_by_name = models.CharField(max_length=200, null=True, blank=True)
    updated_by_name = models.CharField(max_length=200, null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)
    company_name = models.CharField(max_length=250, db_collation='latin1_general_ci', null=True, blank=True)
    dp_id = models.CharField(max_length=250, null=True, blank=True)
    head_id = models.CharField(max_length=250, null=True, blank=True)
    login_logout = models.CharField(max_length=50, null=True, blank=True)
    emp_type = models.CharField(max_length=50, null=True, blank=True)
    emp_id = models.IntegerField(null=True, blank=True)
    intern_id = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='employee/', null=True,default=r"")

    class Meta:
        # Specify the actual table name
        db_table = 'tbl_users2'

        
class tbl_meeting(models.Model):
    meet_id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50, default="Meeting")
    mobile = models.CharField(max_length=50)
    meeting_time = models.CharField(max_length=100)
    remark   = models.CharField(max_length=50)
    created_time = models.DateTimeField(default=datetime.now)
    # meet_date = models.DateTimeField()
    add_by_name = models.CharField(max_length=50)
    add_by_id = models.CharField(max_length=50)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    company_id = models.IntegerField(null=True, blank=True)
    
    class Meta:
        # Specify the actual table name
        db_table = 'tbl_meeting'
        
class tbl_meeting_history(models.Model):
    meet_id  = models.AutoField(primary_key=True)
      
   
    name = models.CharField(max_length=50)
    
    mobile = models.CharField(max_length=50)
    remark   = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_time = models.DateTimeField(default=datetime.now)
    meet_date = models.DateTimeField()
    
    add_by_name = models.CharField(max_length=50)
    add_by_id = models.CharField(max_length=50)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    
    class Meta:
        # Specify the actual table name
        db_table = 'tbl_meeting_history'


class tbl_todo(models.Model):
    todoId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    des = models.CharField(max_length=50)
    date = models.DateTimeField()
    create_time = models.DateTimeField(default=datetime.now)
   
    class Meta:
        # Specify the actual table name
        db_table = 'tbl_todo'
# ritik login        
class tbl_log(models.Model):
    id  = models.AutoField(primary_key=True)
    ope = models.CharField(max_length=150)
    comment = models.CharField(max_length=50)
    lanti = models.FloatField()
    longti = models.FloatField()
    by_user_id = models.CharField(max_length=50)
    by_user_name = models.CharField(max_length=50)
    date_time = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'tbl_log'

class tbl_crm_todo(models.Model):
    c_t_d_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    des = models.CharField(max_length=50)
    date = models.DateTimeField()
    add_by_id = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default="Pending")
    create_time = models.DateTimeField(default=datetime.now)
    company_id = models.CharField(max_length=50)
   
    class Meta:
        # Specify the actual table name
        db_table = 'tbl_crm_todo'

class tbl_lead(models.Model):
    l_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True) 
    address = models.CharField(max_length=700, null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    remark = models.CharField(max_length=50, null=True, blank=True) 
    stage_by = models.CharField(max_length=255, null=True, blank=True)
    next_followup_date = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    segment = models.CharField(max_length=100, null=True, blank=True)
    
    user_id = models.CharField(max_length=50, null=True, blank=True) 
    name = models.CharField(max_length=50, null=True, blank=True) 
    wp_no = models.CharField(max_length=50, null=True, blank=True)
    house_no = models.CharField(max_length=50, null=True, blank=True)
    next_followup_date = models.DateTimeField(null=True, blank=True)
    lead_type = models.CharField(max_length=50, null=True, blank=True)
    service = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50 , default="Fresh", null=True, blank=True)
    file_path = models.FileField(upload_to= 'files/', null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    next_meeting_date = models.DateTimeField(null=True, blank=True)
    reason = models.CharField(max_length=50, null=True, blank=True)
    company_id = models.CharField(max_length=50, null=True, blank=True)
    lead_inq_dcr = models.CharField(max_length=50, null=True, blank=True)
    dp_id = models.CharField(max_length=50, null=True, blank=True)
    head_id = models.CharField(max_length=50, null=True, blank=True)
    add_by_id = models.CharField(max_length=50, null=True, blank=True)
    add_by_name = models.CharField(max_length=50, null=True, blank=True)
    update_by_id = models.CharField(max_length=50, null=True, blank=True)
    update_by_name = models.CharField(max_length=50, null=True, blank=True)
    date1 = models.DateTimeField(null=True, blank=True)
    assign_to = models.IntegerField(null=True, blank=True)
    business_name = models.CharField(max_length=200, null=True, blank=True)
    inqu_for = models.CharField(max_length=200, null=True, blank=True)
    
    class Meta:
        # Specify the actual table name
        db_table = 'tbl_lead'

class tbl_lead_client(models.Model):
    id = models.AutoField(primary_key=True)
    l_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100,null=True, blank=True)
    mobile = models.CharField(max_length=20,null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True)
    add_by_name = models.CharField(max_length=50, null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now,null=True, blank=True)
    
    class Meta:
        db_table = 'tbl_lead_client'
        
class tbl_cold_list(models.Model):
    l_id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.IntegerField()  
    create_time = models.DateTimeField(default=datetime.now)
    
    class Meta:
        # Specify the actual table name
        db_table = 'tbl_cold_list'
        
class tbl_dcr(models.Model):
    l_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    house_no = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=700, null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    segment = models.CharField(max_length=100, null=True, blank=True)
    remark = models.CharField(max_length=50, null=True, blank=True)
    lead_type = models.CharField(max_length=50, null=True, blank=True)
    next_meeting_date = models.DateTimeField(null=True, blank=True)
    assign_to = models.IntegerField(null=True, blank=True)
    stage_by = models.CharField(max_length=255, null=True, blank=True)
    add_by_id = models.CharField(max_length=50, null=True, blank=True)
    add_by_name = models.CharField(max_length=50, null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50 , default="Fresh")
    next_followup_date = models.DateTimeField(null=True, blank=True)
    company_id = models.CharField(max_length=50, null=True, blank=True)
    user_id = models.CharField(max_length=50, null=True, blank=True)
    wp_no = models.CharField(max_length=50, null=True, blank=True)
    service = models.CharField(max_length=50, null=True, blank=True)
    file_path = models.FileField(upload_to= 'files/',null=True)
    reason = models.CharField(max_length=50, null=True, blank=True)
    dp_id = models.CharField(max_length=50, null=True, blank=True)
    head_id = models.CharField(max_length=50, null=True, blank=True)
    inqu_for = models.CharField(max_length=200, null=True, blank=True)
    
    class Meta:
        db_table = 'tbl_dcr'

class tbl_dcr_client(models.Model):
    id = models.AutoField(primary_key=True)
    l_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100,null=True, blank=True)
    mobile = models.CharField(max_length=20,null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True)
    add_by_name = models.CharField(max_length=50, null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now,null=True, blank=True)
    
    class Meta:
        db_table = 'tbl_dcr_client'

# class master_city(models.Model):
#     city_id = models.CharField(primary_key=True, max_length=50)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     country = models.CharField(max_length=50)
#     class Meta:
#         # Specify the actual table name
#         db_table = 'master__city'

class master_service(models.Model):
    srv_id = models.AutoField(primary_key=True)
    service = models.CharField(max_length=50)
    
    class Meta:
        # Specify the actual table name
        db_table = 'master__service'

class master_leadtype(models.Model):
    ldt_id = models.AutoField(primary_key=True)
    lead_Type = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.now)
    
    class Meta:
        # Specify the actual table name
        db_table = 'master__leadtype'
        

class master_shift(models.Model):
    s_id = models.AutoField(primary_key=True)
    shift = models.CharField(max_length=50)
    start_time = models.TimeField()  # Changed to TimeField
    end_time = models.TimeField()    # Changed to TimeField
    create_time = models.DateTimeField(default=datetime.now)
    
    class Meta:
        # Specify the actual table name
        db_table = 'master__shift'

class master_status(models.Model):
    s_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.now)
    
    
    class Meta:
        # Specify the actual table name
        db_table = 'master__status'

class master_service(models.Model):
    srv_id = models.AutoField(primary_key=True)
    service = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.now)
    
    class Meta:
        # Specify the actual table name
        db_table = 'master__service'


class tbl_quatation_history(models.Model):
    qu_id = models.AutoField(primary_key=True)
    file_name = models.FileField(upload_to='uploads/', null=True)
    l_id = models.CharField(max_length=50)
    createDtm = models.DateTimeField(default=datetime.now)

    class Meta:
        # Specify the actual table name
        db_table = 'tbl_quatation_history'

class master_inqclosereason(models.Model):
    id = models.AutoField(primary_key=True)
    inqCloseReason = models.CharField(max_length=50)
    

    class Meta:
        # Specify the actual table name
        db_table = 'master__inqclosereason'

class tbl_followup(models.Model):
    f_id = models.AutoField(primary_key=True)
    lead_id = models.CharField(max_length=50,null=True, blank=True)
    followupRemarks = models.CharField(max_length=50,null=True, blank=True)
    remark = models.CharField(max_length=50,null=True, blank=True)
    reason = models.CharField(max_length=50,null=True, blank=True)
    company_id = models.CharField(max_length=50,null=True, blank=True)
    next_meeting_date = models.DateTimeField(null=True, blank=True)
    next_followup_date = models.DateTimeField(null=True, blank=True)
    create_time = models.DateTimeField(default=timezone.now)
    add_by_name = models.CharField(max_length=50)
    add_by_id = models.CharField(max_length=50)
   
    head_id = models.CharField(max_length=50)



    class Meta:
        # Specify the actual table name
        db_table = 'tbl_followup'

class tbl_crm_mobile(models.Model):
    m_id = models.AutoField(primary_key=True)
    lead_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
   


    class Meta:
        # Specify the actual table name
        db_table = 'tbl_crm_mobile'

class master_company(models.Model):
    com_id = models.AutoField(primary_key=True)
    add_by_id = models.CharField(max_length=50)
    com_name = models.CharField(max_length=50)
    add_by_name = models.CharField(max_length=50)
    mobile = models.BigIntegerField()  
    address = models.CharField(max_length=50)
    area = models.CharField(max_length=50) 
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    gst_no = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.now)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    acc_no = models.CharField(max_length=50) 
    ifsc_code = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    beneficiary_name = models.CharField(max_length=255)
    opening_balance = models.IntegerField()  
    class Meta:
        # Specify the actual table name
        db_table = 'master__company'
 
class master_product(models.Model):
    pro_id = models.AutoField(primary_key=True)
    add_by_id = models.CharField(max_length=50)
    pro_name = models.CharField(max_length=50)
    gst_no = models.CharField(max_length=50)
    add_by_name = models.CharField(max_length=50)
    hsn_code = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.now)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    class Meta:
        # Specify the actual table name
        db_table = 'master__product'

class tbl_invc(models.Model):
    inv_id = models.AutoField(primary_key=True)
    inv_number = models.CharField(max_length=50)
    client_name = models.CharField(max_length=50)
    add_by_id = models.CharField(max_length=50)   
    comp_name = models.CharField(max_length=50)
    add_by_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    quantity = models.IntegerField()
    mobile = models.IntegerField()
    pv_id  = models.IntegerField()
    rv_id  = models.IntegerField()
    clt_id  = models.IntegerField()
    address = models.CharField(max_length=50) 
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50) 
    gst_no = models.CharField(max_length=50)
    perticular = models.CharField(max_length=50)
    gst_per = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_status = models.CharField(max_length=50, default="Pending")
    pay_mode = models.CharField(max_length=50)
    invc_date = models.DateTimeField()
    company_id = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.now)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50)
    HSN_code = models.CharField(max_length=50)
    texable_am = models.DecimalField(max_digits=10, decimal_places=2)
    gst_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cgst_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sgst_amount = models.DecimalField(max_digits=10, decimal_places=2)
    igst_amount = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_st = models.CharField(max_length=50)
    unit_measure = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'tbl_invc'
        
        
class tbl_invoice(models.Model):
    inv_id = models.AutoField(primary_key=True)
    
    # Details:
    invNumber = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    compGst = models.CharField(max_length=50, null=True, blank=True)
    
    # Company:
    compName = models.CharField(max_length=50, null=True, blank=True)
    compAddress = models.CharField(max_length=50, null=True, blank=True)
    compMoNumber = models.BigIntegerField(null=True, blank=True)  # Use BigIntegerField for large numbers
    
    # Client:
    clt_id  = models.IntegerField()
    clientName = models.CharField(max_length=100, null=True, blank=True)
    clientcom = models.CharField(max_length=100, null=True, blank=True)
    clientMail = models.EmailField(max_length=50, null=True, blank=True)  # Consider using EmailField for email
    clientMoNumber = models.BigIntegerField(null=True, blank=True)  # Use BigIntegerField for large numbers
    clientAddress = models.CharField(max_length=255, null=True, blank=True)
    clientGst = models.CharField(max_length=50, null=True, blank=True)
    clientState = models.CharField(max_length=50, null=True, blank=True)
    
    # Product:
    productName = models.CharField(max_length=50, null=True, blank=True)
    unitOfMeasure = models.CharField(max_length=50, null=True, blank=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Changed to DecimalField
    hsn = models.BigIntegerField(null=True, blank=True)  # Use BigIntegerField for HSN codes
    rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Changed to DecimalField
    taxableAmount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Changed to DecimalField
    gstPercentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Changed to DecimalField
    gstAmount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Changed to DecimalField
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Changed to DecimalField
    
    # GST Type:
    cgst = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Changed to DecimalField
    sgst = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Changed to DecimalField
    igst = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Changed to DecimalField
    grandAmount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Changed to DecimalField
    
    add_by_id = models.CharField(max_length=50, null=True, blank=True)
    add_by_name = models.CharField(max_length=50, null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)  # Automatically set on creation
    update_by_id = models.CharField(max_length=50, null=True, blank=True)
    update_by_name = models.CharField(max_length=50, null=True, blank=True)
    company_id = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'tbl_invoice'


class tbl_payment_v(models.Model):
    pv_id = models.AutoField(primary_key=True)
    vouch_num = models.CharField(max_length=50)
    name = models.CharField(max_length=100, null=True, blank=True)
    comp_name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    gst_no = models.CharField(max_length=50, null=True, blank=True)
    perticular = models.CharField(max_length=50, null=True, blank=True)
    gst_per = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    remark = models.CharField(max_length=100, null=True, blank=True)
    payment_mode = models.CharField(max_length=50, null=True, blank=True)
    online_payment_method = models.CharField(max_length=50, null=True, blank=True)
    bank_name = models.CharField(max_length=50, null=True, blank=True)
    cheque_no = models.CharField(max_length=50, null=True, blank=True)
    cheque_date = models.DateTimeField(null=True, blank=True)
    cheque_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    client_type = models.CharField(max_length=50, null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=50, null=True, blank=True)
    add_by_name = models.CharField(max_length=50, null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now)
    update_by_id = models.CharField(max_length=50, null=True, blank=True)
    update_by_name = models.CharField(max_length=50, null=True, blank=True)
    inv_number = models.CharField(max_length=50 ,null=True, blank=True)
    city = models.CharField(max_length=50 , null=True, blank=True) 
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    clt_id = models.IntegerField(null=True, blank=True)
    cheque = models.CharField(max_length=50, null=True, blank=True)
    reason = models.CharField(max_length=100, null=True, blank=True)
    transaction_type = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        # Specify the actual table name
        db_table = 'tbl_payment_v'

class tbl_receive_v(models.Model): 
    rv_id = models.AutoField(primary_key=True)
    vouch_num = models.CharField(max_length=50)
    name = models.CharField(max_length=100, null=True, blank=True)
    comp_name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    gst_no = models.CharField(max_length=50, null=True, blank=True)
    perticular = models.CharField(max_length=50, null=True, blank=True)
    gst_per = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    remark = models.CharField(max_length=100, null=True, blank=True)
    payment_mode = models.CharField(max_length=50, null=True, blank=True)
    online_payment_method = models.CharField(max_length=50, null=True, blank=True)
    bank_name = models.CharField(max_length=50, null=True, blank=True)
    cheque_no = models.CharField(max_length=50, null=True, blank=True)
    cheque_date = models.DateTimeField(null=True, blank=True)
    cheque_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    client_type = models.CharField(max_length=50, null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=50, null=True, blank=True)
    add_by_name = models.CharField(max_length=50, null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now)
    update_by_id = models.CharField(max_length=50, null=True, blank=True)
    update_by_name = models.CharField(max_length=50, null=True, blank=True)
    inv_number = models.CharField(max_length=50 ,null=True, blank=True)
    city = models.CharField(max_length=50 , null=True, blank=True) 
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    clt_id = models.IntegerField(null=True, blank=True)
    cheque = models.CharField(max_length=50, null=True, blank=True)
    reason = models.CharField(max_length=100, null=True, blank=True)
    transaction_type = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        # Specify the actual table name
        db_table = 'tbl__receive_v'

class tbl_expense(models.Model):
    exp_id = models.AutoField(primary_key=True)
    
    add_by_id = models.CharField(max_length=50)   
   
    add_by_name = models.CharField(max_length=50)
   
    perticular = models.CharField(max_length=50)
  
    amount = models.CharField(max_length=50)
  
    exp_date = models.CharField(max_length=50)
    company_id = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.now)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    class Meta:
        # Specify the actual table name
        db_table = 'tbl_expense'

class tbl_amc(models.Model):
    amc_id = models.AutoField(primary_key=True)
    clt_id = models.IntegerField(null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    p_name = models.CharField(max_length=50, null=True, blank=True)
    amc_type= models.CharField(max_length=50, null=True, blank=True)
    amc_percentage = models.CharField(max_length=50, null=True, blank=True) 
    amc_amount = models.CharField(max_length=50, null=True, blank=True)
    server_sdate = models.DateTimeField(null=True, blank=True)
    server_edate = models.DateTimeField(null=True, blank=True)
    server_price = models.CharField(max_length=50, null=True, blank=True)
    Domain_type = models.CharField(max_length=50, null=True, blank=True)
    domain_company = models.CharField(max_length=50, null=True, blank=True)
    dom_startdate = models.DateTimeField(null=True, blank=True)
    dom_redate = models.DateTimeField(null=True, blank=True)
    dom_amount = models.CharField(max_length=50, null=True, blank=True)
    
    email = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True) 
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    amc_redate = models.DateTimeField(null=True, blank=True)
    host_ser_type = models.CharField(max_length=50, null=True, blank=True)
    host_ser_price = models.CharField(max_length=50, null=True, blank=True)
    host_ser_redate = models.DateTimeField(null=True, blank=True)
    project_include = models.CharField(max_length=50, null=True, blank=True) 
    host_type = models.CharField(max_length=50, null=True, blank=True)
    host_amount = models.CharField(max_length=50, null=True, blank=True)
    user_id = models.CharField(max_length=50, null=True, blank=True)
    add_by_id = models.CharField(max_length=50, null=True, blank=True)   
    add_by_name = models.CharField(max_length=50, null=True, blank=True)
    domtype = models.CharField(max_length=50, null=True, blank=True)
    dom_id = models.CharField(max_length=50, null=True, blank=True)
    dom_pass = models.CharField(max_length=50, null=True, blank=True)
    host_redate = models.DateTimeField(null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    company_id = models.CharField(max_length=50)
    
    class Meta:
        # Specify the actual table name
        db_table = 'tbl_amc'

class tbl_smo(models.Model):
    smoId = models.AutoField(primary_key=True)
    clt_id  = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=250, null=True, blank=True)
    comp_name = models.CharField(max_length=250, null=True, blank=True)
    c_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    mobile = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    service_type = models.CharField(max_length=50, null=True, blank=True)
    plan_type = models.CharField(max_length=250, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    no_of_post = models.CharField(max_length=250, null=True, blank=True)
    no_of_reel = models.CharField(max_length=250, null=True, blank=True)
    remark = models.CharField(max_length=50, null=True, blank=True)
    seo_start = models.DateTimeField(null=True, blank=True)
    seo_expire = models.DateTimeField(null=True, blank=True)
    add_by_name = models.CharField(max_length=250, null=True, blank=True)
    add_by_id = models.CharField(max_length=250, null=True, blank=True)
    update_by_name = models.CharField(max_length=250, null=True, blank=True)
    update_by_id = models.CharField(max_length=250, null=True, blank=True)
    company_id = models.CharField(max_length=50, null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    post_count = models.CharField(max_length=50, null=True, blank=True)
    reel_count = models.CharField(max_length=50, null=True, blank=True)
    plan_id = models.IntegerField(null=True, blank=True)
    seo_plan_id = models.IntegerField(null=True, blank=True)
    web_url = models.CharField(max_length=50, null=True, blank=True)
    face_uname = models.CharField(max_length=50, null=True, blank=True)
    face_pass = models.CharField(max_length=50, null=True, blank=True)
    insta_uname = models.CharField(max_length=50, null=True, blank=True)
    insta_pass = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'tbl_smo'

class master_client(models.Model):
    clt_id = models.AutoField(primary_key=True)
    add_by_id = models.CharField(max_length=50, null=True, blank=True)   
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    comp_name = models.CharField(max_length=50, null=True, blank=True)
    add_by_name = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    client_type = models.CharField(max_length=50, null=True, blank=True)
    billing_add = models.CharField(max_length=500, null=True, blank=True)
    shipping_add = models.CharField(max_length=500, null=True, blank=True)
    same_as_billing = models.CharField(max_length=10, null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    gst_number = models.CharField(max_length=50, null=True, blank=True)
    pan_card = models.CharField(max_length=50, null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)
    service_type = models.CharField(max_length=50, null=True, blank=True)
    Plan = models.CharField(max_length=50, null=True, blank=True)
    remark = models.CharField(max_length=50, null=True, blank=True)
    p_s_date = models.DateTimeField(null=True, blank=True)
    p_e_date = models.DateTimeField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    expire_date = models.DateTimeField(null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    transaction_type = models.CharField(max_length=50, null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    
    class Meta:
        # Specify the actual table name
        db_table = 'master__client'
        
class master_client1(models.Model):
    cId = models.AutoField(primary_key=True)
    add_by_id = models.CharField(max_length=50, null=True, blank=True)
    add_by_name = models.CharField(max_length=50, null=True, blank=True)
    company_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=10)
    gst_no = models.CharField(max_length=15)
    bill_add = models.CharField(max_length=255)
    ope_balance = models.DecimalField(max_digits=10, decimal_places=2)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    class Meta:
        # Specify the actual table name
        db_table = 'master__client1'

class master_bank(models.Model):
    b_id = models.AutoField(primary_key=True)
    add_by_id = models.CharField(max_length=50)   
    bank_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    add_by_name = models.CharField(max_length=50)
    acc_no = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=50)
    opening_bal = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=50)
    cheque = models.ImageField(upload_to='uploads/', null=True)
    create_dnt = models.DateTimeField(default=datetime.now)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    class Meta:
        # Specify the actual table name
        db_table = 'master__bank'

class master_project(models.Model):
    pj_id = models.AutoField(primary_key=True)
    add_by_id = models.CharField(max_length=50, null=True, blank=True)
    c_name = models.CharField(max_length=50, null=True, blank=True)
    pro_name = models.CharField(max_length=50, null=True, blank=True)
    com_id = models.IntegerField(null=True, blank=True)
    des = models.CharField(max_length=50, null=True, blank=True)
    add_by_name = models.CharField(max_length=50, null=True, blank=True)
    service = models.CharField(max_length=50, null=True, blank=True)
    client_date = models.DateField(null=True, blank=True)
    tech_date = models.DateField(null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now, null=True, blank=True)
    status = models.CharField(max_length=50 , default="Pending", null=True, blank=True)
    update_by_id = models.CharField(max_length=50, null=True, blank=True)
    update_by_name = models.CharField(max_length=50, null=True, blank=True)
    complete_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        # Specify the actual table name
        db_table = 'master__project'

class tbl_task(models.Model):
    taskId = models.AutoField(primary_key=True)
    task_type = models.CharField(max_length=50, null=True, blank=True)
    task_name = models.CharField(max_length=50, null=True, blank=True)
    assign_to = models.IntegerField(null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    dead_date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=50 , default="Pending", null=True, blank=True)
    assign_by = models.CharField(max_length=50, null=True, blank=True)
    assign_date = models.DateTimeField(null=True, blank=True)
    company_id = models.CharField(max_length=50, null=True, blank=True)
    add_by_id = models.CharField(max_length=50, null=True, blank=True)
    add_by_name = models.CharField(max_length=50, null=True, blank=True)
    createdDtm = models.DateTimeField(null=True, blank=True)
    update_by_id = models.CharField(max_length=50, null=True, blank=True)
    update_by_name = models.CharField(max_length=50, null=True, blank=True)
    updatedDtm = models.DateTimeField(null=True, blank=True)
    remark = models.CharField(max_length=500, null=True, blank=True)
    complete_date = models.DateTimeField(null=True, blank=True)
    delay_count = models.CharField(max_length=500, null=True, blank=True)
    # uniqueId = models.CharField(max_length=50, null=True, blank=True)
    # client_date = models.DateTimeField(null=True, blank=True)
    # tech_date = models.DateTimeField(null=True, blank=True)
    # service = models.CharField(max_length=50, null=True, blank=True)
    # modual = models.CharField(max_length=50, null=True, blank=True)
    # total_task = models.CharField(max_length=50, null=True, blank=True)
    # head_id = models.CharField(max_length=50, null=True, blank=True)
    # dp_id = models.CharField(max_length=50, null=True, blank=True)
    
    
    class Meta:
        # Specify the actual table name
        db_table = 'tbl_task'

class tbl_task2(models.Model):
    taskId = models.AutoField(primary_key=True)
    uniqueId = models.CharField(max_length=50)
    task_name = models.CharField(max_length=50)
    add_by_id = models.CharField(max_length=50)   
    description = models.CharField(max_length=50)
    add_by_name = models.CharField(max_length=50)
    client_date = models.IntegerField()  
    tech_date = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    assign_to = models.CharField(max_length=50)
    assign_by = models.CharField(max_length=50)
    assign_date = models.CharField(max_length=50)
   
    updatedDtm = models.CharField(max_length=50)
    dead_date = models.CharField(max_length=50)
   
    task_type = models.CharField(max_length=50)
    total_task = models.CharField(max_length=50)
    company_id = models.CharField(max_length=50)
    createdDtm = models.DateTimeField(default=datetime.now)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50 , default="Pending")
    
    
    class Meta:
        # Specify the actual table name
        db_table = 'tbl_task2'

class master_department(models.Model):
    dp_id  = models.AutoField(primary_key=True)
    add_by_id = models.CharField(max_length=50)   
    dep_name = models.CharField(max_length=100)
    add_by_name = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.now)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    company_id = models.IntegerField(null=True, blank=True)
    
    class Meta:
        # Specify the actual table name
        db_table = 'master__department'

class tbl_daily_report(models.Model):
    repoId  = models.AutoField(primary_key=True)
    userId = models.CharField(max_length=50)
    lep1 = models.CharField(max_length=1000)
    add_by_id = models.IntegerField(null=True, blank=True)   
    lep2 = models.CharField(max_length=1000)
    add_by_name = models.CharField(max_length=50)
    lep3 = models.CharField(max_length=1000) 
    status = models.CharField(max_length=50) 
    leave_type = models.CharField(max_length=50)
    l_type_id = models.CharField(max_length=50)  
    company_id = models.CharField(max_length=50)
    dp_id = models.CharField(max_length=50)
    head_id = models.CharField(max_length=50)
    reportDate = models.DateTimeField(default=datetime.now)
    leave_date = models.DateField(default=date.today)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    
    class Meta:
        # Specify the actual table name
        db_table = 'tbl_daily_report'
        
class master_city(models.Model):
    city_id  = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    add_by_id = models.CharField(max_length=50)
    add_by_name = models.CharField(max_length=50)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    
    createdDtm = models.DateTimeField(default=datetime.now)
   
    class Meta:
        # Specify the actual table name
        db_table = 'master__city'
        
        
class master_state(models.Model):
    st_id   = models.AutoField(primary_key=True)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    add_by_id = models.CharField(max_length=50)
    add_by_name = models.CharField(max_length=50)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    
    createdDtm = models.DateTimeField(default=datetime.now)
   
    class Meta:
        # Specify the actual table name
        db_table = 'master__state'
        
class master_country(models.Model):
    con_id    = models.AutoField(primary_key=True)
    
    country = models.CharField(max_length=50)
    add_by_id = models.CharField(max_length=50)
    add_by_name = models.CharField(max_length=50)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    
    createdDtm = models.DateTimeField(default=datetime.now)
   
    class Meta:
        # Specify the actual table name
        db_table = 'master__country'
       
class tbl_intern(models.Model):
    emp_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=200, null=True, blank=True)
    
    # personal information
    name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    marital_status = models.CharField(max_length=200, null=True, blank=True)
    machine_id = models.IntegerField(null=True, blank=True)
    ph_no = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    emer_cont_pers = models.CharField(max_length=200, null=True, blank=True)
    emer_cont_ph_no = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=200, null=True, blank=True)
    
    # other information
    emp_type = models.CharField(max_length=200, null=True, blank=True)
    attendence_time = models.CharField(max_length=200, null=True, blank=True)
    gross_sal = models.CharField(max_length=200, null=True, blank=True)
    college_name = models.CharField(max_length=200, null=True, blank=True)
    college_id = models.CharField(max_length=200, null=True, blank=True)
    enrollment_no = models.CharField(max_length=200, null=True, blank=True)
    intern_id_custom = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    head_id = models.IntegerField(null=True, blank=True)
    join_date = models.DateTimeField(null=True, blank=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)
    company_name = models.CharField(max_length=250, db_collation='latin1_general_ci', null=True, blank=True)
    dp_id = models.CharField(max_length=250, null=True, blank=True)
    role_id = models.CharField(max_length=12, null=True, blank=True)
    role_name = models.CharField(max_length=50, null=True, blank=True)
    
    # Bank information
    stipend = models.CharField(max_length=20, null=True, blank=True)
    acc_num = models.CharField(max_length=200, null=True, blank=True)
    acc_holder_name = models.CharField(max_length=200, null=True, blank=True)
    bank_name = models.CharField(max_length=200, null=True, blank=True)
    ifsc_code = models.CharField(max_length=200, null=True, blank=True)
    branch_add = models.CharField(max_length=200, null=True, blank=True)
    
    # Benifits
    med_benifit = models.CharField(max_length=200, null=True, blank=True)
    family_benifit = models.CharField(max_length=200, null=True, blank=True)
    transport_benifit = models.CharField(max_length=200, null=True, blank=True)
    other_benifit = models.CharField(max_length=200, null=True, blank=True)
    
    # others imp
    add_by_id = models.CharField(max_length=200, null=True, blank=True)
    add_by_name = models.CharField(max_length=200, null=True, blank=True)
    update_by_id = models.CharField(max_length=200, null=True, blank=True)
    update_by_name = models.CharField(max_length=200, null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now) 
    is_active = models.BooleanField(default=True)
    
    # doccuments
    aadhar_pdf = models.FileField(upload_to='intern/', null=True,default=r"")
    pan_pdf = models.FileField(upload_to='intern/', null=True,default=r"")
    photo = models.ImageField(upload_to='intern/', null=True,default=r"")
    joining_letter = models.FileField(upload_to='intern/', null=True,default=r"")
    bank_statement = models.FileField(upload_to='intern/', null=True,default=r"")

    class Meta:
        db_table = 'tbl_intern'

class tbl_employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=200, null=True, blank=True)
    
    # personal information
    name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    marital_status = models.CharField(max_length=200, null=True, blank=True)
    machine_id = models.IntegerField(null=True, blank=True)
    ph_no = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    emer_cont_pers = models.CharField(max_length=200, null=True, blank=True)
    emer_cont_ph_no = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=200, null=True, blank=True)
    
    # other information
    attendence_time = models.CharField(max_length=200, null=True, blank=True)
    gross_sal = models.CharField(max_length=200, null=True, blank=True)
    emp_type = models.CharField(max_length=200, null=True, blank=True)
    employee_id_custom = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    head_id = models.IntegerField(null=True, blank=True)
    join_date = models.DateTimeField(null=True, blank=True)
    termi_date = models.DateTimeField(null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)
    company_name = models.CharField(max_length=250, db_collation='latin1_general_ci', null=True, blank=True)
    dp_id = models.CharField(max_length=250, null=True, blank=True)
    role_id = models.CharField(max_length=12, null=True, blank=True)
    role_name = models.CharField(max_length=50, null=True, blank=True)
    
    # Bank information
    acc_num = models.CharField(max_length=200, null=True, blank=True)
    acc_holder_name = models.CharField(max_length=200, null=True, blank=True)
    bank_name = models.CharField(max_length=200, null=True, blank=True)
    ifsc_code = models.CharField(max_length=200, null=True, blank=True)
    branch_add = models.CharField(max_length=200, null=True, blank=True)
    
    # Benifits
    med_benifit = models.CharField(max_length=200, null=True, blank=True)
    family_benifit = models.CharField(max_length=200, null=True, blank=True)
    transport_benifit = models.CharField(max_length=200, null=True, blank=True)
    other_benifit = models.CharField(max_length=200, null=True, blank=True)
    
    # others imp
    add_by_id = models.CharField(max_length=200, null=True, blank=True)
    add_by_name = models.CharField(max_length=200, null=True, blank=True)
    update_by_id = models.CharField(max_length=200, null=True, blank=True)
    update_by_name = models.CharField(max_length=200, null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now) 
    is_active = models.BooleanField(default=True)
    
    # doccuments
    aadhar_pdf = models.FileField(upload_to='employee/', null=True,default=r"")
    pan_pdf = models.FileField(upload_to='employee/', null=True,default=r"")
    photo = models.ImageField(upload_to='employee/', null=True,default=r"")
    joining_letter = models.FileField(upload_to='employee/', null=True,default=r"")
    bank_statement = models.FileField(upload_to='employee/', null=True,default=r"")
    # aadhar_pdf = models.FileField(upload_to='employee/', null=True,default=r"/employee/default.pdf")
    # pan_pdf = models.FileField(upload_to='employee/', null=True,default=r"/employee/default.pdf")
    # photo = models.ImageField(upload_to='employee/', null=True,default=r"/employee/default.png")
    # joining_letter = models.FileField(upload_to='employee/', null=True,default=r"/employee/default.pdf")
    # bank_statement = models.FileField(upload_to='employee/', null=True,default=r"/employee/default.pdf")

    class Meta:
        db_table = 'tbl_employee'

# class tbl_employee(models.Model):
#     emp_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     maiden_name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     ph_no = models.CharField(max_length=200)
#     alt_ph_no = models.CharField(max_length=200)
#     country = models.CharField(max_length=200)
#     city = models.CharField(max_length=200)
#     zip_code = models.CharField(max_length=200)
#     password = models.CharField(max_length=50)
#     attendence_time = models.CharField(max_length=200)
#     emp_type = models.CharField(max_length=200)
#     acc_num = models.CharField(max_length=200)
#     bank_name = models.CharField(max_length=200)
#     ifsc_code = models.CharField(max_length=200)
#     branch_add = models.CharField(max_length=200)
#     basic_sal = models.CharField(max_length=200)
#     travel_allow = models.CharField(max_length=200)
#     gross_sal = models.CharField(max_length=200)
#     tin_no = models.CharField(max_length=200)
#     sub_dept = models.CharField(max_length=200)
#     position = models.CharField(max_length=200)
#     duty_type = models.CharField(max_length=200)
#     join_date = models.DateTimeField()
#     hire_date = models.DateTimeField()
#     rate_type = models.CharField(max_length=200)
#     monthly_work_hrs = models.CharField(max_length=200)
#     pay_freq = models.CharField(max_length=200)
#     hourly_rate = models.CharField(max_length=200)
#     dept_tax = models.CharField(max_length=200)
#     termi_date = models.DateTimeField()
#     volunt_termi = models.CharField(max_length=200)
#     re_hire_date = models.DateTimeField()
#     rate = models.CharField(max_length=200)
#     rejoin_pay_freq = models.CharField(max_length=200)
#     rehourly_rate = models.CharField(max_length=200)
#     home_dept = models.CharField(max_length=200)
#     med_benifit = models.CharField(max_length=200)
#     family_benifit = models.CharField(max_length=200)
#     transport_benifit = models.CharField(max_length=200)
#     other_benifit = models.CharField(max_length=200)
#     class_code = models.CharField(max_length=200)
#     class_desc = models.CharField(max_length=200)
#     class_acc_date = models.DateTimeField()
#     class_status = models.CharField(max_length=200)
#     supervisor_name = models.CharField(max_length=200)
#     first_superv = models.CharField(max_length=200)
#     superv_class_desc = models.CharField(max_length=200)
#     report_to = models.CharField(max_length=200)
#     date_of_birth = models.DateTimeField()
#     gender = models.CharField(max_length=200)
#     marital_status = models.CharField(max_length=200)
#     ethnic_group = models.CharField(max_length=200)
#     sos = models.CharField(max_length=200)
#     work_city = models.CharField(max_length=200)
#     city_residence = models.CharField(max_length=200)
#     work_permit = models.CharField(max_length=200)
#     photo = models.ImageField(upload_to='uploads/', null=True)
#     home_mail = models.CharField(max_length=200)
#     business_mail = models.CharField(max_length=200)
#     home_ph_no = models.CharField(max_length=200)
#     busi_ph_no = models.CharField(max_length=200)
#     cell_phone = models.CharField(max_length=200)
#     emer_cont_pers = models.CharField(max_length=200)
#     emer_cont_ph_no = models.CharField(max_length=200)
#     emer_home_ph_no = models.CharField(max_length=200)
#     emer_work_ph_no = models.CharField(max_length=200)
#     emer_cont_relation = models.CharField(max_length=200)
#     busi_mail = models.CharField(max_length=200)
#     alt_emer_cont_ph_no = models.CharField(max_length=200)
#     alt_emer_home_ph_no = models.CharField(max_length=200)
#     alt_emer_work_ph_no = models.CharField(max_length=200)
#     add_by_id = models.CharField(max_length=200)
#     add_by_name = models.CharField(max_length=200)
#     update_by_id = models.CharField(max_length=200)
#     update_by_name = models.CharField(max_length=200)
#     company_id = models.CharField(max_length=50)
#     create_time = models.DateTimeField(default=datetime.now) 
    
#     class Meta:
#         # Specify the actual table name
#         db_table = 'tbl_employee'
        
        
class master_unit(models.Model):
    unit_id  = models.AutoField(primary_key=True)
    add_by_id = models.CharField(max_length=50)
    unit_of_measurment = models.CharField(max_length=50)
    
    add_by_name = models.CharField(max_length=50)
   
    create_time = models.DateTimeField(default=datetime.now)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    class Meta:
        # Specify the actual table name
        db_table = 'master__unit'
        
class tbl_holiday(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    no_days = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10,null=True, blank=True)
    add_by_name = models.CharField(max_length=50, null=True, blank=True)
    update_by_id = models.CharField(max_length=10,null=True, blank=True)
    update_by_name = models.CharField(max_length=50,null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table = 'tbl_holiday'   
        
        
class tbl_holiday_week(models.Model):
    h_id = models.CharField(primary_key=True, max_length=150)
    name = models.CharField(max_length=100)
    add_by_id = models.CharField(max_length=50)
    update_by_id = models.CharField(max_length=50)
    update_by_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'tbl_holiday_week'   
        
    
class tbl_leave_appli(models.Model):
    leave_id = models.AutoField(primary_key=True) 
    emp_id = models.CharField(max_length=50, null=True, blank=True)
    emp_name = models.CharField(max_length=50, null=True, blank=True)
    leave_type = models.CharField(max_length=50, null=True, blank=True)
    app_start_date = models.DateTimeField(null=True, blank=True)
    app_end_date = models.DateTimeField(null=True, blank=True)
    apply_day = models.CharField(max_length=50)
    app_hard_copy = models.FileField(upload_to='uploads/', null=True)
    appr_start_date = models.DateTimeField(null=True, blank=True)
    appr_end_date = models.DateTimeField(null=True, blank=True)
    appr_day = models.CharField(max_length=50, null=True, blank=True)
    reason = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    add_by_id = models.CharField(max_length=50)
    add_by_name = models.CharField(max_length=50)
    upd_by_id = models.CharField(max_length=50, null=True, blank=True)
    upd_by_name = models.CharField(max_length=50, null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now)
    allocation_to = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'tbl_leave_appli' 
    
    
class tbl_letter(models.Model):
    l_Id = models.AutoField(primary_key=True) 
    appointment_letter = models.FileField(upload_to='uploads/appointment_letters/')
    offer_letter = models.FileField(upload_to='uploads/offer_letters/')
    bond_letter = models.FileField(upload_to='uploads/bond_letters/')
    experience_letter = models.FileField(upload_to='uploads/experience_letters/')
    salary_slip = models.FileField(upload_to='uploads/salary_slips/')
    
    class Meta:
        db_table = 'tbl_letter' 

class tbl_messages(models.Model):
    messages_id = models.AutoField(primary_key=True)
    message_name = models.CharField(max_length=255, null=True, blank=True)
    change_status = models.CharField(max_length=255, null=True, blank=True)
    added_date = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    
    class Meta:
        db_table = 'tbl_messages'      
    
class tbl_plan(models.Model):
    id = models.AutoField(primary_key=True)
    plan = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    duration = models.CharField(max_length=500, null=True, blank=True)
    type = models.CharField(max_length=2000, null=True, blank=True)
    plan_duration = models.CharField(max_length=500, null=True, blank=True)
    feature = models.CharField(max_length=2000, null=True, blank=True)
    status = models.CharField(max_length=500, null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now)
    add_by_id = models.CharField(max_length=200, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_plan'
    
class tbl_post(models.Model):
    id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=500, null=True, blank=True)
    client_id = models.IntegerField(null=True, blank=True)
    post_date =  models.DateTimeField(null=True, blank=True)
    post_type = models.CharField(max_length=500, null=True, blank=True)
    no_of_post = models.CharField(max_length=500, null=True, blank=True)
    no_of_reel = models.CharField(max_length=500, null=True, blank=True)
    remark = models.CharField(max_length=500, null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now)
    add_by_name = models.CharField(max_length=200, null=True, blank=True) 
    add_by_id = models.CharField(max_length=200, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_post'  
    
class tbl_reason(models.Model):
    id = models.AutoField(primary_key=True)
    reason = models.CharField(max_length=500, null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_reason' 
        
class tbl_pending(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.IntegerField(null=True, blank=True)
    product = models.CharField(max_length=100, null=True, blank=True)
    amount = models.CharField(max_length=50, null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_pending'    
   
class tbl_adv_salary(models.Model):
    s_id = models.AutoField(primary_key=True)
    emp_id = models.IntegerField(null=True, blank=True)
    adv_salary = models.IntegerField(null=True, blank=True)
    salary_date = models.DateTimeField(null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 
    remark = models.CharField(max_length=200, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_adv_salary'    

class tbl_attendances(models.Model):
    att_id = models.AutoField(primary_key=True)
    machine_id = models.CharField(max_length=50, null=True, blank=True)
    user_name = models.CharField(max_length=100, null=True, blank=True)
    punch_in = models.CharField(max_length=50, null=True, blank=True)
    punch_out = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    days = models.CharField(max_length=50, null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_attendances'

class tbl_break(models.Model):
    br_id = models.AutoField(primary_key=True)
    machine_id = models.CharField(max_length=50, null=True, blank=True)
    user_name = models.CharField(max_length=100, null=True, blank=True)
    punches = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    days = models.CharField(max_length=50, null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_break'


class tbl_hiring(models.Model):
    hiring_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    applying_for = models.CharField(max_length=50, null=True, blank=True)
    preferred_technology = models.CharField(max_length=50, null=True, blank=True)
    clg_name = models.CharField(max_length=100, null=True, blank=True)
    internship_duration = models.CharField(max_length=50, null=True, blank=True)
    uploaded_cv = models.FileField(upload_to='uploads/', null=True)
    last_company = models.CharField(max_length=50, null=True, blank=True)
    last_CTC = models.CharField(max_length=50, null=True, blank=True)
    expected_salary = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    apply_date = models.CharField(max_length=50, null=True, blank=True)
    apply_time = models.CharField(max_length=50, null=True, blank=True)
    
    applied_from_company = models.CharField(max_length=200, null=True, blank=True)
    interview_date = models.CharField(max_length=50, null=True, blank=True)
    interview_time = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    joining_date =models.CharField(max_length=50, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'tbl_hiring'
        
class tbl_promocode(models.Model):
    id = models.AutoField(primary_key=True)
    promocode = models.CharField(max_length=500, null=True, blank=True)
    promo_dis= models.CharField(max_length=500, null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_promocode'
        
# class tbl_pure_client(models.Model):
#     id = models.AutoField(primary_key=True)
#     client_id = models.CharField(max_length=10, null=True, blank=True)
#     plan_id= models.CharField(max_length=10, null=True, blank=True)
#     plan_amount= models.CharField(max_length=50, null=True, blank=True)
#     discount= models.CharField(max_length=50, null=True, blank=True)
#     final_amount= models.CharField(max_length=50, null=True, blank=True)
#     promocode = models.CharField(max_length=50, null=True, blank=True)
#     start_date = models.DateTimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#     created_time = models.DateTimeField(default=datetime.now)

#     class Meta:
#         db_table = 'tbl_pure_client' 
        
class tbl_order(models.Model):
    id = models.AutoField(primary_key=True)
    plan_id = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True, blank=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    promo_code = models.CharField(max_length=255, blank=True, null=True)
    payment_status = models.CharField(max_length=20, default="pending",null=True, blank=True)
    phonepe_transaction_id = models.CharField(max_length=255, blank=True, null=True)
    phonepe_reference_id = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    order_id = models.CharField(max_length=50, unique=True, null=True, blank=True)

    class Meta:
        db_table = 'tbl_order'  
    
class master_area(models.Model):
    id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    city_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 
    update_by_id = models.CharField(max_length=50, null=True, blank=True)
    update_by_name = models.CharField(max_length=50, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    
    class Meta:
        # Specify the actual table name
        db_table = 'master__area'
        
class tbl_inqiry_for(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now,null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_inqiry_for' 
        
class tbl_bussi_seg(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now,null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_bussi_seg' 
        
class tbl_smo_plan(models.Model):
    id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=100, null=True, blank=True)
    plan_duration = models.CharField(max_length=100, null=True, blank=True)
    no_of_post = models.CharField(max_length=100, null=True, blank=True)
    no_of_reel = models.CharField(max_length=100, null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now,null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_smo_plan'
        
class tbl_smo_plan_hsty(models.Model):
    id = models.AutoField(primary_key=True)
    clt_id = models.IntegerField(null=True, blank=True)
    smo_id = models.IntegerField(null=True, blank=True)
    plan_id = models.IntegerField(null=True, blank=True)
    plan_name = models.CharField(max_length=100, null=True, blank=True)
    plan_duration = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    no_of_post = models.CharField(max_length=100, null=True, blank=True)
    no_of_reel = models.CharField(max_length=100, null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now,null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_smo_plan_hsty'
        
class tbl_seo_plan(models.Model):
    id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=100, null=True, blank=True)
    plan_duration = models.CharField(max_length=100, null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now,null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_seo_plan'    
        
class tbl_seo_plan_hsty(models.Model):
    id = models.AutoField(primary_key=True)
    clt_id = models.IntegerField(null=True, blank=True)
    seo_id = models.IntegerField(null=True, blank=True)
    plan_id = models.IntegerField(null=True, blank=True)
    plan_name = models.CharField(max_length=100, null=True, blank=True)
    plan_duration = models.CharField(max_length=100, null=True, blank=True)
    seo_start = models.DateTimeField(null=True, blank=True)
    seo_expire = models.DateTimeField(null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now,null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_seo_plan_hsty'
        
        
class tbl_applicant_status(models.Model):
    status = models.CharField(max_length=100, null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.now,null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 
    
    class Meta:
        db_table = 'tbl_applicant_status'        
        
class tbl_salary_history(models.Model):
    emp_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    salary = models.CharField(max_length=200, null=True, blank=True)
    increment_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(default=datetime.now,null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 
    
    class Meta:
        db_table = 'tbl_salary_history'        
        
class tbl_monthly_report(models.Model):
    month = models.CharField(max_length=200, null=True, blank=True, unique=True)
    report_path = models.FileField(upload_to='monthly_reports/')
    created_date = models.DateTimeField(default=datetime.now,null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 
    
    class Meta:
        db_table = 'tbl_monthly_report'        
        
        
class tbl_made_salary(models.Model):
    emp_id = models.IntegerField(null=True, blank=True)
    month = models.CharField(max_length=200, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(default=datetime.now,null=True, blank=True)
    add_by_id = models.CharField(max_length=10, null=True, blank=True) 
    add_by_name = models.CharField(max_length=50, null=True, blank=True) 
    
    class Meta:
        db_table = 'tbl_made_salary'        
        


        
