@extends('layouts.usr')

@section('content')
<div class="container" id="hm">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header">{{ __('Donation') }}</div>

                <div class="card-body">
                    @if (session('status'))
                        <div class="alert alert-success" role="alert">
                            {{ session('status') }}
                        </div>
                    @endif

                    {{ __('You are in Donation!') }}

                    <form>
                        <script
                            src="https://checkout.stripe.com/checkout.js" class="stripe-button"
                            data-key="pk_test_pIaGoPD69OsOWmh1FIE8Hl4J"
                            data-amount="500"
                            data-name="CUEH"
                            data-description="Better Hackers"
                            data-image="/logo/logo.png"
                            data-locale="auto"
                            data-currency="gbp">
                        </script>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

@endsection