from .models import Banner

def banner(request):
	first_banner = Banner.objects.first()
	second_banner = Banner.objects.last()
	return dict(first_banner=first_banner, second_banner=second_banner)
