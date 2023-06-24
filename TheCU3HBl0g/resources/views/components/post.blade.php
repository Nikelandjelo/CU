@props(['post' => $post])

<div class="bg-sucses">
    <div class="row  p-4 bg-secondary mx-auto">
        <a href="{{ route('users.posts', $post->user) }}" class="nav-link text-warning">
            <div class="row d-flex justify-content-start">
                <img src="/storage/{{ $post->user->profile->image }}" style="width:80px; height:80px; float:left; border-radius:50%; margin-right:5px;">
                <h4 class="pr-4"><b>{{ $post->user->username }}</b><h4>
            </div>
            </a></a>
        <span class="text-wite" style="font-size: 14px;">{{ $post->created_at->diffForHumans() }}</span>
    </div>
    <p class="p-2 bg-info" style="font-size: 18px;">{{ $post->body }}</p>
</div>
<div class="container">
    <div class="row pb-4">
        @auth
            @can('delete', $post)
                <div class="pr-2 ml-2">
                    <form action="{{ route('post.destroy', $post) }}" method="post">
                        @csrf
                        @method('DELETE')
                        <button type="submit" class="btn btn-sm btn-danger">DELETE</button>
                    </form>
                </div>
            @endcan
            @if (!$post->likedBy(auth()->user()) and !$post->dislikedBy(auth()->user()))
                <form action="{{ route('posts.likes', $post) }}" method="post" class="ml-2">
                    @csrf
                    <button type="submit" class="btn btn-sm btn-primary">Like</button>
                </form>
                <form action="{{ route('posts.dislikes', $post) }}" method="post" class="ml-1">
                    @csrf
                    <button type="submit" class="btn btn-sm btn-outline-danger">Dislike</button>
                </form>
            @else
                @if ($post->likedBy(auth()->user()))
                <form action="{{ route('posts.likes', $post) }}" method="post">
                    @csrf
                    @method('DELETE')
                    <button type="submit" class="btn btn-sm btn-outline-danger">Unlike</button>
                </form>
                @endif
                @if ($post->dislikedBy(auth()->user()))
                <form action="{{ route('posts.dislikes', $post) }}" method="post">
                    @csrf
                    @method('DELETE')
                    <button type="submit" class="btn btn-sm btn-primary">Undislike</button>
                </form>
                @endif
            @endif
        @endauth
        @guest
            <form action="{{ route('posts.likes', $post) }}" method="post" class="ml-2">
                @csrf
                <button type="submit" class="btn btn-sm btn-primary">Like</button>
            </form>
            <form action="{{ route('posts.dislikes', $post) }}" method="post" class="ml-1">
                @csrf
                <button type="submit" class="btn btn-sm btn-outline-danger">Dislike</button>
            </form>
        @endguest
        <span class="text-primary pl-2">{{ $post->likes->count() }} {{ Str::plural('like', $post->likes->count()) }}</span>
        <span class="text-danger pl-2">{{ $post->dislikes->count() }} {{ Str::plural('dislike', $post->dislikes->count()) }}</span>
        <a href="{{ route('posts.show', $post) }}" class="btn btn-lg btn-primary ml-auto mr-2" role="button">View</a>
    </div>
</div>
<br>