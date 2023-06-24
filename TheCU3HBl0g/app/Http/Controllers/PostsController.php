<?php

namespace App\Http\Controllers;

use App\Models\Post;
use Illuminate\Http\Request;

class PostsController extends Controller
{
    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Contracts\Support\Renderable
     */

    public function __construct()
    {
        $this->middleware(['auth'])->only(['store', 'destroy']);
    }
    
    public function index()
    {
        $posts = Post::latest()->with(['user', 'likes', 'dislikes'])->paginate(10);


        return view('posts', [
            'posts' => $posts
        ]);
    }

    public function store(Request $request)
    {
        $this->validate($request, [
            'body' => 'required'
        ]);

        $request->user()->posts()->create($request->only('body'));

        return back();
    }

    public function show(Post $post)
    {
        return view('users.others.show', [
            'post' => $post
        ]);
    }

    public function destroy(Post $post)
    {
        $this->authorize('delete', $post);

        $post->delete();

        return back();
    }
}
