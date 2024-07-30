from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'address_line1', 'city', 'state', 'pincode')
    search_fields = ('user__username', 'user__email', 'address_line1', 'city', 'state', 'pincode')
    list_filter = ('user_type',)
    readonly_fields = ('user',) 

    def get_readonly_fields(self, request, obj=None):
        if obj:  
            return self.readonly_fields + ('user',)
        return self.readonly_fields
