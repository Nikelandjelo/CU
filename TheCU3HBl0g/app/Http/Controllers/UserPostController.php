<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;

class UserPostController extends Controller
{
    public function index(User $user)
    {
        $posts = $user->posts()->with(['user', 'likes', 'dislikes'])->latest()->paginate(10);
        $profile = $user->profile;

        return view('users.others.index', [
            'user' => $user,
            'posts' => $posts,
            'profile' => $profile
        ]);
    }
}
