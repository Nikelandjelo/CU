@extends('layouts.mid')

@section('content')
    <div class="container" id="hm" style="top: 20vh;">
        <x-newp />
            @if ($posts->count())
                @foreach ($posts as $post)
                    <x-post :post="$post" />
                @endforeach
                {{ $posts->links() }}
            @else
                <h4>No posts!</h4>
            @endif
        </div>
    </div>

@endsection