@extends('layouts.usr')

@section('content')
<div class="container" id="hm">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header">{{ __('Settings') }}</div>

                <div class="card-body">
                    <div class="row mx-auto d-flex justify-content-between">
                        <div>
                            <form enctype="multipart/form-data" action="/home/{{ $user->id }}" method="post">
                                @csrf
                                @method('PATCH')
                                <label>Update Profile Image</label>
                                <input type="file" class="form-control-file" id="image" name="image">
                                <div class="p-1">
                                    <img src="/storage/{{ Auth::user()->profile->image }}" style="width:150px; height:150px; float:left; border-radius:50%; margin-right:80px;">
                                </div>
                                @if ($errors->has('image'))
                                    <span class="invalid-feedback" role="alert">
                                        <strong>{{ $error->first('image') }}</strong>
                                    </span>
                                @endif

                                <br>
                                <div class="p-4 pb-4">
                                    <h5 style="margin-top 20px;"><b>Update Status</b></h5>
                                    <textarea class="from-control{{ $errors->has('caption') ? ' is-invalid' : '' }} p-2" rows="5" cols="60" name="description" id="description"
                                        placeholder="{{ old('caption') }}" autocomplete="caption" autoficus></textarea>
                                    @error('body')
                                        <div class="text-danger text-sm">
                                            {{ $message }}
                                        </div>
                                    @enderror
                                    <input type="submit" class="m-2 btn btn-lg btn-primary">
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

@endsection