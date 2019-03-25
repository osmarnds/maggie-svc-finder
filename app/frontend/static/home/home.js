angular.module("myApp").controller("HomeController", function ($scope, $http) {

    $http({
        method: 'GET',
        url: '/api/login/whoami'
    }).then(function successCallback(response) {
        $scope.user = response.data
    }, function errorCallback(response) {
        $scope.user = null
    });

});
