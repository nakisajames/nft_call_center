from django.db import models


class UserGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "user_group"


class GroupPermission(models.Model):
    id = models.AutoField(primary_key=True)
    user_group = models.ForeignKey(UserGroup, on_delete=models.PROTECT, null=True, blank=True)
    table_name = models.CharField(max_length=200)
    add = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
    list = models.BooleanField(default=False)
    view = models.BooleanField(default=False)

    class Meta:
        db_table = "group_permission"


class UserAccount(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    user_photo = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    sur_name = models.CharField(max_length=50, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    primary_email = models.CharField(max_length=50, null=True, blank=True)
    secondary_email = models.CharField(max_length=50, null=True, blank=True)
    primary_phone = models.CharField(max_length=50, null=True, blank=True)
    secondary_phone = models.CharField(max_length=50, null=True, blank=True)

    user_group = models.ForeignKey(UserGroup, on_delete=models.PROTECT, null=True, blank=True)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=15, null=True, blank=True)
    entry_date = models.DateTimeField(null=True, blank=True)
    entered_by = models.CharField(max_length=50, null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "user_account"


class UserSetting(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(UserAccount, on_delete=models.PROTECT, null=True, blank=True,
                                   related_name="user_setting_user")
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    entry_date = models.DateTimeField(null=True, blank=True)
    entered_by = models.ForeignKey(UserAccount, on_delete=models.PROTECT, null=True, blank=True, related_name="user_setting_entered_by")
    last_modified = models.DateTimeField(null=True, blank=True)
    modified_by = models.ForeignKey(UserAccount, on_delete=models.PROTECT, null=True, blank=True, related_name="user_setting_modified_by")

    class Meta:
        db_table = "user_setting"


class SystemLog(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    entry_date = models.DateTimeField(null=True, blank=True)
    table_name = models.CharField(max_length=50)
    record_id = models.CharField(max_length=50, null=True, blank=True)
    operation_type = models.CharField(max_length=50)
    operation_summary = models.CharField(max_length=100)
    full_description = models.CharField(max_length=500)
    user_id = models.CharField(max_length=50, null=True, blank=True)
    account_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "system_log"


class SystemSetting(models.Model):
    id = models.CharField(max_length=50, primary_key=True)

    lab_id_counter = models.IntegerField(null=True, blank=True)

    entry_date = models.DateTimeField(null=True, blank=True)
    entered_by = models.ForeignKey(UserAccount, on_delete=models.PROTECT, null=True, blank=True, related_name="system_setting_entered_by")
    last_modified = models.DateTimeField(null=True, blank=True)
    modified_by = models.ForeignKey(UserAccount, on_delete=models.PROTECT, null=True, blank=True, related_name="system_setting_modified_by")

    class Meta:
        db_table = "system_setting"


class SatisfactionForm(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    agent = models.ForeignKey(UserAccount, on_delete=models.PROTECT, null=True, blank=True,
                              related_name="satisfaction_form_agent")
    consent = models.CharField(max_length=20)

    rate_nft_services = models.TextField(null=True, blank=True)
    why_rate_nft_services = models.TextField(null=True, blank=True)
    rate_nft_recommendation = models.IntegerField(null=True, blank=True)
    why_rate_nft_recommendation = models.TextField(null=True, blank=True)

    improve_nft_experience = models.TextField(null=True, blank=True)
    any_comments = models.TextField(null=True, blank=True)

    entry_date = models.DateTimeField(null=True, blank=True)
    entered_by = models.ForeignKey(UserAccount, on_delete=models.PROTECT, null=True, blank=True,
                                   related_name="satisfaction_form_entered_by")
    last_modified = models.DateTimeField(null=True, blank=True)
    modified_by = models.ForeignKey(UserAccount, on_delete=models.PROTECT, null=True, blank=True,
                                    related_name="satisfaction_form_modified_by")

    class Meta:
        db_table = "satisfaction_form"








