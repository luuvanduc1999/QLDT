from django.db import models
from django.conf import settings



# Create your models here.
class Student(models.Model):
    class Meta:
        verbose_name = 'Học Sinh'
        verbose_name_plural = 'Học Sinh'
    
    STATUS= [ ('ON' , 'Đang học'), ('OFF' , 'Thôi học') ]
    GENDERs= [ ('M' , 'Nam'), ('F' , 'Nữ') ]
    Years=models.IntegerField(default=2019,verbose_name="Năm vào học")
    identityS = models.CharField(max_length=10, primary_key=True, verbose_name="Mã HS")
    name=models.CharField(max_length=200, null=False,default='', verbose_name="Họ và tên")
    gender=models.CharField(max_length=2, choices=GENDERs, default='M',verbose_name='Giới tính')
    dob=models.DateField( verbose_name='Ngày sinh')



    status=models.CharField( max_length=5, choices=STATUS, null=False, default='ON', verbose_name='Trạng thái')
    image=models.ImageField(verbose_name='Ảnh thẻ',default='default_image.jpg')
    edit = models.ImageField(null=True,default="edit.png")
    objects = models.Manager()
    def __str__(self):
        return self.identityS




    