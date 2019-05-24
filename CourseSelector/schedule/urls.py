from django.urls import path
from .views import HomeView, scheduleUpdateView, update_schedule, add_course_in_schedule

app_name = 'schedule'

urlpatterns = [
    path('', HomeView.as_view(), name='schedule'),
    path('update', scheduleUpdateView.as_view(), name='update_schedule'),
    path('addcourse', update_schedule.as_view(), name='add_course_table'),
    path('add_courses_in_schedule', add_course_in_schedule.as_view(), name='add_course_in_schedule'),
]