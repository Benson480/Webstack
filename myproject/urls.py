"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.conf.urls.static import static
from grappelli import urls as grappelli_urls



from myapp.views import (
    register_view, login_view, logout_view, dashboard, Employee_view, index, about,
    contacts, Employer_dashboard, Inventory, profile, Employee_details, departments, report_dashboard,
    daily_usage_report, purchased_stock_report, physical_stock_take_report, budget_report, price_list_report, items_classification_report,
    forex_exchange_rates_report, mysettings, analytics_view, DynamicChartView, business_settings, announcement_list, add_to_cart,
    purchase_item, make_order, cart_view, remove_from_cart, order_confirmation_view, enroll_student, success_page,careers_list,
    career_detail, request_software, request_success, upload_file,  sales_list, download_sales_csv, delete_sales, student_manage,
    upload_certificate, student_list, student_delete
    )

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/register/', register_view, name='register'),
    path('Employee/', Employee_view, name='Employee'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('Employer_dashboard/', Employer_dashboard, name='Employer_dashboard'),
    path('Inventory/', Inventory, name='Inventory'),
    path('profile/', profile, name='profile'),
    path('Employee_details/', Employee_details, name='Employee_details'),
    path('departments/', departments, name='departments'),
    path('report_dashboard/', report_dashboard, name='report_dashboard'),
    path('daily-usage/', daily_usage_report, name='daily_usage_report'),
    path('purchased-stock/', purchased_stock_report, name='purchased_stock_report'),
    path('physical-stock-take/', physical_stock_take_report, name='physical_stock_take_report'),
    path('budget/', budget_report, name='budget_report'),
    path('price-list/', price_list_report, name='price_list_report'),
    path('items-classification/', items_classification_report, name='items_classification_report'),
    path('forex-exchange-rates/', forex_exchange_rates_report, name='forex_exchange_rates_report'),
    path('mysettings/', mysettings, name='settings'),
    path('business_settings/', business_settings, name='business_settings'),
    path('analytics/', analytics_view, name='analytics'),
    path('dynamic_chart/', DynamicChartView.as_view(), name='dynamic_chart'),
    path('announcements/', announcement_list, name='announcements'),
    path('add_to_cart/<int:image_id>/', add_to_cart, name='add_to_cart'),
    path('purchase_item/<int:image_id>/', purchase_item, name='purchase_item'),
    path('make_order/', make_order, name='make_order'),
    path('cart_view/', cart_view, name='cart_view'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('order_confirmation/<int:order_id>/', order_confirmation_view, name='order_confirmation_view'),
    path('enroll_student/', enroll_student, name='enroll_student'),
    path('success/', success_page, name='success_page'),
    path('logout/', logout_view, name='logout'),
    path('grappelli/', include(grappelli_urls)),
    path('careers/', careers_list, name='careers_list'),
    path('careers/<int:pk>/', career_detail, name='career_detail'),
    path('request_software/', request_software, name='request_software'),
    path('request_success/', request_success, name='request_success'),
    path('upload/', upload_file, name='upload_file'),
    path('sales/', sales_list, name='sales_list'),
    path('download/', download_sales_csv, name='download_sales_csv'),
    path('delete/', delete_sales, name='delete_sales'),
    path('student_list/', student_list, name='student_list'),
    path('manage/', student_manage, name='student_manage'),
    path('manage/<int:pk>/', student_manage, name='student_manage'),
    path('upload_certificate/<int:pk>/', upload_certificate, name='upload_certificate'),
    path('delete/<int:pk>/', student_delete, name='student_delete'),
    

    # path('images/', include('myapp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)