'use strict';
var mainApp = angular.module('djangoAngular', [
    //External
    'ui.router',
    'ngFlash',
    'ngMaterial',

    //Internal Module List
    'users'

]);

mainApp.config(function ($stateProvider, $locationProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise("/");
    $locationProvider.html5Mode(true).hashPrefix('');
    $stateProvider

        .state('first', {
            url: "/",
            views: {
                "@": {
                    template: '<users></users>'
                }
            },
            display: "User"
        })
        .state('about', {
            url: "/about",
            views: {
                "@": {
                    template: '<h1>About Peerbits </h1><br> <a href="https://www.google.com/">https://www.google.com/</a> '
                }
            },
            display: "User"
        });
});

mainApp.run(['$state', '$rootScope', function ($state, $rootScope) {
    $rootScope.$on('$stateChangeStart', function (e, toState, toParams, fromState, fromParams) {
        $rootScope.currentState = toState;
    });
}]);