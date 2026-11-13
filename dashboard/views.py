from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from accounts.models import CustomUser


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Main dashboard — visible to all authenticated users.
    Coaches and Players see different content via the template.
    """
    template_name = 'dashboard/home.html'

    def get_template_names(self):
        """Return role-specific dashboard template."""
        user = self.request.user
        if user.role == CustomUser.Role.COACH:
            return ['dashboard/coach_dashboard.html']
        return ['dashboard/player_dashboard.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['total_users'] = CustomUser.objects.count()
        context['total_players'] = CustomUser.objects.filter(
            role=CustomUser.Role.PLAYER
        ).count()
        context['total_coaches'] = CustomUser.objects.filter(
            role=CustomUser.Role.COACH
        ).count()
        context['is_coach'] = user.role == CustomUser.Role.COACH
        return context


class CoachPanelView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """
    Coach-only panel — returns 403 if a Player tries to access it.
    """
    template_name = 'dashboard/coach_panel.html'

    def test_func(self):
        return self.request.user.role == CustomUser.Role.COACH

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_users'] = CustomUser.objects.all().order_by('-date_joined')
        context['total_users'] = CustomUser.objects.count()
        context['total_players'] = CustomUser.objects.filter(
            role=CustomUser.Role.PLAYER
        ).count()
        context['total_coaches'] = CustomUser.objects.filter(
            role=CustomUser.Role.COACH
        ).count()
        return context
