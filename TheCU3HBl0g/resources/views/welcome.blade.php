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
            <div class="mx-auto row d-flex justify-content-between bg-secondary shadow-lg">
                <div>
                    <img src="/logo/logo.png" alt="No image" width="100" height="100" class="height img-fluid"/>
                </div>
                <div class="align-self-center"><h1 style="text-align: center; margin-left: 12px; font-size: 44px;"><b>The CU3H Bl0g</b></h1></div>

                @if (Route::has('login'))
                    <div class="align-self-center" style="margin-right: 1%">
                        @auth
                            <a href="/home" class="btn btn-lg btn-outline-success text-success" role="button">Home</a>
                        @else
                            <a href="{{ route('login') }}" class="btn btn-lg btn-outline-success" role="button">Login</a>
                        @if (Route::has('register'))
                            <a href="{{ route('register') }}" class="btn btn-lg btn-outline-success" role="button">Register</a>
                        @endif
                        @endauth
                @endif
                <div>
            </div>

            <div class="container" id="tm">
                <div class="nav-item bg-white text-center">
                    <a href="{{ route('posts') }}" class="nav-link text-success" style="font-size: 28px;"><b>Posts</b></a>
                </div>
                <div class="shadow-lg p-3 mb-5 rounded bg-white" style="margin-top: 5%">
                    <div class="shadow">
                        <h1 style="text-align: center"><a href="#what" data-toggle="collapse" class="nav-link text-success">What is The C3UH Bl0g</a></h1>
                        <div id="what" class="collapse p-3">
                            <p style="font-size: 20px;"><b>The CU3H Bl0g</b> is a social media platform providing <b>Ethical Hacking</b> content and letting everyone 
                            customize their profiles and share their knowledge with other users.</p>
                        </div>
                    </div>
                    <div class="shadow">
                        <h1 style="text-align: center"><a href="#News" data-toggle="collapse" class="nav-link text-success">News</a></h1>
                        <div id="News" class="collapse p-3">
                            <h3>No News!</h3>
                        </div>
                    </div>
                    <div class="shadow" style="margin-top: 2%">
                        <h1 style="text-align: center"><a href="#AboutCUEH" data-toggle="collapse" class="nav-link text-success">About CUEH</a></h1>
                        <div id="AboutCUEH" class="collapse p-3">
                            <h4><a href="http://cueh.coventry.ac.uk/">The Official Site of CUEH</a></h4>
                        </div>
                    </div>
                    <div class="shadow" style="margin-top: 2%">
                        <h1 style="text-align: center"><a href="#AboutCU" data-toggle="collapse" class="nav-link text-success">About Coventry University</a></h1>
                        <div id="AboutCU" class="collapse p-3">
                            <h4>Who we are and what we do</h4>
                            <p>We are a forward-looking, modern university with a proud tradition as a provider of high quality education and a focus on applied research.</p>
                            <img src="/logo/CU.jpeg" alt="No image" width="600" height="600" class="height img-fluid"/>
                            <p>Our students benefit from state-of-the-art equipment and facilities in all academic disciplines including health, design and engineering laboratories,
                            performing arts studios and computing centres. We have been chosen to host three national Centres of Excellence in Teaching and Learning which has enabled us to invest substantial sums of money in health, design and mathematics.</p>
                            <p>Our city-centre campus is continually developing and evolving, and we have plans for further investment in it over the next few years.
                            We are a major presence in Coventry, which contributes to the city's friendly and vibrant atmosphere and also enables us to foster successful business partnerships.</p>
                            <p>Through our links with leading edge businesses and organisations in the public and voluntary sectors, our students are able to access project and placement opportunities that enhance their employability on graduation.</p>
                            <a href="https://www.coventry.ac.uk">The Official Site of Coventry University</a>
                        </div>
                    </div>
                    <div class="shadow" style="margin-top: 2%">
                        <h1 style="text-align: center"><a href="#AboutDev" data-toggle="collapse" class="nav-link text-success">About the Developer</a></h1>
                        <div id="AboutDev" class="collapse p-3"><p style="font-size: 18px; margin-left:10px;">
                        The developer of this app is oneman army who loves writing code.
                        </p></div>
                    </div>
                </div>

                <div class="row justify-content-sm-end" style="margin-right: 2%">
                    <div style="margin-left: 4px">
                        <a href="https://github.com/Nikelandjelo" class="ml-1 underline" style="font-size: 16px;">
                            <img src="/logo/gitHub.png" class="height" width="20" height="20">GitHub
                        </a>
                    </div>

                    <div style="margin-left: 4px">
                        <a href="https://gitlab.com/Nikelandjelo" class="ml-1 underline" style="font-size: 16px;">
                            <img src="/logo/gitLab.png" class="height" width="20" height="20">GitLab  
                        </a>
                    </div>

                    <div style="margin-left: 6px; font-size: 16px;">
                        theCu3hBl0g_v0
                    </div>
                </dev>

            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>

        <script>
            particlesJS.load('particles-js', '/js/part.json', function(){
                console.log('part.json loaded...');
            });
        </script>



    </body>
</html>
