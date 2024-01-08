from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from wishlist.models import WishlistItem
from .forms import ProductForm
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

    if request.user.is_authenticated:
        wishlist_product_ids = WishlistItem.objects.filter(user=request.user).values_list('product_id', flat=True)
    else:
        wishlist_product_ids = []

    context = {
        'product': product,
        'wishlist_product_ids': wishlist_product_ids,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product successfully added!')
            return redirect(reverse('product_detail', args=[product.slug]))
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can edit products.')
        return redirect('home')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully updated!')
            return redirect('product_detail', slug=product.slug)
        else:
            form = ProductForm(instance=product)

    form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product
    }

    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can delete products.')
        return redirect('home')

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product successfully deleted!')
        return redirect(reverse('products'))

    context = {'product': product}
    return render(request, 'products/delete_product.html', context)
