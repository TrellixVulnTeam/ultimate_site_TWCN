from django.shortcuts import render

# Create your views here.


def chartView(request):
	print('chart View pokrenut')
	print('pokrenut view')
	broj = 15000
	return render(request, 'charts/chart.html', {'broj': broj})