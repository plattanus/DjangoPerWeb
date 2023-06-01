__author__ = 'plattanus'

import importlib
from myblog import blogroll
from blog.models import Category, Article, Tag, Comment


def sidebar(request):
    # 所有类型
    category_list = Category.objects.all()
    
    # 文章排行
    blog_top = Article.objects.all().values("id", "title", "view").order_by('-view')[0:6]
    
    # 标签
    tag_list = Tag.objects.all()
    
    # 评论
    comment = Comment.objects.all().order_by('-create_time')[0:6]
    
    # 友链
    importlib.reload(blogroll)

    return {
        'category_list': category_list,
        'blog_top': blog_top,
        'tag_list': tag_list,
        'comment_list': comment,
        'blogroll': blogroll.sites
    }


if __name__ == '__main__':
    pass
