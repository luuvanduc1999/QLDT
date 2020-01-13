from django.db import models
from django.conf import settings
from datetime import datetime   


# Create your models here.
class ScheduleWeek(models.Model):
    class Meta:
        verbose_name = 'Lịch công tác'
        verbose_name_plural = 'Lịch công tác'
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500, verbose_name="Tiêu đề")
    note=models.CharField(max_length=500, verbose_name="Ghi chú", help_text="VD: Lớp trực tuần, ...")
    caption = models.TextField(blank=True, verbose_name="Nội dung", help_text="VD: Nhắc nhở, Thông tin thêm...")
    thumb= models.ImageField(null=True, verbose_name="Thumb", help_text="Hiển thị trên trang chủ")
    image= models.ImageField(null=True, verbose_name="Lịch công tác", help_text="Lịch công tác")
    submission_date = models.DateTimeField(default=datetime.now(), editable=False)
    edit = models.ImageField(null=True, blank=True, default="edit.png")

    objects = models.Manager()

    def __str__(self):
        return self.title

class Notification(models.Model):
    class Meta:
        verbose_name = 'Thông báo'
        verbose_name_plural = 'Thông báo'

    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500, verbose_name="Tiêu đề")
    note=models.CharField(max_length=500, verbose_name="Ghi chú", help_text="VD: Học kỳ, ...")
    caption = models.TextField(blank=True, verbose_name="Nội dung", help_text="VD: Nhắc nhở, Thông tin thêm...")
    thumb= models.ImageField(null=True, verbose_name="Thumb", help_text="Hiển thị trên trang chủ")
    file= models.FileField(null=True, blank=True, verbose_name="File đính kèm", help_text="Văn bản")
    submission_date = models.DateTimeField(default=datetime.now(), editable=False)
    edit = models.ImageField(null=True, blank=True, default="edit.png")

    objects = models.Manager()
    def __str__(self):
        return self.title

class Event(models.Model):
    class Meta:
        verbose_name = 'Tin tức, Sự kiện'
        verbose_name_plural = 'Tin tức, Sự kiện'
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500, verbose_name="Tiêu đề")
    note=models.CharField(max_length=500, verbose_name="Ghi chú", help_text="VD: Lớp trực tuần, ...")
    caption = models.TextField(blank=True, verbose_name="Nội dung", help_text="VD: Nhắc nhở, Thông tin thêm...")
    thumb= models.ImageField(null=True, verbose_name="Thumb", help_text="Hiển thị trên trang chủ")
    image= models.ImageField(null=True, verbose_name="Hình ảnh", help_text="Thông tin, hình ảnh")
    submission_date = models.DateTimeField(default=datetime.now(), editable=False)
    edit = models.ImageField(null=True, blank=True, default="edit.png")

    objects = models.Manager()

    def __str__(self):
        return self.title

class Document(models.Model):
    class Meta:
        verbose_name = 'Văn bản trường'
        verbose_name_plural = 'Văn bản trường'

    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500, verbose_name="Tiêu đề")
    note=models.CharField(max_length=500, verbose_name="Ghi chú", help_text="VD: Văn bản số, quyết định ...")
    caption = models.TextField(blank=True, verbose_name="Nội dung")
    thumb= models.ImageField(null=True, verbose_name="Thumb", help_text="Hiển thị trên trang chủ")
    file= models.FileField(null=True, verbose_name="File đính kèm", help_text="Văn bản")
    submission_date = models.DateTimeField(default=datetime.now(), editable=False)
    edit = models.ImageField(null=True, blank=True, default="edit.png")

    objects = models.Manager()
    def __str__(self):
        return self.title        