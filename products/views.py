from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from wishlist.models import WishlistItem
from .models import Product, Category


def all_products_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    query = request.GET.get('q')
    search_done = False
    search_result = True

    if query:
        search_done = True
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

        if not products.exists():
            search_result = False

    if request.user.is_authenticated:
        wishlist_product_ids = WishlistItem.objects.filter(user=request.user).values_list('product_id', flat=True)
    else:
        wishlist_product_ids = []

    paginator = Paginator(products, 6)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'page': page,
        'query': query,
        'search_done': search_done,
        'search_result': search_result,
        'wishlist_product_ids': wishlist_product_ids,
    }

    return render(request, 'products/products.html', context)


def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})
