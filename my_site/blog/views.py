from datetime import date

from django.shortcuts import render

from .models import Post

all_posts = [
    {
        "slug": "hike-through-the-city",
        "image": "ChicagoFireworks.jpg",
        "author": "Randy Zeleznak",
        "date": date(2021, 6, 15),
        "title": "City Boating",
        "excerpt": "There's nothing like a Downtown Lakefront view! I wasn't prepared for the wonderously beautiful views from the lake!",
        "content": """
    (1)Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque dolorum magni
		aut consequuntur, eveniet debitis ducimus quasi veniam inventore at
		asperiores ad porro modi optio totam eum iusto aliquid. Doloremque!
    """
    },
    {
        "slug": "hike-through-the-city2",
        "image": "trebleheartbear.png",
        "author": "Randy Zeleznak",
        "date": date(2021, 6, 25),
        "title": "City Hiking",
        "excerpt": "(2)There's nothing like a Downtown Lakefront view! I wasn't prepared for the wonderously beautiful views from the lake!",
        "content": """
    (2)Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque dolorum magni
		aut consequuntur, eveniet debitis ducimus quasi veniam inventore at
		asperiores ad porro modi optio totam eum iusto aliquid. Doloremque!
    """
    },
    {
        "slug": "hike-through-the-city3",
        "image": "springdemoone.png",
        "author": "Randy Zeleznak",
        "date": date(2021, 6, 28),
        "title": "City Walking",
        "excerpt": "(3)There's nothing like a Downtown Lakefront view! I wasn't prepared for the wonderously beautiful views from the lake!",
        "content": """
    (3)Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque dolorum magni
		aut consequuntur, eveniet debitis ducimus quasi veniam inventore at
		asperiores ad porro modi optio totam eum iusto aliquid. Doloremque!
    """
    }

]


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
