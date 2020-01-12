from django.db import models
from django.conf import settings


# HOCSINH .
class Student(models.Model):
    class Meta:
        verbose_name = 'Học Sinh'
        verbose_name_plural = 'Học Sinh'

    STATUS = [('ON', 'Đang học'), ('OFF', 'Thôi học')]
    GENDERs = [('M', 'Nam'), ('F', 'Nữ')]
    Years = models.IntegerField(
        default=2019, null=False, verbose_name="Khóa học (VD:2019) ")
    identityS = models.CharField(
        max_length=10, primary_key=True, verbose_name="Mã HS")
    name = models.CharField(max_length=200, null=False,
                            default='', verbose_name="Họ và tên")
    gender = models.CharField(
        max_length=2, choices=GENDERs, default='M', verbose_name='Giới tính')
    dob = models.DateField(verbose_name='Ngày sinh')

    hometown = models.CharField(null=True, blank=True, max_length=200, verbose_name="Quê quán")
    ethnic = models.CharField(
        null=True, blank=True, max_length=100, verbose_name="Dân tộc")
    religion = models.CharField(
        null=True, blank=True,max_length=100, default='Không', verbose_name="Tôn giáo")
    datebegin = models.DateField(null=True, blank=True, verbose_name='Ngày nhập học')
    addr = models.TextField(null=True, blank=True,max_length=500, default='',
                            verbose_name="Địa chỉ thường trú")
    phonenum = models.CharField(
        null=True, blank=True, max_length=20, verbose_name="Số điện thoại liên hệ")
    status = models.CharField(max_length=5, choices=STATUS,
                              null=False, default='ON', verbose_name='Trạng thái')

    namedad = models.CharField(
        null=True, blank=True, max_length=200, verbose_name="Họ tên bố")
    dobdad = models.IntegerField(null=True, blank=True, verbose_name='Năm sinh bố')
    jobdad = models.CharField(
        null=True, blank=True, max_length=200, verbose_name="Nghề nghiệp bố")
    phonenumdad = models.CharField(
        null=True, blank=True, max_length=20, verbose_name="SĐT bố")    
    namemom = models.CharField(
        null=True, blank=True, max_length=200, verbose_name="Họ tên mẹ")
    dobmom = models.IntegerField(null=True, blank=True, verbose_name='Năm sinh bố')
    jobmom = models.CharField(
        null=True, blank=True, max_length=200, verbose_name="Nghề nghiệp mẹ")
    phonenummom = models.CharField(
        null=True, blank=True, max_length=20, verbose_name="SĐT mẹ")    



    image = models.ImageField(verbose_name='Ảnh thẻ',
                              default='default_image.jpg')
    edit = models.ImageField(null=True, blank=True, default="edit.png")
    
    
    
    objects = models.Manager()

    def __str__(self):
        return self.identityS+' '+self.name


# GIAOVIEN .
class Teacher(models.Model):
    class Meta:
        verbose_name = 'Giáo viên'
        verbose_name_plural = 'Giáo viên'

    STATUS = [('ON', 'Đang dạy'), ('OFF', 'Thôi dạy')]
    GENDERs = [('M', 'Nam'), ('F', 'Nữ')]

    identityT = models.CharField(
        max_length=10, primary_key=True, verbose_name="Mã GV")
    name = models.CharField(max_length=200, null=False,
                            default='', verbose_name="Họ và tên")
    gender = models.CharField(
        max_length=2, choices=GENDERs, default='M', verbose_name='Giới tính')
    dob = models.DateField(verbose_name='Ngày sinh')

    hometown = models.CharField(null=True, blank=True, max_length=200, verbose_name="Quê quán")
    ethnic = models.CharField(
        null=True, blank=True, max_length=100, verbose_name="Dân tộc")
    religion = models.CharField(
        null=True, blank=True,max_length=100, default='Không', verbose_name="Tôn giáo")
    datebegin = models.DateField(null=True, blank=True, verbose_name='Ngày vào dạy')
    addr = models.TextField(null=True, blank=True,max_length=500, default='',
                            verbose_name="Địa chỉ thường trú")
    phonenum = models.CharField(
        null=True, blank=True, max_length=20, verbose_name="Số điện thoại liên hệ")
    status = models.CharField(max_length=5, choices=STATUS,
                              null=False, default='ON', verbose_name='Trạng thái')
    level=models.CharField(
        null=True, blank=True,max_length=100, default='', verbose_name="Trình độ cấp bậc")

    image = models.ImageField(verbose_name='Ảnh thẻ',
                              default='default_image.jpg')
    edit = models.ImageField(null=True, blank=True, default="edit.png")
    
    
    
    objects = models.Manager()

    def __str__(self):
        return self.identityT+' '+self.name


# GIAOVIEN .
class Class(models.Model):
    class Meta:
        verbose_name = 'Lớp học'
        verbose_name_plural = 'Lớp học'

    identityC = models.CharField(
        max_length=10, primary_key=True, verbose_name="Mã Lớp học", help_text="VD: 2019A, 2018B")

    gvcn = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    classname=models.CharField(
        max_length=10, verbose_name="Tên Lớp học", help_text="VD: 1A, 2B")
    edit = models.ImageField(null=True, blank=True, default="edit.png")

    objects = models.Manager()

    def __str__(self):
        return self.identityC
