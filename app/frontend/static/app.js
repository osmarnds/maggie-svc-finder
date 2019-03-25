var app = angular.module("myApp", ["ngRoute", "ngAnimate"]);

app.config(function($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "./home/home.html"
        });
});

app.config(function($httpProvider){
    $httpProvider.defaults.headers.common['Cache-Control'] = 'no-cache';
    $httpProvider.defaults.cache = false;

    if (!$httpProvider.defaults.headers.get) {
        $httpProvider.defaults.headers.get = {};
    }
    $httpProvider.defaults.headers.get['If-Modified-Since'] = '0';
});
