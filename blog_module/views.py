from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views import View
from .models import Blog, BlogCategory
from site_module.models import Visit
from comment_module.models import Comment
from comment_module.forms import CommentForm
from account_module.models import User
from tools._main_service import newest_blogs
from tools.http_service import UserIp

# Create your views here.

class BlogsView(ListView):
    template_name = r'blog_module/blogs.html'
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.filter(is_active=True).all()
        context['the_newest_blogs'] = newest_blogs(Blog.objects.filter(is_active=True).all(), 4)
        return context
    
    def get_queryset(self):
        if self.kwargs == {}:
            query = super().get_queryset()
            return query
        else:
            query = super().get_queryset()
            query = query.filter(category__url_title=self.kwargs.get('cat')).all()
            return query



class BlogDetailView(View):
    def get(self, request: HttpRequest, slug):
        comment_form: CommentForm = CommentForm()

        blog: Blog = Blog.objects.filter(is_active=True, slug=slug).first()
        categories: BlogCategory = BlogCategory.objects.filter(is_active=True).all()
        the_newest_blogs: Blog = newest_blogs(Blog.objects.filter(is_active=True).exclude(id=blog.id).all(), 4)
        blog_view: Visit = Visit.objects.filter(blog_id=blog.id, is_visit=True, product_or_blog=Visit.ProductOrBlog.blog_detail).count()

        if request.user.is_authenticated == True:
            new_visit: Visit = Visit()
            new_visit.user_id = request.user.id
            new_visit.ip = UserIp(request)
            new_visit.product_or_blog = new_visit.ProductOrBlog.blog_detail
            new_visit.blog_id = blog.id
            new_visit.is_visit = True
            new_visit.save()
        elif request.user.is_anonymous == True:
            new_visit: Visit = Visit()
            new_visit.ip = UserIp(request)
            new_visit.product_or_blog = new_visit.ProductOrBlog.blog_detail
            new_visit.blog_id = blog.id
            new_visit.is_visit = False
            new_visit.save()

        return render(request, r'blog_module/blog_detail.html', context={
            'blog': blog,
            'categories': categories,
            'the_newest_blogs': the_newest_blogs,
            'blog_view': blog_view,
            'comment_form': comment_form,
        })

    def post(self, request: HttpRequest, slug):
        comment_form: CommentForm = CommentForm(request.POST)

        blog: Blog = Blog.objects.filter(is_active=True, slug=slug).first()
        categories: BlogCategory = BlogCategory.objects.filter(is_active=True).all()
        the_newest_blogs: Blog = newest_blogs(Blog.objects.filter(is_active=True).exclude(id=blog.id).all(), 3)
        blog_view: Visit = Visit.objects.filter(blog_id=blog.id, is_visit=True, product_or_blog=Visit.ProductOrBlog.blog_detail).count()
        
        if comment_form.is_valid() == True:
            email_user: User = User.objects.filter(email__iexact=comment_form.cleaned_data.get('email')).first()
            if User is not None:
                if request.user.email == email_user:
                    new_comment: Comment = Comment()
                    new_comment.email = comment_form.cleaned_data.get('email')
                    new_comment.full_name = comment_form.cleaned_data.get('full_name')
                    new_comment.text = comment_form.cleaned_data.get('text')
                    new_comment.commentposition = Comment.CommentPosition.blog_detail
                    new_comment.read_by_admin = False
                    new_comment.is_accepted = False
                    new_comment.is_subcomment = False
                    new_comment.save()
                    return redirect(reverse('home-page'))
                else:
                    comment_form.add_error('email', 'ایمیل وارد شده با ایمیل کاربری شما مطابقت دارد')
            else:
                comment_form.add_error('email', 'همچین کاربری با این ایمیل یافت نشد')
        else:
            comment_form.add_error('email', 'خطایی در تکمیل فرم رخ داده')
                    
        return render(request, r'blog_module/blog_detail.html', context={
            'blog': blog,
            'categories': categories,
            'the_newest_blogs': the_newest_blogs,
            'blog_view': blog_view,
            'comment_form': comment_form,
        })