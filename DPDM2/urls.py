from django.urls import path

from Disasterprjt import settings
from django.conf.urls.static import static
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('admin_path',views.admin_index,name='admin_path'),
    path('login',views.login_index,name='login'),
    path('campregi',views.campreg,name='campregi'),
    path('publicpath',views.publicreg,name='publicpath'),
    path('volpath',views.volunteerreg,name='volpath'),
    path('stationpath',views.stationreg,name='stationpath'),
    path('camppage',views.camp_entry,name='camppage'),
    path('publicpage',views.public_entry,name='publicpage'),
    path('volunteerpage',views.volunteer_entry,name='volunteerpage'),
    path('stationpage',views.station_entry,name='stationpage'),
    path('camp_profile_path',views.camp_pro,name='camp_profile_path'),
    path('public_profile_path',views.public_pro,name='public_profile_path'),
    path('station_profile_path',views.station_pro,name='station_profile_path'),
    path('volunteer_profile_path',views.volunteer_pro,name='volunteer_profile_path'),
    path('camp_table_path',views.camp_tab,name='camp_table_path'),
    path('public_table_path',views.public_tab,name='public_table_path'),
    path('volunteer_table_path',views.volunteer_tab,name='volunteer_table_path'),
    path('station_table_path',views.station_tab,name='station_table_path'),
    path('camp_approve/<int:id>/',views.camp_approve,name='camp_approve'),
    path('camp_reject/<int:id>/',views.camp_reject,name='camp_reject'),
    path('station_approve/<int:id>/',views.station_approve,name='station_approve'),
    path('station_reject/<int:id>/',views.station_reject,name='station_reject'),
    path('volunteer_approve/<int:id>/',views.volunteer_approve,name='volunteer_approve'),
    path('volunteer_reject/<int:id>/',views.volunteer_reject,name='volunteer_reject'),
    path('add_refugee',views.add_refugee,name='add_refugee'),
    path('view_refugee',views.view_refugee,name='view_refugee'),
    path('delete_refugee/<int:id>/',views.delete_refugee,name='delete_refugee'),
    path('edit_refugee/<int:id>/',views.edit_refugee,name='edit_refugee'),
    path('view_refugee_public',views.view_refugee_public,name='view_refugee_public'),
    path('needs_camp',views.needs_camp,name='needs_camp'),
    path('manage_needs',views.manage_needs,name='manage_needs'),
    path('edit_needs/<int:id>/',views.edit_needs,name='edit_needs'),
    path('delete_needs/<int:id>/',views.delete_needs,name='delete_needs'),
    path('admin_needs',views.admin_needs,name='admin_needs'),
    path('update_needs_status/<int:id>/',views.update_needs_status,name='update_needs_status'),
    path('volunteer_request',views.volunteer_request_camp,name='volunteer_request'),
    path('admin_volunteer_request',views.admin_volunteer_request,name='admin_volunteer_request'),
    path('allot_volunteers/<int:id>/',views.allot_volunteers,name='allot_volunteers'),
    path('allot_now/<int:vid>/<int:rid>/', views.allot_now, name='allot_now'),
    # path('assigned_volunteers/', views.assigned_volunteers, name='assigned_volunteers'),
    path('volunteer_camp',views.volunteer_camp,name='volunteer_camp'),
    path('duty_camp/<int:id>/',views.duty_camp,name='duty_camp'),
    path('duty_volunteer',views.duty_volunteer,name='duty_volunteer'),
    path('duty_complete/<int:id>/',views.duty_complete,name='duty_complete'),
    path('emergency_request_camp',views.emergency_request_camp,name='emergency_request_camp'),
    path('missing_person_details',views.missing_person_details,name='missing_person_details'),
    path('registered_station',views.registered_station,name='registered_station'),
    path('find_vehicle/<int:id>/',views.find_vehicle,name='find_vehicle'),
    path('missing_vehicle',views.missing_vehicle_details,name='missing_vehicle'),
    path('found_person/<int:id>/',views.found_person,name='found_person'),
    path('not_found_person/<int:id>/',views.not_found_person,name='not_found_person'),
    path('missing_person_station',views.missing_person_station,name='missing_person_station'),
    path('missing_person_public',views.missing_person_public,name='missing_person_public'),
    path('edit_missing_person/<int:id>/',views.edit_missing_person,name='edit_missing_person'),
    path('delete_missing_person/<int:id>/',views.delete_missing_person,name='delete_missing_person'),
    path('mark_as_found/<int:id>/',views.mark_as_found,name='mark_as_found'),
    path('fund_allocation',views.fund_allocation,name='fund_allocation'),
    path('fund_allocation_public',views.fund_allocation_public,name='fund_allocation_public'),
    path('edit_fund_public/<int:id>/',views.edit_fund_public,name='edit_fund_public'),
    path('delete_fund_public/<int:id>/',views.delete_fund_public,name='delete_fund_public'),
    path('fund_allocation_admin',views.fund_allocation_admin,name='fund_allocation_admin'),
    path('assign_camp/<int:id>/',views.assign_camp,name='assign_camp'),
    path('assign_the_camp/<int:camp_id>/<int:fund_id>/', views.assign_the_camp, name='assign_the_camp'),
    path('fund_allocation_camp',views.fund_allocation_camp,name='fund_allocation_camp'),
    path('approve_fund_by_camp/<int:assign_id>/',views.approve_fund_by_camp,name='approve_fund_by_camp'),
    path('reject_fund_by_camp/<int:assign_id>/',views.reject_fund_by_camp,name='reject_fund_by_camp'),
    path('view_assigned_camp/<int:fund_id>/',views.view_assigned_camp,name='view_assigned_camp'),
    path('approve_fund_by_admin/<int:id>/',views.approve_fund_by_admin,name='approve_fund_by_admin'),
    path('reject_fund_by_admin/<int:id>/',views.reject_fund_by_admin,name='reject_fund_by_admin'),
    path('amount_transfer/<int:id>/<int:fund_id>/',views.amount_transfer,name='amount_transfer'),
    path('paymentindex/<int:amt>/<int:fund_id>/',views.paymentindex,name='paymentindex'),
    path('emergency_request_station',views.emergency_request_station,name='emergency_request_station'),
    path('volunteer_camp_list',views.volunteer_camp_list, name='volunteer_camp_list'),
    path('logout/', views.logout_view, name='logout'),
    path("weather/", views.get_weather, name="weather"),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
