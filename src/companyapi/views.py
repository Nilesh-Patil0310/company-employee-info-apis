from django.http import HttpResponse,JsonResponse


def home_page(request):
    print("Home page requested")
    friends = [
        'Nilesh',
        'Kiran',
        'sagar',
        'Rahul'
    ]
    return JsonResponse(friends,safe=False)