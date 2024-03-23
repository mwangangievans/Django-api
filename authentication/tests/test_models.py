from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):

    def test_create_user(self):
      user = User.objects.create_user('evans','evans@gmail.com','1234')
      self.assertIsInstance(user,User)
      self.assertFalse(user.is_staff)
      self.assertFalse(user.is_superuser)
      self.assertEqual(user.email ,'evans@gmail.com')


    def test_create_super_user(self): 
      user = User.objects.create_superuser('evans','evans@gmail.com','1234')
      self.assertIsInstance(user,User)
      self.assertTrue(user.is_staff)
      self.assertTrue(user.is_superuser)
      self.assertEqual(user.email ,'evans@gmail.com')
        

    def test_raises_error_with_message_when_no_email_supplied(self):
       with self.assertRaisesMessage(ValueError,'The given email must be set'):
          User.objects.create_superuser(username='username',email='',password='1234')


    def test_cant_create_super_user_with_no_is_staff_status(self):
       with self.assertRaisesMessage(ValueError,'Super user must have is_staff=True.'):
          User.objects.create_superuser(username='evans',email='evan@gmail.com',password='1234',is_staff=True)

    def test_cant_create_super_user_with_no_is_super_user_status(self):
       with self.assertRaisesMessage(ValueError,'Super user must have is_superuser=True.'):
          User.objects.create_superuser(username='evans',email='evan@gmail.com',password='1234',is_superuser=True)

          