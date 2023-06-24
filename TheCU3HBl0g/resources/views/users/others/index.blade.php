@extends('layouts.mid')

@section('content')
    <div class="container" id="hm" style="top: 20vh;">
        <div class="shadow bg-dark">
            <h1 style="text-align: left"><a href="#info" data-toggle="collapse" class="nav-link text-white">{{ $user->username }}</a></h1>
            <div id="info" class="collapse pb-4">
                <p style="font-size: 16px;" class="text-info ml-5">({{ $user->name }})</p>
                <p style="font-size: 18px;" class="text-white ml-5">Joined {{ $user->created_at->diffForHumans() }}<br>
                    Posted {{ $posts->count() }} {{ Str::plural('post', $posts->count()) }}</p>
                <div class="d-flex justify-content-end">
                    <div>
                        <h5 class="text-warning pr-6 p-2"><i class="text-light">Status:</i><br>{{ $profile->description }}
                    </div>
                </div>
                <div class="d-flex justify-content-center row">
                    @auth
                        <p class="text-primary pr-2"><b>Total {{ Str::plural('like', $user->receivedLikes->count()) }}: {{ $user->receivedLikes->count() }}</b></p>
                    @endauth
                    <img src="/storage/{{ $profile->image }}" style="width:150px; height:150px; float:left; border-radius:50%;">
                    @auth
                        <p class="text-danger pl-2"><b>Total {{ Str::plural('dislike', $user->receivedDislikes->count()) }}: {{ $user->receivedDislikes->count() }}</b></p>
                    @endauth
                </div>
            </div>
        </div>
        <div class="shadow-lg">
            <h1 style="text-align: center"><a href="#posts" data-toggle="collapse" class="nav-link text-dark">Posts</a></h1>
            <div id="posts" class="collapse">
                @if ($posts->count())
                @foreach ($posts as $post)
                    <x-post :post="$post" />
                @endforeach
                {{ $posts->links() }}
                @else
                    <h4>{{ $user->username }} has no posts!</h4>
                @endif
            </div>
        </div>
    </div>
@endsection