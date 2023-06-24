<!doctype html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- CSRF Token -->
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <link rel="shortcut icon" href="/logo/icon.ico">
    <title>TheCU3Hbl0g</title>

    <!-- Scripts -->
    <script src="{{ asset('js/app.js') }}"></script>

    <!-- Fonts -->
    <link rel="dns-prefetch" href="//fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet">

    <!-- Styles -->
    <link href="{{ asset('css/app.css') }}" rel="stylesheet">
</head>
<body id="particles-js">
    <div>
        <nav class="navbar navbar-expand-md shadow-lg bg-secondary">
            <div class="container d-flex justify-content-between">
                <a class="navbar-brand text-success" style="font-size: 20px;" href="{{ url('/') }}">
                    <img src="/logo/logo.png" while="30" height="30" class="height">
                    <b>The CU3H Bl0g</b>
                </a>

                <ul class="nav nav-tabs nav-justified mx-auto">
                    <li class="nav-item">
                        <a href="{{ route('home') }}" class="nav-link active text-success"><b>Home</b></a>
                    </li>

                    <li class="nav-item">
                        <a href="{{ route('posts') }}" class="nav-link text-success"><b>Posts</b></a>
                    </li>

                    <li class="nav-item">
                        <a href="{{ route('donation') }}" class="nav-link text-success"><b>Donate</b></a>
                    </li>
                    
                </ul>

                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="{{ __('Toggle navigation') }}">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <!-- Left Side Of Navbar -->
                    <ul class="navbar-nav mr-auto">

                    </ul>

                    <!-- Right Side Of Navbar -->
                    <ul class="navbar-nav ml-auto">
                        <!-- Authentication Links -->
                        
                        <li class="nav-item dropdown">    
                            <img src="/storage/{{ Auth::user()->profile->image }}" style="width:45px; height:45px; float:left; border-radius:50%; margin-right:5px;">
                            <a id="navbarDropdown" style="font-size: 16px;" class="nav-link dropdown-toggle text-success" href="#" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" v-pre>
                            <b>{{ Auth::user()->username }}</b>
                            </a>
                        
                            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
                                <a class="dropdown-item" href="/home/{{ Auth::user()->id }}/settings">Settings</a>
                                <a class="dropdown-item" href="{{ route('logout') }}"
                                   onclick="event.preventDefault();
                                                 document.getElementById('logout-form').submit();">
                                    {{ __('Logout') }}
                                </a>
                                <form id="logout-form" action="{{ route('logout') }}" method="POST" class="d-none">
                                    @csrf
                                </form>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <main class="py-4">
            @yield('content')
        </main>
    </div>

    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>

    <script>
        particlesJS.load('particles-js', '/js/part.json', function(){
            console.log('part.json loaded...');
        });
    </script>

</body>
</html>
