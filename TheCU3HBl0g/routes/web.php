<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PostsController;
use App\Http\Controllers\PostLikeController;
use App\Http\Controllers\PostDislikeController;
use App\Http\Controllers\DonationController;
use App\Http\Controllers\ProfileController;
use App\Http\Controllers\UserPostController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');

Route::patch('/home/{user}', [App\Http\Controllers\ProfileController::class, 'update'])->name('update');
Route::get('/home/{user}/settings', [App\Http\Controllers\ProfileController::class, 'edit'])->name('settings');

Route::get('/posts', [App\Http\Controllers\PostsController::class, 'index'])->name('posts');
Route::post('/posts', [App\Http\Controllers\PostsController::class, 'store']);
Route::get('/posts/{post}', [App\Http\Controllers\PostsController::class, 'show'])->name('posts.show');
Route::delete('/posts/{post}', [App\Http\Controllers\PostsController::class, 'destroy'])->name('post.destroy');

Route::post('/posts/{post}/likes', [App\Http\Controllers\PostLikeController::class, 'store'])->name('posts.likes');
Route::delete('/posts/{post}/likes', [App\Http\Controllers\PostLikeController::class, 'destroy'])->name('posts.likes');

Route::post('/posts/{post}/dislikes', [App\Http\Controllers\PostDislikeController::class, 'store'])->name('posts.dislikes');
Route::delete('/posts/{post}/dislikes', [App\Http\Controllers\PostDislikeController::class, 'destroy'])->name('posts.dislikes');

Route::get('/user/{user:username}', [App\Http\Controllers\UserPostController::class, 'index'])->name('users.posts');
Route::get('/donation', [App\Http\Controllers\DonationController::class, 'index'])->name('donation');