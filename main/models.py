from django.db import models
YES_NO_CHOICES = (
    (0, 'No'),
    (1, 'Yes'),
)

class Mst_Extractor_Type(models.Model):
    type_name = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.type_name
    
    class Meta:
        db_table = u'mst_extractor_type'
        verbose_name = u'Extractor Type'
    def get_extractor_type(self): #s2
        return self.type_name
    
class Mst_Instance(models.Model):
    private_hostname = models.CharField(max_length=250)
    public_hostname = models.CharField(max_length=250)
    instance_name = models.CharField(max_length=250)
    is_test_instance = models.IntegerField(choices = YES_NO_CHOICES)
    def __unicode__(self):
        return self.instance_name
    
    def test_instance(self):
        return True if self.is_test_instance else False
    
    class Meta:
        db_table = u'mst_instance'
        verbose_name = u'Extractor Instance'


class Extractor_File(models.Model):
    
    file_name = models.CharField(max_length = 250, unique=True)
    
    def __unicode__(self):
        return self.file_name
    
    class Meta:
        db_table="extractor_file"
        verbose_name = "Extractor File"


class Extractor(models.Model):
    
    extractor_type = models.ForeignKey(Mst_Extractor_Type)
    instance = models.ForeignKey(Mst_Instance)
    extractor_file = models.ForeignKey(Extractor_File)
    extractor_name = models.CharField(unique=True, max_length=250)
    prefix = models.CharField(max_length=100, blank=True)
    prefix_range = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=10, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    number_of_days_to_negate_from_start_date = models.IntegerField(null=True, blank=True, default=0)
    number_of_days_to_extract = models.IntegerField(null=True, blank=True, default=0)
    number_of_slots = models.IntegerField(null=True, blank=True)
    slot_to_fetch = models.IntegerField(null=True, blank=True)
    info = models.TextField(blank=True)
    start_case_number = models.IntegerField(null=True, blank=True)
    number_of_cases_to_fetch = models.IntegerField(default = 0)
    threshold = models.IntegerField(null=True, blank=True)
    number_of_digits_in_case_number = models.IntegerField(null=True, blank=True)
    local_only = models.IntegerField(null=True, blank=True, choices=YES_NO_CHOICES)
    verbose = models.IntegerField(null=True, blank=True, choices=YES_NO_CHOICES)
    output = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.extractor_name
    
