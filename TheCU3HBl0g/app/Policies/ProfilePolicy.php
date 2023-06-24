<?php

namespace App\Policies;

use App\Models\User;
use App\Models\Profile;
use Illuminate\Auth\Access\HandlesAuthorization;

class ProfilePolicy
{
    use HandlesAuthorization;

    /**
     * Create a new policy instance.
     *
     * @return void
     */

    public function edit(User $user, Profile $profile)
    {
        return $user->id === $profile->user_id;
    }

    public function update(User $user, Profile $profile)
    {
        return $user->id === $profile->user_id;
    }
}
