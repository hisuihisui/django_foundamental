from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Group, Message


# Create your tests here.
class SnsTests(TestCase):
    # setUpClassが初めに実行される
    @classmethod
    def setUpClass(cls):
        # 初めに必ず実行する
        super().setUpClass()
        (user, pb_grp) = cls.create_user_and_group()
        cls.create_message(user, pb_grp)

    # setupclassでselfを引数に取っていないため、呼び出すメソッドにも@classmethodをつける
    @classmethod
    def create_user_and_group(cls):
        # Create public user & public group
        User(username="public", password="public", is_staff=False, is_active=True).save()
        pb_user = User.objects.filter(username="public").first()
        Group(title="public", owner_id=pb_user.id).save()
        pb_grp = Group.objects.filter(title="public").first()

        # Create test user
        User(username="test", password="test", is_staff=True, is_active=True).save()
        user = User.objects.filter(username="test").first()

        return (user, pb_grp)

    @classmethod
    def create_message(cls, user, group):
        # Create test message
        Message(content="this is test message.", owner_id=user.id, group_id=group.id).save()
        Message(content="test", owner_id=user.id, group_id=group.id).save()
        Message(content="ok", owner_id=user.id, group_id=group.id).save()
        Message(content="ng", owner_id=user.id, group_id=group.id).save()
        Message(content="finish", owner_id=user.id, group_id=group.id).save()

    def test_check(self):
        user = User.objects.filter(username="test").first()
        message = Message.objects.filter(content="test").first()

        self.assertIs(message.owner_id, user.id)
        self.assertEqual(message.owner.username, user.username)
        self.assertEqual(message.group.title, "public")

        c = Message.objects.all().count()
        self.assertIs(c, 5)

        message1 = Message.objects.all().first()
        message2 = Message.objects.all().last()
        self.assertIsNot(message1, message2)

        # access to SNS.
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)

        # login test account and access to SNS.
        self.client.force_login(user)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "this is test message.")

