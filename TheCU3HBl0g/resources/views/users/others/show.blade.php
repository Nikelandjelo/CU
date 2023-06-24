@extends('layouts.mid')

@section('content')
<div class="container" style="top: 20vh;" id="hm">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <x-post :post="$post" />
        </div>
    </div>
</div>

@endsection