from django.shortcuts import redirect, render
from reviews.forms import ReviewsForm
from .models import Reviews


# Create your views here.
def home(request):
    return render(request, "reviews/home.html")


def index(request):
    reviews = Reviews.objects.all()

    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)

def create(request):

    if request.method == "POST":
        reviews_form = ReviewsForm(request.POST)
        if reviews_form.is_valid():
            reviews_form.save()
            return redirect("reviews:index")
    else:
        reviews_form = ReviewsForm()

    context = {
        "reviews_form": reviews_form,
    }

    return render(request, "reviews/create.html", context)


def detail(request, pk):

    review = Reviews.objects.get(pk=pk)

    context = {
        "review": review,
    }

    return render(request, "reviews/detail.html", context)


def update(request, pk):

    review = Reviews.objects.get(pk=pk)

    if request.method == "POST":
        reviews_form = ReviewsForm(request.POST, instance=review)
        if reviews_form.is_valid():
            reviews_form.save()
            return redirect("reviews:detail", review.pk)
    else:
        reviews_form = ReviewsForm(instance=review)

    context = {
        "reviews_form": reviews_form,
    }

    return render(request, "reviews/update.html", context)


# get으로 구현, post로 변경 필요
def delete(request, pk):

    review = Reviews.objects.get(pk=pk)
    review.delete()

    return redirect("reviews:index")



# written by RJ
def find(request):
    search = request.GET.get('search')
    reviews = Reviews.objects.all()
    if reviews.exists():
        review = Reviews.objects.get(title=search)
        return redirect('reviews:detail', reviews.pk)
    else:
        return render(request, 'reviews/notfind.html')


# written by sb
# def search(request):
#     if request.method == "POST":
#         searched = request.POST["search"]
#         movie_name = Reviews.objects.filter(movie_name=searched)[0].movie_name
#         correctPK = Reviews.objects.filter(movie_name=movie_name).values("pk")[0]["pk"]
#     return redirect("reviews:detail", correctPK)
