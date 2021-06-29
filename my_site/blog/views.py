from datetime import date

from django.shortcuts import render

posts = [
    {
        "slug": "hike-through-the-city",
        "image": "ChicagoFireworks.jpg",
        "author": "Randy Zeleznak",
        "date": date(2021, 6, 15),
        "title": "City Boating",
        "excerpt": "There's nothing like a Downtown Lakefront view! I wasn't prepared for the wonderously beautiful views from the lake!",
        "content": """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque dolorum magni
		aut consequuntur, eveniet debitis ducimus quasi veniam inventore at
		asperiores ad porro modi optio totam eum iusto aliquid. Doloremque!
    """
    },
    {
        "slug": "hike-through-the-city2",
        "image": "ChicagoFireworks.jpg",
        "author": "Randy Zeleznak",
        "date": date(2021, 6, 25),
        "title": "City Hiking",
        "excerpt": "There's nothing like a Downtown Lakefront view! I wasn't prepared for the wonderously beautiful views from the lake!",
        "content": """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque dolorum magni
		aut consequuntur, eveniet debitis ducimus quasi veniam inventore at
		asperiores ad porro modi optio totam eum iusto aliquid. Doloremque!
    """
    },
    {
        "slug": "hike-through-the-city3",
        "image": "ChicagoFireworks.jpg",
        "author": "Randy Zeleznak",
        "date": date(2021, 6, 28),
        "title": "City Walking",
        "excerpt": "There's nothing like a Downtown Lakefront view! I wasn't prepared for the wonderously beautiful views from the lake!",
        "content": """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque dolorum magni
		aut consequuntur, eveniet debitis ducimus quasi veniam inventore at
		asperiores ad porro modi optio totam eum iusto aliquid. Doloremque!
    """
    }
]


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = posts.sort(key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
