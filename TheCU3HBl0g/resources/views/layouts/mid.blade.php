<!DOCTYPE html>
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
    <body style="background: #333333;">
        <div id="particles-js">
            <nav class="fixed-top mx-auto row d-flex justify-content-between bg-secondary shadow-lg">
                <div>
                    <a href="{{ url('/') }}"><img src="/logo/logo.png" alt="No image" width="150" height="150" style="position:absolute;" class="height img-fluid"/></a>
                </div>
                <div><h1 style="text-align: center; padding-left: 100px; font-size: 54px;"><b>The CU3H Bl0g</b></h1></div>

                @if (Route::has('login'))
                    <div class="align-self-center" style="margin-right: 1%">
                        @auth
                            <a href="{{ route('home') }}" class="btn btn-lg btn-outline-success text-success" role="button">Home</a>
                        @else
                            <a href="{{ route('login') }}" class="btn btn-lg btn-outline-success" role="button">Login</a>
                        @if (Route::has('register'))
                            <a href="{{ route('register') }}" class="btn btn-lg btn-outline-success" role="button">Register</a>
                        @endif
                        @endauth
                    </div>
                @endif
            </nav>

            <main class="py-4" id="particles-js">
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