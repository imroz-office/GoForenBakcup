from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings
# from .views import InitiatePhonePePayment
from . import views

urlpatterns = [
    #Login
        path("", views.login, name='login'),
        path('logout/', views.logout_view, name='logout'),
        path('unlock_screen/', views.unlock_screen, name='unlock_screen'),
        path('deactivate_completed_interns/', views.deactivate_completed_interns, name='deactivate_completed_interns'),
        path('deactivate_old_employees/', views.deactivate_old_employees, name='deactivate_old_employees'),
     
    # Common Functin
        path('index/', views.index, name='index'),  
        path('profile/', views.profile, name='profile'),  
        path('profile_Update/', views.profile_Update, name='profile_Update'), 
        path('change_Password/', views.change_Password, name='change_Password'), 
        
        path('Log/', views.Log, name='Log'),
        path('fetch_new_messages/', views.fetch_new_messages, name='fetch_new_messages'),
        path('fetch_companies/', views.fetch_companies, name='fetch_companies'),
        path('save_selected_company/', views.save_selected_company, name='save_selected_company'),
        
        path('today_meeting/', views.today_meeting, name='today_meeting'),
        path('new_lead/', views.new_lead, name='new_lead'),
        
        path('account_today_expense/', views.account_today_expense, name='account_today_expense'), 
        
        path('today_amc/', views.today_amc, name='today_amc'), 
        
        path('smo_today_renewal/', views.smo_today_renewal, name='smo_today_renewal'), 
        path('smo_active_client/', views.smo_active_client, name='smo_active_client'), 
        
    # Master
        path('company/', views.company, name='company'),   
        path('add_company/', views.add_company, name='add_company'),
        path('update_company/<int:com_id>/', views.update_company, name='update_company'),
        path('delete_company/<int:com_id>/', views.delete_company, name='delete_company'),
        path('company_view/<int:com_id>/', views.company_view, name='company_view'),
        path('get_departments_by_company/', views.get_departments_by_company, name='get_departments_by_company'), 
        
        path('department/', views.department, name='department'),
        path('add_department/', views.add_department, name='add_department'),
        path('update_department/<int:dp_id>/', views.update_department, name='update_department'),
        path('delete_department/<int:dp_id>/', views.delete_department, name='delete_department'),
        
        path('lead_source/', views.lead_source, name='lead_source'),
        path('add_lead_source/', views.add_lead_source, name='add_lead_source'),
        path('update_lead_source/<int:ldt_id>/', views.update_lead_source, name='update_lead_source'),
        path('delete_lead_source/<int:ldt_id>/', views.delete_lead_source, name='delete_lead_source'),
        
        path('shift_list/', views.shift_list, name='shift_list'),
        path('add_shift/', views.add_shift, name='add_shift'),
        path('update_shift/<int:s_id>/', views.update_shift, name='update_shift'),
        path('delete_shift/<int:s_id>/', views.delete_shift, name='delete_shift'),
        
        path('Product/', views.Product, name='Product'),
        path('add_product/', views.add_product, name='add_product'),
        path('update_product/<int:pro_id>/', views.update_product, name='update_product'),
        path('delete_product/<int:pro_id>/', views.delete_product, name='delete_product'),
        
        path('Reason/', views.Reason, name='Reason'),
        path('add_reason/', views.add_reason, name='add_reason'),
        path('update_reason/<int:id>/', views.update_reason, name='update_reason'),
        path('delete_reason/<int:id>/', views.delete_reason, name='delete_reason'), 
        
        path('Promocode/', views.Promocode, name='Promocode'),
        path('Promocode_view/', views.Promocode_view, name='Promocode_view'),
        path('add_promocode/', views.add_promocode, name='add_promocode'),
        path('update_promocode/<int:id>/', views.update_promocode, name='update_promocode'),
        path('delete_promocode/<int:id>/', views.delete_promocode, name='delete_promocode'), 
        
        # path('client_purchase/', views.client_purchase, name='client_purchase'),
        # path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
        # path('payment-callback/', views.payment_callback, name='payment_callback'),
        # path('CreatePaymentSession/', views.CreatePaymentSession, name='CreatePaymentSession'),
        # path('api/initiate-payment/', InitiatePhonePePayment.as_view(), name='initiate-payment'),
        path('initiate_payment/', views.initiate_payment, name='initiate_payment'), 
        path('payment_callback/', views.payment_callback, name='payment_callback'),
        
        path('Holiday/', views.Holiday, name='Holiday'),
        path('add_holiday/', views.add_holiday, name='add_holiday'),
        path('update_holiday/<int:id>/', views.update_holiday, name='update_holiday'), 
        path('delete_holiday/<int:id>/', views.delete_holiday, name='delete_holiday'),
        
        path('Area/', views.Area, name='Area'),
        path('add_area/', views.add_area, name='add_area'),
        path('update_area/<int:id>/', views.update_area, name='update_area'), 
        path('delete_area/<int:id>/', views.delete_area, name='delete_area'),
        
        path('Inqiry_for/', views.Inqiry_for, name='Inqiry_for'),
        path('add_inqiry_for/', views.add_inqiry_for, name='add_inqiry_for'),
        path('up_inqfor/<int:id>/', views.up_inqfor, name='up_inqfor'),
        path('delete_inqiry_for/<int:id>/', views.delete_inqiry_for, name='delete_inqiry_for'), 
        
        path('Business_segment/', views.Business_segment, name='Business_segment'),
        path('add_busi_seg/', views.add_busi_seg, name='add_busi_seg'),
        path('up_segment/<int:id>/', views.up_segment, name='up_segment'),
        path('delete_segment/<int:id>/', views.delete_segment, name='delete_segment'), 
        
        path('SMO_Plan/', views.SMO_Plan, name='SMO_Plan'),
        path('add_smo_plan/', views.add_smo_plan, name='add_smo_plan'),
        path('update_smo_plan/<int:id>/', views.update_smo_plan, name='update_smo_plan'),
        path('delete_smo_plan/<int:id>/', views.delete_smo_plan, name='delete_smo_plan'),
        
        path('SEO_Plan/', views.SEO_Plan, name='SEO_Plan'),
        path('add_seo_plan/', views.add_seo_plan, name='add_seo_plan'),
        path('update_seo_plan/<int:id>/', views.update_seo_plan, name='update_seo_plan'),
        path('delete_seo_plan/<int:id>/', views.delete_seo_plan, name='delete_seo_plan'),
        
    # User
        path('User/', views.User, name='User'),
        path('user_excel/', views.user_excel, name='user_excel'),
        path('add_user/', views.add_user, name='add_user'),
        path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
        path('delete_user/<int:userId>/', views.delete_user, name='delete_user'),
        path('view_user/<int:userId>/', views.view_user, name='view_user'),

        
    # CRM
        path('crm_dashboard/', views.crm_dashboard, name='crm_dashboard'),
        path('inquiry/', views.inquiry, name='inquiry'),
        path('fresh_inquiry/', views.fresh_inquiry, name='fresh_inquiry'),
        path('today_followup/', views.today_followup, name='today_followup'),
        path('pending_followup/', views.pending_followup, name='pending_followup'),
        path('Meeting_inquiry/', views.Meeting_inquiry, name='Meeting_inquiry'),
        path('Contacted_inquiry/', views.Contacted_inquiry, name='Contacted_inquiry'),
        path('Quotation_inquiry/', views.Quotation_inquiry, name='Quotation_inquiry'),
        path('Contracted_inquiry/', views.Contracted_inquiry, name='Contracted_inquiry'),
        path('Onhold_inquiry/', views.Onhold_inquiry, name='Onhold_inquiry'),
        path('Lost_inquiry/', views.Lost_inquiry, name='Lost_inquiry'),
        path('today_meetings/', views.today_meetings, name='today_meetings'), 
        path('today_dcr/', views.today_dcr, name='today_dcr'), 
        
        path('upload_lead/', views.upload_lead, name='upload_lead'),
        
        path('lead_list/', views.lead_list, name='lead_list'),
        path('addlead/', views.addlead, name='addlead'),
        path('lead_excel/', views.lead_excel, name='lead_excel'),
        path('add_lead/', views.add_lead, name='add_lead'),
        path('edit_lead/<int:l_id>/', views.edit_lead, name='edit_lead'),
        path('delete_lead/<int:l_id>/', views.delete_lead, name='delete_lead'),
        path('lead_view/<int:l_id>/', views.lead_view, name='lead_view'),
        path('lead_update_view/<int:l_id>/', views.lead_update_view, name='lead_update_view'),
        path('edit_lead_status/<int:l_id>/', views.edit_lead_status, name='edit_lead_status'),
        
        path('assign_lead/', views.assign_lead, name='assign_lead'),
        path('delete_select_leads/', views.delete_select_leads, name='delete_select_leads'),
        path('assign_leads/', views.assign_leads, name='assign_leads'),

        
        path('add_dcr/', views.add_dcr, name='add_dcr'),
        path('adddcr/', views.adddcr, name='adddcr'),
        
        path('dcr_list/', views.dcr_list, name='dcr_list'),
        path('dcr_excel/', views.dcr_excel, name='dcr_excel'), 
        path('open_dcr_view/<int:l_id>/', views.open_dcr_view, name='open_dcr_view'), 
        path('edit_dcr/<int:l_id>/', views.edit_dcr, name='edit_dcr'), 
        path('delete_dcr/<int:l_id>/', views.delete_dcr, name='delete_dcr'),
        path('convert_lead/<int:l_id>/', views.convert_lead, name='convert_lead'),
        path('convert_lead_bulk/', views.convert_lead_bulk, name='convert_lead_bulk'),
         
        path('open_report_least_page/', views.open_report_least_page, name='open_report_least_page'),
        
        path('client_excel/', views.client_excel, name='client_excel'), 

        
    # Account
        path('open_ledger_least_page/', views.open_ledger_least_page, name='open_ledger_least_page'),
        
        path('open_client_vendor_least_page/', views.open_client_vendor_least_page, name='open_client_vendor_least_page'),
        path('open_add_client_page/', views.open_add_client_page, name='open_add_client_page'),
        path('add_client_page/', views.add_client_page, name='add_client_page'),
        path('open_edit_client/<int:cId>/', views.open_edit_client, name='open_edit_client'), 
        path('open_delete_client/<int:cId>/', views.open_delete_client, name='open_delete_client'),
        
        path('open_employee_other_least_page/', views.open_employee_other_least_page, name='open_employee_other_least_page'),
        
    # voucher
        path('account_dashboard/', views.account_dashboard, name='account_dashboard'),
        path('account_client/', views.account_client, name='account_client'),
        path('account_add_client/', views.account_add_client, name='account_add_client'),
        path('account_edit_client/<int:clt_id>/', views.account_edit_client, name='account_edit_client'),
        path('account_delete_client/<int:clt_id>/', views.account_delete_client, name='account_delete_client'),
        path('account_view_client/<int:clt_id>/', views.account_view_client, name='account_view_client'),
    
        path('payment_voucher/', views.payment_voucher, name='payment_voucher'),
        path('receipt_excel/', views.receipt_excel, name='receipt_excel'),
        path('create_payment_voucher/', views.create_payment_voucher, name='create_payment_voucher'),
        path('edit_payment/<int:pv_id>/', views.edit_payment, name='edit_payment'),
        path('delete_payment_voucher/<int:pv_id>/', views.delete_payment_voucher, name='delete_payment_voucher'),
        path('view_payment/<int:pv_id>/', views.view_payment, name='view_payment'),
        path('add_payment/', views.add_payment, name='add_payment'), 
        path('payment_voucher_pdf/<int:pv_id>/', views.payment_voucher_pdf, name='payment_voucher_pdf'),
        path('generate_payment_invoice/', views.generate_payment_invoice, name='generate_payment_invoice'),
        
        path('add_receipt/', views.add_receipt, name='add_receipt'),
        path('create_receipt_voucher/', views.create_receipt_voucher, name='create_receipt_voucher'),
        path('edit_receipt/<int:rv_id>/', views.edit_receipt, name='edit_receipt'),
        path('delete_receipt_voucher/<int:rv_id>/', views.delete_receipt_voucher, name='delete_receipt_voucher'),
        path('view_client_receipt_voucher/<int:rv_id>/', views.view_client_receipt_voucher, name='view_client_receipt_voucher'),
        path('receipt_voucher/', views.receipt_voucher, name='receipt_voucher'),
        path('receipt_voucher_pdf/<int:rv_id>/', views.receipt_voucher_pdf, name='receipt_voucher_pdf'),
        path('generate_receipt_invoice/', views.generate_receipt_invoice, name='generate_receipt_invoice'),
        
        path('client_voucher/', views.client_voucher, name='client_voucher'),
        path('client_invoice/<str:name>/<int:clt_id>/', views.open_client_invoice_least_page, name='open_client_invoice_least_page'),
        re_path(r'^client_payment/(?P<name>[\w-]+)/(?P<clt_id>\d+)/$', views.open_client_payment_voucer_least_page, name='open_client_payment_voucer_least_page'),
        re_path(r'^client_recipt/(?P<name>[\w-]+)/(?P<clt_id>\d+)/$', views.open_client_recipt_voucer_least_page, name='open_client_recipt_voucer_least_page'),
        
        path('payment_v_excel/', views.payment_v_excel, name='payment_v_excel'),
        
        
    # ledger
        path('ledger/', views.ledger, name='ledger'),
        
    # invoice
        path('invoice/', views.invoice, name='invoice'),
        path('invoice_excel/', views.invoice_excel, name='invoice_excel'),
        
        path('create_invoice/', views.create_invoice, name='create_invoice'),
        path('invoice_listing/', views.invoice_listing, name='invoice_listing'),
        path('edit-invoice/<int:inv_id>/', views.edit_invoice, name='edit_invoice'),
        path('delete_invoice/<int:inv_id>/', views.delete_invoice, name='delete_invoice'),
        path('invoice_pdf/<str:invNumber>/', views.invoice_pdf, name='invoice_pdf'),
        path('invoice_share/<str:invNumber>/', views.invoice_pdf_share, name='invoice_pdf_share'),
        
    # report
        path('reports/', views.reports, name='reports'),
        path('payment_report/', views.payment_report, name='payment_report'),
        path('receipt_report/', views.receipt_report, name='receipt_report'),
        path('receipt_invoice/', views.receipt_invoice, name='receipt_invoice'),
        path('total_pending/', views.total_pending, name='total_pending'),
        
        path('download_report/', views.download_report, name='download_report'),
        path('download_pdf/', views.download_pdf, name='download_pdf'),
        path('download_excel/', views.download_excel, name='download_excel'),
        
        path('profit_loss/', views.profit_loss, name='profit_loss'),

        
        path('client_project/', views.client_project, name='client_project'),
        path('add_client_project/', views.add_client_project, name='add_client_project'),
        path('add_client_pro/', views.add_client_pro, name='add_client_pro'),
        path('edit_client_pro/<str:id>/', views.edit_client_pro, name='edit_client_pro'),
        path('delete_client_pro/<str:id>/', views.delete_client_pro, name='delete_client_pro'),

    
    # AMC
        path('addamc/', views.addamc, name='addamc'),
        path('add_amc/', views.add_amc, name='add_amc'),
        path('AMC/', views.AMC, name='AMC'),
        path('edit_amc/<int:amc_id>/', views.edit_amc, name='edit_amc'),
        path('delete_amc/<int:amc_id>/', views.delete_amc, name='delete_amc'),
        path('view_amc/<int:amc_id>/', views.view_amc, name='view_amc'),
        path('AMC_excel/', views.AMC_excel, name='AMC_excel'),
        
    # SMO/SEO
        path('add_smo/', views.add_smo, name='add_smo'),
        path('addsmo/', views.addsmo, name='addsmo'),
        path('edit_smo/<int:smoId>/', views.edit_smo, name='edit_smo'),
        path('delete_smo/<int:smoId>/', views.delete_smo, name='delete_smo'), 
        path('view_smo/<int:smoId>/', views.view_smo, name='view_smo'),
        path('SMO/', views.SMO, name='SMO'),
        path('smo_excel/', views.smo_excel, name='smo_excel'),
        # path('amc_least/', views.amc_least, name='amc_least'),
        path('post_report/', views.post_report, name='post_report'), 
        path('add_post/', views.add_post, name='add_post'),
        path('addpost/', views.addpost, name='addpost'),
        path('edit_post/<int:id>/', views.edit_post, name='edit_post'),
        path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
        path('smo/renew/', views.renew_smo_plan, name='renew_smo_plan'),
        
        path('SEO/', views.SEO, name='SEO'),
        path('add_seo/', views.add_seo, name='add_seo'),
        path('addseo/', views.addseo, name='addseo'),
        path('edit_seo/<int:smoId>/', views.edit_seo, name='edit_seo'),
        path('view_seo/<int:smoId>/', views.view_seo, name='view_seo'),
        path('seo/renew/', views.renew_seo_plan, name='renew_seo_plan'),
        
    # task
        path('addproject/', views.addproject, name='addproject'),
        path('add_project/', views.add_project, name='add_project'),
        path('edit_project/<int:pj_id>/', views.edit_project, name='edit_project'), 
        path('delete_project/<int:pj_id>/', views.delete_project, name='delete_project'),
        path('view_project/<int:pj_id>/', views.view_project, name='view_project'),  
        path('complete_project/<int:pj_id>/', views.complete_project, name='complete_project'),  
        path('project_list/', views.project_list, name='project_list'),
        path('project_excel/', views.project_excel, name='project_excel'),
        
        path('add_task/', views.add_task, name='add_task'),
        path('update_task_remark/<int:taskId>/', views.update_task_remark, name='update_task_remark'), 
        path('fetch_users_for_assign_to/', views.fetch_users_for_assign_to, name='fetch_users_for_assign_to'), 
        path('add_new_task/', views.add_new_task, name='add_new_task'),
        path('edit_task/<int:taskId>/', views.edit_task, name='edit_task'),
        path('delete_task/<int:taskId>/', views.delete_task, name='delete_task'),
        path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
        path('rewaise_task/<int:task_id>/', views.rewaise_task, name='rewaise_task'),
        path('task_list/', views.task_list, name='task_list'),
        path('task_view/<int:userId>/', views.task_view, name='task_view'),
        path('Urgent_task/', views.Urgent_task, name='Urgent_task'),
        path('completed_task/', views.completed_task, name='completed_task'),
        path('revise_task/', views.revise_task, name='revise_task'),
        path('task_report/', views.task_report, name='task_report'),
        path('task_excel/', views.task_excel, name='task_excel'),
        path('view_task/<int:taskId>/', views.view_task, name='view_task'),
        
        path('my_task/', views.my_task, name='my_task'),
        path('my_urgent_task/', views.my_urgent_task, name='my_urgent_task'),
        path('my_completed_task/', views.my_completed_task, name='my_completed_task'),
        path('my_revise_task/', views.my_revise_task, name='my_revise_task'),
        
        path('add_meeting/', views.add_meeting, name='add_meeting'),
        path('addmeeting/', views.addmeeting, name='addmeeting'),
        path('edit_meeting/<int:meet_id>/', views.edit_meeting, name='edit_meeting'),
        path('delete_meeting/<int:meet_id>/', views.delete_meeting, name='delete_meeting'),
        path('meeting_list/', views.meeting_list, name='meeting_list'),
        path('meeting_excel/', views.meeting_excel, name='meeting_excel'),
        
        path('add_report/', views.add_report, name='add_report'),
        path('add_daily_report/', views.add_daily_report, name='add_daily_report'),
        path('daily_report/', views.daily_report, name='daily_report'),
        path('user_report/<int:userId>/', views.user_report, name='user_report'),
        path('edit_report/<int:repoId>/', views.edit_report, name='edit_report'),
        path('edit_daily_report_record/<int:repoId>/', views.edit_daily_report_record, name='edit_daily_report_record'),
        path('view_report/<int:repoId>/', views.view_report, name='view_report'),
        path('delete_daily_report/<int:repoId>/', views.delete_daily_report, name='delete_daily_report'),
        path('report_download/', views.report_download, name='report_download'),
        path('daily_excel/', views.daily_excel, name='daily_excel'),
        
    # HRMS
        path('add_employee/', views.add_employee, name='add_employee'),
        path('add_employee_onboarding/', views.add_employee_onboarding, name='add_employee_onboarding'),
        path('edit_employee/<int:emp_id>/', views.edit_employee, name='edit_employee'),
        path('delete_employee_onboarding/<int:emp_id>/', views.delete_employee_onboarding, name='delete_employee_onboarding'),
        path('employee_list/', views.employee_list, name='employee_list'),
        path('employee_details/<int:emp_id>/', views.employee_details, name='employee_details'),
        
        path('add_intern/', views.add_intern, name='add_intern'),
        path('add_intern_onboarding/', views.add_intern_onboarding, name='add_intern_onboarding'),
        path('edit_intern/<int:intern_id>/', views.edit_intern, name='edit_intern'),
        path('delete_intern_onboarding/<int:intern_id>/', views.delete_intern_onboarding, name='delete_intern_onboarding'),
        path('intern_list/', views.intern_list, name='intern_list'),
        path('intern_details/<int:emp_id>/', views.intern_details, name='intern_details'),
        path('details_count_intern/', views.details_count_intern, name='details_count_intern'),
        path('intern_excel/', views.intern_excel, name='intern_excel'),

        # path('intern_details/<int:emp_id>/', views.intern_details, name='intern_details'),

        path('details_count/', views.details_count, name='details_count'),
        path('emp_excel/', views.emp_excel, name='emp_excel'),
        
        path('approved_leave/', views.approved_leave, name='approved_leave'),
        path('rejected_leave/', views.rejected_leave, name='rejected_leave'),
        path('pending_leave/', views.pending_leave, name='pending_leave'),
        path('approve_leave/<int:leave_id>/', views.approve_leave, name='approve_leave'),
        path('reject_leave/<int:leave_id>/', views.reject_leave, name='reject_leave'),
        path('delete_leave/<int:leave_id>/', views.delete_leave, name='delete_leave'),
        path('del_leave/<int:leave_id>/', views.del_leave, name='del_leave'),
        path('view_leave/<int:leave_id>/', views.view_leave, name='view_leave'),
        path('edit_leave/<int:leave_id>/', views.edit_leave, name='edit_leave'),
        
        path('addleave/', views.addleave, name='addleave'),
        path('add_leave/', views.add_leave, name='add_leave'),
        path('hiring_list/', views.hiring_list, name='hiring_list'),
        path('career_view/<int:id>/', views.view_hiring, name='view_hiring'),
        path('hiring_status/<int:id>/', views.hiring_status, name='hiring_status'),
        path('update-status/<int:id>/', views.update_applicant_status, name='update_applicant_status'),
        path('add_hiring/', views.add_hiring, name='add_hiring'),
        path('delete_hiring/<int:id>/', views.delete_hiring, name='delete_hiring'),

        path('open_letter_least/', views.open_letter_least, name='open_letter_least'),
        # path('upload_letters/', views.upload_letters, name='upload_letters'),
        path('download_experience_letter/<int:employee_id>/', views.download_experience_letter, name='download_experience_letter'),
        path('download_appointment_letter/<int:employee_id>/', views.download_appointment_letter, name='download_appointment_letter'),
        path('download_offer_letter/<int:employee_id>/', views.download_offer_letter, name='download_offer_letter'),
        path('download_bond_letter/<int:employee_id>/', views.download_bond_letter, name='download_bond_letter'),
        
        path('download_intern_offer_letter/<int:intern_id>/', views.download_intern_offer_letter, name='download_intern_offer_letter'),
        path('download_intern_appointment_letter/<int:intern_id>/', views.download_intern_appointment_letter, name='download_intern_appointment_letter'),
        path('download_intern_experience_letter/<int:intern_id>/', views.download_intern_experience_letter, name='download_intern_experience_letter'),

        path('open_payroll_least/', views.open_payroll_least, name='open_payroll_least'),
        path('monthly_report_list/', views.monthly_report_list, name='monthly_report_list'),
        # path('download_report_file/', views.download_report_file, name='download_report_file'),
        path('download-report-file/<str:filename>/', views.download_report_file, name='download_report_file'),
        
        path('delete_monthly_report/<int:report_id>/', views.delete_monthly_report, name='delete_monthly_report'),
        path('download_monthly_report_all_employees/', views.download_monthly_report_all_employees, name='download_monthly_report_all_employees'),
        path('add_attendance_sheet/', views.add_attendance_sheet, name='add_attendance_sheet'),
        path('salary/<int:emp_id>/', views.salary, name='salary'),
        path('attendance_count/', views.attendance_count, name='attendance_count'),
        path('salary_slip/', views.salary_slip, name='salary_slip'),
        path('salary_slip_/', views.salary_slip_, name='salary_slip_'),
        
        
        path('advance_salary/', views.advance_salary, name='advance_salary'),
        path('add_salary/', views.add_salary, name='add_salary'),
        path('edit_salary/<int:s_id>/', views.edit_salary, name='edit_salary'),
        path('delete_salary/<int:s_id>/', views.delete_salary, name='delete_salary'),

    #puresaas
        path('plan/', views.plan, name='plan'),
        path('add_plan/', views.add_plan, name='add_plan'),
        path('edit_plan/<int:id>/', views.edit_plan, name='edit_plan'), 
        path('delete_plan/<int:id>/', views.delete_plan, name='delete_plan'), 
        path('view_plan/<int:id>/', views.view_plan, name='view_plan'), 
        path('plan_view/', views.plan_view, name='plan_view'), 
        path('monthly_plan_view/', views.monthly_plan_view, name='monthly_plan_view'),
        
    # puresaas Inquiry
        path('free_trial/', views.free_trial, name='free_trial'),
        path('freetrial/<int:id>/', views.freetrial, name='freetrial'),
        
        path('request_call/', views.request_call, name='request_call'),
        path('requestcall/<int:id>/', views.requestcall, name='requestcall'),
        path('view_call/<int:id>/', views.view_call, name='view_call'),
        
        path('price_quote/', views.price_quote, name='price_quote'),
        path('pricequote/<int:id>/', views.pricequote, name='pricequote'),
        path('view_quote/<int:id>/', views.view_quote, name='view_quote'),
        
        path('book_demo/', views.book_demo, name='book_demo'),
        path('bookdemo/<int:id>/', views.bookdemo, name='bookdemo'),
        
        path('ask_question/', views.ask_question, name='ask_question'),
        path('askquestion/<int:id>/', views.askquestion, name='askquestion'),
        
        path('blogs_comment/', views.blogs_comment, name='blogs_comment'),
        path('blogscomment/<int:id>/', views.blogscomment, name='blogscomment'),
        
        path('message/', views.message, name='message'),
        path('del_message/<int:id>/', views.del_message, name='del_message'),
        
        path('all_demo/', views.all_demo, name='all_demo'),
        path('del_all_demo/<int:id>/', views.del_all_demo, name='del_all_demo'),
        path('view_demo/<int:id>/', views.view_demo, name='view_demo'),
        path('demo_convert_lead/<int:id>/', views.demo_convert_lead, name='demo_convert_lead'),
        path('book_bulk_convert/', views.book_bulk_convert, name='book_bulk_convert'),
        
    # puresaas
        path('puresaas_list/', views.puresaas_list, name='puresaas_list'),
        path('puresaas_renewal/', views.puresaas_renewal, name='puresaas_renewal'),
        path('puresaas_renewal_week/', views.puresaas_renewal_week, name='puresaas_renewal_week'),
        path('puresaas_view/<int:id>/', views.puresaas_view, name='puresaas_view'),
        path('pure_view/<int:id>/', views.pure_view, name='pure_view'),
        path('puresaas_client/<int:id>/', views.puresaas_client, name='puresaas_client'),
        
    # SIT Career
        path('sit_career/', views.sit_career, name='sit_career'),
        
        path('send_tomorrow_meeting_reminders/', views.send_tomorrow_meeting_reminders, name='send_tomorrow_meeting_reminders'),

        path('toggle_active_user/<int:user_id>/', views.toggle_active_user, name='toggle_active_user'),

    # salary history
        path('salary_history/', views.salary_history, name='salary_history'),
        path('add_salary_history/', views.add_salary_history, name='add_salary_history'),
        path('salary_history_list/', views.salary_history_list, name='salary_history_list'),
        path('edit_salary_history/<int:id>/', views.edit_salary_history, name='edit_salary_history'),
        path('delete_salary_history/<int:id>/', views.delete_salary_history, name='delete_salary_history'),
        
        path('salary_record/', views.salary_record, name='salary_record'),
        path('add_salary_record/<int:emp_id>/', views.add_salary_record, name='add_salary_record'),
        path('edit_salary_record/<int:id>/<int:emp_id>/', views.edit_salary_record, name='edit_salary_record'),
         
        
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)