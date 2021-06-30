from django.shortcuts import render, redirect
from .forms import DonationForm
from .models import donations

charity = [{"name": "World Vision", "imageurl": "https://bit.ly/3x6Xv3k", "url": "https://bit.ly/3dkDhLB"},
           {"name": "SOS Children",
               "imageurl": "https://www.soschildrensvillages.in/wp-content/uploads/2020/09/SOS-Logo-Actual.png",
           "url": "https://www.soschildrensvillages.in/"},
           {"name": "UNHCR", "imageurl": "https://donate.unhcr.org/themes/custom/donate/logo.svg",
               "url": "https://bit.ly/3jnM5UK"},
           {"name": "WHO", "imageurl": "https://www.who.int/images/default-source/infographics/logo-who.tmb-1200v.jpg?Culture=en&sfvrsn=2fcc68a0_15",
               "url": "https://www.who.int/"},
           {"name": "Akshaya Patra",
               "imageurl": "https://images.jg-cdn.com/image/e5c1b8c7-43c9-4550-bfad-26025ced5541.png", "url": "https://bit.ly/3xXzknP"},
           {"name": "giveIndia", "imageurl": "https://cdn.givind.org/static/images/giveindia-logo-v2.jpg", "url": "https://www.giveindia.org/"}]


def donations_main(request):
    dons = donations.objects.all().order_by("-id")
    print(dons)
    d = {"charities": charity, "donations": dons}
    return render(request, 'donations/donation_main.html', d)

# Create your views here.


def add_donation(request):
    print(request.user)
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.instance.reciever = request.user
            form.save()
            return redirect('/donations/')
    else:
        form = DonationForm()
        return render(request, 'donations/donation_details.html', {'form': form})
