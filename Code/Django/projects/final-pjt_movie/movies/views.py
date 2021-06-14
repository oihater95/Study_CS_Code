from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Movie, Rate, Genre
from .forms import MovieForm, RateForm
import random
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from accounts.models import User


@require_safe
def index(request):
    movies = Movie.objects.all()
    recommend_movies = set()
    sorted_dict_top2 = set()
    flag = 1
    if request.user.is_authenticated:
        liked_movies = Movie.objects.filter(user_like=request.user)
        recommend_genres = []
        recommend_genres_dict = dict()
        for movie in liked_movies:
            for genre in movie.genres.all():
                recommend_genres.append(genre.name)  # 좋아요 누른 영화의 장르를 모아둔 리스트
                if genre.name in recommend_genres_dict:  # 좋아요 누른 영화들의 장르들이 몇 번 나왔는지
                    recommend_genres_dict[genre.name] += 1
                else:
                    recommend_genres_dict[genre.name] = 0
        if len(recommend_genres):
            flag = 0
            sorted_dict_top2 = sorted(recommend_genres_dict.items(), key=lambda x:x[1], reverse=True)[:2]  # 많이 나온 장르 순 top3
            genre_1 = Genre.objects.get(name=sorted_dict_top2[0][0])
            genre_2 = Genre.objects.get(name=sorted_dict_top2[1][0])
            for movie in movies:
                if genre_1 in movie.genres.all() and genre_2 in movie.genres.all() and movie not in liked_movies:
                    recommend_movies.add(movie)

    if flag:
        while len(recommend_movies) < 3:
            random_num = random.randint(1, len(movies))
            movie = Movie.objects.get(pk=random_num)
            if request.user.is_authenticated:
                if movie not in request.user.movie_like.all():
                    recommend_movies.add(movie)

            else:
                recommend_movies.add(movie)

    context = {
        'movies': movies,
        'sorted_dict_top2': sorted_dict_top2,
        'recommend_movies': recommend_movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rates = movie.rate_set.all()
    rate_users = []
    for i in range(len(rates)):
        rate_users.append(rates[i].user)

    rate_form = RateForm()
    total = rates_sum(rates)
    length = len(rates)

    if length == 0:
        avg = 0
    else:
        avg = round(total/length, 2)

    context = {
        'movie': movie,
        'rate_form': rate_form,
        'rates': rates,
        'avg': avg,
        'rate_users': rate_users,
        'genres': []
    }
    for genre in movie.genres.all():
        context['genres'].append(genre.name)    
    
    return render(request, 'movies/detail.html', context)


@require_POST
def create_rate(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        rate_form = RateForm(request.POST)
        if rate_form.is_valid():
            rate = rate_form.save(commit=False)
            rate.movie = movie
            rate.user = request.user
            rate.save()
            return redirect('movies:detail', movie_pk)
        context = {
            'rate_form': rate_form,
            'movie': movie
        }
        return render(request, 'movies/detail.html', context)
    return redirect('accounts:login')


@require_http_methods(['GET', 'POST'])
def update_rate(request, movie_pk, rate_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rate = get_object_or_404(Rate, pk=rate_pk)
    rates = movie.rate_set.all()
    if request.user == rate.user:
        if request.method == 'POST':
            rate_form = RateForm(request.POST, instance=rate)
            if rate_form.is_valid():
                rate_form.save()

                return redirect('movies:detail', movie.pk)
        else:
            rate_form = RateForm(instance=rate)
        context = {
            'rate_form': rate_form,
            'rates': rates,
            'movie': movie,
        }
        return render(request, 'movies/detail.html', context)

    else:
        return redirect('movies:detail', movie_pk)
    


@require_POST
def delete_rate(request, movie_pk, rate_pk):
    if request.user.is_authenticated:
        rate = get_object_or_404(Rate, pk=rate_pk)
        if request.user == rate.user:
            rate.delete()
    return redirect('movies:detail', movie_pk)


@require_POST
def like_from_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.is_authenticated:
        if movie.user_like.filter(pk=request.user.pk).exists():
            movie.user_like.remove(request.user)
        else:
            movie.user_like.add(request.user)

        return redirect('movies:detail', movie_pk)

    return redirect('accounts:login')

@require_POST
def like_from_index(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.is_authenticated:
        if movie.user_like.filter(pk=request.user.pk).exists():
            movie.user_like.remove(request.user)
        else:
            movie.user_like.add(request.user)

        return redirect('movies:index')

    return redirect('accounts:login')


@require_POST
def like_from_genre_detail(request, genre_pk, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.is_authenticated:
        if movie.user_like.filter(pk=request.user.pk).exists():
            movie.user_like.remove(request.user)
        else:
            movie.user_like.add(request.user)

        return redirect('movies:genre_detail', genre_pk)

    return redirect('accounts:login')


def rates_sum(rates):
    total = 0
    for i in range(len(rates)):
        total += rates[i].rating
    
    return total


# Apriori 연관분석
def recommend2(request):
    dataset = []
    users = User.objects.all()
    for user in users:
        liked_movies = Movie.objects.filter(user_like=user)
        liked_movie_list = []
        for movie in liked_movies:
            liked_movie_list.append(movie.title)
        dataset.append(liked_movie_list)
    
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_) 
    frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)
    
    association = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3) 
    associations = []
    i = 0
    while i >= 0:
        try:
            associations.append(association.iloc[i])
            i += 1
        except:
            break

    
    context = {
        'liked_movies': liked_movies,
        'associations': associations,
    }
    return render(request, 'movies/recommend2.html', context)


def genre_index(request):
    genres = Genre.objects.all()
    context = { 'genres': genres, }
    return render(request, 'movies/genre_index.html', context)


def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    movies = genre.movie_set.all()
    context = { 'genre': genre,
                'movies': movies, }
    return render(request, 'movies/genre_detail.html', context)