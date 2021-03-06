"""hospital_managment_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hms_app.views import *


urlpatterns = [
##    url(r'^admin/', admin.site.urls),
    url(r'^$',index_pg),
    url(r'^index/',index,name='index'),
    url(r'^do_booking/',do_booking,name='do_booking'),
    url(r'^admin_hm_log/',admin_hm_log,name='admin_hm_log'),
    url(r'^Patient_homelog/',Patient_homelog,name='Patient_homelog'),
    url(r'^dhm/',dhm,name='dhm'),
    url(r'^lab_hmlog/',lab_hmlog,name='lab_hmlog'),
    url(r'^phar_hmlog/',phar_hmlog,name='phar_hmlog'),

    url(r'^hospital_pg/',hospital_pg,name='hospital_pg'),
    url(r'^pharmacy_pg/',pharmacy_pg,name='pharmacy_pg'),
    url(r'^patient_reg/',patient_reg,name='patient_reg'),
    url(r'^booking/',booking,name='booking'),
    url(r'^booking_hm/',booking_hm,name='booking_hm'),
    url(r'^login_check/',login_check,name='login_check'),
    url(r'^hospital_reg/',hospital_reg,name='hospital_reg'),
    url(r'^dr_reg/',dr_reg,name='dr_reg'),
    url(r'^list_hosp/',list_hosp,name='list_hosp'),
    url(r'^list_lab/',list_lab,name='list_lab'),
    url(r'^list_dept/',list_dept,name='list_dept'),
    url(r'^list_dr/',list_dr,name='list_dr'),
    url(r'^doctor_reg_fn/',doctor_reg_fn,name='doctor_reg_fn'),
    url(r'^logout_fn/',logout_fn,name='logout_fn'), 
    url(r'^book_now/',book_now,name='book_now'), 
    url(r'^login_check_after/',login_check_after,name='login_check_after'), 
    url(r'^book_pg_msg/',book_pg_msg,name='book_pg_msg'), 
    url(r'^pharmacy_regs_admin/',pharmacy_regs_admin,name='pharmacy_regs_admin'), 
    url(r'^admin_home/',admin_home,name='admin_home'),
    url(r'^patient_home/',patient_home,name='patient_home'), 
    url(r'^medicine/',medicine,name='medicine'),
    url(r'^list_phar/',list_phar,name='list_phar'),
    url(r'^list_cat/',list_cat,name='list_cat'),
    url(r'^list_med/',list_med,name='list_med'),
    url(r'^list_details/',list_details,name='list_details'),
    url(r'^vw_cart/',vw_cart,name='vw_cart'),
    url(r'^add_cart/',add_cart,name='add_cart'),
    url(r'^delete_pdt/',delete_pdt,name='delete_pdt'),
    url(r'^update_cart/',update_cart,name='update_cart'),
    url(r'^cart_sum/',cart_sum,name='cart_sum'),
    url(r'^placeorder/',placeorder,name='placeorder'),
    url(r'^lab_regs_pg/',lab_regs_pg,name='lab_regs_pg'),
    url(r'^lab_regs_fn/',lab_regs_fn,name='lab_regs_fn'),
    url(r'^lab_home/',lab_home,name='lab_home'),
    url(r'^lab_bk_pg/',lab_bk_pg,name='lab_bk_pg'),
    url(r'^book_lab/',book_lab,name='book_lab'),
    url(r'^dr_bk_msg/',dr_bk_msg,name='dr_bk_msg'),
    url(r'^dr_bk_vw/',dr_bk_vw,name='dr_bk_vw'),
    url(r'^hosptl_hm/',hosptl_hm,name='hosptl_hm'),
    url(r'^lab_bk_vw/',lab_bk_vw,name='lab_bk_vw'),
    url(r'^patient_pg_chat/',patient_pg_chat,name='patient_pg_chat'),
    url(r'^hosptl_add_phar_hm/',hosptl_add_phar_hm,name='hosptl_add_phar_hm'),
    url(r'^pharmacy_regs_hosp/',pharmacy_regs_hosp,name='pharmacy_regs_hosp'), 
    url(r'^lab_reg_pg_hosp/',lab_reg_pg_hosp,name='lab_reg_pg_hosp'), 
    url(r'^lab_regs_fn_hosp/',lab_regs_fn_hosp,name='lab_regs_fn_hosp'), 
    url(r'^hospital_dr_bk_vw/',hospital_dr_bk_vw,name='hospital_dr_bk_vw'), 
    url(r'^dr_hm/',dr_hm,name='dr_hm'), 
    url(r'^dr_Vw_bkngs/',dr_Vw_bkngs,name='dr_Vw_bkngs'), 
    url(r'^updt_bkng_tym/',updt_bkng_tym,name='updt_bkng_tym'), 
    url(r'^pharmacy_hm/',pharmacy_hm,name='pharmacy_hm'),
    url(r'^med_add/',med_add,name='med_add'),
    url(r'^med_insert/',med_insert,name='med_insert'), 
    url(r'^purchase_rep/',purchase_rep,name='purchase_rep'), 
    url(r'^addtest/',addtest,name='addtest'),
    url(r'^updt_lab_bkng_tym/',updt_lab_bkng_tym,name='updt_lab_bkng_tym'), 
    url(r'^viewlabookings/',viewlabookings,name='viewlabookings'), 
    url(r'^addingtest/',addingtest,name='addingtest'),
    url(r'^fetchtest/',fetchtest,name='fetchtest'),
    url(r'^articlespg/',articlespg,name='articlespg'),
    url(r'^migraine/',migraine,name='migraine'),
##    url(r'^notificatn_bkng_tym/',notificatn_bkng_tym,name='notificatn_bkng_tym'),
    url(r'^chatting/',chatting,name='chatting'),
    url(r'^vwchatwithdr/',vwchatwithdr,name='vwchatwithdr'),
    url(r'^patients_msgto_dr/',patients_msgto_dr,name='patients_msgto_dr'),
    url(r'^msgfrm_p/',msgfrm_p,name='msgfrm_p'),
    url(r'^sendrply/',sendrply,name='sendrply'),
    url(r'^patient_hm/',patient_hm,name='patient_hm'), 
    url(r'^fever/',fever,name='fever'),
    url(r'^asthma/',asthma,name='asthma'),
    url(r'^stress/',stress,name='stress'),
    url(r'^hospital_profile/',hospital_profile,name='hospital_profile'),
    url(r'^hosp_prof_up/',hosp_prof_up,name='hosp_prof_up'),
    url(r'^vw_cart_order/',vw_cart_order,name='vw_cart_order'),
    url(r'^del_test/',del_test,name='del_test'),
    url(r'^deleting_test/',deleting_test,name='deleting_test'),
    url(r'^admin_hospital_vw/',admin_hospital_vw,name='admin_hospital_vw'),
    url(r'^admin_pharmacy_vw/',admin_pharmacy_vw,name='admin_pharmacy_vw'),
    url(r'^admin_lab_vw/',admin_lab_vw,name='admin_lab_vw'),
    url(r'^admin_patient_vw/',admin_patient_vw,name='admin_patient_vw'),
    url(r'^admin_dr_vw/',admin_dr_vw,name='admin_dr_vw'),
    url(r'^delete_hos/',delete_hos,name='delete_hos'),
    url(r'^delete_phar/',delete_phar,name='delete_phar'),
    url(r'^delete_lab/',delete_lab,name='delete_lab'),
    url(r'^delete_patient/',delete_patient,name='delete_patient'),
    url(r'^delete_dr/',delete_dr,name='delete_dr'),
    url(r'^patient_prof_up/',patient_prof_up,name='patient_prof_up'),
    url(r'^phar_prof_up/',phar_prof_up,name='phar_prof_up'),
    url(r'^dr_prof_up/',dr_prof_up,name='dr_prof_up'),
    url(r'^lab_prof_up/',lab_prof_up,name='lab_prof_up'),
    url(r'^admin_prof_up/',admin_prof_up,name='admin_prof_up'),
    url(r'^apple/',apple,name='apple'),
    url(r'^top10/',top10,name='top10'),
    url(r'^med_vw/',med_vw,name='med_vw'),
    url(r'^delete_med/',delete_med,name='delete_med'),
    url(r'^disease/',disease,name='disease'),
    url(r'^adddisease/',adddisease,name='adddisease'),
    url(r'^viewdiseasepage/',viewdiseasepage,name='viewdiseasepage'),
    url(r'^healthcheck/',healthcheck,name='healthcheck'),
    url(r'^prescription/',prescription,name='prescription'),
    url(r'^uploadprescription/',uploadprescription,name='uploadprescription'),
    url(r'^pharmacyviewprescription/',pharmacyviewprescription,name='pharmacyviewprescription'),
    url(r'^presc_status/',presc_status,name='presc_status'),
    url(r'^dr_dt/',dr_dt,name='dr_dt'),
    url(r'^user_feedback/',user_feedback,name='user_feedback'),
    url(r'^addfeedback/',addfeedback,name='addfeedback'),
    url(r'^viewfeedback/',viewfeedback,name='viewfeedback'),
    

    


]
