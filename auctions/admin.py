from django.contrib import admin

# Register your models here.
from .models import User, Comment, Listing, Bid

admin.site.register(User)


admin.site.register(Comment)




admin.site.register(Listing)


admin.site.register(Bid)
