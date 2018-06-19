from django.db import models


class Accounts(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30)
    passwd = models.CharField(max_length=1024)
    rtime = models.DateField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class Cards(models.Model):
    cardid = models.CharField(primary_key=True, max_length=128)
    upid = models.ForeignKey('Upinfo', models.DO_NOTHING, db_column='upid')
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=512)
    ptime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cards'


class Upinfo(models.Model):
    upid = models.IntegerField(primary_key=True)
    upname = models.CharField(max_length=64)
    des = models.CharField(max_length=512, blank=True, null=True)
    wtime = models.DateField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'upinfo'


class Usrinfo(models.Model):
    uid = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='uid', primary_key=True)
    des = models.CharField(max_length=512, blank=True, null=True)
    face = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usrinfo'


class Watch(models.Model):
    wid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='uid')
    upid = models.ForeignKey(Upinfo, models.DO_NOTHING, db_column='upid')
    uwtime = models.DateField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'watch'