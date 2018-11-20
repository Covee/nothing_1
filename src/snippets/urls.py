from django.conf.urls import url, include  
from snippets import views  
from rest_framework.routers import DefaultRouter

# 라우터를 생성하고 뷰셋을 등록합니다
router = DefaultRouter()  
router.register(r'snippets', views.SnippetViewSet)  
router.register(r'users', views.UserViewSet)

# 이제 API URL을 라우터가 자동으로 인식합니다
# 추가로 탐색 가능한 API를 구현하기 위해 로그인에 사용할 URL은 직접 설정을 했습니다
urlpatterns = [ 
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	
]



# # CBV일때 URL
# from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns  
# from snippets import views

# from snippets.views import SnippetViewSet, UserViewSet, api_root  
# from rest_framework import renderers

# snippet_list = SnippetViewSet.as_view({  
# 	'get': 'list',
# 	'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({  
# 	'get': 'retrieve',
# 	'put': 'update',
# 	'patch': 'partial_update',
# 	'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({  
# 	'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({  
# 	'get': 'list'
# })
# user_detail = UserViewSet.as_view({  
# 	'get': 'retrieve'
# })

# urlpatterns = format_suffix_patterns([
# 	path('', views.api_root),
# 	path('snippets/', snippet_list, name='snippet-list'),
# 	paht('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
# 	path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
# 	path('users/', user_list, name='user-list'),
# 	path('users/<int:pk>', user_detail, name='user-detail'),
# ])

# # 탐색 가능한 API를 위한 로그인/로그아웃 뷰
# urlpatterns += [
# 	path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
# ]


# urlpatterns = [
# 	path('snippets/', views.SnippetList.as_view()),
# 	path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
# 	path('users/', views.UserList.as_view()),
# 	path('users/<int:pk>/', views.UserDetail.as_view()),

# 	path('api-auth', include('rest_framework.urls', namespace='rest_framework')),

# 	path('', views.api_root),
# 	path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()), 
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)  



# FBV일때 URL
# from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views


# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
    
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)


