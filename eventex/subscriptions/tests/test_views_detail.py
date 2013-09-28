# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class DetailTest(TestCase):
	def setUp(self):
		s = Subscription.objects.create(name='Marcelo Dias',
										cpf='12345678901',
										email='marcelo@dias.com',
										phone='27-12345678')
		self.resp = self.client.get(r('subscriptions:detail', args=[s.pk]))


	def test_get(self):
		'GET /inscricao/1/ should return status 200.'
		self.assertEqual(200, self.resp.status_code)


	def test_template(self):
		'Uses template'
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')


	def detail(request, pk):
		return render(request, 'subscriptions/subscription_detail.html')


	def test_context(self):
		'Context must have a subscription instance.'
		subscription = self.resp.context['subscription']
		self.assertIsInstance(subscription, Subscription)


	def test_html(self):
		'CHeck if subscription data was redered.'
		self.assertContains(self.resp, 'Marcelo Dias')


class DetailNotFound(TestCase):
	def test_not_found(self):
		response = self.client.get(r('subscriptions:detail', args=[0]))
		self.assertEqual(404, response.status_code)