from django.db import models

# Create your models here.

class Customer(models.Model):
    # 客户信息表
    name=models.CharField(max_length=32,blank=True,null=True)
    qq=models.CharField(max_length=64,unique=True)
    phone=models.CharField(max_length=64,blank=True,null=True)
    source_choices=(
        (0,'referal'),
        (1,'qq群'),
        (2,'官网'),
        (3,'百度推广'),
        (4,'51CTO'),
        (5,'知乎'),
        (6,'市场推广'),
    )
    source=models.SmallIntegerField(choices=source_choices)

    referral_form=models.CharField(verbose_name="转介绍人qq",max_length=64,blank=True,null=True)

    consult_course=models.ForeignKey('Course',verbose_name='咨询课程')

    consult_content=models.TextField(verbose_name='咨询详情')

    tags=models.ManyToManyField('Tag',blank=True,null=True)

    consultant=models.ForeignKey('UserProfile')

    note=models.TextField(blank=True,null=True)

    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name=models.CharField(unique=True,max_length=32)

class CustomerFollowup(models.Model):
    # 客户跟进表
    customer=models.ForeignKey('Customer')
    content=models.TextField(verbose_name='跟进内容')
    consultant=models.ForeignKey('UserProfile')
    date=models.DateField(auto_now_add=True)
    intention_choices=(
        (0,'2周内报名'),
        (1,'1个月内报名'),
        (2,'近期无报名计划'),
        (3,'已在其他机构报名'),
        (4, '已报名'),
    )
    intention=models.SmallIntegerField(choices=intention_choices)

    def __str__(self):
        return "<%s:%s>" %(self.customer.name,self.intention)

class UserProfile(models.Model):
    # 账户表
    pass

class Role(models.Model):
    # 角色表
    pass

class Course(models.Model):
    # 课程表
    name=models.CharField(max_length=64,unique=True)
    price=models.PositiveIntegerField()
    period=models.PositiveIntegerField(verbose_name='周期(月)')
    outline=models.TextField()
    def __str__(self):
        return self.name

class Branch(models.Model):
    # 校区
    name=models.CharField(max_length=128,unique=True)
    addr=models.CharField(max_length=128)
    def __str__(self):
        return self.name


class classList(models.Model):
    # 班级表
    branch=models.ForeignKey("Branch")
    course=models.ForeignKey("Course")
    class_type_choices=(
        (0,'面授(脱产)'),
        (1,'面授(周末)'),
        (2,'网络班'),
    )
    choice=models.SmallIntegerField(choices=class_type_choices,verbose_name="班级类型")
    semester=models.PositiveIntegerField(verbose_name="学期")
    teachers=models.ManyToManyField("UserProfile")
    start_date=models.DateField(verbose_name="开班日期")
    end_date=models.DateField(verbose_name="结业日期",blank=True,null=True)

    def __str__(self):
        return "%s-%s-%s" %(self.branch,self.course,self.semester)



class CourseRecord(models.Model):
    # 上课记录
    pass

class StudyRecord(models.Model):
    # 学习记录表
    pass

class Enrollment(models.Model):
    # 报名表
    pass

class Student(models.Model):
    pass