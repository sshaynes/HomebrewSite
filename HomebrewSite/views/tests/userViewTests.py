from rest_framework.test import APIRequestFactory

factory = APIRequestFactory(enforce_csrf_checks=True)

request = factory.post('/user/create/', {'user':'drew','age':28,'location':'seattle','name':'westcoast','yearsExperience':3,'avatarURL':'google.com'
}, format='json')

response = view(request)