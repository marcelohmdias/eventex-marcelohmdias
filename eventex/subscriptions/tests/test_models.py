# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(name='Marcelo Dias', 
								cpf='12345678901',
								email='marcelo@dias.com',
								phone='27-12345678')

	def test_create(self):
		'Subscription must have name, cpf, email, phone'
		self.obj.save()
		self.assertEqual(1, self.obj.id)


	def test_has_created_at(self):
		'Subscription must have automatic created_at'
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)


	def test_unicode(self):
		self.assertEqual(u'Marcelo Dias', unicode(self.obj))


	def test_paid_default_value_is_False(self):
		'By default paid must be False.'
		self.assertEqual(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):
	def setUp(self):
		Subscription.objects.create(name='Marcelo Dias',
									cpf='12345678901',
									email='marcelo@dias.com',
									phone='27-12345678')

	def test_cpf_unique(self):
		'CPF must be unique'
		s = Subscription(name='Marcelo Dias',
						cpf='12345678901',
						email='outro@email.com',
						phone='27-12345678')
		self.assertRaises(IntegrityError, s.save)

	def test_email_unique(self):
		'Email must be unique'
		s = Subscription(name='Marcelo Dias',
						cpf='98765432101',
						email='marcelo@dias.com',
						phone='27-12345678')
		self.assertRaises(IntegrityError, s.save)