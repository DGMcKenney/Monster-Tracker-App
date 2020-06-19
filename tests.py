from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Monster, Sighting
from .forms import MonsterForm, SightingForm

#model tests
class MonsterTest(TestCase):
    def test_string(self):
        monster = Monster('kaiju')
        self.assertEqual(str(monster), monster.monster_type)

    def test_table(self):
        self.assertEqual(str(Monster._meta.db_table), 'monster')

class SightingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='myuser')
        self.monster = Monster.objects.create(monster_type = 'kaiju')
        self.sighting = Sighting.objects.create(which_monster = self.monster, when = '2020-06-16', where = 'Tokyo', who = self.user)

    def test_string(self):
        self.assertEqual(str(self.sighting), 'Monster Sighting #: ' + str(self.sighting.id))

    def test_table(self):
        self.assertEqual(str(Sighting._meta.db_table), 'sighting')

#form tests
class Monster_Form_Test(TestCase):
    def test_monsterform_is_valid(self):
        form = MonsterForm(data={'monster_type': 'kaiju', 'monster_name': 'Godzilla', 'monster_details': 'big amphibious reptile'})
        self.assertTrue(form.is_valid())

    def test_monsterform_with_null(self):
        form = MonsterForm(data={'monster_type': 'kaiju'})
        self.assertTrue(form.is_valid())
        
    def test_monsterform_empty(self):
        form = MonsterForm(data={'monster_type': ''})
        self.assertFalse(form.is_valid())

#authentication tests
class New_Monster_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser', password = 'P@ssw0rd1')
        self.monster = Monster(monster_type = 'kaiju', monster_name = 'Godzilla', monster_details = 'big amphibious reptile')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('new_monster'))
        self.assertRedirects(response, '/accounts/login/?next=/monstertrackerapp/new_monster/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username = 'testuser', password = 'P@ssw0rd1')
        response = self.client.get(reverse('new_monster'))
        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monstertrackerapp/new_monster.html')

class New_Sighting_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser', password = 'P@ssw0rd1')
        self.monster = Monster(monster_type = 'kaiju', monster_name = 'Godzilla', monster_details = 'big amphibious reptile')
        self.sighting = Sighting(which_monster = self.monster, when = '2020-06-18', where = 'Tokyo', who = self.test_user, description = 'did not make landfall')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('new_sighting'))
        self.assertRedirects(response, '/accounts/login/?next=/monstertrackerapp/new_sighting/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username = 'testuser', password = 'P@ssw0rd1')
        response = self.client.get(reverse('new_sighting'))
        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monstertrackerapp/new_sighting.html')