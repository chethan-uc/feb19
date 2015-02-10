from django.test import TestCase
from main.models import *

class Mst_Extractor_TypeCase(TestCase):
    
    def setUp(self):
        Mst_Extractor_Type.objects.create(type_name='local')
        Mst_Extractor_Type.objects.create(type_name='remote')
        
    def test_mst_extractor_return(self):
        local = Mst_Extractor_Type.objects.get(type_name='local')
        self.assertEqual(local.get_extractor_type(),u'local')
        remote = Mst_Extractor_Type.objects.get(type_name='remote')
        self.assertEqual(remote.get_extractor_type(), u'remote')

class Mst_InstanceCase(TestCase):
    
    def setUp(self):
        Mst_Instance.objects.create(private_hostname='localhost', public_hostname='localhost', instance_name='test', is_test_instance=True)
        Mst_Instance.objects.create(private_hostname='10.20.30.50', public_hostname='54.64.74.84', instance_name='prod', is_test_instance=False)
        
    def test_is_test_instance(self):
        test_instance = Mst_Instance.objects.get(instance_name='test')
        self.assertEqual(test_instance.test_instance(), True)
        prod_instance = Mst_Instance.objects.get(instance_name='prod')
        self.assertEqual(prod_instance.test_instance(), False)
        