from django.contrib import admin

from cms.models import Book, Impression

# admin.site.register(Book)
# admin.site.register(Impression)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'page',)  # 一覧に表示したい項目
    list_display_links = ('id', 'name',)  # リンクをクリックできるようにする項目


admin.site.register(Book, BookAdmin)


class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
    raw_id_fields = ('book',)  # 外部キーをプルダウンしない（データ件数が増加した場合のタイムアウト予防）


admin.site.register(Impression, ImpressionAdmin)