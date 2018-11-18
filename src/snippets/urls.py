# CBV일때 URL
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns  
from snippets import views


# API endpoints
urlpatterns = format_suffix_patterns([
	path('', views.api_root),
	path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
	paht('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
	path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
	path('users/', views.UserList.as_view(), name='user-list'),
	path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
])

# 탐색 가능한 API를 위한 로그인/로그아웃 뷰
urlpatterns += [
	path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]


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


