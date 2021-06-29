from datetime import date

from django.shortcuts import render

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
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts": all_posts
    })


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
