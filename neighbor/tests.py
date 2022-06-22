from django.test import TestCase
from .models import post, profile,  Business
# Create your tests here.
               
class BusinessTestClass(TestCase):
    def setUp(self):
        self.business = Business(name='fish palor', location='Rpysambu', occupants='0', description='description', admin='admin', police_number=999, health_number=07123456)
        self.business.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def tearDown(self):
        Business.objects.all().delete()

    def test_save_business(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_delete_business(self):
        self.business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)

    def test_search_business(self):
        self.business.save_business()
        business = Business.search_business('fish')
        self.assertTrue(len(business) > 0)   

class ProfileTestClass(TestCase):
    def test_is_true(self):
        self.assertTrue(True)

    def tearDown(self) :
        profile.objects.all().delete()
        post.objects.all().delete() 

    def test_instance(self):
        self.assertTrue(isinstance(self.post, post))     


class post_test(TestCase):
    def setup(self):
        self.neighborhood = NeighborHood(name='fish palor', location='Rpysambu', occupants='0', description='description', admin='admin', police_number=999, health_number=07123456)
        self.neighborhood.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.neighborhood, NeighborHood))

    def test_delete_method(self):
        self.neighborhood.delete_neighborhood()
        neighborhoods = NeighborHood.objects.all()
        self.assertTrue(len(neighborhoods) == 0)       

         

class profile_test(TestCase):
    def test_is_true(self):
        self.assertTrue(True)

class neighborhood_test(TestCase):
    def test_is_true(self):
        self.assertTrue(True)

class user_test(TestCase):
    def test_is_true(self):
        self.assertTrue(True)         
   


        