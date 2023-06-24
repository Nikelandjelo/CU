<?php


namespace App\Http\Controllers;

use App\Models\User;
use App\Models\Profile;
use Illuminate\Support\Facades\Auth;
use Intervention\Image\Facades\Image;
use Illuminate\Http\Request;

class ProfileController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Contracts\Support\Renderable
     */
    public function edit(User $user)
    {
        return view('users.settings', compact('user'));
    }

    public function update(User $user)
    {
        request()->validate([
            'description' => 'max:255',
            'image' => 'mimes:jpeg,bmp,png',
        ]);

        if(request('image'))
        {
            $imagePath = request('image')->store('avatars', 'public');
            
            $image = Image::make(public_path("storage/{$imagePath}"))->fit(1000, 1000);
            $image->save();

            Profile::where('user_id', $user->id)->update(['image' => $imagePath]);
        }

        if(request('description'))
        {
            $description = request('description');

            Profile::where('user_id', $user->id)->update(['description' => $description]);
        }
        
    	return redirect("/home");
    }
}

