from django.urls import path
from .views import DashboardView, CoachPanelView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('coach-panel/', CoachPanelView.as_view(), name='coach_panel'),
]
