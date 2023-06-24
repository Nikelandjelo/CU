@auth
    <div class="d-flex justify-content-center p-4">
        <form action="{{ route('posts') }}" method="post">
            @csrf
            <h1 style="text-align: center;" class="p-2"><a href="#NewPost" data-toggle="collapse" class="btn btn-lg btn-info text-white">New Post</a></h1>
                <div id="NewPost" class="collapse">
                    <label for="body" class="sr-only">Body</label>
                    <textarea name="body" id="body" cols="100" rows="6" class="rounded-lg
                    @error('body') border-red-500 @enderror" placeholder="Text"></textarea>
                    @error('body')
                        <div class="text-danger text-sm">
                            {{ $message }}
                        </div>
                    @enderror
                    <br>
                    <button type="submit" class="btn btn-primary p-2">Post</button>
                </div>
        </form>
    </div>
@endauth